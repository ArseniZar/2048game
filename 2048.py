import pygame
import random
import copy
HIGHT_SIZE = 500
WIGHT_SIZE = 500
HIGHT = 700
WIGHT = 700
SIZE_X = 4
SIZE_Y = 4

pygame.init()
window_size = (WIGHT, HIGHT)
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((WIGHT,HIGHT), pygame.RESIZABLE)
saturation = 100
black = (0, 0, 0) 
white = (255, 255, 255)                        
gray = (192, 192, 192)
crem = (250, 248, 239)
gray_black = (128, 128, 128)
game_over = (119, 110, 101)
ret = (187, 173, 160)
color_number = gray_black
bag_ground_play = ret
bag_ground = crem
fps = 10 



# fild1 = [[0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0]]

class Plyta:
    
    COLOR_PLYT = [[0, 2, 4, 8, 16, 32, 64, 128],
             [(205, 193, 180), (238, 228, 218), (238, 225, 201), (243, 178, 122), (246, 150, 100), (247, 124, 95),(247, 95, 59), (237, 208, 115)]]
    
    COLOR_NUMBER_2_4 = (119, 110, 101)
    COLOR_OTHER = (249, 246, 242)
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__valut = random.randrange(0, 4, 2)
        self.setColor()
    
                    
                    
    def setColor(self):
        if(self.__valut == 2 or self.__valut == 4):
            color_object= (self.COLOR_NUMBER_2_4[0]*saturation/100,self.COLOR_NUMBER_2_4[1]*saturation/100,self.COLOR_NUMBER_2_4[2]*saturation/100)
            self.__colorNum = color_object
        else:
            color_object= (self.COLOR_OTHER[0]*saturation/100,self.COLOR_OTHER[1]*saturation/100,self.COLOR_OTHER[2]*saturation/100)
            self.__colorNum = color_object
        
        if(self.__valut>= self.COLOR_PLYT[0][len(self.COLOR_PLYT[0])-1]):
            self.__color = self.COLOR_PLYT[1][len(self.COLOR_PLYT[1])-1]
        else:
            for index in range(len(self.COLOR_PLYT[0])-1):
                if (self.COLOR_PLYT[0][index]== self.__valut):
                    color_object = (self.COLOR_PLYT[1][index][0]*saturation/100,self.COLOR_PLYT[1][index][1]*saturation/100,self.COLOR_PLYT[1][index][2]*saturation/100)
                    self.__color= color_object
                    break    
    
    def getColorNum(self):
        return self.__colorNum
    
    def getColor(self):
        return self.__color 
                  
    def getValut(self):
        return self.__valut

    def setValut(self,valut):
        self.__valut = valut
        self.setColor()
        return self.__valut 
    
    def __eq__(self, other):
        return self.__valut == other.getValut()

