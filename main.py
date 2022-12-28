# import necessary modules
import streamlit as st
import openai
from pytube import YouTube
import whisper

# Set OpenAI organization and API key from secrets
openai.organization = st.secrets["openai"]["organization"]
openai.api_key = st.secrets["openai"]["api_key"]

# Define the YouTubeTransummerizeAI class
class YouTubeTransummerizeAI:
    def __init__(self, video_url):
        self.video_url = video_url
        self.audio_file = "audio.mp3"
        self.tldr_tag = "\n\nTL;DR"
        self.transcribed_text = ""
        self.summary = ""

    def download_audio(self):
        yt = YouTube(self.video_url)
        yt.streams.filter(file_extension='mp3')
        stream = yt.streams.get_by_itag(139)
        stream.download('',"audio.mp3")

    def transcribe_audio(self):
        model = whisper.load_model("base")
        transcription = model.transcribe(self.audio_file)
        self.transcribed_text = transcription["text"]

    def generate_summary(self):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.transcribed_text + self.tldr_tag,
            temperature=0.3,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0,
        )
        self.summary = response["choices"][0]["text"]

# Create a Streamlit container for the header and title
with st.container():
    st.header("YouTube TransummerizeAI")
    st.title("Get the summary of any YouTube video in any language")

# Create a Streamlit container for the URL input form
with st.container():
    st.write("---")
    video_url = st.text_input(
        "Paste the URL of the YouTube video here👇",
        placeholder="paste the url",
    )

    # If a video URL is entered, start the summary process
    if video_url:
        try:
            # Display a Streamlit spinner while the process is running
            with st.spinner('Transummerization in progress...'):
                # Create a YouTubeTransummerizeAI object
                yt_summary = YouTubeTransummerizeAI(video_url)

                # Download the audio file
                yt_summary.download_audio()

                # Transcribe the downloaded audio file
                yt_summary.transcribe_audio()

                # Generate a summary of the transcribed text
                yt_summary.generate_summary()

                # Display the transcribed text and summary
                st.write(yt_summary.transcribed_text)
                st.subheader("Here is your summary!")
                st.write(yt_summary.summary)

                # Display a success message
                st.success('Transummerization completed!')
        except Exception as error:
            print(error)
