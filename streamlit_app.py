import streamlit as st

# st.set_page_config(
#     page_title="Words_app_top",
#     page_icon="icon.png",
#     layout="wide",
#     # initial_sidebar_state="expanded",
#     initial_sidebar_state="collapsed",
#     menu_items={
#         # 'Get Help': 'https://www.extremelycoolapp.com/help',
#         # 'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is wordbook-app!"
#     }
# )

st.header('Welcome!')
st.checkbox(label='Check')
st.slider(label='Slider')
st.selectbox(label='Choose Your Favourite Function', options=['','Create wordlist', 'Record', 'Setting'])

# サイドバーにテーマの選択オプションを追加
theme = st.sidebar.radio(
    "テーマを選択してください",
    options=["ライトモード", "ダークモード"]
)

# 選択されたテーマに基づいてスタイルを適用
if theme == "ライトモード":
    st.markdown(
        """
        <style>
        body {
            background-color: #FFFFFF;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: #2c3e50;
            color: #ecf0f1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
