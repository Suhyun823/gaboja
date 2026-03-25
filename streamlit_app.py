import streamlit as st

# 한글 웹폰트 적용 (Google Fonts)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif !important;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Noto Sans KR', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="wide")

# 헤더 섹션
st.title("👋 안녕하세요")
st.subheader("저는 김수현입니다")

# 소개 섹션
st.markdown("---")
st.header("📝 소개")
st.write("""
저는 인천대학교 수학교육과에 재학중인 2학년 김수현입니다.unsafe_all
여기에 간단한 자기소개를 작성해주세요.
- 직업, 관심사 등을 적을 수 있습니다.
- 마크다운 형식으로 작성 가능합니다.
""")

# 스킬 섹션
st.markdown("---")
st.header("🛠️ 스킬")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("프로그래밍")
    st.write("- Python\n- JavaScript")
    
with col2:
    st.subheader("도구 및 라이브러리")
    st.write("- Streamlit\n- Pandas")
    
with col3:
    st.subheader("기타")
    st.write("- 항목1\n- 항목2")

# 프로젝트 섹션
st.markdown("---")
st.header("📚 프로젝트")
project1, project2 = st.columns(2)
with project1:
    st.subheader("프로젝트 1")
    st.write("프로젝트 설명을 여기에 작성하세요.")
    st.write("링크: https://example.com")
    
with project2:
    st.subheader("프로젝트 2")
    st.write("프로젝트 설명을 여기에 작성하세요.")
    st.write("링크: https://example.com")

# 연락처 섹션
st.markdown("---")
st.header("📧 연락처")
st.write("""
- 이메일: your-email@example.com
- GitHub: https://github.com/yourname
- LinkedIn: https://linkedin.com/in/yourname
""")
