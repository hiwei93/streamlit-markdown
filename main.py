import os
import streamlit as st

base_dir = os.path.dirname(__file__)

st.set_page_config(page_title="啊阿伟啊个人主页")

# 内容类型和内容文件的配置
config = {
    "关于我": "introduction.md",
    "技能": "skills.md",
    "相关链接": "links.md",
}


def read_markdown_file(filename):
    filepath = os.path.join(base_dir, 'docs', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def render_markdown(filename):
    content = read_markdown_file(filename)
    st.markdown(content)


content_type = st.sidebar.selectbox("选择一个主题", config.keys())
render_markdown(config[content_type])
