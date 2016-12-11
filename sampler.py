import pygame
from os import listdir, system
from os.path import isfile, join
import os

loop = False
stop = False

def loadSounds():
    soundsPath = "./sounds/"
    soundFiles = [join(soundsPath, f) for f in listdir(soundsPath) if isfile(join(soundsPath, f))]
    soundFiles.sort()
    print soundFiles
    result = [pygame.mixer.Sound(f) for f in soundFiles]
    while len(result) < 8:
        result.append(None)
    return result

def play (sounds, soundId, looping):
    soundsPath = "./sounds/"
    if stop:
        system("bash copy-1-file.sh " + `soundId + 1`)
        print "assign new song to " + `soundId + 1`
        sounds[soundId] = pygame.mixer.Sound(join(soundsPath, `soundId + 1` + ".wav"))
    elif sounds[soundId] is not None:
        if loop:
            if looping[soundId] is not None:
                looping[soundId].stop()
                looping[soundId] = None
            else:
                looping[soundId] = sounds[soundId].play(-1)
        else:
            sounds[soundId].play(0)

def copySamples():
    system("bash mount-usb.sh")

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
pygame.init()
pygame.display.set_mode((1, 1), pygame.HWSURFACE | pygame.DOUBLEBUF)
sounds = loadSounds()
looping = [None] * 8

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
                    sounds = loadSounds()
            if event.key == pygame.K_0:
                pygame.mixer.stop() 
                looping = [None] * 8  
                stop = True 
            if event.key == pygame.K_1:
                play(sounds, 0, looping)
            if event.key == pygame.K_2:
                play(sounds, 1, looping)
            if event.key == pygame.K_3:
                play(sounds, 2, looping)
            if event.key == pygame.K_4:
                play(sounds, 3, looping)
            if event.key == pygame.K_5:
                play(sounds, 4, looping)
            if event.key == pygame.K_6:
                play(sounds, 5, looping)
            if event.key == pygame.K_7:
                play(sounds, 6, looping)
            if event.key == pygame.K_8:
                play(sounds, 7, looping)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                loop = False
            if event.key == pygame.K_0:
                stop = False
