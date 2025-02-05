import pygame
print ('Você está escutando: NEXT! by: NCTS')
pygame.init()
pygame.mixer.music.load('NEXT.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
