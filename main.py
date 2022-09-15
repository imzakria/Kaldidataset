import spleeter
from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment
from pydub.silence import split_on_silence

ydl_opts = {
    "format": "bestaudio/best",
    "audio-format": "wav",
    "outtmpl": "audio.wav",
}
try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
except Exception as e:
    print("Video cannot be downloaded. Exception:/n{}".format(e))

