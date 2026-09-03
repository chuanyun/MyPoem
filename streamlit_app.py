import json
import hashlib
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# ---- My App --------

st.set_page_config(page_title="小小学贯中西", page_icon="🌟", layout="wide")

if "active_page" not in st.session_state:
    st.session_state["active_page"] = "上学啦"

def render_top_nav():
    #nav_left, nav_center,nav_right = st.columns(3)
    nav_left, nav_center = st.columns(2)
    with nav_left:
        if st.button("诗词", use_container_width=True):
            st.session_state["active_page"] = "诗词"
            st.rerun()
    with nav_center:
        if st.button("上学啦", use_container_width=True):
            st.session_state["active_page"] = "上学啦"
            st.rerun()
    # with nav_right:
    #         if st.button("Stocks", use_container_width=True):
    #             st.session_state["active_page"] = "Stocks"
    #             st.rerun()

if st.session_state["active_page"] == "上学啦":
    st.title("上学啦")
    render_top_nav()
    st.markdown("---")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🎵 Music", "📖 Readings", " Literacy",  "🧮 Math"])
    
    with tab1: #music
        st.info("2026 K - I love mountains. \n")
        st.markdown(
            """
            <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
              <iframe
                src="https://www.youtube.com/embed/mmjbF3A30eQ?si=m7-_bxUurWzIluq2"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
                style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
              ></iframe>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with tab2: #readings
    
        st.info("2026 Sep K - In the Middle of Fall | Kevin Henkes\n")
        st.markdown(
    """
    <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe
        src="https://www.youtube.com/embed/luYR13s_Mvg"
        title="In the Middle of Fall - Read Aloud Children's Book"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
      ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

        st.markdown("---")
        st.info("2026 K - Hello, Fall! | Deborah Diesen\n")
        st.markdown(
    """
    <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe
        src="https://www.youtube.com/embed/jkLK2a3Ca9Q"
        title="Hello, Fall! | Deborah Diesen"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
      ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)


        st.markdown("---")
        st.info("2026 K - Splat the Cat and the Pumpkin-Picking Plan | Rob Scotton\n")
        st.markdown(
    """
    <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe
        src="https://www.youtube.com/embed/W8El2WrvgqE"
        title="Splat the Cat and the Pumpkin-Picking Plan | Rob Scotton"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
      ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

        st.markdown("---")
        st.info("2026 K - A Tree for All Seasons | Robin Bernard\n")
        st.markdown(
    """
    <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe
        src="https://www.youtube.com/embed/9X-Pm9jT6uA"
        title="A Tree for All Seasons | Robin Bernard"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
      ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)


        st.markdown("---")
        st.info("2026 K - From Seed to Pumpkin | Wendy Pfeffer\n")
        st.markdown(
    """
    <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe
        src="https://www.youtube.com/embed/I0poArP3YCg"
        title="From Seed to Pumpkin | Wendy Pfeffer"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
      ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)


        st.markdown("---")
        st.info("2026 K - Curious George: Curious About Fall | H. A. Rey\n")
        st.markdown(
    """
    <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe
        src="https://www.youtube.com/embed/a6FPYkXVj0w"
        title="Curious George: Curious About Fall | H. A. Rey"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
      ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)



        st.markdown("---")
        st.info("2026 K - Pete the Cat: Falling for Autumn | Kimberly & James Dean\n")
        st.markdown(
    """
    <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
      <iframe
        src="https://www.youtube.com/embed/mAF5iF-_JdM"
        title="Pete the Cat: Falling for Autumn | Kimberly & James Dean"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen
        style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
      ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)


        st.info("2026 K - The Day You Begin \n")

        st.markdown("---")

        st.info("2026 K - Peanut Butter and Homework Sandwiches \n")

        st.markdown("---")

        st.info("2026 K - The RECESS QUEEN by Alexis O'Neill and Laura Huliska-Beith \n")

        st.markdown("---")


        st.info("2026 K - Chrysanthemum Storytime Read Aloud | Learning to Love Your Name \n")
        st.markdown(
            """
            <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
              <iframe
                src="https://www.youtube.com/embed/dKQQPBSuKuU"
                title="Chrysanthemum Storytime Read Aloud | Learning to Love Your Name"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
                style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
              ></iframe>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        st.info("2026 K - We are all wonders \n")
        st.markdown(
            """
            <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
              <iframe
                src="https://www.youtube.com/embed/b2zG_lb31y0?si=fteENgH1Ksa8nCiJ"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
                style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
              ></iframe>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        st.info("2026 K - (3Y) Letter, Sound, and Picture Identification - Beat the Teach Game \n")
        st.markdown(
            """
            <div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;">
              <iframe
                src="https://www.youtube.com/embed/ntBi4mtolCM?si=HM8Wosr9DJXTLQib"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
                style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:8px;"
              ></iframe>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with tab3: #Literacy
        st.write("Coming soon...")

    with tab4: #math
        st.write("Coming soon...")

    st.stop()


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


def render_threejs_scene(poem_title, poem_content, poem_translate=""):
    content_text = str(poem_content or "")
    translate_text = str(poem_translate or "")
    primary_text = translate_text if translate_text.strip() else content_text
    all_text = f"{content_text}\n{translate_text}".strip()
    text_lower = all_text.lower()

    def has_any(text, words):
        return any(word in text for word in words)

    has_sun = has_any(all_text, ["夕阳", "落日", "斜阳", "日", "白日", "朝阳"]) or has_any(
        text_lower, ["sun", "sunset", "sunrise"]
    )
    has_moon = has_any(all_text, ["月", "明月", "月光", "月色", "寒月"]) or has_any(text_lower, ["moon", "moonlight"])
    has_river = has_any(all_text, ["黄河", "长江", "江", "河", "海", "流水", "波", "浪", "溪"]) or has_any(
        text_lower, ["river", "sea", "ocean", "water"]
    )
    has_mountain = has_any(all_text, ["山", "峰", "岭", "崖", "川"]) or has_any(text_lower, ["mountain", "cliff", "hill"])
    has_tower = has_any(all_text, ["楼", "城楼", "塔", "台", "亭", "登"]) or has_any(text_lower, ["tower", "pavilion"])
    has_rain = has_any(all_text, ["雨", "细雨", "夜雨", "风雨"]) or has_any(text_lower, ["rain", "drizzle"])
    has_snow = has_any(all_text, ["雪", "飞雪", "冰", "寒"]) or has_any(text_lower, ["snow", "ice"])
    has_wind = has_any(all_text, ["风", "秋风", "春风", "北风"]) or has_any(text_lower, ["wind", "breeze", "gust"])
    has_frontier = has_any(all_text, ["塞", "边", "关", "胡", "沙", "漠"]) or has_any(text_lower, ["frontier", "desert", "sand"])
    has_flower = has_any(all_text, ["花", "桃", "梅", "柳", "荷"]) or has_any(text_lower, ["flower", "blossom", "lotus", "willow"])
    has_cloud = has_any(all_text, ["云", "烟", "草"]) or has_any(text_lower, ["cloud", "mist", "fog", "grass"])
    has_building = has_any(all_text, ["城", "桥", "寺"]) or has_any(text_lower, ["city", "bridge", "temple"])
    has_tree = has_any(all_text, ["柳", "树", "松", "桃"]) or has_any(text_lower, ["tree", "pine", "willow", "peach"])
    has_animal = has_any(all_text, ["马", "鸟", "黄莺", "鹤", "黄鹂", "燕"]) or has_any(text_lower, ["horse", "bird", "oriole", "crane"])
    has_people = has_any(all_text, ["美人", "妾", "人", "客", "翁", "叟", "君", "郎", "夫", "童子", "姑", "女", "少妇", "红颜"]) or has_any(
        text_lower, ["lady", "person", "guest", "old man", "gentleman", "boy", "girl"]
    )
    has_transport = has_any(all_text, ["车", "舟", "船"]) or has_any(text_lower, ["cart", "carriage", "boat", "ship"])

    tree_willow = has_any(all_text, ["柳"])
    tree_pine = has_any(all_text, ["松"])
    tree_peach = has_any(all_text, ["桃"])
    animal_horse = has_any(all_text, ["马"])
    animal_bird = has_any(all_text, ["鸟", "黄莺", "鹤", "黄鹂", "燕"])
    animal_crane = has_any(all_text, ["鹤"])
    people_lady = has_any(all_text, ["美人", "妾", "少妇", "红颜"])
    people_old = has_any(all_text, ["翁", "叟"])
    people_child = has_any(all_text, ["童子"])
    people_girl = has_any(all_text, ["姑", "女"])
    transport_boat = has_any(all_text, ["舟", "船"])
    transport_cart = has_any(all_text, ["车"])

    season = "neutral"
    if has_any(all_text, ["春", "桃", "柳", "燕"]):
        season = "spring"
    elif has_any(all_text, ["夏", "荷", "暑"]):
        season = "summer"
    elif has_any(all_text, ["秋", "霜", "落叶"]):
        season = "autumn"
    elif has_any(all_text, ["冬", "雪", "冰", "寒"]):
        season = "winter"

    tone = "day"
    if has_moon or has_any(all_text, ["夜", "暮", "暗", "灯"]):
        tone = "night"
    if has_sun and has_any(all_text, ["夕", "落日", "残阳"]):
        tone = "sunset"

    seed_hex = hashlib.md5((str(poem_title) + "|" + primary_text).encode("utf-8")).hexdigest()[:8]

    payload = json.dumps(
        {
            "title": str(poem_title or ""),
            "sceneText": primary_text,
            "seed": int(seed_hex, 16),
            "tone": tone,
            "season": season,
            "hasSun": has_sun,
            "hasMoon": has_moon,
            "hasRiver": has_river,
            "hasMountain": has_mountain,
            "hasTower": has_tower,
            "hasRain": has_rain,
            "hasSnow": has_snow,
            "hasWind": has_wind,
            "hasFrontier": has_frontier,
            "hasFlower": has_flower,
            "hasCloud": has_cloud,
            "hasBuilding": has_building,
            "hasTree": has_tree,
            "hasAnimal": has_animal,
            "hasPeople": has_people,
            "hasTransport": has_transport,
            "treeWillow": tree_willow,
            "treePine": tree_pine,
            "treePeach": tree_peach,
            "animalHorse": animal_horse,
            "animalBird": animal_bird,
            "animalCrane": animal_crane,
            "peopleLady": people_lady,
            "peopleOld": people_old,
            "peopleChild": people_child,
            "peopleGirl": people_girl,
            "transportBoat": transport_boat,
            "transportCart": transport_cart,
        },
        ensure_ascii=False,
    )

    block_id = "three_scene_" + hashlib.md5((str(poem_title) + primary_text).encode("utf-8")).hexdigest()[:10]

    components.html(
        f"""
        <div id="{block_id}" style="width: 100%; height: 420px; border-radius: 14px; overflow: hidden; border: 1px solid #e5e7eb; background: linear-gradient(180deg, #d5ecff 0%, #eff7ff 100%);"></div>
        <script src="https://unpkg.com/three@0.160.0/build/three.min.js"></script>
        <script>
            (() => {{
                const data = {payload};
                const container = document.getElementById('{block_id}');
                if (!container) {{
                    return;
                }}

                function showError(msg) {{
                    container.innerHTML = '<div style="padding:14px;color:#7f1d1d;background:#fee2e2;font:14px -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif;">Scene failed to load: ' + msg + '</div>';
                }}

                const setupScene = () => {{
                    try {{
                        const THREE = window.THREE;
                        if (!THREE) {{
                            showError('Three.js unavailable (network/CSP).');
                            return;
                        }}

                        const width = Math.max(container.clientWidth || 0, 360);
                        const height = Math.max(container.clientHeight || 0, 320);

                        const rand = (() => {{
                            let s = (data.seed >>> 0) || 1;
                            return () => {{
                                s = (1664525 * s + 1013904223) >>> 0;
                                return s / 4294967296;
                            }};
                        }})();

                        let skyTop = 0x8fd0ff;
                        let skyBottom = 0xeff7ff;
                        let fogColor = 0xbdd7ee;
                        let groundColor = data.hasFrontier ? 0xc9aa74 : 0xc7b58a;
                        let waterColor = data.hasRiver ? 0x3e8fd1 : 0x6aa8dc;
                        let sunColor = data.hasSun ? 0xff9f43 : 0xffe3a3;

                        if (data.tone === 'night') {{
                            skyTop = 0x12203f;
                            skyBottom = 0x1e3259;
                            fogColor = 0x2a3f6b;
                            groundColor = data.hasFrontier ? 0x7d6a4b : 0x5e6a72;
                            waterColor = 0x2f5f98;
                        }} else if (data.tone === 'sunset') {{
                            skyTop = 0xffb36c;
                            skyBottom = 0xffdfb3;
                            fogColor = 0xe3b588;
                            sunColor = 0xff7e35;
                            waterColor = data.hasRiver ? 0x5b8fc3 : 0x7ca2c8;
                        }}

                        if (data.season === 'spring') {{
                            groundColor = 0x8cab76;
                        }}
                        if (data.season === 'winter') {{
                            groundColor = 0xd6dde8;
                            waterColor = 0x8eb1ce;
                        }}

                        const scene = new THREE.Scene();
                        scene.fog = new THREE.Fog(fogColor, 80, 260);

                        const movingBirds = [];
                        const movingBoats = [];
                        const movingCarts = [];
                        const movingClouds = [];
                        const movingPeople = [];
                        const movingHorses = [];

                        const camera = new THREE.PerspectiveCamera(55, width / height, 0.1, 800);
                        camera.position.set(0, 16, 56);

                        const renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
                        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
                        renderer.setSize(width, height);
                        renderer.setClearColor(skyBottom, 1);
                        container.innerHTML = '';
                        container.appendChild(renderer.domElement);

                        const sky = new THREE.Mesh(
                            new THREE.SphereGeometry(320, 24, 24),
                            new THREE.MeshBasicMaterial({{
                                color: skyTop,
                                side: THREE.BackSide,
                                fog: false,
                            }})
                        );
                        scene.add(sky);

                        const ambient = new THREE.AmbientLight(0xffffff, 0.65);
                        scene.add(ambient);

                        const sun = new THREE.Mesh(
                            new THREE.SphereGeometry(4.2, 32, 32),
                            new THREE.MeshStandardMaterial({{ color: sunColor, emissive: sunColor, emissiveIntensity: 0.55 }})
                        );
                        sun.position.set(-24, 18, -50);
                        if (data.hasSun || data.tone !== 'night') {{
                            scene.add(sun);
                        }}

                        const sunGlow = new THREE.PointLight(sunColor, 1.9, 170, 2);
                        sunGlow.position.copy(sun.position);
                        if (data.hasSun || data.tone !== 'night') {{
                            scene.add(sunGlow);
                        }}

                        if (data.hasMoon || data.tone === 'night') {{
                            const moon = new THREE.Mesh(
                                new THREE.SphereGeometry(3.6, 24, 24),
                                new THREE.MeshStandardMaterial({{ color: 0xeaf1ff, emissive: 0xcdd9ff, emissiveIntensity: 0.35 }})
                            );
                            moon.position.set(18, 22, -60);
                            scene.add(moon);

                            const moonLight = new THREE.PointLight(0xbfd3ff, 0.9, 180, 2);
                            moonLight.position.copy(moon.position);
                            scene.add(moonLight);

                            const starGeo = new THREE.BufferGeometry();
                            const starPoints = [];
                            for (let i = 0; i < 120; i++) {{
                                starPoints.push((rand() - 0.5) * 180, 18 + rand() * 42, -80 + rand() * 40);
                            }}
                            starGeo.setAttribute('position', new THREE.Float32BufferAttribute(starPoints, 3));
                            const stars = new THREE.Points(
                                starGeo,
                                new THREE.PointsMaterial({{ color: 0xf5f8ff, size: 0.8, sizeAttenuation: true }})
                            );
                            scene.add(stars);
                        }}

                        function createMountain(x, y, z, w, h, color) {{
                            const g = new THREE.ConeGeometry(w, h, 4);
                            const m = new THREE.MeshStandardMaterial({{ color, flatShading: true }});
                            const mesh = new THREE.Mesh(g, m);
                            mesh.position.set(x, y, z);
                            mesh.rotation.y = Math.PI * 0.25;
                            return mesh;
                        }}

                        if (data.hasMountain || rand() > 0.35) {{
                            scene.add(createMountain(-30, 1, -70, 16 + rand() * 10, 18 + rand() * 12, 0x566b84));
                            scene.add(createMountain(-10, 2, -74, 15 + rand() * 9, 16 + rand() * 11, 0x5f7690));
                            scene.add(createMountain(15, 1, -72, 16 + rand() * 11, 18 + rand() * 12, 0x4f6580));
                            scene.add(createMountain(36, 2, -76, 14 + rand() * 10, 15 + rand() * 10, 0x5d7390));
                        }}

                        let river = null;
                        if (data.hasRiver || rand() > 0.45) {{
                            river = new THREE.Mesh(
                                new THREE.PlaneGeometry(140, 34, 90, 18),
                                new THREE.MeshStandardMaterial({{ color: waterColor, transparent: true, opacity: 0.9 }})
                            );
                            river.rotation.x = -Math.PI / 2;
                            river.position.set(8, -1.4, -20);
                            scene.add(river);
                        }}

                        const ground = new THREE.Mesh(
                            new THREE.PlaneGeometry(220, 160),
                            new THREE.MeshStandardMaterial({{ color: groundColor }})
                        );
                        ground.rotation.x = -Math.PI / 2;
                        ground.position.y = -1.8;
                        scene.add(ground);

                        function addCloud(x, y, z, scale = 1) {{
                            const group = new THREE.Group();
                            const cloudMat = new THREE.MeshStandardMaterial({{
                                color: data.tone === 'night' ? 0xd9e3ff : 0xfafcff,
                                transparent: true,
                                opacity: data.tone === 'night' ? 0.6 : 0.78,
                            }});

                            const puffs = [
                                [-1.6, 0.0, 0.0, 1.2],
                                [-0.2, 0.4, 0.0, 1.55],
                                [1.2, 0.1, 0.0, 1.15],
                            ];
                            for (const [px, py, pz, s] of puffs) {{
                                const puff = new THREE.Mesh(new THREE.SphereGeometry(s, 14, 12), cloudMat);
                                puff.position.set(px, py, pz);
                                puff.scale.set(1.25, 0.78, 1.0);
                                group.add(puff);
                            }}

                            group.scale.set(scale, scale, scale);
                            group.position.set(x, y, z);
                            scene.add(group);
                            movingClouds.push({{ group, baseX: x, speed: 0.08 + rand() * 0.08, phase: rand() * Math.PI * 2 }});
                        }}

                        function addBuilding(x, z, type = 'city') {{
                            const group = new THREE.Group();
                            const stone = new THREE.MeshStandardMaterial({{ color: 0x8f7b64 }});
                            const wood = new THREE.MeshStandardMaterial({{ color: 0x6d4f38 }});
                            const roofMat = new THREE.MeshStandardMaterial({{ color: 0x4a3320, flatShading: true }});

                            if (type === 'bridge') {{
                                const bridge = new THREE.Mesh(new THREE.BoxGeometry(12, 1.3, 3.2), stone);
                                bridge.position.set(0, 1.4, 0);
                                group.add(bridge);
                                for (const lx of [-4.2, -1.4, 1.4, 4.2]) {{
                                    const arch = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 2.5, 8), stone);
                                    arch.position.set(lx, 0.25, 0);
                                    group.add(arch);
                                }}
                            }} else if (type === 'temple') {{
                                const hall = new THREE.Mesh(new THREE.BoxGeometry(8.5, 4.5, 6.2), wood);
                                hall.position.set(0, 2.4, 0);
                                group.add(hall);
                                const roof = new THREE.Mesh(new THREE.ConeGeometry(6.2, 2.6, 4), roofMat);
                                roof.position.set(0, 6.2, 0);
                                roof.rotation.y = Math.PI / 4;
                                group.add(roof);
                            }} else {{
                                const wall = new THREE.Mesh(new THREE.BoxGeometry(10.5, 6.2, 5.8), stone);
                                wall.position.set(0, 3.1, 0);
                                group.add(wall);
                                const gate = new THREE.Mesh(new THREE.BoxGeometry(3.0, 3.2, 6.0), wood);
                                gate.position.set(0, 1.65, 0.02);
                                group.add(gate);
                            }}

                            group.position.set(x, -1.8, z);
                            scene.add(group);
                        }}

                        function addTree(x, z, style = 'normal') {{
                            const trunk = new THREE.Mesh(
                                new THREE.CylinderGeometry(0.35, 0.55, 4.2, 8),
                                new THREE.MeshStandardMaterial({{ color: 0x6a4b2f }})
                            );
                            trunk.position.set(x, 0.2, z);
                            scene.add(trunk);

                            const crownColor = style === 'peach' ? 0xf3b7c6 : (style === 'pine' ? 0x3f6742 : 0x5d8a57);
                            const crownH = style === 'willow' ? 5.6 : 4.0;
                            const crownW = style === 'pine' ? 2.7 : 3.5;
                            const crown = new THREE.Mesh(
                                new THREE.ConeGeometry(crownW, crownH, 10),
                                new THREE.MeshStandardMaterial({{ color: crownColor }})
                            );
                            crown.position.set(x, 4.6, z);
                            scene.add(crown);

                            if (style === 'willow') {{
                                for (let i = 0; i < 6; i++) {{
                                    const strand = new THREE.Mesh(
                                        new THREE.CylinderGeometry(0.04, 0.06, 2.0 + rand() * 1.2, 6),
                                        new THREE.MeshStandardMaterial({{ color: 0x6d9a63 }})
                                    );
                                    strand.position.set(x + (rand() - 0.5) * 2.2, 3.0, z + (rand() - 0.5) * 2.2);
                                    scene.add(strand);
                                }}
                            }}
                        }}

                        function addPerson(x, z, variant = 'normal') {{
                            const group = new THREE.Group();
                            const bodyColor = variant === 'lady' ? 0xc86f8b : (variant === 'old' ? 0x7a665a : 0x5c6c8d);
                            const robeHeight = variant === 'child' ? 3.0 : 3.8;
                            const shoulderWidth = variant === 'child' ? 0.95 : 1.15;

                            const head = new THREE.Mesh(
                                new THREE.SphereGeometry(0.72, 16, 16),
                                new THREE.MeshStandardMaterial({{ color: 0xf3d3b3 }})
                            );
                            head.position.set(0, robeHeight + 0.95, 0);
                            group.add(head);

                            const robe = new THREE.Mesh(
                                new THREE.CylinderGeometry(shoulderWidth * 0.58, shoulderWidth, robeHeight, 18),
                                new THREE.MeshStandardMaterial({{ color: bodyColor }})
                            );
                            robe.position.set(0, robeHeight * 0.5, 0);
                            group.add(robe);

                            const shoulder = new THREE.Mesh(
                                new THREE.SphereGeometry(shoulderWidth, 16, 12),
                                new THREE.MeshStandardMaterial({{ color: bodyColor }})
                            );
                            shoulder.scale.set(1, 0.55, 0.65);
                            shoulder.position.set(0, robeHeight, 0);
                            group.add(shoulder);

                            const sleeveGeo = new THREE.CylinderGeometry(0.18, 0.28, 1.7, 10);
                            const sleeveMat = new THREE.MeshStandardMaterial({{ color: bodyColor }});
                            const leftSleeve = new THREE.Mesh(sleeveGeo, sleeveMat);
                            leftSleeve.position.set(-shoulderWidth * 0.95, robeHeight - 0.45, 0);
                            leftSleeve.rotation.z = 0.7;
                            group.add(leftSleeve);

                            const rightSleeve = new THREE.Mesh(sleeveGeo, sleeveMat);
                            rightSleeve.position.set(shoulderWidth * 0.95, robeHeight - 0.45, 0);
                            rightSleeve.rotation.z = -0.7;
                            group.add(rightSleeve);

                            const leftLeg = new THREE.Mesh(
                                new THREE.CylinderGeometry(0.13, 0.16, 1.1, 8),
                                new THREE.MeshStandardMaterial({{ color: 0x2f2b28 }})
                            );
                            leftLeg.position.set(-0.24, 0.1, 0);
                            group.add(leftLeg);

                            const rightLeg = new THREE.Mesh(
                                new THREE.CylinderGeometry(0.13, 0.16, 1.1, 8),
                                new THREE.MeshStandardMaterial({{ color: 0x2f2b28 }})
                            );
                            rightLeg.position.set(0.24, 0.1, 0);
                            group.add(rightLeg);

                            if (variant === 'old') {{
                                const cane = new THREE.Mesh(
                                    new THREE.CylinderGeometry(0.05, 0.05, 2.8, 8),
                                    new THREE.MeshStandardMaterial({{ color: 0x6e5233 }})
                                );
                                cane.position.set(1.0, 1.2, 0.12);
                                cane.rotation.z = -0.15;
                                group.add(cane);
                            }}

                            if (variant === 'lady') {{
                                const hair = new THREE.Mesh(
                                    new THREE.SphereGeometry(0.76, 14, 12),
                                    new THREE.MeshStandardMaterial({{ color: 0x2b211d }})
                                );
                                hair.scale.set(1.02, 0.95, 0.96);
                                hair.position.set(0, robeHeight + 1.0, -0.08);
                                group.add(hair);
                            }}

                            if (variant === 'child') {{
                                group.scale.set(0.82, 0.82, 0.82);
                            }}

                            group.position.set(x, 0, z);
                            scene.add(group);
                            movingPeople.push({{ group, baseY: 0, phase: rand() * Math.PI * 2 }});
                        }}

                        function addBird(x, y, z, isCrane = false) {{
                            const group = new THREE.Group();
                            const wingColor = isCrane ? 0xe8edf5 : 0xf1d56b;
                            const body = new THREE.Mesh(
                                new THREE.SphereGeometry(isCrane ? 0.56 : 0.44, 12, 12),
                                new THREE.MeshStandardMaterial({{ color: wingColor }})
                            );
                            body.position.set(0, 0, 0);
                            group.add(body);

                            const leftWing = new THREE.Mesh(
                                new THREE.BoxGeometry(isCrane ? 1.1 : 0.75, 0.08, 0.34),
                                new THREE.MeshStandardMaterial({{ color: wingColor }})
                            );
                            leftWing.position.set(-(isCrane ? 0.7 : 0.5), 0, 0);
                            group.add(leftWing);

                            const rightWing = new THREE.Mesh(
                                new THREE.BoxGeometry(isCrane ? 1.1 : 0.75, 0.08, 0.34),
                                new THREE.MeshStandardMaterial({{ color: wingColor }})
                            );
                            rightWing.position.set(isCrane ? 0.7 : 0.5, 0, 0);
                            group.add(rightWing);

                            group.position.set(x, y, z);
                            scene.add(group);
                            movingBirds.push({{
                                group,
                                leftWing,
                                rightWing,
                                baseX: x,
                                baseY: y,
                                baseZ: z,
                                radius: 1.0 + rand() * 3.2,
                                speed: 0.6 + rand() * 0.8,
                                phase: rand() * Math.PI * 2,
                            }});
                        }}

                        function addHorse(x, z) {{
                            const horseColor = 0x7a563b;
                            const group = new THREE.Group();

                            const body = new THREE.Mesh(
                                new THREE.BoxGeometry(5.2, 2.0, 1.8),
                                new THREE.MeshStandardMaterial({{ color: horseColor }})
                            );
                            body.position.set(0, 1.6, 0);
                            group.add(body);

                            const neck = new THREE.Mesh(
                                new THREE.BoxGeometry(1.25, 1.9, 0.92),
                                new THREE.MeshStandardMaterial({{ color: horseColor }})
                            );
                            neck.position.set(2.55, 2.55, 0);
                            neck.rotation.z = -0.55;
                            group.add(neck);

                            const head = new THREE.Mesh(
                                new THREE.BoxGeometry(1.45, 1.05, 0.88),
                                new THREE.MeshStandardMaterial({{ color: horseColor }})
                            );
                            head.position.set(3.35, 3.2, 0);
                            head.rotation.z = -0.18;
                            group.add(head);

                            const earGeo = new THREE.ConeGeometry(0.12, 0.45, 6);
                            const leftEar = new THREE.Mesh(earGeo, new THREE.MeshStandardMaterial({{ color: 0x5c402c }}));
                            leftEar.position.set(3.7, 3.95, -0.2);
                            leftEar.rotation.z = -0.2;
                            group.add(leftEar);

                            const rightEar = new THREE.Mesh(earGeo, new THREE.MeshStandardMaterial({{ color: 0x5c402c }}));
                            rightEar.position.set(3.7, 3.95, 0.2);
                            rightEar.rotation.z = -0.2;
                            group.add(rightEar);

                            const mane = new THREE.Mesh(
                                new THREE.BoxGeometry(1.0, 2.0, 0.2),
                                new THREE.MeshStandardMaterial({{ color: 0x3c2a20 }})
                            );
                            mane.position.set(2.1, 2.65, -0.5);
                            mane.rotation.z = -0.55;
                            group.add(mane);

                            const legGeo = new THREE.CylinderGeometry(0.18, 0.22, 2.9, 10);
                            const legMat = new THREE.MeshStandardMaterial({{ color: 0x684733 }});
                            for (const [lx, lz] of [[-1.55, -0.55], [-1.55, 0.55], [1.35, -0.55], [1.35, 0.55]]) {{
                                const leg = new THREE.Mesh(legGeo, legMat);
                                leg.position.set(lx, 0.35, lz);
                                group.add(leg);
                            }}

                            const tail = new THREE.Mesh(
                                new THREE.CylinderGeometry(0.08, 0.18, 2.2, 8),
                                new THREE.MeshStandardMaterial({{ color: 0x2e2118 }})
                            );
                            tail.position.set(-2.75, 2.25, 0);
                            tail.rotation.z = 0.65;
                            group.add(tail);

                            group.position.set(x, 0, z);
                            scene.add(group);
                            movingHorses.push({{ group, baseY: 0, phase: rand() * Math.PI * 2 }});
                        }}

                        function addBoat(x, z) {{
                            const group = new THREE.Group();
                            const hull = new THREE.Mesh(
                                new THREE.CylinderGeometry(1.35, 1.35, 10.2, 14),
                                new THREE.MeshStandardMaterial({{ color: 0x65462f }})
                            );
                            hull.rotation.z = Math.PI / 2;
                            hull.position.set(0, -1.0, 0);
                            group.add(hull);

                            const mast = new THREE.Mesh(
                                new THREE.CylinderGeometry(0.14, 0.14, 5.0, 12),
                                new THREE.MeshStandardMaterial({{ color: 0x6f573f }})
                            );
                            mast.position.set(0.3, 1.1, 0);
                            group.add(mast);

                            const sail = new THREE.Mesh(
                                new THREE.PlaneGeometry(2.8, 2.8),
                                new THREE.MeshStandardMaterial({{ color: 0xf0e6d6, side: THREE.DoubleSide }})
                            );
                            sail.position.set(1.2, 1.3, 0);
                            sail.rotation.y = Math.PI / 2;
                            group.add(sail);

                            group.scale.set(1.2, 1.2, 1.2);

                            group.position.set(x, 0, z);
                            scene.add(group);
                            movingBoats.push({{
                                group,
                                baseX: x,
                                baseY: 0,
                                baseZ: z,
                                drift: 0.3 + rand() * 0.55,
                                phase: rand() * Math.PI * 2,
                            }});
                        }}

                        function addCart(x, z) {{
                            const group = new THREE.Group();
                            const cart = new THREE.Mesh(
                                new THREE.BoxGeometry(5.2, 2.1, 2.8),
                                new THREE.MeshStandardMaterial({{ color: 0x6f4a2e }})
                            );
                            cart.position.set(0, 0.6, 0);
                            group.add(cart);

                            const wheelMat = new THREE.MeshStandardMaterial({{ color: 0x3a2c1f }});
                            const wheels = [];
                            for (const dx of [-0.7, 0.7]) {{
                                for (const dz of [-0.7, 0.7]) {{
                                    const wheel = new THREE.Mesh(new THREE.CylinderGeometry(0.75, 0.75, 0.24, 16), wheelMat);
                                    wheel.rotation.x = Math.PI / 2;
                                    wheel.position.set(dx * 1.9, -0.8, dz * 0.95);
                                    group.add(wheel);
                                    wheels.push(wheel);
                                }}
                            }}

                            group.scale.set(1.15, 1.15, 1.15);

                            group.position.set(x, 0, z);
                            scene.add(group);
                            movingCarts.push({{
                                group,
                                wheels,
                                baseX: x,
                                baseZ: z,
                                speed: 0.28 + rand() * 0.36,
                                phase: rand() * Math.PI * 2,
                            }});
                        }}

                        if (data.hasTree || rand() > 0.7) {{
                            const treeCount = data.hasTree ? 2 + Math.floor(rand() * 3) : 1;
                            for (let i = 0; i < treeCount; i++) {{
                                let style = 'normal';
                                if (data.treeWillow) style = 'willow';
                                else if (data.treePine) style = 'pine';
                                else if (data.treePeach) style = 'peach';
                                addTree(-26 + rand() * 52, -8 + rand() * 26, style);
                            }}
                        }}

                        if (data.hasPeople) {{
                            const peopleCount = 1 + (rand() > 0.7 ? 1 : 0);
                            for (let i = 0; i < peopleCount; i++) {{
                                let variant = 'normal';
                                if (data.peopleLady) variant = 'lady';
                                else if (data.peopleOld) variant = 'old';
                                else if (data.peopleChild) variant = 'child';
                                addPerson(-9 + rand() * 22, 6 + rand() * 11, variant);
                            }}
                        }}

                        if (data.hasAnimal) {{
                            if (data.animalHorse) {{
                                addHorse(-8 + rand() * 14, 8 + rand() * 10);
                            }}
                            if (data.animalBird || rand() > 0.5) {{
                                const birdCount = data.animalCrane ? 2 : 3;
                                for (let i = 0; i < birdCount; i++) {{
                                    addBird(-18 + rand() * 36, 11 + rand() * 11, -22 + rand() * 20, data.animalCrane);
                                }}
                            }}
                        }}

                        if (data.hasTransport) {{
                            if (data.transportBoat && river) {{
                                addBoat(8 + rand() * 16, -17 + rand() * 6);
                            }}
                            if (data.transportCart) {{
                                addCart(-7 + rand() * 18, 9 + rand() * 10);
                            }}
                        }}

                        if (data.hasFlower || data.season === 'spring') {{
                            const flowerMat = new THREE.MeshStandardMaterial({{ color: 0xf3b7c6 }});
                            for (let i = 0; i < 26; i++) {{
                                const flower = new THREE.Mesh(new THREE.SphereGeometry(0.35, 10, 10), flowerMat);
                                flower.position.set((rand() - 0.5) * 46, -1.2, -4 + rand() * 22);
                                scene.add(flower);
                            }}
                        }}

                        if (data.hasCloud || rand() > 0.4) {{
                            const cloudCount = data.hasCloud ? 4 : 2;
                            for (let i = 0; i < cloudCount; i++) {{
                                addCloud(-34 + rand() * 68, 17 + rand() * 11, -74 + rand() * 20, 0.9 + rand() * 0.8);
                            }}
                        }}

                        if (data.hasBuilding) {{
                            if (data.sceneText.includes('桥')) {{
                                addBuilding(6 + rand() * 8, -16 + rand() * 5, 'bridge');
                            }}
                            if (data.sceneText.includes('寺')) {{
                                addBuilding(20 + rand() * 10, -8 + rand() * 6, 'temple');
                            }}
                            if (data.sceneText.includes('城')) {{
                                addBuilding(24 + rand() * 8, -4 + rand() * 5, 'city');
                            }}
                        }}

                        if (data.hasTower || rand() > 0.55) {{
                            const towerGroup = new THREE.Group();
                            const towerBase = new THREE.Mesh(
                                new THREE.BoxGeometry(7 + rand() * 3, 5.5 + rand() * 2, 7 + rand() * 3),
                                new THREE.MeshStandardMaterial({{ color: data.hasFrontier ? 0x8d6a47 : 0x6d4f38 }})
                            );
                            towerBase.position.y = 3;
                            towerGroup.add(towerBase);

                            const topFloor = new THREE.Mesh(
                                new THREE.BoxGeometry(9 + rand() * 2, 3, 9 + rand() * 2),
                                new THREE.MeshStandardMaterial({{ color: 0x8f6742 }})
                            );
                            topFloor.position.y = 7.2;
                            towerGroup.add(topFloor);

                            const roof = new THREE.Mesh(
                                new THREE.ConeGeometry(6.5 + rand() * 1.2, 3.1, 4),
                                new THREE.MeshStandardMaterial({{ color: 0x3f2b1a, flatShading: true }})
                            );
                            roof.position.y = 10.5;
                            roof.rotation.y = Math.PI / 4;
                            towerGroup.add(roof);

                            towerGroup.position.set(data.hasTower ? 18 : 24, -1.8, -5);
                            scene.add(towerGroup);
                        }}

                        let weatherDrops = null;
                        if (data.hasRain || data.hasSnow) {{
                            const weatherGeo = new THREE.BufferGeometry();
                            const points = [];
                            for (let i = 0; i < 300; i++) {{
                                points.push((rand() - 0.5) * 110, rand() * 46, -70 + rand() * 80);
                            }}
                            weatherGeo.setAttribute('position', new THREE.Float32BufferAttribute(points, 3));
                            weatherDrops = new THREE.Points(
                                weatherGeo,
                                new THREE.PointsMaterial({{
                                    color: data.hasSnow ? 0xf8fbff : 0xbfd8f5,
                                    size: data.hasSnow ? 1.6 : 0.8,
                                    transparent: true,
                                    opacity: data.hasSnow ? 0.85 : 0.6,
                                }})
                            );
                            scene.add(weatherDrops);
                        }}

                        let disposed = false;
                        const onResize = () => {{
                            if (disposed) return;
                            const w = Math.max(container.clientWidth || 0, 360);
                            const h = Math.max(container.clientHeight || 0, 320);
                            camera.aspect = w / h;
                            camera.updateProjectionMatrix();
                            renderer.setSize(w, h);
                        }};
                        window.addEventListener('resize', onResize);

                        let t = 0;
                        const animate = () => {{
                            if (disposed) return;
                            t += 0.015;

                            for (const personObj of movingPeople) {{
                                personObj.group.position.y = personObj.baseY + Math.sin(t * 1.8 + personObj.phase) * 0.09;
                                personObj.group.rotation.y = Math.sin(t * 0.7 + personObj.phase) * 0.05;
                            }}

                            for (const horseObj of movingHorses) {{
                                horseObj.group.position.y = horseObj.baseY + Math.sin(t * 2.1 + horseObj.phase) * 0.08;
                                horseObj.group.rotation.y = Math.sin(t * 0.9 + horseObj.phase) * 0.04;
                            }}

                            for (const birdObj of movingBirds) {{
                                const angle = t * birdObj.speed + birdObj.phase;
                                birdObj.group.position.x = birdObj.baseX + Math.cos(angle) * birdObj.radius;
                                birdObj.group.position.z = birdObj.baseZ + Math.sin(angle) * birdObj.radius * 0.55;
                                birdObj.group.position.y = birdObj.baseY + Math.sin(angle * 1.6) * 0.8;
                                birdObj.group.rotation.y = -angle;

                                const flap = Math.sin(t * 9.5 + birdObj.phase) * 0.9;
                                birdObj.leftWing.rotation.z = flap;
                                birdObj.rightWing.rotation.z = -flap;
                            }}

                            for (const boatObj of movingBoats) {{
                                const driftPhase = t * boatObj.drift + boatObj.phase;
                                boatObj.group.position.x = boatObj.baseX + Math.sin(driftPhase) * 1.8;
                                boatObj.group.position.y = boatObj.baseY + Math.sin(driftPhase * 1.4) * 0.18;
                                boatObj.group.rotation.z = Math.sin(driftPhase * 1.2) * 0.05;
                            }}

                            for (const cartObj of movingCarts) {{
                                const movePhase = t * cartObj.speed + cartObj.phase;
                                cartObj.group.position.x = cartObj.baseX + Math.sin(movePhase) * 1.15;
                                cartObj.group.rotation.y = Math.sin(movePhase) * 0.06;
                                for (const wheel of cartObj.wheels) {{
                                    wheel.rotation.y += 0.08;
                                }}
                            }}

                            for (const cloudObj of movingClouds) {{
                                cloudObj.group.position.x = cloudObj.baseX + Math.sin(t * cloudObj.speed + cloudObj.phase) * 3.8;
                            }}

                            if (river) {{
                                const stripePos = river.geometry.attributes.position;
                                for (let i = 0; i < stripePos.count; i++) {{
                                    const x = stripePos.getX(i);
                                    const base = data.hasWind ? 0.3 : 0.2;
                                    const y = Math.sin((x + t * 35) * 0.09) * base + Math.cos((i + t * 8) * 0.02) * 0.06;
                                    stripePos.setY(i, y);
                                }}
                                stripePos.needsUpdate = true;
                            }}

                            if (weatherDrops) {{
                                const p = weatherDrops.geometry.attributes.position;
                                for (let i = 0; i < p.count; i++) {{
                                    const speed = data.hasSnow ? 0.08 : 0.18;
                                    const drift = data.hasWind ? Math.sin(t + i) * 0.03 : 0;
                                    const y = p.getY(i) - speed;
                                    p.setY(i, y < -2 ? 42 + rand() * 4 : y);
                                    p.setX(i, p.getX(i) + drift);
                                }}
                                p.needsUpdate = true;
                            }}

                            if (data.hasSun) {{
                                sun.position.y = 18 + Math.sin(t * 0.65) * 0.9;
                            }}
                            camera.position.x = Math.sin(t * 0.2) * (data.hasFrontier ? 2.4 : 1.2);
                            camera.lookAt(4, data.hasTower ? 5 : 3.4, -24);

                            renderer.render(scene, camera);
                            requestAnimationFrame(animate);
                        }};
                        animate();

                        window.addEventListener('beforeunload', () => {{
                            disposed = true;
                            window.removeEventListener('resize', onResize);
                            renderer.dispose();
                        }});
                    }} catch (err) {{
                        showError((err && err.message) ? err.message : String(err));
                    }}
                }};

                if (window.THREE) {{
                    setupScene();
                    return;
                }}

                const waitStart = Date.now();
                const timer = setInterval(() => {{
                    if (window.THREE) {{
                        clearInterval(timer);
                        setupScene();
                        return;
                    }}
                    if (Date.now() - waitStart > 5000) {{
                        clearInterval(timer);
                        showError('Timeout loading Three.js from CDN.');
                    }}
                }}, 80);
            }})();
        </script>
        """,
        height=430,
    )


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
                        <button id="{block_id}_speak" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #111827; color: #ffffff;">▶️</button>
                        <button id="{block_id}_pause" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #ffffff; color: #111827;">⏸️</button>
                        <button id="{block_id}_resume" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #ffffff; color: #111827;">⏯️</button>
                        <button id="{block_id}_stop" style="padding: 8px 12px; border-radius: 8px; border: 1px solid #d1d5db; background: #ffffff; color: #111827;">⏹️</button>
                    </div>

                    <div style="display: flex; align-items: center; gap: 8px; color: #374151; font-size: 14px;">
                        <label for="{block_id}_rate">Speed</label>
                        <input id="{block_id}_rate" type="range" min="0.3" max="1" step="0.05" value="0.5" style="width: 170px;" />
                        <span id="{block_id}_rate_value">0.50x</span>
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

st.title("诗词")
render_top_nav()
#st.markdown("---")
with st.expander("Filters and Browse", expanded=True):
    #st.markdown("<div class='filter-note'>Designed for phone-sized screens: filters, poem picker, and navigation stay in the main page.</div>", unsafe_allow_html=True)

    top_left, top_right = st.columns(2)
    with top_left:
        selected_dynasty = st.selectbox("朝代", options=DYNasty_OPTIONS, index=0)
    with top_right:
        filter_mode = st.radio("筛选", options=["类型", "格式"], index=0, horizontal=True)

    mid_left, mid_right = st.columns(2)
    with mid_left:
        if filter_mode == "类型":
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
            if filter_mode == "类型"
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

with st.expander("朗诵", expanded=False):
    include_translate_audio = st.checkbox("包括译文", value=False)
    include_notes_audio = st.checkbox("包括注释", value=False)
    include_author_audio = st.checkbox("包括作者简介", value=True)
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

st.markdown("<div class='section-label'>scene</div>", unsafe_allow_html=True)
render_threejs_scene(name, content, translate_text)

#st.markdown("---")

if translate_text:
    st.markdown("<div class='section-label'>译文</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-body'>{translate_text}</div>", unsafe_allow_html=True)

if notes_text:
    st.markdown("<div class='section-label'>注释</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-body'>{notes_text}</div>", unsafe_allow_html=True)

if appreciation_text:
    with st.expander("appreciation (hide/show)", expanded=False):
        st.markdown(f"<div class='section-body'>{appreciation_text}</div>", unsafe_allow_html=True)

st.markdown("<div class='section-label'>作者简介</div>", unsafe_allow_html=True)
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
