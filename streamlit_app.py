import json
import hashlib
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="诗词", page_icon="🌟", layout="wide")

if "active_page" not in st.session_state:
    st.session_state["active_page"] = "诗词"

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


def set_selected_poem_idx(new_idx, poem_labels):
    st.session_state["selected_poem_idx"] = new_idx
    st.session_state["poem_selector"] = poem_labels[new_idx]


def move_selected_poem(step, poem_labels):
    current_idx = st.session_state.get("selected_poem_idx", 0)
    new_idx = (current_idx + step) % len(poem_labels)
    set_selected_poem_idx(new_idx, poem_labels)


def sync_selected_poem(filtered_poems, poem_labels):
    if "selected_poem_idx" not in st.session_state:
        st.session_state["selected_poem_idx"] = 0

    if st.session_state["selected_poem_idx"] >= len(poem_labels):
        st.session_state["selected_poem_idx"] = 0

    current_idx = st.session_state["selected_poem_idx"]
    current_label = poem_labels[current_idx]

    if st.session_state.get("poem_selector") not in poem_labels:
        st.session_state["poem_selector"] = current_label

    selected_label = st.selectbox(
        "标题 - 作者",
        options=poem_labels,
        key="poem_selector",
    )
    selected_idx = poem_labels.index(selected_label)
    if selected_idx != st.session_state["selected_poem_idx"]:
        st.session_state["selected_poem_idx"] = selected_idx
    return selected_idx, filtered_poems[selected_idx]


def build_read_aloud_text(
    name,
    dynasty,
    author,
    content,
    translate_text,
    notes_text,
    author_lifetime,
    author_describe,
    include_translate,
    include_notes,
    include_author_intro,
):
    parts = []

    header = "，".join([item for item in [name, dynasty, author] if item])
    if header:
        parts.append(header)

    if content:
        parts.append(content)

    if include_translate and translate_text:
        parts.append("译文")
        parts.append(translate_text)

    if include_notes and notes_text:
        parts.append("注释")
        parts.append(notes_text)

    if include_author_intro and (author_lifetime or author_describe):
        parts.append("作者简介")
        if author_lifetime:
            parts.append(author_lifetime)
        #if author_describe:
        #    parts.append(author_describe)

    return "\n\n".join(parts).strip()


def render_read_aloud_controls(text_to_read):
        text_payload = json.dumps(text_to_read)
        block_id = "tts_" + hashlib.md5(text_to_read.encode("utf-8")).hexdigest()[:10]

        components.html(
                f"""
                <div style="padding: 8px 0 2px 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
                    <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 8px;">
                        <button id="{block_id}_speak" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #111827; color: #ffffff;">Play</button>
                        <button id="{block_id}_pause" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #ffffff; color: #111827;">Pause</button>
                        <button id="{block_id}_resume" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #ffffff; color: #111827;">Resume</button>
                        <button id="{block_id}_stop" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #ffffff; color: #111827;">Stop</button>
                    </div>

                    <div style="display: flex; align-items: center; gap: 8px; color: #374151; font-size: 14px;">
                        <label for="{block_id}_rate">Speed</label>
                        <input id="{block_id}_rate" type="range" min="0.7" max="1.3" step="0.05" value="1" style="width: 170px;" />
                        <span id="{block_id}_rate_value">1.00x</span>
                    </div>

                    <div id="{block_id}_status" style="margin-top: 8px; color: #4b5563; font-size: 13px;">Ready</div>
                </div>

                <script>
                    (() => {{
                        const text = {text_payload};
                        const synth = window.speechSynthesis;

                        const speakBtn = document.getElementById("{block_id}_speak");
                        const pauseBtn = document.getElementById("{block_id}_pause");
                        const resumeBtn = document.getElementById("{block_id}_resume");
                        const stopBtn = document.getElementById("{block_id}_stop");
                        const rateInput = document.getElementById("{block_id}_rate");
                        const rateValue = document.getElementById("{block_id}_rate_value");
                        const statusNode = document.getElementById("{block_id}_status");

                        function setStatus(msg) {{
                            statusNode.textContent = msg;
                        }}

                        function pickVoice() {{
                            const voices = synth.getVoices() || [];
                            const exact = voices.find(v => v.lang === "zh-CN");
                            if (exact) return exact;
                            const zh = voices.find(v => (v.lang || "").toLowerCase().startsWith("zh"));
                            return zh || null;
                        }}

                        function speak() {{
                            if (!text || !text.trim()) {{
                                setStatus("No text to read.");
                                return;
                            }}

                            synth.cancel();
                            const utter = new SpeechSynthesisUtterance(text);
                            utter.lang = "zh-CN";
                            utter.rate = parseFloat(rateInput.value || "1");

                            const voice = pickVoice();
                            if (voice) utter.voice = voice;

                            utter.onstart = () => setStatus("Reading...");
                            utter.onend = () => setStatus("Finished");
                            utter.onerror = () => setStatus("Read failed in this browser.");

                            synth.speak(utter);
                        }}

                        speakBtn.addEventListener("click", speak);
                        pauseBtn.addEventListener("click", () => {{ synth.pause(); setStatus("Paused"); }});
                        resumeBtn.addEventListener("click", () => {{ synth.resume(); setStatus("Reading..."); }});
                        stopBtn.addEventListener("click", () => {{ synth.cancel(); setStatus("Stopped"); }});
                        rateInput.addEventListener("input", () => {{
                            rateValue.textContent = `${{parseFloat(rateInput.value).toFixed(2)}}x`;
                        }});

                        if (typeof synth.onvoiceschanged !== "undefined") {{
                            synth.onvoiceschanged = () => {{}};
                        }}
                    }})();
                </script>
                """,
                height=165,
        )


