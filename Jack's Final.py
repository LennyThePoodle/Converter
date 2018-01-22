import pygame
import random

WIDTH = 600
HEIGHT = 400
FPS = 1000

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (30,144,255)
PURPLE = (204,0,204)
# initialize pygame and create window
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Measurment Calculator by Jack Campbell")
clock = pygame.time.Clock()

font_name=pygame.font.match_font('Arial')
#Used dictionaries, which are lists where each element has a value, to convert all to one unit and then from there to all other units as oppose
#to manualy putting every conversion in
def Temprature(n,it,et):
    if it == 'farenheit':
        c = (n-32)/1.8
        if et == 'celsius':
            return format(c,',.2f')
        elif et == 'kalvin':
            return format(c+273.15,',.2f')
    elif it == 'celsius':
        if et == 'farenheit':
            return format(1.8*n+32,',.2f')
        elif et == 'kalvin':
            return format(n+273.15,',.2f')
    elif it == 'kalvin':
        c = n-273.15
        if et == 'celsius':
            return format(c,',.2f')
        elif et == 'farenheit':
            return format(1.8*c+32,',.2f')
def Area(n,ia,ea):
    #convert all to squared meters
    c_dic = {'squared kilometers':n*1000000,'squared feet':n*0.09290304,'squared inches':n*0.00064516,'squared centimeters':n/10000,
             'squared meters':n,'acres':n*4046.8564224}
    #get the value in square meters
    x = c_dic[ia]
    #convert to the desired unit
    v_dic = {'acres':x*0.0002471053814672,'squared centimeters':x*10000,'squared feet':x*10.76391041671,
             'squared inches':x*1550.003100006,'squared kilometers':x*0.000001,'squared meters':x}
    return str(format(v_dic[ea], ',.2f'))
def Distance(n,id,ed):
    #convert all to meters
    meter_value_dic = {'kilometers':n*1000,'centimeters':n*0.01,'miles':n*1609.344,
            'meters':n,'feet': n*0.3048,'inches':n*0.0254}
    v = meter_value_dic[id]
    #convert meter to all units
    final_value_dic = {'kilometers':v/1000,'centimeters':v*100,'miles':v*0.00062137119223733,
            'meters':v,'inches':v*39.370078740157,'feet':v*3.2808398950131}
    return str(format(final_value_dic[ed],',.2f'))
def Volume(n,iv,ev):
    #convert all to liters
    liter_value_dict = {"liters":n,"milliliters":n/1000,"gallons":n*3.78541,
                "fluid ounces":n*0.0295735,"pints":n*0.473176}
    x = liter_value_dict[iv]
    #convert from liter to all other units
    final_value_dic = {"liters":x, "milliliters":x*100,"gallons":x*0.264172,
                "fluid ounces":x*33.814,"pints":n*2.11338}
    return str(format(final_value_dic[ev],',.2f'))
#font_size get a default value of 18 and pressed a default value  of false
def Draw_Text(text,size,x,y,color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)
def History_file(initial,end,x):
    #opens up a file and writes the conversion into it
    f=open('history.txt','w+')
    f.write(x+' '+ initial+' = '+end)
    f.close()
#gives a default font size of 18
def Button(x,y,width,height,color,msg,font_size=18):
    #draws the rectangles
    pygame.draw.rect(screen, color,(x,y,width,height))
    pygame.draw.rect(screen, WHITE,(x,y,width,height),1)
    Draw_Text(str(msg),font_size,x+width/2,y+height/4,BLACK)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #checks if the button is pressd
    if x+width > mouse[0] > x and y+height > mouse[1] > y and click[0]:
        pygame.draw.rect(screen, (255,0,0),(x,y,width,height))
        Draw_Text(str(msg),font_size,x+width/2,y+height/4,BLACK)
        return True
def Keyoard_Input():
    #function to input keyboard keys
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
            if event.key == pygame.K_PERIOD:
                return '.'
    return ''
