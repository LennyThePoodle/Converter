import pygame
import random

WIDTH = 600
HEIGHT = 400
FPS = 30

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Measurment Calculator by Jack Campbell")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
font_name=pygame.font.match_font('Arial')
def Temprature(n,it,et):
    if it == 'f':
        c = (n-32)/1.8
        if et == 'c':
            return format(c,',.2f')
        elif et == 'k':
            return format(c+273.15,',.2f')
    elif it == 'c':
        if et == 'f':
            return format(1.8*n+32,',.2f')
        elif et == 'k':
            return format(n+273.15,',.2f')
    elif it == 'k':
        c = n-273.15
        if et == 'c':
            return format(c,',.2f')
        elif et == 'f':
            return format(1.8*c+32,',.2f')
def Area(n,ia,ea):
    #convert all to squared meters
    c_dic = {'skm':n*1000000,'sf':n*0.09290304,'si':n*0.00064516,'scm':n/10000,
             'sm':n*2589988.110336,'acre':n*4046.8564224}
    #get the value in square meters
    x = c_dic[ia]
    #convert to the desired unit
    v_dic = {'acre':x*0.0002471053814672,'scm':x*10000,'sf':x*10.76391041671,
             'si':x*1550.003100006,'skm':x*0.000001,'sm':x*(3.86102158542510**-7)}
    return str(format(v_dic[ea],',.2f'))+' '+ea
#km,cm,miles,yards,inches,feet all to m
def Distance(n,id,ed):
    meter_value_dic = {'km':n*1000,'cm':n*0.01,'miles':n*1609.344,
            'yards':n*0.91440000000001,'inches':n*0.0254,'feet': n*0.3048}
    v = meter_value_dic[id]
    final_value_dic = {'km':v/1000,'cm':v*100,'miles':v*0.00062137119223733,
            'yards':v*1.0936132983377,'inches':v*39.370078740157,'feet':v*3.2808398950131}
    return str(format(final_value_dic[ed],',.2f'))+' '+ed
def Draw_Text(text,size,x,y,color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

#FIX COLOR

def Button(x,y,width,height,color,msg,pressed=False):
    pygame.draw.rect(screen, color,(x,y,width,height))
    Draw_Text(str(msg),18,x+width/2,y+height/4,BLACK)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y+height > mouse[1] > y and click[0]:
        pygame.draw.rect(screen, (255,0,0),(x,y,width,height))
        Draw_Text(str(msg),18,x+width/2,y+height/4,BLACK)
        pressed = True
        return True
def Keyoard_Input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                return '0'
            if event.key == pygame.K_1:
                return '1'
            if event.key == pygame.K_2:
                return '2'
            if event.key == pygame.K_3:
                return '3'
            if event.key == pygame.K_4:
                return '4'
            if event.key == pygame.K_5:
                return '5'
            if event.key == pygame.K_6:
                return '6'
            if event.key == pygame.K_7:
                return '7'
            if event.key == pygame.K_8:
                return '8'
            if event.key == pygame.K_9:
                return '9'
    return ''
def Area_Screen(Show):
    Draw = False
    it = ''
    et = ''
    x=''
    while Show:
        screen.fill(BLACK)
        for event in pygame.event.get():
        # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    x=x[:-1]
                    Draw_Text(x,18,200,200,WHITE)
        if Button(0,HEIGHT-50,100,50,GREEN,'Back'):
            Show = False
        if Button(100,50,100,50,GREEN,'Celsius'):
            if it == '':
                it =  'c'
            else:
                et = 'c'
        if Button(250,50,100,50,GREEN,'Kalvin'):
            if it == '':
                it =  'k'
            else:
                et = 'k'
        if Button(400,50,100,50,GREEN,'Farenheit'):
            if it == '':
                it =  'f'
            else:
                et = 'f'
        x += Keyoard_Input()
        if Button(300,350,100,100,GREEN,'Convert'):
            Draw = True
        Draw_Text(x,18,200,200,WHITE)
        if Draw:
            Draw_Text(Temprature(int(x),it,et),18,300,200,WHITE)
        pygame.display.flip()
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Draw/render
    screen.fill(BLACK)
    if Button(200,25,100,50,GREEN,'Temprature'):
        Area_Screen(True)
    Button(200,125,100,50,GREEN,'Distance')
    Button(200,225,100,50,GREEN,'Area')
    Button(200,325,100,50,GREEN,'Volume')
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
