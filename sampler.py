import pygame
from os import listdir, system
from os.path import isfile, join
import os

def loadSounds():
    soundsPath = "./sounds/"
    soundFiles = [join(soundsPath, f) for f in listdir(soundsPath) if isfile(join(soundsPath, f))]
    print soundFiles
    return [pygame.mixer.Sound(f) for f in soundFiles]   

def play (sound):
    sound.play(-1 if loop else 0)

def copySamples():
    system("bash mount-usb.sh")

pygame.init()
pygame.display.set_mode((1, 1), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.mixer.init(44100, -16, 2, 2048)
sounds = loadSounds()

loop = False
stop = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.quit()
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                loop = True
                if stop:
                    print "copy all files"
                    copySamples()
                    loadSounds()
            if event.key == pygame.K_0:
                pygame.mixer.stop()   
                stop = True 
            if event.key == pygame.K_1:
                play(sounds[0])
            if event.key == pygame.K_2:
                play(sounds[1])
            if event.key == pygame.K_3:
                play(sounds[2])
            if event.key == pygame.K_4:
                play(sounds[3])
            if event.key == pygame.K_5:
                play(sounds[4])
            if event.key == pygame.K_6:
                play(sounds[5])
            if event.key == pygame.K_7:
                play(sounds[6])
            if event.key == pygame.K_8:
                play(sounds[7])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                loop = False
            if event.key == pygame.K_0:
                stop = False
