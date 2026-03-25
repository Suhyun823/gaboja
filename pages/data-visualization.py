import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import plotly.express as px
import plotly.graph_objects as go

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

# 한글 폰트 설정 (fonts/NotoSansKR-Bold.ttf)
base_dir = os.path.dirname(__file__)
font_path = os.path.join(base_dir, '..', 'fonts', 'NotoSansKR-Bold.ttf')
font_path = os.path.normpath(font_path)
try:
    font_prop = fm.FontProperties(fname=font_path)
    font_name = font_prop.get_name()
    plt.rcParams["font.family"] = font_name
    plt.rcParams["axes.unicode_minus"] = False
    plotly_font_family = font_name
except Exception as e:
    st.warning(f"한글 폰트 설정에 실패했습니다: {e}")
    plotly_font_family = "Arial"

st.title("데이터 시각화 페이지")

st.markdown("""
이 페이지에서는 다양한 데이터 시각화 예시를 제공합니다.
샘플 데이터를 사용한 차트와 사용자가 직접 데이터를 입력하여 생성한 차트를 볼 수 있습니다.
""")

# 섹션 1: 샘플 데이터 시각화
st.header("샘플 데이터 시각화")

# 샘플 데이터 생성
sample_data = pd.DataFrame({
    '카테고리': ['A', 'B', 'C', 'D', 'E'],
    '값1': [10, 20, 15, 25, 30],
    '값2': [5, 15, 10, 20, 25]
})

st.subheader("샘플 데이터")
st.dataframe(sample_data)

# 막대 그래프 (Matplotlib)
st.subheader("막대 그래프 (Matplotlib)")
fig, ax = plt.subplots()
ax.bar(sample_data['카테고리'], sample_data['값1'], label='값1')
ax.bar(sample_data['카테고리'], sample_data['값2'], bottom=sample_data['값1'], label='값2')
ax.set_xlabel('카테고리')
ax.set_ylabel('값')
ax.legend()
st.pyplot(fig)

# 선 그래프 (Plotly)
st.subheader("선 그래프 (Plotly)")
fig_line = px.line(sample_data, x='카테고리', y=['값1', '값2'], title='샘플 선 그래프')
fig_line.update_layout(font=dict(family=plotly_font_family))
st.plotly_chart(fig_line)

# 산점도 (Plotly)
st.subheader("산점도 (Plotly)")
fig_scatter = px.scatter(sample_data, x='값1', y='값2', color='카테고리', title='샘플 산점도')
fig_scatter.update_layout(font=dict(family=plotly_font_family))
st.plotly_chart(fig_scatter)

# 섹션 2: 사용자 데이터 입력 및 시각화
st.header("사용자 데이터 입력 및 시각화")

st.markdown("CSV 파일을 업로드하거나, 텍스트로 데이터를 입력하세요.")

# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=['csv'])

# 텍스트 입력
text_input = st.text_area("데이터를 텍스트로 입력 (CSV 형식)", placeholder="카테고리,값1,값2\nA,10,5\nB,20,15\n...")

if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)
elif text_input:
    try:
        from io import StringIO
        user_data = pd.read_csv(StringIO(text_input))
    except Exception as e:
        st.error(f"데이터 파싱 오류: {e}")
        user_data = None
else:
    user_data = None

if user_data is not None:
    st.subheader("사용자 데이터")
    st.dataframe(user_data)

    # 차트 타입 선택
    chart_type = st.selectbox("차트 타입 선택", ["막대 그래프", "선 그래프", "산점도", "히스토그램"])

    if chart_type == "막대 그래프":
        if len(user_data.columns) >= 2:
            x_col = st.selectbox("X축 컬럼", user_data.columns)
            y_col = st.selectbox("Y축 컬럼", user_data.columns)
            fig_bar = px.bar(user_data, x=x_col, y=y_col, title=f"{x_col} vs {y_col} 막대 그래프")
            fig_bar.update_layout(font=dict(family=plotly_font_family))
            st.plotly_chart(fig_bar)
        else:
            st.warning("적어도 2개의 컬럼이 필요합니다.")

    elif chart_type == "선 그래프":
        if len(user_data.columns) >= 2:
            x_col = st.selectbox("X축 컬럼", user_data.columns)
            y_col = st.selectbox("Y축 컬럼", user_data.columns)
            fig_line = px.line(user_data, x=x_col, y=y_col, title=f"{x_col} vs {y_col} 선 그래프")
            fig_line.update_layout(font=dict(family=plotly_font_family))
            st.plotly_chart(fig_line)
        else:
            st.warning("적어도 2개의 컬럼이 필요합니다.")

    elif chart_type == "산점도":
        if len(user_data.columns) >= 2:
            x_col = st.selectbox("X축 컬럼", user_data.columns)
            y_col = st.selectbox("Y축 컬럼", user_data.columns)
            fig_scatter = px.scatter(user_data, x=x_col, y=y_col, title=f"{x_col} vs {y_col} 산점도")
            fig_scatter.update_layout(font=dict(family=plotly_font_family))
            st.plotly_chart(fig_scatter)
        else:
            st.warning("적어도 2개의 컬럼이 필요합니다.")

    elif chart_type == "히스토그램":
        numeric_cols = user_data.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            col = st.selectbox("컬럼 선택", numeric_cols)
            fig_hist = px.histogram(user_data, x=col, title=f"{col} 히스토그램")
            fig_hist.update_layout(font=dict(family=plotly_font_family))
            st.plotly_chart(fig_hist)
        else:
            st.warning("숫자형 컬럼이 필요합니다.")

else:
    st.info("데이터를 업로드하거나 입력하세요.")
