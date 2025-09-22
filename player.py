import pygame

pygame.init()

class Player:
    def __init__(self, velocidade, x, y, hp, cargabequer, altura, largura, viradoesquerda, sprites):
        self.velocidade = velocidade
        self.x = x
        self.y = y
        self.vida = hp
        self.cargabequer = cargabequer
        self.viradoesquerda = viradoesquerda
        self.rect = pygame.Rect(x - (largura / 2), y - (altura / 2), largura, altura)
