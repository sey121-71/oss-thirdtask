print(">>> [LOG] 사용자가 페이지를 새로고침하거나 조작 중입니다.")
import streamlit as st
import pandas as pd
import time

@st.cache_data
def load_questions():
    return [
        {"q": "주말에 운동을 한다면?", "a": "팀", "b": "개인", "text_a": "여러명이서 같이 하는 운동", "text_b": "혼자서 즐길 수 있는 운동"},
        {"q": "경기에 임할 때 더 중요한 것은?", "a": "전략", "b": "체력", "text_a": "상대를 파악하는 치밀한 수싸움", "text_b": "한계를 시험하는 폭발적 에너지"},
        {"q": "내가 추구하는 운동의 미학은?", "a": "예술", "b": "팀", "text_a": "군더더기 없는 아름다운 동작", "text_b": "함께해서 만드는 결과"},
        {"q": "규칙에 대한 나의 태도는?", "a": "규칙", "b": "전략", "text_a": "엄격한 규정을 준수하는 정교함", "text_b": "상황에 따라 유연한 임기응변"},
        {"q": "팀워크에서 내가 선호하는 상황은?", "a": "팀", "b": "개인", "text_a": "동료와 소통하며 채워가는 즐거움", "text_b": "내 실력이 곧 결과로 나오는 책임감"},
        {"q": "훈련을 할 때 더 집중하는 부분은?", "a": "체력", "b": "속도", "text_a": "긴 호흡으로 밀어붙이는 지구력", "text_b": "짧고 굵게 쏟아붓는 폭발력"},
        {"q": "새로운 기술을 배울 때 나는?", "a": "규칙", "b": "예술", "text_a": "정해진 매뉴얼대로 정확하게", "text_b": "창의적이고 화려하게 구현하기"},
        {"q": "스포츠 관람 중 더 매력적인 것은?", "a": "속도", "b": "전략", "text_a": "빠른 공수전환", "text_b": "감독의 전술이 맞아떨어지는 순간"},
        {"q": "위기 상황이 닥쳤을 때 나는?", "a": "팀", "b": "개인", "text_a": "주변에 도움을 구하고 협력한다", "text_b": "스스로 마인드 컨트롤하며 해결한다"},
        {"q": "운동 후 가장 뿌듯한 순간은?", "a": "체력", "b": "예술", "text_a": "몸이 녹초가 될 정도로 땀 흘렸을 때", "text_b": "완벽한 폼을 만들어냈을 때"},
        {"q": "경기 준비 시 나의 스타일은?", "a": "전략", "b": "규칙", "text_a": "상대의 약점을 분석한 전략 수립", "text_b": "정해진 나만의 루틴"},
        {"q": "더 선호하는 경기장 분위기는?", "a": "팀", "b": "예술", "text_a": "관중의 함성이 가득한 곳", "text_b": "선수에게만 집중되는 고요함"},
        {"q": "내가 선호하는 역할은?", "a": "전략", "b": "예술", "text_a": "전체 판을 읽고 지휘하는 리더", "text_b": "기술로 시선을 사로잡는 플레이어"},
        {"q": "반칙에 대한 나의 생각은?", "a": "규칙", "b": "전략", "text_a": "사소한 규정 위반도 엄단해야 한다", "text_b": "경기 흐름을 위한 유연함이 필요하다"},
        {"q": "운동 중 에너지를 얻는 방식은?", "a": "체력", "b": "속도", "text_a": "한계를 돌파할 때의 쾌감", "text_b": "남들보다 빠르게 앞서나갈 때의 쾌감"},
        {"q": "나의 운동 스타일을 한 단어로?", "a": "개인", "b": "팀", "text_a": "철저한 자기와의 싸움", "text_b": "함께 만드는 시너지"}
    ]


if "page" not in st.session_state:
    st.session_state.page = "intro"


if st.session_state.page == "intro":
    st.title("중간고사 대체 과제-나에게 어울리는 스포츠 찾기")
    st.write("학과: 정보융합학부")
    st.write("학번: 2025204008")
    st.write("이름: 송은영")
    
    if st.button("다음 페이지로"):
        st.session_state.page = "login"
        st.rerun()


elif st.session_state.page == "login":
    st.title("로그인 페이지")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        if username == "송은영" and password == "0121": 
            st.success("로그인 성공! 테스트를 시작합니다.")
            time.sleep(1)
            st.session_state.page = "main" # 로그인 성공 시 질문 페이지로
            st.rerun()
        else:
            st.error("아이디 또는 비밀번호를 다시 입력하세요.")