def Temprature_Screen(Show):
    Draw = False
    it = ''
    et = ''
    x=''
    Empty = True
    while Show:
        screen.fill(BLACK)
        if x != '':
            Empty = False
        for event in pygame.event.get():
        # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    x=x[:-1]
                    Draw_Text(x,18,200,200,WHITE)
                if not Empty:
                    if event.key == pygame.K_RETURN and x[-1] != '.':
                        Draw = True
        if Button(WIDTH-100,HEIGHT-50,100,50,GREEN,'Back'):
            Show = False
        if Button(100,50,100,50,GREEN,'Celsius') and it!='celsius':
            if it == '':
                it =  'celsius'
            else:
                et = 'celsius'
        if Button(250,50,100,50,GREEN,'Kalvin')and it!='kalvin':
            if it == '':
                it =  'kalvin'
            else:
                et = 'kalvin'
        if Button(400,50,100,50,GREEN,'Farenheit')and it!='farenheit':
            if it == '':
                it =  'farenheit'
            else:
                et = 'farenheit'
        x += Keyoard_Input()
        if x.count('.') == 2:
            x=x[:-1]
        if Button(300,300, 50,50,GREEN,'Convert')and not Empty:
            if x[-1] !='.':
                Draw = True
                History_file(it,str(Temprature(float(x),it,et))+' '+et,x)
        Draw_Text(x+' '+ it,18,150,200,WHITE)
        if Draw:
            Draw_Text(str(Temprature(float(x),it,et))+ ' '  + et,18,400,200,WHITE)
        else:
            Draw_Text(et,18,400,200,WHITE)
        if Button(150,300,50,50,GREEN,'New'):
            it = ''
            et=''
            Draw = False
            Empty = True
            x=''
        pygame.display.flip()
def Area_Screen(Show):
    Draw = False
    #initial area, end area, and the number
    ia= ''
    ea = ''
    x=''
    Empty = True
    while Show:
        screen.fill(BLACK)
        if x != '':
            Empty = False
        for event in pygame.event.get():
        # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    x=x[:-1]
                    Draw_Text(x,18,200,200,WHITE)
                if not Empty:
                    if event.key == pygame.K_RETURN and x[-1] != '.':
                        Draw = True
        if Button(WIDTH-100,HEIGHT-50,100,50,GREEN,'Back'):
            Show = False
        if Button(100,10,100,50,GREEN,'Squared Kilometers',14) and ia!='squared kilometers':
            if ia == '':
                ia =  'squared kilometers'
            else:
                ea = 'squared kilometers'
        if Button(220,10,100,50,GREEN,'Squared Feet',16)and ia!='squared feet':
            if ia == '':
                ia =  'squared feet'
            else:
                ea = 'squared feet'
        if Button(340,10,100,50,GREEN,'Squared Inches',16)and ia!='squared inches':
            if ia == '':
                ia =  'squared inches'
            else:
                ea = 'squared inches'
        if Button(100,80,100,50,GREEN,'Squared Centimeters',14) and ia!='squared centimeters':
            if ia == '':
                ia =  'squared centimeters'
            else:
                ea = 'squared centimeters'
        if Button(220,80,100,50,GREEN,'Squared Meters',16)and ia!='squared meters':
            if ia == '':
                ia =  'squared meters'
            else:
                ea = 'squared meters'
        if Button(340,80,100,50,GREEN,'Acres')and ia!='acres':
            if ia == '':
                ia =  'acres'
            else:
                ea = 'acres'
        x += Keyoard_Input()
        if x.count('.') == 2:
            x=x[:-1]
        if Button(300,300, 50,50,GREEN,'Convert')and not Empty:
            if x[-1] !='.':
                Draw = True
                History_file(ia,str(Area(float(x),ia,ea))+' '+ea,x)
        Draw_Text(x+' '+ ia,18,150,200,WHITE)
        if Draw:
            Draw_Text(str(Area(float(x),ia,ea))+ ' '  + ea,18,400,200,WHITE)
        else:
            Draw_Text(ea,18,400,200,WHITE)
        if Button(150,300,50,50,GREEN,'New'):
            ia = ''
            ea=''
            Draw = False
            Empty = True
            x=''
        pygame.display.flip()
