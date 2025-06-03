# YT-TO-MP3-CONVERTER
## A simple Python GUI that converts a given link to an .MP3 file format

### Description
The application opens a window where you can input the link you want to download and convert.
The app supports links for playlists (public only), and YouTube links. For YouTube Music, ydl looks for the appropriate YouTube link, as YouTube Music is not supported.

### Dependencies
The app requires ffmpeg and ydl in order to run.

- In order to install ydl, run:
`pip install yt-dlp`
    
- **Please note that for ffmpeg, you will need the binary, not the Python lib with the same name.**
ffmpeg: [Download ffmpeg](https://www.ffmpeg.org/download.html)

**For Windows**
Make sure to also add ffmpeg to PATH, like so:
- rename the download folder to /ffmpeg/
- move it to C:\
- run in CMD: `setx /m PATH "C:\ffmpeg\bin;%PATH%"`
- to test, type `ffmpeg -version` in CMD

**To run, you can use the below while in the folder**
- `python main.py`

You can also create a .bat file in the same folder and paste the above command and run it that way.