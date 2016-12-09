import pygame

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)


crash = pygame.mixer.Sound("crash.wav")
beat = pygame.mixer.Sound("beat.wav")
# load sounds function
# put sounds in array
# load from sd / zoom
# loop yes / no 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                pygame.mixer.stop()    
            if event.key == pygame.K_1:
                crash.play()
            if event.key == pygame.K_2:
                beat.play()
