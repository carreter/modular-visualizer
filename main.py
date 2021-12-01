import pygame
import pygame.locals
import pyaudio
import numpy as np
from scipy.fft import fft

from bars import VisualizerBars

CHUNK = 1024
FORMAT = pyaudio.paInt16
NP_FORMAT = np.int16
CHANNELS = 2
RATE = 44100
DEVICE_ID = 4

SIZE = 500, 200
NUM_BARS = 10

pygame.init()

screen = pygame.display.set_mode(SIZE)
screen.fill(pygame.Color(0,0,0))
pygame.display.update()

bars = VisualizerBars(screen, 0, 0, SIZE[0], SIZE[1], n_bars = NUM_BARS)

p = pyaudio.PyAudio()

SPEAKERS = p.get_default_output_device_info()["hostApi"] #The part I have modified

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=DEVICE_ID,
                input_host_api_specific_stream_info=SPEAKERS) #The part I have modified


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            running = False

    data = stream.read(CHUNK)
    data = np.frombuffer(data, dtype=NP_FORMAT)
    data = np.log(abs(fft(data)))
    data[data < 0] = -1
    hist = np.histogram(data[len(data)//2:], range=(2,20), bins=NUM_BARS)[0]/3

    screen.fill(pygame.Color(0,0,0,1))
    bars.draw(hist)
    pygame.display.update()



    