def Distance_Screen(Show):
    Draw = False
    #initial distance, distance, and the number
    id= ''
    ed= ''
    x=''
    Empty = True
    while Show:
        screen.fill(BLACK)
        if x != '':
            Empty = False
        for event in pygame.event.get():
        # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    x=x[:-1]
                    Draw_Text(x,18,200,200,WHITE)
                if not Empty:
                    if event.key == pygame.K_RETURN and x[-1] != '.':
                        Draw = True
        if Button(WIDTH-100,HEIGHT-50,100,50,GREEN,'Back'):
            Show = False
        if Button(100,10,100,50,GREEN,'Kilometers') and id!='kilometers':
            if id == '':
                id =  'kilometers'
            else:
                ed = 'kilometers'
        if Button(220,10,100,50,GREEN,'Centimeters')and id!='centimeters':
            if id == '':
                id =  'centimeters'
            else:
                ed = 'centimeters'
        if Button(340,10,100,50,GREEN,'Miles')and id!='miles':
            if id == '':
                id =  'miles'
            else:
                ed = 'miles'
        if Button(100,80,100,50,GREEN,'Meters') and id!='meters':
            if id == '':
                id =  'meters'
            else:
                ed = 'meters'
        if Button(220,80,100,50,GREEN,'Inches')and id!='inches':
            if id == '':
                id =  'inches'
            else:
                ed = 'inches'
        if Button(340,80,100,50,GREEN,'Feet')and id!='feet':
            if id == '':
                id =  'feet'
            else:
                ed = 'feet'
        x += Keyoard_Input()
        if x.count('.') == 2:
            x=x[:-1]
        if Button(300,300, 50,50,GREEN,'Convert')and not Empty:
            if x[-1] !='.':
                Draw = True
                History_file(id,str(Distance(float(x),id,ed))+' '+ed,x)
        Draw_Text(x+' '+ id,18,150,200,WHITE)
        if Draw:
            Draw_Text(str(Distance(float(x),id,ed))+ ' '  + ed,18,400,200,WHITE)
        else:
            Draw_Text(ed,18,400,200,WHITE)
        if Button(150,300,50,50,GREEN,'New'):
            id = ''
            ed=''
            Draw = False
            Empty = True
            x=''
        pygame.display.flip()
def Volume_Screen(Show):
    Draw = False
    #initial distance, distance, and the number
    iv= ''
    ev= ''
    x=''
    Empty = True
    while Show:
        screen.fill(BLACK)
        if x != '':
            Empty = False
        for event in pygame.event.get():
        # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    x=x[:-1]
                    Draw_Text(x,18,200,200,WHITE)
                if not Empty:
                    if event.key == pygame.K_RETURN and x[-1] != '.':
                        Draw = True
        if Button(WIDTH-100,HEIGHT-50,100,50,GREEN,'Back'):
            Show = False
        if Button(100,10,100,50,GREEN,'Liters') and iv!='liters':
            if iv == '':
                iv =  'liters'
            else:
                ev = 'liters'
        if Button(220,10,100,50,GREEN,"Milliliters")and iv!='milliliters':
            if iv == '':
                iv =  'milliliters'
            else:
                ev = 'milliliters'
        if Button(340,10,100,50,GREEN,'US Liquid Gallons',14)and iv!='gallons':
            if iv == '':
                iv =  'gallons'
            else:
                ev = 'gallons'
        if Button(220,80,100,50,GREEN,'US Fluid Ounces',14) and iv!='fluid ounces':
            if iv == '':
                iv =  'fluid ounces'
            else:
                ev = 'fluid ounces'
        if Button(100,80,100,50,GREEN,'US Liquid Pinrs',14) and iv!='pints':
            if iv == '':
                iv =  'pints'
            else:
                ev = 'pints'

        x += Keyoard_Input()
        if x.count('.') == 2:
            x=x[:-1]
        if Button(300,300, 50,50,GREEN,'Convert')and not Empty:
            if x[-1] !='.':
                Draw = True
                History_file(iv,str(Volume(float(x),iv,ev))+' '+ev,x)
        Draw_Text(x+' '+ iv,18,150,200,WHITE)
        if Draw:
            Draw_Text(str(Volume(float(x),iv,ev))+ ' '  + ev,18,400,200,WHITE)
        else:
            Draw_Text(ev,18,400,200,WHITE)
        if Button(150,300,50,50,GREEN,'New'):
            iv = ''
            ev=''
            Draw = False
            Empty = True
            x=''
        pygame.display.flip()
Main_Screen = True
while Main_Screen:
    clock.tick(10)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            Main_Screen = False

    screen.fill(BLACK)
    Draw_Text('UNIT CONVERTER',45,WIDTH/2,HEIGHT/3,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
    Draw_Text('BY JACK CAMPBELL',30,WIDTH/2,HEIGHT/3+50,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
    if Button(WIDTH/2-50,300,100,50,PURPLE,'START',24):
        Main_Screen = False
        running = True
    pygame.display.flip()
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Draw/render
    screen.fill(BLACK)
    if Button(50,25,100,50,GREEN,'Temprature',23):
        Temprature_Screen(True)
    if Button(50,125,100,50,GREEN,'Distance',24):
        Distance_Screen(True)
    if Button(50,225,100,50,GREEN,'Area',24):
        Area_Screen(True)
    if Button(50,325,100,50,GREEN,'Volume',24):
        Volume_Screen(True)
    f=open('history.txt','r')
    Draw_Text("Last Conversion:",24,325,60,WHITE)
    Draw_Text(f.read(),24,325,85,WHITE)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
