import pygame
import random
pygame.init()
branches=["START","ABOUT","EXIT"]
colors=[(255,0,0),(0,255,0),(0,0,255)]
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("road fighter")
font1=pygame.font.SysFont(pygame.font.get_fonts()[0],60,True,False)
font2=pygame.font.SysFont(pygame.font.get_fonts()[1],30,False,False)
def gameloop():
    ycord,yax,xax=500,0,100
    image1=pygame.image.load("-04.png")
    imagetrans1=pygame.transform.scale(image1,(600,600))
    exit_game=False
    mainmenu=True
    options=False
    carsdoged=0
    enemyx=random.randint(100,500)
    enemyy,playery=-50,500
    choice=random.randint(0,3)
    gameplay,gameover=False,False
    image2=pygame.image.load("1.png")
    player=pygame.image.load("player_burned.png")
    playertransformed=pygame.transform.scale(player,(100,100))
    imagetrans2=pygame.transform.scale(image2,(600,600))
    text1=font1.render("ROAD FIGHTER",1,(255,255,255))
    text3=font2.render("Press enter to retry",1,(255,255,255))
    text4=font2.render("Press enter to go to main menu",1,(0,0,255))
    image3=[pygame.image.load("enemy1.png"),pygame.image.load("enemy2.png"),pygame.image.load("enemy3.png"),pygame.image.load("enemy4.png")]
    image4=pygame.image.load("options.png")
    image4transformed=pygame.transform.scale(image4,(600,600))
    movements={"FORWARD":(70,65),"RIGHT":(440,510),"DOWN":(280,560),"LEFT":(180,510)}
    pygame.mixer_music.load("Knight Rider - The Game - 03 - Menu Music.wav")
    pygame.mixer_music.play(-1)
    while not(exit_game):
        if mainmenu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if 20<=pygame.mouse.get_pos()[0]<=170 and 500<=pygame.mouse.get_pos()[1]<=540:
                        gameplay=True
                        mainmenu=False
                    elif 220<=pygame.mouse.get_pos()[0]<=370 and 500<=pygame.mouse.get_pos()[1]<=540:
                        options=True
                        mainmenu=False
                    elif 420<=pygame.mouse.get_pos()[0]<=570 and 500<=pygame.mouse.get_pos()[1]<=540:
                        exit_game=True
            screen.blit(imagetrans1,(0,0))
            screen.blit(text1,(100,4))
            xcord=30
            for i in range(3):
                text2=font2.render(branches[i],1,(0,0,0))
                pygame.draw.rect(screen,colors[i],(xcord-10,ycord,150,40))
                screen.blit(text2,(xcord,ycord))
                xcord+=200
        elif options:
            screen.blit(image4transformed,(0,0))
            pygame.draw.line(screen,(255,0,0),(350,250),(100,100),4)
            pygame.draw.line(screen,(255,0,0),(450,350),(450,500),4)
            pygame.draw.line(screen,(255,0,0),(300,350),(300,550),4)
            pygame.draw.line(screen,(255,0,0),(150,350),(200,500),4)
            screen.blit(text4,(40,3))
            pygame.draw.line(screen,(0,0,255),(0,5),(600,5),4)
            for i in movements:
                optiontext=font2.render(i,1,(255,0,0))
                screen.blit(optiontext,movements[i])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        options=False
                        mainmenu=True
        elif gameover:
            screen.blit(text3,(200,550))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameplay=True
                        gameover=False
                        enemyy=-50
                        carsdoged=0
                        enemyx=random.randint(100,500)
        elif gameplay:
            
            screen.fill((255,255,255))
            pygame.mixer_music.load("Road Fighter (1985-07-11)(Konami) [6].wav")
            pygame.mixer_music.play(-1)
            score=font2.render(f"CARS DOGED:{carsdoged}",1,(255,255,255))
            if yax==600:
                yax=0
            screen.blit(imagetrans2,(0,yax))
            screen.blit(imagetrans2,(0,-600+yax))
            screen.blit(playertransformed,(xax,playery))
            image3trans=pygame.transform.scale(image3[choice],(100,100))
            screen.blit(image3trans,(enemyx,enemyy))
            screen.blit(score,(3,20))
            enemyy+=1
            if (enemyx<=xax<=enemyx+90 and enemyy<=playery<=enemyy+90) or (enemyx<=xax+90<=enemyx+90 and enemyy<=playery<=enemyy+90) or (enemyx<=xax+90<=enemyx+90 and enemyy<=playery+90<=enemyy+90) or (enemyx<=xax<=enemyx+90 and enemyy<=playery+90<=enemyy+90):
                gameplay=False
                gameover=True
                pygame.mixer_music.stop()
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("Road Fighter (1985-07-11)(Konami) [5].wav"))
            elif enemyy>600:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("Road Fighter (1985-07-11)(Konami) [13].wav"))
                enemyy=-50
                carsdoged+=1
                enemyx=random.randint(100,500)
                choice=random.randint(0,3)
                image3trans=pygame.transform.scale(image3[choice],(100,100))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        if xax>=0:
                            xax-=10
                    elif event.key==pygame.K_RIGHT:
                        if xax<=500:
                            xax+=10
                    elif event.key==pygame.K_UP:
                        if playery>=10:
                            playery-=10
                    elif event.key==pygame.K_DOWN:
                        if playery<=500:
                            playery+=10
            yax+=1
        pygame.display.update()
    pygame.quit()
gameloop()
