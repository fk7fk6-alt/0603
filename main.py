import streamlit as st
import random
import datetime

# 1. 페이지 기본 설정 (가장 상단에 위치해야 합니다)
st.set_page_config(
    page_title="🐾 개팔자가 상팔자! 댕사주 🔮",
    page_icon="🐶",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. 화려한 스타일을 위한 커스텀 CSS 적용
st.markdown("""
    <style>
    /* 전체 배경에 약간의 감성 더하기 */
    .stApp {
        background: linear-gradient(to bottom, #FFF5EE, #FFF0F5);
    }
    /* 메인 타이틀 스타일 */
    .main-title {
        font-size: 3rem !important;
        font-weight: 900;
        color: #FF6B6B;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 5px;
    }
    /* 서브타이틀 스타일 */
    .sub-title {
        font-size: 1.2rem;
        color: #4A4A4A;
        text-align: center;
        margin-bottom: 30px;
    }
    /* 결과 박스 스타일 */
    .result-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 10px 25px rgba(255, 107, 107, 0.15);
        border: 2px solid #FFD1D1;
        margin-top: 20px;
    }
    </style>
""", unsafe_view_menu=False)

# 3. 헤더 영역
st.markdown("<h1 class='main-title'>🔮 🐾 개팔자가 상팔자! 🐾 🔮</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>우리 집 귀염둥이의 생년월일시로 보는 신기방기 댕사주·오행 분석! ✨</p>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=800&q=80", caption="오늘의 주인공은 나야 나! 🐶")

st.divider()

# 4. 사이드바 - 입력 폼
st.sidebar.header("💌 댕댕이 정보 입력")
dog_name = st.sidebar.text_input("🐶 강아지 이름", value="초코")
dog_gender = st.sidebar.radio("⚧ 성별", ["남아 ♂️", "여아 ♀️"], horizontal=True)

st.sidebar.markdown("---")
st.sidebar.subheader("📅 태어난 시간 정보")
birth_date = st.sidebar.date_input("🗓️ 태어난 날짜", datetime.date(2020, 1, 1))
birth_time = st.sidebar.time_input("⏰ 태어난 시간 (모르면 대략 적어주세요!)", datetime.time(12, 0))

# 🔮 사주 분석 데이터 셋
saju_titles = [
    "👑 천상천하 유아독존형 '우주 대스타' 팔자",
    "🍖 평생 고기 걱정 없는 '만석꾼 댕댕이' 팔자",
    "🛋️ 침대가 곧 내 세상, 유유자적 '베짱이 프로 눕방러' 팔자",
    "💖 온 동네 사람들의 심장을 폭행하는 '글로벌 사랑꾼' 팔자",
    "🛡️ 듬직하고 영리한 우리 집 대장님, '용맹무쌍 호위무사' 팔자",
    "🎓 사람 말을 다 알아듣는 '천재 댕선생' 팔자"
]

saju_details = {
    "👑 천상천하 유아독존형 '우주 대스타' 팔자": "태어날 때부터 온 우주의 기운이 우리 댕댕이를 향해 있네요! 🌟 어딜 가나 시선집중! 산책길만 나서도 동네 사람들의 귀여움을 독차지하는 연예인형 팔자입니다. 가끔 고집을 부려도 그것마저 힙함으로 승화시키는 마성의 매력 소유자! 😎",
    "🍖 평생 고기 걱정 없는 '만석꾼 댕댕이' 팔자": "사주에 '간식 복'과 '재물 운'이 가득 차 있습니다! 🥩 간식 창고가 마를 날이 없으며, 보호자가 맛있는 고기를 끊임없이 바치게 만드는 묘한 신통력이 있군요. 평생 먹을 복 하나는 타고난 최고의 상팔자입니다! 츄르와 고기길만 걸으세요! 🍗",
    "🛋️ 침대가 곧 내 세상, 유유자적 '베짱이 프로 눕방러' 팔자": "정말 부러운 유유자적 팔자입니다! 💤 세상만사 태평하며, 가장 폭신한 이불과 베개를 찾아내는 귀신같은 능력이 있습니다. 보호자가 열심히 일하는 모습을 침대 위에서 아련하게 바라보며 '개팔자가 상팔자'임을 온몸으로 증명하는 평화주의자입니다. 🛌",
    "💖 온 동네 사람들의 심장을 폭행하는 '글로벌 사랑꾼' 팔자": "눈빛 한 번으로 모든 사람과 동물의 마음을 녹여버리는 도화살(?) 가득한 치명적인 팔자! 💕 애교가 넘쳐나서 보호자가 화를 낼 수가 없습니다. 사고를 쳐도 꼬리 한 번 흔들면 상황 종료! 사랑을 주고받는 데 타고난 진정한 행복 전도사입니다. 🥰",
    "🛡️ 듬직하고 영리한 우리 집 대장님, '용맹무쌍 호위무사' 팔자": "사주에용맹함과 충성심이 가득합니다! 🎖️ 작은 소리도 놓치지 않고 집을 지키며, 보호자가 우울해 보일 때 귀신같이 다가와 위로해 주는 든든한 보디가드네요. 책임감이 강하고 영리하여 온 가족의 정신적 지주 역할을 합니다. 🦅",
    "🎓 사람 말을 다 알아듣는 '천재 댕선생' 팔자": "댕댕이의 탈을 쓴 사람이 아닐까 의심될 정도로 영리한 사주입니다! 🧠 '앉아', '손'은 기본이고 보호자의 감정과 단어들을 스펀지처럼 흡수합니다. 가끔은 보호자 머리 꼭대기 위에서 밀당을 즐기기도 하는 똑쟁이 중의 똑쟁이 팔자입니다! 🎓"
}

lucky_items = ["황태 북어국 🍲", "소리 나는 삑삑이 인형 🧸", "새로운 냄새가 가득한 풀숲 산책로 🌿", "주인의 최애 수면양말 🧦", "치즈가 들어간 덴탈껌 🧀", "새로 산 푹신한 마약방석 🛋️"]
lucky_colors = ["🔥 열정의 핫핑크", "☀️ 에너제틱 노란색", "🍀 행운을 부르는 초록색", "🌊 마음이 편안해지는 하늘색", "🔮 고귀한 보라색"]

# 5. 메인 화면 작동 버튼
if st.sidebar.button("🔮 댕사주 확인하기! 🔮", use_container_width=True):
    # 애니메이션 효과로 화려함 추가!
    st.balloons()
    st.snow()
    
    # 입력값을 기반으로 일관된 결과를 주기 위해 해시 값 사용
    seed_string = f"{dog_name}{birth_date}{birth_time.hour}{dog_gender}"
    random.seed(seed_string)
    
    selected_saju = random.choice(saju_titles)
    item = random.choice(lucky_items)
    color = random.choice(lucky_colors)
    energy_level = random.randint(80, 100)
    
    # 오행 가상 점수 생성
    wood = random.randint(10, 30)
    fire = random.randint(10, 30)
    earth = random.randint(10, 30)
    metal = random.randint(10, 30)
    water = random.randint(10, 30)
    
    # 6. 결과 출력 영역
    st.markdown(f"### 🐾 {dog_name}의 사주팔자 감정서 결과가 나왔습니다! 🐾")
    
    st.markdown(f"""
    <div class='result-box'>
        <h2 style='text-align: center; color: #FF6B6B;'>{selected_saju}</h2>
        <hr style='border: 1px dashed #FFD1D1;'>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #333333;'>
            {saju_details[selected_saju]}
        </p>
        <br>
        <p style='font-size: 1.05rem;'><b>✨ 성별:</b> {dog_gender}</p>
        <p style='font-size: 1.05rem;'><b>📅 생년월일시:</b> {birth_date} {birth_time.strftime('%H시 %M분')}</p>
        <p style='font-size: 1.05rem;'><b>💖 타고난 귀여움 지수:</b> {energy_level}% / 100% (초과 측정 불가!)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # 행운의 아이템 정보 카드 형태로 배치
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"🍀 **{dog_name}의 행운의 아이템**\n\n👉 {item}")
    with col2:
        st.success(f"🎨 **{dog_name}의 행운의 컬러**\n\n👉 {color}")
        
    st.write("")
    st.markdown("#### 📊 댕댕이 오행(五行) 분석 차트")
    
    # [수정 완료] 중괄호 { } 짝을 올바르게 맞췄습니다.
    chart_data = {
        "🌳 목(나무 - 활동성)": wood,
        "🔥 화(불 - 애교와 열정)": fire,
        "🌱 토(흙 - 듬직함)": earth,
        "💎 금(쇠 - 영리함)": metal,
        "🌊 수(물 - 유연함)": water
    }
    st.bar_chart(chart_data)
    
    st.warning(f"💡 **재미로 보는 {dog_name}의 팔자 총평**: '개팔자가 상팔자'라는 말은 오늘날 {dog_name}(이)를 두고 만든 말임이 틀림없습니다. 보호자님의 극진한 사랑 속에서 평생 행복할 운명이니, 오늘 저녁은 특별히 맛있는 간식을 하사하시는 것이 좋습니다! 🍖✨")

else:
    # 버튼을 누르기 전 대기 화면
    st.info("👈 왼쪽 사이드바에 귀여운 댕댕이의 정보를 입력하고 **[🔮 댕사주 확인하기!]** 버튼을 눌러주세요!")
    
    # 데코레이션용 이모지 박스
    st.markdown("""
        <div style='text-align: center; margin-top: 50px; font-size: 1.2rem; color: #888;'>
            🐶 🐩 🐕 🐾 🦴 🍖 🍼 🧸 🔮 ✨ 🪐 🌟
            <br>
            "댕댕이의 시간은 사람보다 빠르다개! 사주 보고 더 잘해달라개!"
        </div>
    """, unsafe_allow_html=True)