class Right:
   

    def __sortR(y):
        previous_index_x = -1
        previous_index_y = -1
        for x in range(len(fild[y])-1, -1, -1):

            if (previous_index_x != -1 and previous_index_y != -1):
                Right.__swapR(x, y, previous_index_x, previous_index_y)
            previous_index_x = x
            previous_index_y = y
            # print(fild[0], end=" ")

    def __swapR(index_new_x, index_new_y, index_old_x, index_old_y):
        if  fild[index_old_y][index_old_x].getValut() == 0 and fild[index_new_y][index_new_x].getValut() != 0:
            fild[index_old_y][index_old_x].setValut(fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            if (index_old_x != len(fild[index_new_y])-1 and fild[index_old_y][index_old_x+1].getValut() == 0):
                Right.__swapR(index_new_x + 1, index_new_y,
                            index_old_x + 1, index_old_y)

    def __sumR(index_new_x, index_new_y, index_old_x, index_old_y):
        if (fild[index_new_y][index_new_x].getValut() != 0 and fild[index_old_y][index_old_x].getValut() == fild[index_new_y][index_new_x].getValut()):
            fild[index_old_y][index_old_x].setValut(fild[index_old_y][index_old_x].getValut() + fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            Right.__sortR(index_new_y)
            return True
        elif (index_new_x != 0 and fild[index_new_y][index_new_x].getValut() != 0):
            Right.__sumR(index_new_x-1, index_new_y, index_old_x-1, index_old_y)
        else:
            return False
    def right():
        for y in range(len(fild)):
            Right.__sortR(y)

        for y in range(len(fild)):
            previous_index_x = -1
            previous_index_y = -1
            for x in range(len(fild[y])-1, -1, -1):
                if (previous_index_x != -1 and previous_index_y != -1):
                    Right.__sumR(x, y, previous_index_x, previous_index_y)
                previous_index_x = x
                previous_index_y = y
        for row in fild:
            print("[", end=' ')
            for plyta_obj in row:
                print(plyta_obj.getValut(), end=' ')
            print("]")
    

class Left:

    def __sortL(y):
        previous_index_x = -1
        previous_index_y = -1
        for x in range(len(fild[y])):

            if (previous_index_x != -1 and previous_index_y != -1):
                Left.__swapL(x, y, previous_index_x, previous_index_y)
            previous_index_x = x
            previous_index_y = y
            # print(fild[0], end=" ")


    def __swapL(index_new_x, index_new_y, index_old_x, index_old_y):
        if fild[index_old_y][index_old_x].getValut() == 0 and fild[index_new_y][index_new_x].getValut() != 0:
            fild[index_old_y][index_old_x].setValut(fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            if (index_old_x != 0 and fild[index_old_y][index_old_x-1].getValut() == 0):
                Left.__swapL(index_new_x - 1, index_new_y,
                           index_old_x - 1, index_old_y)

    def __sumL(index_new_x, index_new_y, index_old_x, index_old_y):
        if (fild[index_new_y][index_new_x].getValut() != 0 and fild[index_old_y][index_old_x].getValut() == fild[index_new_y][index_new_x].getValut()):
            fild[index_old_y][index_old_x].setValut(fild[index_old_y][index_old_x].getValut() + fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            Left.__sortL(index_new_y)
            return True
        elif (index_new_x != len(fild[index_new_y])-1 and fild[index_new_y][index_new_x].getValut() != 0):
            Left.__sumL(index_new_x+1, index_new_y, index_old_x+1, index_old_y)
        else:
            return False
    def left():

        for y in range(len(fild)):
            Left.__sortL(y)

        for y in range(len(fild)):
            previous_index_x = -1
            previous_index_y = -1
            for x in range(len(fild[y])):
                if (previous_index_x != -1 and previous_index_y != -1):
                    Left.__sumL(x, y, previous_index_x, previous_index_y)
                previous_index_x = x
                previous_index_y = y
        for row in fild:
            print("[", end=' ')
            for plyta_obj in row:
                print(plyta_obj.getValut(), end=' ')
            print("]")


class Up:
    def __sortUp(x):
        previous_index_x = -1
        previous_index_y = -1
        for y in range(len(fild)):

            if (previous_index_x != -1 and previous_index_y != -1):
                Up.__swapUp(x, y, previous_index_x, previous_index_y)
            previous_index_x = x
            previous_index_y = y
            # print(fild[0], end=" ")

    def __swapUp(index_new_x, index_new_y, index_old_x, index_old_y):
        if fild[index_old_y][index_old_x].getValut() == 0 and fild[index_new_y][index_new_x].getValut() != 0:
            fild[index_old_y][index_old_x].setValut(fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            if (index_old_y != 0 and fild[index_old_y-1][index_old_x].getValut() == 0):
                Up.__swapUp(index_new_x, index_new_y-1,
                          index_old_x, index_old_y-1)

    def __sumUp(index_new_x, index_new_y, index_old_x, index_old_y):
        if (fild[index_new_y][index_new_x].getValut() != 0 and fild[index_old_y][index_old_x].getValut() == fild[index_new_y][index_new_x].getValut()):
            fild[index_old_y][index_old_x].setValut(fild[index_old_y][index_old_x].getValut() + fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            Up.__sortUp(index_new_x)
            return True
        elif (index_new_y != len(fild)-1 and fild[index_new_y][index_new_x].getValut() != 0):
            Up.__sumUp(index_new_x, index_new_y+1, index_old_x, index_old_y+1)
        else:
            return False

    def up():

        for x in range(len(fild[0])):
            Up.__sortUp(x)

        for x in range(len(fild[0])):
            previous_index_x = -1
            previous_index_y = -1
            for y in range(len(fild)):
                if (previous_index_x != -1 and previous_index_y != -1):
                    Up.__sumUp(x, y, previous_index_x, previous_index_y)
                previous_index_x = x
                previous_index_y = y
        for row in fild:
            print("[", end=' ')
            for plyta_obj in row:
                print(plyta_obj.getValut(), end=' ')
            print("]")


class Down:
    def __sortDown(x):
        previous_index_x = -1
        previous_index_y = -1
        for y in range(len(fild) - 1, -1, -1):

            if (previous_index_x != -1 and previous_index_y != -1):
                Down.__swapDown(x, y, previous_index_x, previous_index_y)
            previous_index_x = x
            previous_index_y = y
            # print(fild[0], end=" ")

    def __swapDown(index_new_x, index_new_y, index_old_x, index_old_y):
        if fild[index_old_y][index_old_x].getValut() == 0 and fild[index_new_y][index_new_x].getValut() != 0:
            fild[index_old_y][index_old_x].setValut(fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            if (index_old_y != len(fild) - 1 and fild[index_old_y+1][index_old_x].getValut() == 0):
                Down.__swapDown(index_new_x, index_new_y+1,
                              index_old_x, index_old_y+1)

    def __sumDown(index_new_x, index_new_y, index_old_x, index_old_y):
        if ((fild[index_new_y][index_new_x].getValut() != 0 and fild[index_old_y][index_old_x].getValut() == fild[index_new_y][index_new_x].getValut())):
            fild[index_old_y][index_old_x].setValut(fild[index_old_y][index_old_x].getValut() + fild[index_new_y][index_new_x].getValut())
            fild[index_new_y][index_new_x].setValut(0)
            Down.__sortDown(index_new_x)
            return True
        elif (index_new_y != 0 and fild[index_new_y][index_new_x].getValut() != 0):
            Down.__sumDown(index_new_x, index_new_y-1,
                         index_old_x, index_old_y-1)
        else:
            return False
    def down():

        for x in range(len(fild[0])):
            Down.__sortDown(x)

        for x in range(len(fild[0])):
            previous_index_x = -1
            previous_index_y = -1
            for y in range(len(fild)-1, -1, -1):
                if (previous_index_x != -1 and previous_index_y != -1):
                    Down.__sumDown(x, y, previous_index_x, previous_index_y)
                previous_index_x = x
                previous_index_y = y
        for row in fild:
            print("[", end=' ')
            for plyta_obj in row:
                print(plyta_obj.getValut(), end=' ')
            print("]")
# def super(valut):
#       if(valut == 2048 ):
#         ;


def draw_plyt():
    probel = 20
    for y in range(len(fild)):
        for x in range(len(fild[y])):
            pygame.draw.rect(screen, fild[y][x].getColor(), ((WIGHT-WIGHT_SIZE)/2+(0+5)+(WIGHT_SIZE/SIZE_X+1)*x, (HIGHT-HIGHT_SIZE)/2+(0+5)+(HIGHT_SIZE/SIZE_Y+1)*y, (WIGHT_SIZE/SIZE_X-13), (HIGHT_SIZE/SIZE_Y-13)),border_radius = 6)
            if(fild[y][x].getValut() != 0):
                
                __string = str(fild[y][x].getValut())
                font_size = 60
                change = 35*len(__string)
                if( int (len(__string)) > 3):
                    if((len(__string)-3) %2 ==1):
                        font_size=font_size-20*(len(__string)-3) 
                        change = change - 13*len(__string)
                    else:
                        font_size=font_size-20*(len(__string)-4) 
                        change = change - 13*len(__string)
                    
                    
                __font = pygame.font.SysFont('Helvetica', font_size)
                __text = __font.render(__string, True, fild[y][x].getColorNum())   
                        
                screen.blit(__text, ((WIGHT-WIGHT_SIZE)/2+(WIGHT_SIZE/SIZE_X-change)/2+(WIGHT_SIZE/SIZE_X+1)* x, (HIGHT-HIGHT_SIZE)/2+(HIGHT_SIZE/SIZE_Y-40)/2+(HIGHT_SIZE/SIZE_Y+1)*y))
    pygame.display.update()

def clear():
    
    screen.fill(bag_ground)
    radius = 6
    rect = pygame.Rect((WIGHT-WIGHT_SIZE)/2,
                       (HIGHT-HIGHT_SIZE)/2, (WIGHT_SIZE), (HIGHT_SIZE))
    pygame.draw.rect(screen, bag_ground_play, rect, border_radius=radius)
    pygame.display.update()

def rad():
    
    
    global fild
    number = 0
    __exit =  False
    for y in range(len(fild)):
        for x in range(len(fild[y])):
            if (number == 2):
                break

            if (fild[y][x].getValut() == 0 and (random.randint(0, 4) == 2 or random.randint(0, 4) == 4)):
                fild[y][x] = Plyta(x, y)
                number += 1
        
        
    fild_past = copy.deepcopy(fild)
    
    Up.up()
    if(fild_past.__eq__( fild)):
        Right.right()
        if(fild_past.__eq__( fild)):
            Left.left() 
            if(fild_past.__eq__( fild)):
                Down.down()  
                if(fild_past.__eq__( fild)):
                    __exit = True
    
    fild = copy.deepcopy(fild_past)
    
    return __exit
# clear()
# draw_plyt()
# text = font.render(str(fild[0][0].getValut()), True, color_number, color_number)
def saturations(): 
    global bag_ground
    global bag_ground_play
    global color_number
    
    bag_ground = (250*saturation/100, 248*saturation/100, 239*saturation/100)
    bag_ground_play = (187*saturation/100, 173*saturation/100, 160*saturation/100)
    color_number = (128*saturation/100, 128*saturation/100, 128*saturation/100)
        
    for y in range(len(fild)):
        for x in range(len(fild[y])):
            fild[y][x].setColor()


def restrart():
    global fild 
    global last
    global exits
    global flag 
    fild = [[Plyta(x, y) for x in range(SIZE_X)] for y in range(SIZE_Y)]
    # for row in fild:
    #     print("[", end=' ')
    #     for plyta_obj in row:
    #         print(plyta_obj.getValut(), end=' ')
    #     print("]")
    # print()
    clear()
    draw_plyt()
    last = ""
    exits = False
    flag = True



# textRect = text.get_rect()
# textRect.center = ((WIGHT/4)/2,(HIGHT/4)/2)
# screen.blit(text, textRect)
# def animation(direction):
#     for f in range (fps+1):
#         for y in range(len(fild_past)):
#             for x in range(len(fild_past[y])-1 ,-1,-1):
#                 if(fild_past[y][x].getValut() !=  0 and x != len(fild_past[y])-1):
#                     pygame.draw.rect(screen, fild_past[y][x].getColor(), ((WIGHT-WIGHT_SIZE)/2+(0+5)+(WIGHT_SIZE/4+1)*x +(WIGHT_SIZE/4+1)*(len(fild_past[y])-1-x)/fps*f, (HIGHT-HIGHT_SIZE)/2+(0+5)+(HIGHT_SIZE/4+1)*y, (WIGHT_SIZE/4-13), (HIGHT_SIZE/4-13)),border_radius = 6)
#                     pygame.display.update()
        
#         for y in range(len(fild_past)):
#             for x in range(len(fild_past[y])-1 ,-1,-1):
#                 if(fild_past[y][x].getValut() !=  0 and x != len(fild_past[y])-1):   
#                     pygame.time.delay(4)
#                     pygame.draw.rect(screen, bag_ground_play, ((WIGHT-WIGHT_SIZE)/2+(0+5)+(WIGHT_SIZE/4+1)*x +(WIGHT_SIZE/4+1)*(len(fild_past[y])-1-x)/fps*f, (HIGHT-HIGHT_SIZE)/2+(0+5)+(HIGHT_SIZE/4+1)*y, (WIGHT_SIZE/4-13), (HIGHT_SIZE/4-13)),border_radius = 6)            
                   
                    
#         for y in range(len(fild_past)):
#             for x in range(len(fild_past[y])-1 ,-1,-1):
#                 if(fild_past[y][x].getValut() ==  0):
#                     pygame.draw.rect(screen, fild[y][x].getColor(), ((WIGHT-WIGHT_SIZE)/2+(0+5)+(WIGHT_SIZE/4+1)*x, (HIGHT-HIGHT_SIZE)/2+(0+5)+(HIGHT_SIZE/4+1)*y, (WIGHT_SIZE/4-13), (HIGHT_SIZE/4-13)),border_radius = 6)
    #  for y in range(len(fild_past)):
    #     for x in range(len(fild_past[y])-1 ,-1,-1):
    #         if(fild_past[y][x].getValut() !=  0):
    #           
                   
# Right.right()
# Left.left()
# Up.Up()
# Down.Down()

restrart()


while True:

        for event in pygame.event.get():
            # random.randrange(0, 4, 1)
            # match random.randrange(1, 4, 1):
            #     case 1:
            #         keyboard.press('a')
            #         keyboard.release('a')
            #     case 2:
            #         keyboard.press('w')
            #         keyboard.release('w')
            #     case 3:
            #         keyboard.press('s')
            #         keyboard.release('s')
            #     case 4:
            #         keyboard.press('d')
            #         keyboard.release('d')
                    
                    
            keys = pygame.key.get_pressed()
            
                   
                    
            if(flag):
                
                if( keys[pygame.K_LEFT] or keys[pygame.K_a] ) and exits == False:
                    Left.left()
                    if (last != keys):
                        exits = rad()
                        last = keys
                    draw_plyt()

                if (keys[pygame.K_RIGHT] or keys[pygame.K_d] ) and exits == False:
                    Right.right()

                    if (last != keys):
                        exits = rad()
                        last = keys
                    draw_plyt()

                if (keys[pygame.K_UP] or keys[pygame.K_w] ) and exits == False:
                    Up.up()

                    if (last != keys):
                        exits = rad()
                        last = keys
                    draw_plyt()

                if (keys[pygame.K_DOWN] or keys[pygame.K_s] ) and exits == False:
                    Down.down()

                    if (last != keys):
                        exits = rad()
                        last = keys
                    draw_plyt()
                    
                if (exits and flag):
                    saturation = 80
                    saturations()
                    clear()
                    draw_plyt()
                    font = pygame.font.SysFont('Helvetica', 80, 1)
                    name = "Game Over"
                    text = font.render(name, True,game_over)     
                                  
                    screen.blit(text, ((WIGHT-WIGHT_SIZE)/2+WIGHT_SIZE/2-len(name)/2*50 , (HIGHT-HIGHT_SIZE)/2+HIGHT_SIZE/2-40))
                    pygame.display.update()
                    flag = False
            
            if keys[pygame.K_r] and pygame.key.get_mods() & pygame.K_LCTRL:
                restrart()
            
                
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif keys[pygame.K_q] and pygame.key.get_mods() & pygame.K_LCTRL: 
                pygame.quit()
                exit()
            
            
                
               