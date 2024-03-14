# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# pip install (metodo) - linha de instalação de metodos do python (identificado no ChatGPT)

import pygame
pygame.init()

pygame.mixer.music.load('exe021audio.ogg')
pygame.mixer.music.play()
pygame.event.wait()


