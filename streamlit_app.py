import json
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="My Peoms", layout="wide")

DATA_PATH = Path(__file__).resolve().parent / "peoms1_tang_song.json"
AUTHORS_PATH = Path(__file__).resolve().parent / "peoms_authors_tang_song.json"
CIPAI_DESC_PATH = Path(__file__).resolve().parent / "peoms_cipai_desc.json"

DYNasty_OPTIONS = ["唐代", "宋代"]
CZ_TYPE_OPTIONS = ["词牌", "诗文", "作者", "唐诗三百首", "抒情", "写人", "写景", "Other"]
FORMAT_OPTIONS = ["七言古诗", "七言律诗", "七言绝句", "乐府", "五言古诗", "五言律诗", "五言绝句", "古诗词"]
KNOWN_CZ_TYPES = ["词牌", "诗文", "作者", "唐诗三百首", "抒情", "写人", "写景"]


@st.cache_data
def load_poems(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_authors(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


@st.cache_data
def load_cipai_desc(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def as_text(value):
    if isinstance(value, list):
        text = "\n".join(str(item).strip() for item in value if str(item).strip())
        return text.strip()
    if isinstance(value, str):
        return value.strip()
    return ""


def cz_type_match(poem, selected_cz_type):
    poem_cz = str(poem.get("CZ_Type", "")).strip()
    if selected_cz_type == "Other":
        return poem_cz not in KNOWN_CZ_TYPES
    return poem_cz == selected_cz_type


def keyword_match(poem, keyword):
    keyword = keyword.strip().lower()
    if not keyword:
        return True

    name_text = str(poem.get("name", "")).strip().lower()
    content_text = as_text(poem.get("content", [])).lower()
    return keyword in name_text or keyword in content_text


def normalize_name(value):
    return "".join(str(value).split())


def find_author_intro(author_name, authors):
    author_name = str(author_name).strip()
    normalized_author_name = normalize_name(author_name)

    for item in authors:
        item_name = str(item.get("name", "")).strip()
        if item_name == author_name:
            return item

    for item in authors:
        item_name = str(item.get("name", "")).strip()
        if normalize_name(item_name) == normalized_author_name:
            return item

    return None


def describe_to_text(value):
    if isinstance(value, str):
        return value.strip()

    if isinstance(value, list):
        blocks = []
        for item in value:
            if isinstance(item, dict):
                item_type = str(item.get("type", "")).strip()
                item_content = as_text(item.get("content", ""))
                if item_type and item_content:
                    blocks.append(f"{item_type}\n{item_content}")
                elif item_content:
                    blocks.append(item_content)
            else:
                text = str(item).strip()
                if text:
                    blocks.append(text)

        return "\n\n".join(blocks).strip()

    return ""


def normalize_text(value):
    text = str(value).strip()
    for ch in [" ", "\u3000", "\t", "\n", "\r"]:
        text = text.replace(ch, "")
    return text


def extract_cipai_name(poem_name):
    name = str(poem_name).strip()
    if not name:
        return ""

    for sep in ["·", "（", "(", "-", "——"]:
        if sep in name:
            name = name.split(sep, 1)[0].strip()
            break

    return name


def find_cipai_desc(poem_name, cipai_desc_data):
    cipai_name = extract_cipai_name(poem_name)
    normalized_cipai_name = normalize_text(cipai_name)

    for item in cipai_desc_data:
        item_name = str(item.get("name", "")).strip()
        if item_name == cipai_name:
            return item

    for item in cipai_desc_data:
        item_name = str(item.get("name", "")).strip()
        if normalize_text(item_name) == normalized_cipai_name:
            return item

    return None


poems = load_poems(DATA_PATH)
authors = load_authors(AUTHORS_PATH)
cipai_desc_data = load_cipai_desc(CIPAI_DESC_PATH)

st.markdown(
    """
    <style>
        .poem-title {
            font-size: 2.1rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }
        .poem-meta {
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: #1f2937;
        }
        .section-label {
            font-size: 1.05rem;
            font-weight: 800;
            margin-top: 0.6rem;
            margin-bottom: 0.35rem;
        }
        .poem-content {
            font-size: 1.1rem;
            line-height: 1.95;
            font-weight: 700;
            white-space: pre-wrap;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("诗词")

with st.sidebar:
    st.subheader("Filters")
    selected_dynasty = st.selectbox("dynasty", options=DYNasty_OPTIONS, index=0)
    filter_mode = st.radio("Filter by", options=["Type", "Format"], index=0)
    keyword = st.text_input("Keyword", placeholder="Search in title or content")

    selected_cz_type = None
    selected_format = None
    if filter_mode == "Type":
        selected_cz_type = st.selectbox("Type", options=CZ_TYPE_OPTIONS, index=0)
    else:
        selected_format = st.selectbox("Format", options=FORMAT_OPTIONS, index=0)

    filtered_poems = [
        p
        for p in poems
        if str(p.get("dynasty", "")).strip() == selected_dynasty
        and (
            cz_type_match(p, selected_cz_type)
            if filter_mode == "Type"
            else str(p.get("format", "")).strip() == selected_format
        )
        and keyword_match(p, keyword)
    ]

    st.markdown("---")
    st.subheader("Poems")

    if not filtered_poems:
        st.warning("No poems match the selected filters.")
        st.stop()

    poem_labels = [
        f"{str(p.get('name', '')).strip()} - {str(p.get('author', '')).strip()}"
        for p in filtered_poems
    ]

    if "selected_poem_idx" not in st.session_state:
        st.session_state["selected_poem_idx"] = 0

    if st.session_state["selected_poem_idx"] >= len(poem_labels):
        st.session_state["selected_poem_idx"] = 0

    selected_label = st.selectbox(
        "Title - Author",
        options=poem_labels,
        index=st.session_state["selected_poem_idx"],
        key="poem_selector",
    )
    selected_idx = poem_labels.index(selected_label)
    st.session_state["selected_poem_idx"] = selected_idx
    selected_poem = filtered_poems[selected_idx]

    st.markdown("---")
    if filter_mode == "Type" and selected_cz_type == "词牌":
        selected_cipai_item = find_cipai_desc(selected_poem.get("name", ""), cipai_desc_data)
        selected_cipai_name = extract_cipai_name(selected_poem.get("name", ""))
        st.subheader("词牌")
        if selected_cipai_name:
            st.markdown(f"**{selected_cipai_name}**")

        if selected_cipai_item:
            cipai_description = as_text(selected_cipai_item.get("description", ""))
            if cipai_description:
                st.markdown(cipai_description)
            else:
                st.info("No description found for this 词牌.")
        else:
            st.info("No 词牌 description match found.")

name = str(selected_poem.get("name", "")).strip()
author = str(selected_poem.get("author", "")).strip()
dynasty = str(selected_poem.get("dynasty", "")).strip()
content = as_text(selected_poem.get("content", []))
translate_text = as_text(selected_poem.get("translate", []))
notes_text = as_text(selected_poem.get("notes", []))
appreciation_text = as_text(selected_poem.get("appreciation", []))
author_intro = find_author_intro(author, authors)
author_lifetime = as_text(author_intro.get("lifetime", "")) if author_intro else ""
author_describe = describe_to_text(author_intro.get("describe", "")) if author_intro else ""

st.markdown(f"<div class='poem-title'>{name}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='poem-meta'>[{dynasty}] {author}</div>", unsafe_allow_html=True)

st.markdown("<div class='section-label'>content</div>", unsafe_allow_html=True)
st.markdown(f"<div class='poem-content'>{content}</div>", unsafe_allow_html=True)

st.markdown("---")

if translate_text:
    st.markdown("<div class='section-label'>translate</div>", unsafe_allow_html=True)
    st.markdown(translate_text)

if notes_text:
    st.markdown("<div class='section-label'>notes</div>", unsafe_allow_html=True)
    st.markdown(notes_text)

if appreciation_text:
    with st.expander("appreciation (hide/show)", expanded=False):
        st.markdown(appreciation_text)

#st.markdown("---")
st.markdown("<div class='section-label'>Author</div>", unsafe_allow_html=True)
if author_intro:
    if author_lifetime:
        st.markdown(author_lifetime)
    else:
        st.info("No lifetime information found.")

    if author_describe:
        with st.expander("describe (hide/show)", expanded=False):
            st.markdown(author_describe)
    else:
        st.info("No describe information found.")
else:
    st.info("No author introduction found for this author.")


st.markdown("---")
prev_col, nav_spacer, next_col = st.columns([2, 6, 2])
with prev_col:
    prev_clicked = st.button("Previous", use_container_width=True)
with next_col:
    next_clicked = st.button("Next", use_container_width=True)

if prev_clicked or next_clicked:
    if prev_clicked:
        new_idx = (selected_idx - 1) % len(filtered_poems)
    else:
        new_idx = (selected_idx + 1) % len(filtered_poems)

    st.session_state["selected_poem_idx"] = new_idx
    st.rerun()
