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
pixels=[]


#parametros da cobrinha
tamanho_quadrado = 10
velocidade_cobra = 15

def gerar_comida():
    comida_x = round(random.randrange(0,largura - tamanho_quadrado) /20.0) * 20.0
    comida_y = round(random.randrange(0,altura - tamanho_quadrado) /20.0) * 20.0
    return comida_x,comida_y

def desenhar_comida(tamanho,comida_x,comida_y):
    pygame.draw.rect(tela, verde,  [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho,pixel):
    for pixel in pixels:
        pygame.draw.rect(tela,branca, [pixel[0] , pixel[1], tamanho , tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont('arial', 50)
    texto = fonte.render(f"pontos: {pontuacao}", False, vermelha)
    tela.blit(texto,(1, 1))

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x= 0 
        velocidade_Y= tamanho_quadrado

    if tecla == pygame.K_UP:
        velocidade_x= 0
        velocidade_Y=  -tamanho_quadrado

    if tecla == pygame.K_RIGHT:
        velocidade_x= tamanho_quadrado
        velocidade_Y= 0

    if tecla == pygame.K_LEFT:
        velocidade_x= -tamanho_quadrado
        velocidade_Y= 0

    return velocidade_x, velocidade_Y


def rodar_jogo():
    fim_jogo = False
    x = largura / 2
    y = altura / 2

    velocidade_x= 0
    velocidade_y= 0

    tamanho_dacobra=1

    comida_x, comida_y= gerar_comida()

    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)



        x += velocidade_x
        y += velocidade_y

        # desenho da comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        #desehar cobra
        pixels.append([x,y])
        if len(pixels) > tamanho_dacobra :
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo = True

        desenhar_pontuacao(tamanho_dacobra - 1)    
        desenhar_cobra(tamanho_quadrado,pixels)
        
        #atualizaçao da tela
        pygame.display.update()
        
        if x == comida_x and y == comida_y:
            tamanho_dacobra += 1  
            comida_x, comida_y = gerar_comida()
        
        relogio.tick(velocidade_cobra)

rodar_jogo()