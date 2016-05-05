import pyaudio
import numpy as np


class Reproo:
    def __init__(self,CHUNK):
        self.CHUNK = CHUNK

    def iniciosum(self,samples):
        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=44100,
                             output=True,
                             )
        # Assuming you have a numpy array called samples
        data = samples.astype(np.float32).tostring()
        self.stream.write(data)




    def cerrarsum(self):

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

