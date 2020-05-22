import os.path
from os import path

class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Format nesuportat")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("se canta {} un mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("se canta {} un wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("se canta {} un ogg".format(self.filename))


class FlacFile:
    def __init__(self,filename):
        if not filename.endswith(".flac"):
            raise Exception("Format necunoscut")
        self.filenname = filename

    def play(self):
        print("se canta {} un flac".format(self.filenname))


if __name__ == '__main__':
    filename = input('*.ogg file = ')
    print('Exista fisierul: ', path.exists(filename))
    ogg = OggFile(filename)
    ogg.play()

    filename = input('*.mp3 file = ')
    print('Exista fisierul: ', path.exists(filename))
    mp3 = MP3File(filename)
    mp3.play()

    filename = input('*.wav file = ')
    print('Exista fisierul: ', path.exists(filename))
    wav = WavFile(filename)
    wav.play()