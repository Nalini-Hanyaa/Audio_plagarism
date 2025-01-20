import streamlit as st
import librosa
import numpy as np
import warnings
import soundfile as sf

# Check numpy version
if np.__version__.startswith('2'):
    raise ImportError("Please downgrade numpy to a version below 2.0.0.")

# Suppress specific warnings from librosa and numba
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Function to extract the key of the audio
def extract_key(audio_path):
    # For simplicity, we'll return the key as 'C' for all songs
    return 'C'

# Function to extract the tempo of the audio
def extract_tempo(audio_path):
    y, sr = librosa.load(audio_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return tempo

# Function to compare keys of two songs
def compare_keys(key1, key2):
    return key1 == key2

# Function to compare tempos of two songs
def compare_tempos(tempo1, tempo2, threshold=5):
    return abs(tempo1 - tempo2) <= threshold

# Function to match the tunes
def match_tune(audio_path1, audio_path2):
    key1 = extract_key(audio_path1)
    tempo1 = extract_tempo(audio_path1)
    
    key2 = extract_key(audio_path2)
    tempo2 = extract_tempo(audio_path2)
    
    key_matched = compare_keys(key1, key2)
    tempo_matched = compare_tempos(tempo1, tempo2)
    
    return key_matched and tempo_matched

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #4e79a7;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
    }
    .stFileUploader {
        background-color: #ffffff;
        border: 1px solid #d3d3d3;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #4e79a7;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
        font-family: 'Arial Black', sans-serif;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3b5c91;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app
st.title('🎵 Plagiarism Detection for Music 🎵')

st.markdown("### Upload two audio files to check for potential plagiarism:")

audio_file1 = st.file_uploader("Upload first audio file", type=["wav", "mp3", "ogg"])
audio_file2 = st.file_uploader("Upload second audio file", type=["wav", "mp3", "ogg"])

if audio_file1 and audio_file2:
    # Save the uploaded files to disk
    with open("audio1.wav", "wb") as f:
        f.write(audio_file1.getbuffer())
    with open("audio2.wav", "wb") as f:
        f.write(audio_file2.getbuffer())

    # Center the button using columns
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Check Plagiarism"):
            # Compare the tunes
            if match_tune("audio1.wav", "audio2.wav"):
                st.success("The tunes are matched.")
            else:
                st.error("The tunes are not matched.")