poems = load_poems(DATA_PATH)
authors = load_authors(AUTHORS_PATH)
cipai_desc_data = load_cipai_desc(CIPAI_DESC_PATH)

st.markdown(
    """
    <style>
        .block-container {
            padding-top: calc(3rem + env(safe-area-inset-top, 0px));
            padding-bottom: 2rem;
            max-width: 900px;
        }
        .poem-title {
            font-size: 1.9rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }
        .poem-meta {
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
            color: #1f2937;
        }
        .section-label {
            font-size: 1rem;
            font-weight: 800;
            margin-top: 0.6rem;
            margin-bottom: 0.35rem;
        }
        .poem-content {
            font-size: 1.18rem;
            line-height: 1.9;
            font-weight: 700;
            white-space: pre-wrap;
        }
        .section-body {
            font-size: 1.08rem;
            line-height: 1.9;
            font-weight: 400;
            white-space: pre-wrap;
        }
        .filter-note {
            color: #4b5563;
            font-size: 0.95rem;
        }
        @media (max-width: 640px) {
            .block-container {
                padding-top: calc(4rem + env(safe-area-inset-top, 0px));
            }
            .poem-title {
                font-size: 1.55rem;
            }
            .poem-content {
                font-size: 1rem;
                line-height: 1.75;
            }
            .section-body {
                font-size: 1rem;
                line-height: 1.75;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def render_top_nav():
    nav_left, nav_right = st.columns(2)
    with nav_left:
        if st.button("诗词", use_container_width=True):
            st.session_state["active_page"] = "诗词"
            st.rerun()
    with nav_right:
        if st.button("AI Podcasts", use_container_width=True):
            st.session_state["active_page"] = "Podcasts"
            st.rerun()

if st.session_state["active_page"] == "Podcasts":
    st.title("AI Podcasts")
    render_top_nav()
    st.markdown("---")
    st.write("Podcast content page")
    st.info("Eps 1: LLM Wiki - Building Smarter Knowledge Bases with LLMs. \n [Listen here](https://www.youtube.com/watch?v=0g1k5J8X9xA)")
    st.info("Eps 2: Deep Agents – The Ultimate Agent Harness for Long-Horizon Tasks. \n [Listen here](https://www.youtube.com/watch?v=0g1k5J8X9xA)")
    st.info("Eps 3: Software Symposium: Exploring Collaboration, Innovation, and Practical Learning. \n [Listen here](https://www.youtube.com/watch?v=0g1k5J8X9xA)")
    st.info("Eps 4: Inside AI's Mind: Anthropic’s paper on exploring the Hidden Workspace of Language Models. \n [Listen here](https://www.youtube.com/watch?v=0g1k5J8X9xA)")
    st.info("Eps 5: Super Agents in Enterprise AI: Lessons and Future Directions. \n [Listen here](https://www.youtube.com/watch?v=0g1k5J8X9xA)")
    st.info("Eps 6: Human-as-Humanoid — Teaching Robots with Human Videos. \n [Listen here](https://www.youtube.com/watch?v=0g1k5J8X9xA)")
    st.info("Eps 7: GPT-Live: OpenAI’s Leap to Human-Like Conversations. \n [Listen here](https://www.youtube.com/watch?v=0g1k5J8X9xA)")
    st.stop()

st.title("诗词")
render_top_nav()
#st.markdown("---")
with st.expander("Filters and Browse", expanded=True):
    st.markdown("<div class='filter-note'>Designed for phone-sized screens: filters, poem picker, and navigation stay in the main page.</div>", unsafe_allow_html=True)

    top_left, top_right = st.columns(2)
    with top_left:
        selected_dynasty = st.selectbox("朝代", options=DYNasty_OPTIONS, index=0)
    with top_right:
        filter_mode = st.radio("Filter by", options=["Type", "Format"], index=0, horizontal=True)

    mid_left, mid_right = st.columns(2)
    with mid_left:
        if filter_mode == "Type":
            selected_cz_type = st.selectbox("类型", options=CZ_TYPE_OPTIONS, index=0)
            selected_format = None
        else:
            selected_format = st.selectbox("格式", options=FORMAT_OPTIONS, index=0)
            selected_cz_type = None
    with mid_right:
        keyword = st.text_input("关键词", placeholder="Search in title or content")

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

    if not filtered_poems:
        st.warning("No poems match the selected filters.")
        st.stop()

    poem_labels = [
        f"{str(p.get('name', '')).strip()} - {str(p.get('author', '')).strip()}"
        for p in filtered_poems
    ]

    selected_idx, selected_poem = sync_selected_poem(filtered_poems, poem_labels)

    prev_col, next_col = st.columns(2)
    with prev_col:
        st.button(
            "Previous",
            use_container_width=True,
            on_click=move_selected_poem,
            args=(-1, poem_labels),
        )
    with next_col:
        st.button(
            "Next",
            use_container_width=True,
            on_click=move_selected_poem,
            args=(1, poem_labels),
        )

    if filter_mode == "Type" and selected_cz_type == "词牌":
        selected_cipai_item = find_cipai_desc(selected_poem.get("name", ""), cipai_desc_data)
        selected_cipai_name = extract_cipai_name(selected_poem.get("name", ""))
        st.markdown("---")
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

#st.markdown("<div class='section-label'>content</div>", unsafe_allow_html=True)
st.markdown(f"<div class='poem-content'>{content}</div>", unsafe_allow_html=True)

with st.expander("Read Aloud", expanded=False):
    include_translate_audio = st.checkbox("Include translate", value=False)
    include_notes_audio = st.checkbox("Include notes", value=False)
    include_author_audio = st.checkbox("Include author", value=True)
    text_to_read = build_read_aloud_text(
        name=name,
        dynasty=dynasty,
        author=author,
        content=content,
        translate_text=translate_text,
        notes_text=notes_text,
        author_lifetime=author_lifetime,
        author_describe=author_describe,
        include_translate=include_translate_audio,
        include_notes=include_notes_audio,
        include_author_intro=include_author_audio,
    )
    render_read_aloud_controls(text_to_read)

st.markdown("---")

if translate_text:
    st.markdown("<div class='section-label'>译文</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-body'>{translate_text}</div>", unsafe_allow_html=True)

if notes_text:
    st.markdown("<div class='section-label'>注释</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-body'>{notes_text}</div>", unsafe_allow_html=True)

if appreciation_text:
    with st.expander("appreciation (hide/show)", expanded=False):
        st.markdown(f"<div class='section-body'>{appreciation_text}</div>", unsafe_allow_html=True)

st.markdown("<div class='section-label'>作者</div>", unsafe_allow_html=True)
if author_intro:
    if author_lifetime:
        st.markdown(f"<div class='section-body'>{author_lifetime}</div>", unsafe_allow_html=True)
    else:
        st.info("No lifetime information found.")

    if author_describe:
        with st.expander("作者介绍", expanded=False):
            st.markdown(f"<div class='section-body'>{author_describe}</div>", unsafe_allow_html=True)
    else:
        st.info("No describe information found.")
else:
    st.info("No author introduction found for this author.")
