import pygame
from os import listdir
from os.path import isfile, join



# copy songs with function / max 8 songs! 
# copy songs on keyboard clicks (with usb mounting)
# stop loops
# load all 8 songs
# copy songs as pi user (why no access to zoom files?)



def loadSounds(soundsPath):
    soundFiles = [join(soundsPath, f) for f in listdir(soundsPath) if isfile(join(soundsPath, f))]
    return [pygame.mixer.Sound(f) for f in soundFiles]   

def play (sound):
    sound.play(-1 if loop else 0)

pygame.init()
pygame.display.set_mode((1, 1), pygame.HWSURFACE | pygame.DOUBLEBUF)
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
            if event.key == pygame.K_3:
                play(sounds[3])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                loop = False
