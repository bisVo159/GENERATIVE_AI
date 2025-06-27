import streamlit as st
from backend import load_video_transcript

st.set_page_config(page_title="ChatTuber - Chat with YouTube Video", layout="wide")

# Sidebar Layout
with st.sidebar:
    st.title("🎥 ChatTuber")
    st.markdown("Chat with any YouTube video using its transcript.")
    st.divider()
    video_url = st.text_input("🔗 Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=VIDEO_ID")
    # st.caption("Example: https://www.youtube.com/watch?v=MdeQMVBuGgY")

# Main Content
st.title("Ask Questions About a YouTube Video")
st.markdown("Enter a YouTube video link in the sidebar to start chatting with its content.")

if video_url:
    video_id = video_url.split("v=")[-1].split("&")[0]

    if 'chain' not in st.session_state or st.session_state.get("video_id") != video_id:
        with st.spinner("🔄 Loading and processing video transcript..."):
            try:
                chain = load_video_transcript(video_id)
                st.session_state.chain = chain
                st.session_state.video_id = video_id
                st.success("✅ Transcript processed. You can now ask questions!")
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.stop()

    question = st.text_input("❓ Ask your question about the video:", placeholder="e.g., What is the main topic?")

    if question:
        with st.spinner("💬 Generating answer..."):
            response = st.session_state.chain.invoke(question)
            st.write("### 🧠 Answer")
            st.write(response)
