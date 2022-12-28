# YouTube Transummerize AI  
Transcribe then summerize any YouTube video using AI using:

- Streamlit
- Whisper (OpenAI speech recognition model)
- OpenAI GPT-3 API
- Python

## Setup Required

Install Whisper and Streamlit using these commands:

```bash
pip install git+https://github.com/openai/whisper.git
pip install streamlit
```

OR

```bash
pip install -r requirements.txt
```

Install FFMPEG:
```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```
Note: Make sure to have the appropriate package manager installed (e.g. apt, pacman, brew, chocolatey, scoop) before running the above commands.

## Usage
0. Create `.streamlit/secrets.toml` in the root of this cloned repo.
   (See `example.secrets.toml` for contents example of `.streamlit/secrets.toml`)

1. Run this by doing:  
```
streamlit run main.py
```

2. You can now view your Streamlit app in your browser.  

Local URL: `http://localhost:8501`
Network URL: `http://192.168.2.3:8501`

3. Paste in your youtube URL and wait for it.

## Limit:
Works on short videos with words less than certain amount see OpenAI documentation about tokens and maximum content length.
