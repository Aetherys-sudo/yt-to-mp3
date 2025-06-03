import yt_dlp
import subprocess
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import shutil

APP_PATH = os.path.dirname(os.path.realpath(__file__))
mp4_path = f"{APP_PATH}/mp4s/"
mp3_path = f"{APP_PATH}/mp3s/"
mp4_tmp_path = f"{APP_PATH}/mp4s/new/"

if not os.path.exists(mp3_path):
    os.mkdir(mp3_path)


def download(link):
    yt_opts = {
        'format': 'bestaudio',
        'outtmpl': f"{mp4_tmp_path}%(title)s.%(ext)s",
        'dump-single-json': True,
        'restrictfilenames': True
    }
    
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        try:
            object = ydl.extract_info(link, download=True)
            ydl.download(link)
        except:
            print("No object with the given link found. Exiting...")
            exit(-1)


        title = object['title']
        entries = {}
        if 'entries' in object.keys():
            entries = object['entries']


def show_labels():
    ttk.Label(frm, text="Downloading mp4...").grid(row=3, column=0) 
    root.update()
    
def show_labels2():
    ttk.Label(frm, text="Converting to mp3...").grid(row=4, column=0)
    root.update()

def convert(): 
    show_labels()
    download(link.get())
    show_labels2()
    for folder, subfolders, files in os.walk(mp4_tmp_path):
        for file in files:
            file = file.replace(".webm", "")
            convert_video_to_audio(mp4_tmp_path + file + '.webm', mp3_path + file + '.mp3')

    shutil.rmtree(mp4_tmp_path)
    Tk.quit(root)

    
def get_text(name):
    return name.get("1.0", "enc-1c")

def convert_video_to_audio(video_file_path, audio_file_path):
    try:
        command = [
            'ffmpeg',
            '-y',  # Overwrite output files without asking
            '-i', video_file_path,
            '-vn', # No video
            '-ar', '44100', # Audio sample rate
            '-ac', '2', # Audio channels (stereo)
            '-b:a', '192k', # Audio bitrate
            audio_file_path
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        print("FFmpeg command executed successfully!")
        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr) # FFmpeg often prints progress to stderr

    except subprocess.CalledProcessError as e:
        print(f"Error executing FFmpeg command: {e}")
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
    except FileNotFoundError:
        print("Error: ffmpeg executable not found. Make sure ffmpeg is installed and in your system's PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
root = Tk()
frm = ttk.Frame(root, padding=10)

frm.grid()
ttk.Label(frm, text="Youtube to Mp3 Converter", padding=20).grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

link = StringVar()
ttk.Label(frm, text="Please enter the link of the video / public plalist:").grid(row=1, column=0)
entry_field = ttk.Entry(frm, textvariable=link, width=50).grid(row=2, column=0)
ttk.Button(frm, text="Next", command=convert).grid(row=2, column=1)
root.mainloop()





