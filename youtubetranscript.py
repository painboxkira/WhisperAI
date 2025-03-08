import os
import tkinter as tk
from tkinter import ttk, messagebox
from openai import OpenAI
import yt_dlp

# ✅ Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# ✅ Function to generate a safe, simple filename
def generate_filename(output_path, ext="webm"):
    """Generates a clean, simple filename."""
    count = 1
    while True:
        filename = f"transcript_{count:03d}.{ext}"
        filepath = os.path.join(output_path, filename)
        if not os.path.exists(filepath):  # Ensure no duplicates
            return filepath
        count += 1

# ✅ Function to download YouTube audio and rename it safely
def download_audio(url, output_path="."):
    """Downloads the best available audio from YouTube and saves it as a clean name."""

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_download.%(ext)s'  # Temporary name
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

        # Find the downloaded file and rename it
        temp_file = f"temp_download.{info['ext']}"
        new_file = generate_filename(output_path, "webm")
        os.rename(temp_file, new_file)  # Rename to clean format

        print(f"✅ Audio downloaded and saved as: {new_file}")
        return new_file

    except Exception as e:
        messagebox.showerror("Error", f"Audio download failed: {str(e)}")
        return None

# ✅ Function to transcribe the `.webm` file using Whisper API
def transcribe_audio(audio_path, start_time=None, end_time=None):   
    """Sends .webm audio file to OpenAI Whisper API for transcription (plain text)."""

    if not client.api_key:
        messagebox.showerror("Error", "OpenAI API key not found!")
        return None

    if not os.path.exists(audio_path):
        messagebox.showerror("Error", f"Audio file not found: {audio_path}")
        return None

    try:
        print(f"🎤 Sending .webm audio to OpenAI Whisper API: {audio_path}")
        
        with open(audio_path, 'rb') as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="srt"
            )
        
        transcript = response
        print(f"✅ Transcription complete:\n{transcript}")

        # Save transcript to a `.txt` file with a safe name
        transcript_file = audio_path.replace('.webm', '.txt')
        with open(transcript_file, 'w', encoding='utf-8') as f:
            f.write(transcript)
        print(f"📄 Transcript saved at: {transcript_file}")

        return transcript

    except Exception as e:
        messagebox.showerror("Error", f"Transcription failed: {str(e)}")
        return None

# ✅ Function to handle the full process: Download & Transcribe
def process_video(url, start_time=None, end_time=None):
    try:
        audio_path = download_audio(url)
        if audio_path:
            transcript = transcribe_audio(audio_path, start_time, end_time)
            if transcript:
                messagebox.showinfo('Success', 'Transcription completed!')
            else:
                messagebox.showerror('Error', 'Transcription failed!')
    except Exception as e:
        messagebox.showerror('Error', f'Failed: {str(e)}')

# ✅ GUI Application
def main(): 
    root = tk.Tk()
    root.title('YouTube Transcript Downloader')
    root.geometry('500x400')

    url_label = ttk.Label(root, text='Enter YouTube URL:')
    url_label.pack(pady=5)  

    url_entry = ttk.Entry(root, width=40)
    url_entry.pack(pady=5)

    start_label = ttk.Label(root, text='Start Time (HH:MM:SS) [Optional]:')
    start_label.pack(pady=5)
    start_entry = ttk.Entry(root, width=20)
    start_entry.pack(pady=5)

    end_label = ttk.Label(root, text='End Time (HH:MM:SS) [Optional]:')
    end_label.pack(pady=5)
    end_entry = ttk.Entry(root, width=20)
    end_entry.pack(pady=5)

    def run_process():
        url = url_entry.get()
        start_time = start_entry.get().strip() or None
        end_time = end_entry.get().strip() or None
        process_video(url, start_time, end_time)

    process_button = ttk.Button(root, text='Download & Transcribe', command=run_process)
    process_button.pack(pady=10)        

    root.mainloop()

if __name__ == '__main__':
    main()
