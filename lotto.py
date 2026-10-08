import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎰", layout="centered")

# 로또 공 색상 스타일 정의 (실제 로또 공 색상 기준)
LOTTO_BALL_STYLE = """
<style>
.lotto-container {
    display: flex;
    gap: 10px;
    margin-bottom: 15px;
    align-items: center;
}
.lotto-ball {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
    font-size: 18px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}
/* 로또 번호별 실제 공 색상 기준 */
.ball-yellow { background-color: #fbc02d; color: black; } /* 1 ~ 10 */
.ball-blue   { background-color: #1e88e5; }               /* 11 ~ 20 */
.ball-red    { background-color: #e53935; }               /* 21 ~ 30 */
.ball-gray   { background-color: #8e24aa; }               /* 31 ~ 40 */
.ball-green  { background-color: #43a047; }               /* 41 ~ 45 */
</style>
"""
st.markdown(LOTTO_BALL_STYLE, unsafe_allow_html=True)


# 로또 번호에 맞는 색상 클래스를 반환하는 함수
def get_ball_color_class(number):
    if number <= 10:
        return "ball-yellow"
    elif number <= 20:
        return "ball-blue"
    elif number <= 30:
        return "ball-red"
    elif number <= 40:
        return "ball-gray"
    else:
        return "ball-green"


# 세션 상태(Session State) 초기화
if "lotto_sets" not in st.session_state:
    st.session_state.lotto_sets = []

# 화면 제목
st.title("🎰 로또 번호 생성기")
st.write("버튼을 누를 때마다 중복 없는 6개 번호 세트가 생성됩니다. (최대 5세트)")

# UI 레이아웃 (버튼 배치)
col1, col2 = st.columns([1, 1])

with col1:
    # 로또번호 생성 버튼
    if st.button("🎲 로또번호 생성", use_container_width=True):
        if len(st.session_state.lotto_sets) < 5:
            # 1~45 사이 중복 없는 6개 번호 추출 후 오름차순 정렬
            new_numbers = sorted(random.sample(range(1, 46), 6))
            st.session_state.lotto_sets.append(new_numbers)
        else:
            st.warning("최대 5개의 로또 번호 세트까지만 생성할 수 있습니다.")

with col2:
    # 초기화 버튼
    if st.button("🔄 전체 초기화", use_container_width=True):
        st.session_state.lotto_sets = []
        st.rerun()

st.divider()

# 생성된 로또 번호 세트 화면에 출력
if st.session_state.lotto_sets:
    st.subheader("📌 생성된 번호 목록")
    for idx, numbers in enumerate(st.session_state.lotto_sets, start=1):
        # HTML을 이용해 공 모양 UI 생성
        balls_html = f"<b>{idx}회차:</b>&nbsp;&nbsp;"
        for num in numbers:
            color_class = get_ball_color_class(num)
            balls_html += f'<div class="lotto-ball {color_class}">{num}</div>'

        st.markdown(
            f'<div class="lotto-container">{balls_html}</div>',
            unsafe_allow_html=True,
        )
else:
    st.info("상단의 [로또번호 생성] 버튼을 눌러 번호를 생성해 보세요!")

