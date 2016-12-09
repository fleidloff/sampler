import pygame
from os import listdir
from os.path import isfile, join



# load sounds function
# put sounds in array
# load from sd / zoom
# loop yes / no 
# load from ditto?



def loadSounds(soundsPath):
    soundFiles = [join(soundsPath, f) for f in listdir(soundsPath) if isfile(join(soundsPath, f))]
    return [pygame.mixer.Sound(f) for f in soundFiles]   

def play (sound):
    sound.play(-1 if loop else 0)

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
sounds = loadSounds("./sounds/")
loop = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.quit()
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                loop = True
            if event.key == pygame.K_0:
                pygame.mixer.stop()    
            if event.key == pygame.K_1:
                play(sounds[0])
            if event.key == pygame.K_2:
                play(sounds[1])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                loop = False
