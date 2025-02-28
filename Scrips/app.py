# app.py
import streamlit as st
from content_engine import generate_summary, generate_interactions, create_h5p_package, get_frameworks
import os

st.title("H5P Interactive Video Generator")
st.markdown("""
Turn your YouTube videos into interactive lessons for Moodle with ease!  
Enter a video URL with captions to generate a summary and activities with Gemini AI.
""")

st.sidebar.subheader("API Configuration")
api_key = st.sidebar.text_input("Google Gemini API Key", type="password", key="gemini_api_key_input")  # Unique key
if not api_key:
    st.sidebar.warning("Please provide a Google Gemini API key to proceed.")

st.subheader("Create Your Interactive Video")
video_url = st.text_input("Enter Your YouTube Video URL", value="https://youtu.be/xv49RRuAI7w", key="video_url_input", help="Paste the full YouTube URL (e.g., https://youtu.be/xv49RRuAI7w or https://www.youtube.com/watch?v=xv49RRuAI7w). Ensure the video has captions for best results.")
frameworks = get_frameworks()
outcome = st.selectbox("Select Learning Outcome", frameworks, key="outcome_select", help="Choose 'summary' to see a video summary, or another option to generate activities based on it.")
generate_button = st.button("Generate", key="generate_button", help="Click to summarize or create your H5P file and Markdown output.")

if generate_button and video_url and api_key:
    with st.spinner("Processing your video..."):
        summary, timestamps = generate_summary(video_url, api_key)
        st.session_state["summary"] = summary
        st.session_state["timestamps"] = timestamps
        st.session_state["video_url"] = video_url
        
        if outcome == "summary":
            st.write("### Video Summary")
            st.write(summary)
            st.write("### Timestamps")
            st.json(timestamps)
            st.success("Summary generated!")
        else:
            interactions = generate_interactions(video_url, api_key, outcome)
            st.write("### Preview Generated Interactions (First 2)")
            st.json(interactions[:2])
            st.write("### Full Interactions")
            st.json(interactions)
            
            h5p_file, md_file = create_h5p_package(video_url, interactions, "interactive_video.h5p")
            st.session_state["h5p_file"] = h5p_file
            st.session_state["md_file"] = md_file
            st.success("Generation complete! Download your files below.")

if "summary" in st.session_state and "timestamps" in st.session_state and outcome == "summary":
    st.write("### Video Summary")
    st.write(st.session_state["summary"])
    st.write("### Timestamps")
    st.json(st.session_state["timestamps"])

if "h5p_file" in st.session_state and "md_file" in st.session_state:
    st.subheader("Download Your Files")
    col1, col2 = st.columns(2)
    with col1:
        with open(st.session_state["h5p_file"], "rb") as f:
            st.download_button("Download H5P File", f, file_name=st.session_state["h5p_file"], key="download_h5p", help="Download the H5P file for Moodle.")
    with col2:
        with open(st.session_state["md_file"], "rb") as f:
            st.download_button("Download Questions (Markdown)", f, file_name=st.session_state["md_file"], key="download_md", help="Download the questions in Markdown format.")

if video_url:
    st.subheader("Video Preview")
    st.video(video_url)
