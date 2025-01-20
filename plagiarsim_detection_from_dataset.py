import streamlit as st
import librosa
import numpy as np
import os
import warnings

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

st.markdown("### Upload an audio file to check for plagiarism against a dataset:")

audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "ogg"])

# Path to the dataset directory
dataset_dir = r"C:\Users\NaliniGarikipati\OneDrive - Hanyaa\Audio_Dataset"

if audio_file:
    # Save the uploaded file to disk
    with open("uploaded_audio.wav", "wb") as f:
        f.write(audio_file.getbuffer())
    
    # Center the button using columns
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Check Plagiarism"):
            matched = False
            st.info("Checking against dataset...")
            for root, dirs, files in os.walk(dataset_dir):
                for file in files:
                    if file.endswith((".wav", ".mp3", ".ogg")):
                        dataset_audio_path = os.path.join(root, file)
                        st.write(f"Comparing with {file}...")
                        if match_tune("uploaded_audio.wav", dataset_audio_path):
                            st.success(f"The uploaded tune matches with {file} in the dataset.")
                            matched = True
                            break
                if matched:
                    break
            if not matched:
                st.error("No matches found in the dataset.")
