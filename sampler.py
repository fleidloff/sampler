import pygame
from os import listdir
from os.path import isfile, join
from subprocess import call

def loadSounds(soundsPath):
    soundFiles = [join(soundsPath, f) for f in listdir(soundsPath) if isfile(join(soundsPath, f))]
    return [pygame.mixer.Sound(f) for f in soundFiles]   

def play (sound):
    sound.play(-1 if loop else 0)

def copySamples():
    call(["./mount-usb.sh"])

pygame.init()
pygame.display.set_mode((1, 1), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.mixer.init(44100, -16, 2, 2048)
sounds = loadSounds("./sounds/")

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
            if event.key == pygame.K_0:
                pygame.mixer.stop()   
                stop = True 
            if event.key == pygame.K_1:
                play(sounds[0])
            if event.key == pygame.K_2:
                play(sounds[1])
            if event.key == pygame.K_3:
                play(sounds[3])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                loop = False
            if event.key == pygame.K_0:
                stop = False
