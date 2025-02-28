
# H5P Interactive Video Generator (WIP) 🎥✨

Welcome to the H5P Interactive Video Generator! This tool transforms YouTube videos into interactive H5P lessons for Moodle using Gemini AI. Built with Streamlit, it’s a work-in-progress that’s already functional but still being polished. Here’s what it does, what works, and how you can get started!

## 🚀 Features

- **Video Summary**: Turns a YouTube video transcript into a concise summary (100-150 words) with timestamps (e.g., "Weekly Team Meetings" at `00:50`).
- **Interactive Activities**: Generates activities like multiple-choice questions (MCQs) from the summary (e.g., "What’s the purpose of the 'parking lot'?" at `03:30`).
- **H5P Output**: Packages the video and interactions into an H5P file for Moodle, plus a Markdown file with questions.
- **User Interface**: A Streamlit app lets you input a URL, pick a learning outcome (e.g., "summary", "analysis"), and download results.

## ✅ What Works

- **Summary Generation**: Reliably creates accurate summaries from YouTube transcripts using Gemini AI. For example, `https://youtu.be/xv49RRuAI7w` gets a spot-on meeting structure summary.
- **H5P Packaging**: Successfully outputs H5P files and Markdown question lists, ready for Moodle.
- **Streamlit Interface**: Easy-to-use UI for inputting URLs and downloading files.

## 🛠️ What Needs Work

- **Interaction Generation**: Sometimes generates off-topic questions (e.g., narrative themes instead of meetings). We’re debugging the prompt replacement to lock it to the summary.
- **Timestamp Alignment**: Fallback questions work but don’t always match summary timestamps—aiming for dynamic alignment.
- **Prompt Selector**: Currently basic; plans to enhance it with summary keyword matching.

## 🏁 Quick Start (For Python Newbies)

Don’t worry if you’re new to Python—we’ve got you covered with a step-by-step setup!

### Prerequisites
- **Python 3.9+**: Download from [python.org](https://www.python.org/downloads/). Check with `python --version` in your terminal.
- **Git**: Install from [git-scm.com](https://git-scm.com/downloads) to clone this repo.
- **A Terminal**: Use Command Prompt (Windows), Terminal (macOS/Linux), or an IDE like VS Code.

### Setup Process
1. **Clone the Repo**:
   ```bash
   git clone https://github.com/yourusername/h5p-interactive-video.git
   cd h5p-interactive-video
   ```
   Replace `yourusername` with your GitHub username after uploading.

2. **Create a Virtual Environment** (keeps dependencies tidy):
   ```bash
   python -m venv venv
   ```
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
   You’ll see `(venv)` in your terminal—nice!

3. **Install Dependencies**:
   ```bash
   pip install streamlit google-generativeai youtube_transcript_api
   ```
   If `pip` fails, try `python -m pip install ...`.

4. **Get a Gemini API Key**:
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Sign in, create a key, and copy it.

5. **Run the App**:
   ```bash
   streamlit run app.py
   ```
   - A browser window should pop up. Enter your YouTube URL (e.g., `https://youtu.be/xv49RRuAI7w`) and API key, then hit "Generate".

### Example Usage
- **Input**: `https://youtu.be/xv49RRuAI7w`, select "analysis".
- **Output**: Downloads an H5P file and Markdown with questions (e.g., "What does the red/yellow/green approach track?").

## ⚙️ How It Works

1. 📥 **Input**: Enter a YouTube URL + Gemini API key.
2. 📜 **Transcript Fetch**: Pulls the transcript with `youtube_transcript_api`.
3. 🤖 **Summary Generation**: Gemini AI crafts a summary with timestamps.
4. ❓ **Interaction Generation**: Creates activities from the summary (WIP for consistency).
5. 📦 **Packaging**: Outputs H5P and Markdown files.

## 🐛 Known Issues
- **Off-Topic Questions**: Interaction generation may drift (e.g., narrative instead of meetings). Fix in progress.
- **Fallback Reliance**: Uses hardcoded questions if Gemini fails, but timestamps may not align perfectly.

## 🌟 Contributing
This is a WIP, and we’d love your help! Fork the repo, tweak the code, and submit a PR. Focus areas:
- Fixing `generate_interactions` prompt replacement.
- Enhancing `prompt_selector` for keyword-based logic.

## 📜 License
MIT License—feel free to use and modify!

## 🙏 Thanks
Built with ❤️ by [yourusername] and the xAI Grok assistant. Stay tuned for updates!

---

## 🌐 External Resources

- [Sample output and import into H5P.com hub](https://acs.h5p.com/content/1292519232931523959)


You're all set! 🚀



