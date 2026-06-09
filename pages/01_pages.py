import streamlit as st

# 페이지 설정
st.set_page_config(page_title="통합과학1 생물 생기부 작성기", page_icon="🧬", layout="centered")

# 제목 및 설명
st.title("🧬 통합과학1 생물 생기부 작성 도움 장치")
st.write("학번과 이름을 입력하면 2022 개정 교육과정 기준의 통합과학1 생물 영역 학습 성취 내용을 생성합니다.")

st.markdown("---")

# 입력 폼
with st.form(key="student_info_form"):
    col1, col2 = st.columns(2)
    with col1:
        student_id = st.text_input("학번", placeholder="예: 10325")
    with col2:
        student_name = st.text_input("이름", placeholder="예: 홍길동")
    
    submit_button = st.form_submit_button(label="생기부 문구 생성하기")

# 결과 출력
if submit_button:
    if not student_id or not student_name:
        st.warning("⚠️ 학번과 이름을 모두 입력해 주세요.")
    else:
        st.success("✨ 생기부 참고 문구가 생성되었습니다!")
        
        # 기본 탑재용 문구 구성 (2022 개정 교육과정 통합과학1 생명과학 영역 반영)
        raw_text = (
            f"({student_id} {student_name}) 2022 개정 교육과정 고등학교 '통합과학1'의 "
            f"생명과학 영역(생명 시스템의 기본 단위, 세포막을 통한 물질 출입, 세포 내 정보의 흐름 등)에 대한 "
            f"주요 개념을 충실히 학습함. 생명 시스템을 구성하는 세포의 구조와 기능을 이해하고, "
            f"다양한 탐구 활동에 적극적으로 참여하며 과학적 탐구 능력을 보여줌."
        )
        
        # 결과 표시 구역
        st.subheader("📋 생성된 문구 (복사하여 사용하세요)")
        st.text_area(label="결과창", value=raw_text, height=120)
        
        # 팁 안내
        st.info("💡 **Tip:** 위 문구를 바탕으로 학생의 개별적인 발표 주제, 실험 참여 태도, 탐구 활동 구체적 내용을 추가하시면 더욱 훌륭한 세특 문장이 완성됩니다.")
