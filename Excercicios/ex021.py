'''
Faça um programa em Python que abra e reproduza um arquivo de audio mp3.
'''

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input() #
pygame.event.wait()
