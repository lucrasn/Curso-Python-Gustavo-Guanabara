import pygame
# iniciar o pygame
pygame.init()
# Carregando um arquivo de música para reprodução
pygame.mixer.music.load('exercício021.mp3')
# Iniciando a reprodução do stream de
# loops é um argumento, que é 0 por padrão, que indica quantas vezes repetir a música.
# A música se repete indefinidamente se este argumento estiver definido como -1.
pygame.mixer.music.play(loops=-1)
# Para o audio reproduzir
input()
# Esperando por um único evento da fila
pygame.event.wait()
