import pygame
pygame.init()
s=pygame.display.set_mode((800,600))
s.fill((0,0,0))
score1=0
score2=0
p1position=10
p1velocity=0
p2velocity=0
p2position=10
clock=pygame.time.Clock()
bxposition=400
byposition=300
bxvelocity=-10
byvelocity=10
def stick(x,y):
    z=10
    if y==2:
        z=780
    pygame.draw.rect(s,(225,225,225),(z,x,10,100))
def ball(x,y):
    pygame.draw.circle(s,(225,225,225),(x,y),5)
while(1):
    for i in pygame.event.get():
        if i.type==12:
            print(score1,score2)
            pygame.quit()
            quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_UP:
                p2velocity=-10
            if i.key==pygame.K_DOWN:
                p2velocity=10
            if i.key==pygame.K_w:
                p1velocity=-10
            if i.key==pygame.K_s:
                p1velocity=10
        if i.type==pygame.KEYUP:
            if i.key==pygame.K_UP:
                p2velocity=0
            if i.key==pygame.K_DOWN:
                p2velocity=0
            if i.key==pygame.K_w:
                p1velocity=0
            if i.key==pygame.K_s:
                p1velocity=0
    if 0 < p1position + p1velocity < 500 :
        p1position=p1position+p1velocity
    if 0 < p2position + p2velocity < 500 :
        p2position=p2position+p2velocity
    s.fill((0, 0, 0))
    stick(p1position,1)
    stick(p2position,2)


    if bxposition+bxvelocity==20:
        if p1position<=byposition<=p1position+100:
            bxvelocity=-bxvelocity
        else:
            score2=score2+1
            bxposition=400
            byposition=300
            bxvelocity=-bxvelocity
    if bxposition+bxvelocity==780:
        if p2position<=byposition<=p2position+100:
            bxvelocity=-bxvelocity
        else:
            score1=score1+1
            bxposition=400
            byposition=300
            bxvelocity=-bxvelocity



    bxposition = bxposition + bxvelocity
    if 10<byposition+byvelocity<590:
        byposition=byposition+byvelocity
    else:
        byvelocity=-byvelocity
    ball(bxposition,byposition)
    pygame.display.update()
    clock.tick(30)