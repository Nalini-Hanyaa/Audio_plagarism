This repository contains two Streamlit-based applications for detecting music plagiarism. Each application performs a specific task to compare audio files based on their musical key and tempo.

**1. Tune Plagiarism Detection App**

**Description**

This application allows users to upload two audio files and compare them to check for potential plagiarism by analyzing their musical key and tempo.

**Execution Process**

**Prerequisites:**

Install Python 3.8 or above.

**Install the required libraries:**

pip install streamlit librosa numpy soundfile

**Run the Application:**

Save the tune_plagiarism_deploy.py file locally.

Open a terminal and navigate to the file's directory.

### Run the Streamlit App
To start the application, use the following command in your terminal:

```bash
streamlit run tune_plagiarism_deploy.py
```

How to Use:

Upload two audio files in WAV, MP3, or OGG format.

Click the Check Plagiarism button.

The app will display whether the tunes are matched or not based on their musical key and tempo.

2. Dataset-Based Plagiarism Detection App

Description

This application allows users to upload an audio file and compare it against a dataset of audio files to check for plagiarism.

Execution Process

Prerequisites:

Install Python 3.8 or above.

Install the required libraries:

pip install streamlit librosa numpy

Dataset Setup:

Ensure your dataset is stored locally and organized as a folder containing subfolders or files with .wav, .mp3, or .ogg extensions.

Update the dataset_dir variable in the plagiarism_detection_from_dataset.py file with the path to your dataset directory.

Run the Application:

Save the plagiarism_detection_from_dataset.py file locally.

Open a terminal and navigate to the file's directory.

Run the Streamlit app using the following command:

streamlit run plagiarism_detection_from_dataset.py

How to Use:

Upload an audio file in WAV, MP3, or OGG format.

Click the Check Plagiarism button.

The app will display whether the uploaded tune matches any file in the dataset.

Notes

Musical Key Extraction: Currently, the key extraction function is a placeholder and assumes all keys are 'C'.

Tempo Threshold: The comparison allows for a tempo difference of up to 5 BPM.

Ensure that uploaded audio files are clear and properly formatted for accurate comparisons.

Use a quality dataset for better detection results.
