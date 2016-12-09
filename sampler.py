import pygame

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)


crash = pygame.mixer.Sound("crash.wav")
beat = pygame.mixer.Sound("beat.wav")
# load sounds function
# put sounds in array
# load from sd / zoom
# loop yes / no 
# load from ditto?

loop = False

def play (sound):
    sound.play(-1 if loop else 0)

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
                play(crash)
            if event.key == pygame.K_2:
                play(beat)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_l:
                loop = False
