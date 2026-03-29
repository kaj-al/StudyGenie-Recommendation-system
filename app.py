import streamlit as st
from tools import documentation,youtube,papers

st.title("Study Genie")

topic = st.text_input("Enter a topic to explore:")

level = st.selectbox("Select your expertise level:",["School","Senior School","College","Researcher"])


if st.button("Explore"):
    query = topic + " " + level
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
            st.write(f"Duration:{video['duration']}")
        st.divider()
        # st.video(video["url"])

    st.header("Documentation")
    for doc in docs:
        st.markdown(f"[{doc['title']}]({doc['url']})")

    if level in ["College","Researcher"]:
        st.header("Research Papers")
        for paper in papers_list:
            st.markdown(f"[{paper['title']}]({paper['url']})")