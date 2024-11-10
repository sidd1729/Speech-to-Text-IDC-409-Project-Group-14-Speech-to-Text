import os
import shutil
from pydub import AudioSegment

#Download the VCTK corpus from:
#https://datashare.ed.ac.uk/handle/10283/3443

# Paths
source_audio_base_path = "C:/Users/siddh/Downloads/VCTK-Corpus-0.92/wav48_silence_trimmed"
source_text_base_path = "C:/Users/siddh/Downloads/VCTK-Corpus-0.92/txt"
destination_path = "C:/Users/siddh/Downloads/VCTK_for_MFA"

# Ensure the destination directory exists
os.makedirs(destination_path, exist_ok=True)

# Function to convert FLAC to WAV
def convert_flac_to_wav(flac_path, wav_path):
    audio = AudioSegment.from_file(flac_path, format="flac")
    audio.export(wav_path, format="wav")

# Loop through each subfolder in both the audio and text directories
for folder_name in os.listdir(source_audio_base_path):
    audio_folder_path = os.path.join(source_audio_base_path, folder_name)
    text_folder_path = os.path.join(source_text_base_path, folder_name)
    
    # Check if both the audio and text folders exist
    if os.path.isdir(audio_folder_path) and os.path.isdir(text_folder_path):
        # Create a new subfolder in VCTK_For_MFA for this folder (e.g., p340)
        destination_folder = os.path.join(destination_path, folder_name)
        os.makedirs(destination_folder, exist_ok=True)
        
        # Copy and convert .flac files from the audio folder to the new destination
        for audio_file in os.listdir(audio_folder_path):
            if audio_file.endswith('.flac'):
                flac_path = os.path.join(audio_folder_path, audio_file)
                wav_file_name = audio_file.replace('.flac', '.wav')
                wav_path = os.path.join(destination_folder, wav_file_name)
                convert_flac_to_wav(flac_path, wav_path)
        
        # Copy .txt files from the text folder to the new destination
        for text_file in os.listdir(text_folder_path):
            if text_file.endswith('.txt'):
                shutil.copy2(os.path.join(text_folder_path, text_file), destination_folder)

print("All FLAC audio and text files have been successfully copied and converted.")
