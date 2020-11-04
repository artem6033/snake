
import pygame 
import random

pygame.init()
dis_width = 800
dis_height = 600
win = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("snake")
     
x = 0 
y = 0


speed = 10
rasvorot = 10
x_fruct = round(random.randrange(0, dis_width - 20) / 10.0) * 10.0
y_fruct = round(random.randrange(0, dis_height - 20) / 10.0) * 10.0
#x_fruct = random.randint(25 , 450)
#y_fruct = random.randint(25, 450)

x_dvihenie = True
y_dvihenie = False
y1_dvihenie = 0
x1_dvihenie = 0
width2 = 10
width = 20
height = 20
num = 20

pole = pygame.image.load('pole.jpg')

f = x - x_fruct
hg = y - y_fruct
xv = x + 15
yv = y + 15
x_v = x_fruct + 15
y_v = y_fruct + 15 


run = True
while run:
    
    pygame.time.delay(30)
   
    
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
        

    if  keys[pygame.K_RIGHT]:
        
   
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
  
    #print(str(y) + "  1y  ")
    #print(str(x_fruct) +  " 2x") 
        
    #print(str(y_fruct) + " 2y")    
    if  x == x_fruct and y == y_fruct:
        x_fruct = round(random.randrange(0, dis_width - 20) / 10.0) * 10.0
        y_fruct = round(random.randrange(0, dis_height - 20) / 10.0) * 10.0
        
       
    if x >= dis_width or x < 0 or y >= dis_height or y < 0:
        run = False
    
    

    win.blit(pole, (0,0))
    

    pygame.draw.rect(win, (0, 0, 255), (x, y, height, width))
        

    
    pygame.draw.rect(win, (0,255, 0, ), (x_fruct, y_fruct, 20, 20))
    
    
    pygame.display.update()
   

pygame.quit()
