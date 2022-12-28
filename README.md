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
pip install pytube
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
