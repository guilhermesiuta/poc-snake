import pygame
import random
pygame.init()
pygame.display.set_caption('jogo da cobrinha')
largura,altura =600,400
tela = pygame.display.set_mode((largura,altura))
relogio= pygame.time.Clock()



#cores
preto =(0,0,0)
vermelha =(255,0,0)
branca = (255,255,255)
verde = (0,255,0)


#parametros da cobrinha
tamanho_quadrado = 10
velocidade_cobra = 15
def gerar_comida():
    comida_x = round(random.randrange(0,largura - tamanho_quadrado) /20.0) * 20.0
    comida_y = round(random.randrange(0,altura - tamanho_quadrado) /20.0) * 20.0

    return comida_x,comida_y
def desenhar_comida(tamanho,comida_x,comida_y):
    pygame.draw.rect(tela, verde,  [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamaho,pixel):
    for pixel in pixel
        pygame.draw.rect(tela,branca, [pixel[0] , pixel[0], tamanho , tamanho])

def rodar_jogo():
    fim_jogo = False
    x  =largura/2
    y = altura /2

    velocidade_x= 0
    velocidade_y= 0

    tamanho_dacobra=1
    pixel=[]

    comida_x, comida_y= gerar_comida()

    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:''
                fim_jogo = True

        # desenho da comida
        desenhar_comida(tamanho_quadrado, 10, 10)





        #atualizaçao da tela
        pygame.display.update()
        relogio.tick(velocidade_cobra)


        #desehar cobra
        pixels.append([x,y])
        if len(pixels) > tamanho_dacobra :
            del pixels[0]

        for pixel in pixels:
            if pixel == [x,y]
                fim_jogo(True)

        desenhar_cobra()





rodar_jogo()