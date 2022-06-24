# import modules and libraries
import numpy as np
import cv2
import random
import pickle
from os import path
from TicTacToeAI import gameAI

def exitGame():
    bg=cv2.blur(game.mygame,(18,18))
    cv2.putText(bg,'THANKS FOR PLAYING',(330,310),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    with open('data.pak','wb') as f:
        pickle.dump(game.player, f)
        pickle.dump(game.computer,f)
        f.close()
    cv2.imshow('Tic Tac Toe AI',bg)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    exit()

# define mouse callback function
def mouseCall(event,xpos,ypos,*args):
    if cv2.EVENT_LBUTTONDOWN==event:
        if xpos>795 and xpos<925 and ypos>240 and ypos<300:
            exitGame()
        elif xpos>645 and xpos<775 and ypos>240 and ypos<300:
            with open('data.pak','wb') as f:
                pickle.dump(0,f)
                pickle.dump(0,f)
                f.close()
            game.player=0
            game.computer=0
    if cv2.EVENT_LBUTTONDOWN==event and game.playermove:
        if xpos<210 and xpos>0:
            if ypos>0 and ypos<210 and game.gamestate[0][0]==' ':
                game.gamestate[0][0]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
            elif ypos>210 and ypos<420 and game.gamestate[1][0]==' ':
                game.gamestate[1][0]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
            elif ypos>420 and ypos<630 and game.gamestate[2][0]==' ':
                game.gamestate[2][0]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
        elif xpos>210 and xpos<420:
            if ypos>0 and ypos<210 and game.gamestate[0][1]==' ':
                game.gamestate[0][1]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
            elif ypos>210 and ypos<420 and game.gamestate[1][1]==' ':
                game.gamestate[1][1]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
            elif ypos>420 and ypos<630 and game.gamestate[2][1]==' ':
                game.gamestate[2][1]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
        elif xpos>420 and xpos<630:
            if ypos>0 and ypos<210 and game.gamestate[0][2]==' ':
                game.gamestate[0][2]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
            elif ypos>210 and ypos<420 and game.gamestate[1][2]==' ':
                game.gamestate[1][2]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
            elif ypos>420 and ypos<630 and game.gamestate[2][2]==' ':
                game.gamestate[2][2]=game.playerSelection
                game.shader()
                game.displayMove()
                if game.compSelection=='O':
                    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
                else:
                    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
                game.playermove=False
        cv2.imshow('Tic Tac Toe AI',game.mygame)
        cv2.waitKey(600)

# Create the window
cv2.namedWindow('Tic Tac Toe AI')

# set mouse callback function
cv2.setMouseCallback('Tic Tac Toe AI',mouseCall)

#! the game object
game=gameAI()

bg=cv2.blur(game.mygame,(18,18))
cv2.putText(bg,'Welcome to Tac Tac Toe',(300,310),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.imshow('Tic Tac Toe AI',bg)
cv2.waitKey(1200)
if game.playerSelection=='X':
    cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
else:
    cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
game.shader()
game.playermove=random.choice([True,False])

# start program loop
while True:
    
    cv2.imshow('Tic Tac Toe AI',game.mygame)
    game.shader()
    if game.playermove:
        if game.compSelection=='X':
            cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
        else:
            cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
    else:
        if game.compfirstmove:
            temp=random.choice([0,1])
            if temp:
                game.gamestate[random.choice([0,2])][random.choice([0,2])]=game.compSelection
            else:
                game.gamestate[1][1]=game.compSelection
            game.displayMove()
            game.compfirstmove=False
            game.playermove=True
            continue

        if game.isGameOver(game.gamestate):
            game.displayMove()
            if game.compSelection=='X':
                cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
            else:
                cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
            cv2.imshow('Tic Tac Toe AI',game.mygame)
            cv2.waitKey(600)
            game.drawLine()
            game.resetgame()
            if game.playermove==False:
                game.compfirstmove=True
            continue

        if game.playerSelection=='X':
            cv2.rectangle(game.mygame,(670,400),(800,530),game.moveHLcolor,9)
        else:
            cv2.rectangle(game.mygame,(820,400),(950,530),game.moveHLcolor,9)
        bestmove=(-1,-1)
        bestscore=-999
        for i in range(3):
            for j in range(3):
                if game.gamestate[i][j]==' ':
                    game.gamestate[i][j]=game.compSelection
                    score=game.minimax(game.gamestate,9,False)
                    game.gamestate[i][j]=' '
                    if score>bestscore:
                        bestscore=score
                        bestmove=(i,j)
        game.gamestate[bestmove[0]][bestmove[1]]=game.compSelection
        game.playermove=True
        
    game.displayMove()
    cv2.imshow('Tic Tac Toe AI',game.mygame)
    if game.isGameOver(game.gamestate):
        cv2.waitKey(600)
        game.drawLine()
        game.resetgame()
        if game.playermove==False:
            game.compfirstmove=True

    if cv2.waitKey(1) & 0xff==ord('q'):
        exitGame()