elif st.session_state.page == "main":
    st.title("나에게 어울리는 스포츠 분석")
    
    st.header("1단계: 평소 운동 습관 조사")
    st.info("본격적인 분석 전, 평소 운동 스타일을 먼저 체크하겠습니다!")
    
    col1, col2 = st.columns(2)
    with col1:
        activity_level = st.slider("평소에 활동량은 얼마나 되시나요?", 1, 10, 5, help="1에 가까울수록 정적인 활동, 10에 가까울수록 동적인 활동을 선호함을 의미합니다.")
    with col2:
        exercise_freq = st.slider("평균적으로 1주일에 몇회 운동하시나요?", 0, 7, 2)

    st.markdown("---")
    
    st.header("2단계: 심층 성향 분석")
    st.write("아래 문항에 답변해 주시면 어울리는 종목을 추천해드립니다.")
    
    questions = load_questions() 

    with st.form("mbti_test"):
        user_picks = []
        for i, item in enumerate(questions):
            st.markdown(f"**Q{i+1}. {item['q']}**")
            ans = st.radio(f"q{i}", [item['text_a'], item['text_b']], label_visibility="collapsed")
            user_picks.append((ans, item))
            st.write("")
            
        submitted = st.form_submit_button("결과 분석하기")

    if submitted:
     
        scores = {"팀": 0, "개인": 0, "예술": 0, "전략": 0, "체력": 0, "속도": 0, "규칙": 0}
        for ans, item in user_picks:
            category = item['a'] if ans == item['text_a'] else item['b']
            scores[category] += 1
        
        sorted_res = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top1, top2 = sorted_res[0][0], sorted_res[1][0]
        
        st.balloons() 
        st.divider()

        st.header(f"분석 결과: #{top1} & #{top2} 성향")
        
        res_set = {top1, top2}
        if {"팀", "전략"}.issubset(res_set):
            rec_sport = "축구, 농구"
            st.write("### 전략을 바탕으로 한 팀스포츠 운동을 좋아하실것 같아요!")
        elif {"개인", "체력"}.issubset(res_set):
            rec_sport = "철인3종, 헬스"
            st.write("### 자기자신과의 싸움으로 체력을 늘려나가는 운동을 좋아하실것 같아요!")
        elif {"예술", "체력"}.issubset(res_set):
            rec_sport = "피겨 스케이팅, 리듬체조"
            st.write("### 예술성이 강한 스포츠를 좋아하실것 같아요!")
        elif {"속도", "규칙"}.issubset(res_set):
            rec_sport = "수영, 육상"
            st.write("### 정해진 규칙 내에서 기록싸움을 하는 스포츠를 좋아하실것 같아요!")
        elif {"전략", "개인"}.issubset(res_set):
            rec_sport = "사격, 양궁"
            st.write("### 철저한 전략을 바탕으로 하는 정신력을 다투는 스포츠를 좋아하실것 같아요!")
        else:
            rec_sport = "요가, 필라테스"
            st.write("### 혼자서 조용히 운동하는것을 좋아하실것 같아요!")

       
        st.success(f"### 추천 종목: **{rec_sport}**")
        
       
        with st.expander(" 맞춤형 운동 가이드", expanded=True):
            
            if activity_level <= 3:
                st.warning(f"현재 활동량이 {activity_level}로 다소 낮은 편입니다.")
                st.write(f"추천드린 **{rec_sport}**은/는 처음부터 무리하기보다 천천히 습관을 들이는 것이 좋습니다.")
            elif exercise_freq >= 3:
                st.success(f"이미 주 {exercise_freq}회나 운동하시고 계십니다.")
                st.write(f"꾸준히 운동하는 성실함을 바탕으로 **{rec_sport}** 을/를 배우시면 더 즐겁게 운동하실 수 있을거에요!")
            else:
                st.info(f"이미 충분한 운동을 하고 계세요.")
                st.write(f"**{rec_sport}** 종목을 통해 현재의 활동량을 유지하면서 즐거움을 찾아보세요.")

      
        st.write("### 상세 성향 지표")
        chart_data = pd.DataFrame(list(scores.items()), columns=["유형", "점수"])
        st.table(chart_data) 
        
        st.markdown("---")
        if st.button("다시 테스트하기"):
            st.session_state.page = "intro"
            st.rerun()
