
import pygame 
import random


pygame.init()
dis_width = 800   # указываем высоту и ширину экрана
dis_height = 600
win = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("snake") # пишем название экрана
     
x = 0 # начальные координаты змейки
y = 0

speed = 10  # скорость змейки 

x_fruct = round(random.randrange(0, dis_width - 20) / 10.0) * 10.0 # спавн фрукта
y_fruct = round(random.randrange(0, dis_height - 20) / 10.0) * 10.0


x_dvihenie = True  # оринтация змейки по направления 
y_dvihenie = False
y1_dvihenie = 0
x1_dvihenie = 0

width = 20  # размеры змейки
height = 20
meny = True

second = 0

pole = pygame.image.load('pole.jpg')     # спрайты поля и меню
meny_jpg = pygame.image.load('meny.jpg')
Game_over = pygame.image.load('Game_over.jpg')





run = True
while run:
  
    pygame.time.delay(30)
   
    if meny == True: # игра после меню 
     

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

 
        keys = pygame.key.get_pressed()
        if x_dvihenie == True:
            x += speed
        if y_dvihenie == True:
            y += speed
        if x1_dvihenie == True:
            x -= speed
        if y1_dvihenie == True:
            y -= speed
        

        if keys[pygame.K_LEFT]:    
            x1_dvihenie  = True
            x_dvihenie = False
            y_dvihenie  = False
            y1_dvihenie = False
            x -= speed
        

        if keys[pygame.K_RIGHT]:
            x_dvihenie  = True
            y_dvihenie  = False
            x1_dvihenie = False
            y1_dvihenie = False
            x += speed
        
            
        if keys[pygame.K_UP]:      
            x1_dvihenie = False
            y1_dvihenie = True
            x_dvihenie  = False    
            y_dvihenie  = False
            y -= speed

        
        if keys[pygame.K_DOWN]:       
            x_dvihenie  = False
            y_dvihenie  = True
            x1_dvihenie = False
            y1_dvihenie = False
            y += speed
  
       
        if  x == x_fruct and y == y_fruct:
            x_fruct = round(random.randrange(0, dis_width - 20) / 10.0) * 10.0
            y_fruct = round(random.randrange(0, dis_height - 20) / 10.0) * 10.0
        
       
        if x >= dis_width or x < 0 or y >= dis_height or y < 0: # границы поля 
                win.blit(Game_over,(0,0))
                if keys[pygame.K_e]:
                    meny = False
            
          
        else:
            win.blit(pole, (0,0))
            pygame.draw.rect(win, (0, 0, 255), (x, y, height, width))       # отрисовка змейки и фрукта
            pygame.draw.rect(win, (0,255, 0, ), (x_fruct, y_fruct, 20, 20))

        pygame.display.update()

    else: #  меню
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        win.blit(meny_jpg, (0,0))
        pygame.display.update()


        

    
 
   

pygame.quit()
