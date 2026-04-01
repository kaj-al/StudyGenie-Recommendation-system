
import streamlit as st
from tools import documentation,youtube,papers


st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #f5f0e6;
    color: #3e2f1c;
}

/* Titles */
h1, h2, h3 {
    color: #5a3e2b;
}

/* Input */
input {
    background-color: #fffaf3 !important;
    color: #3e2f1c !important;
    border-radius: 10px !important;
    border: 1px solid #d2b48c !important;
}

/* Button */
button[kind="primary"] {
    background-color: #8b5e3c !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Cards */
div[data-testid="stHorizontalBlock"] {
    background: #fffaf3;
    padding: 12px;
    border-radius: 12px;
    border: 1px solid #e0c9a6;
}

/* Images */
img {
    border-radius: 10px;
}

/* Links */
a {
    color: #8b5e3c !important;
}

</style>
""", unsafe_allow_html=True)

st.title("Study Genie")

topic = st.text_input("Enter a topic to explore:")

level = st.radio("Select your expertise level:",["School","Senior School","College","Researcher"],
                     index=None,horizontal=True)


if st.button("Explore"):
    query = topic + " for " + level +" students"
    videos = youtube(query)
    docs = documentation(query)
    papers_list = papers(query)

    st.header("YouTube Videos")
    for video in videos:
        col1,col2 = st.columns([1,3])
        with col1:
            st.image(video["thumbnail"],width=140)
        with col2:
            st.markdown(f"###[{video['title']}]({video['url']})")
            st.write(f"Channel:{video['channel']}")
        st.divider()

    st.header("Documentation")
    for doc in docs:
        st.markdown(f"[{doc['title']}]({doc['url']})")

    if level in ["College","Researcher"]:
        st.header("Research Papers")
        for paper in papers_list:
            st.markdown(f"[{paper['title']}]({paper['url']})")