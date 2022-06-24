import numpy as np
from os import path
import pickle
import random
import cv2

# Main game class
class gameAI:
    def __init__(self):
        # define parameters
        self.windowwidth=1000
        self.windowheight=630
        self.mygame=np.zeros([self.windowheight,self.windowwidth,3],dtype=np.uint8)
        self.bgcolour=(70,16,33)
        self.Ocolour=(231,75,229)
        self.Oradius=50
        self.Xcolour=(219,206,60)
        self.gridcolour=(31,217,180)
        self.thickness=7
        self.player=0
        self.computer=0
        if path.exists('data.pak'):
            with open('data.pak','rb') as f:
                self.player=pickle.load(f)
                self.computer=pickle.load(f)
                f.close()
        self.wincolor=(67,130,240)
        self.moveHLcolor=(53,188,50)
        self.gamestate=[
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
        self.playermove=None
        self.compSelection=None
        self.compfirstmove=False
        self.playerSelection=random.choice(['X','O'])
        if self.playerSelection=='X':
            self.compSelection='O'
        else:
            self.compSelection='X'

    def shader(self):
        self.mygame=np.zeros([self.windowheight,self.windowwidth,3],dtype=np.uint8)
        self.mygame[:,:]=self.bgcolour
        cv2.line(self.mygame,(210,30),(210,600),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(420,30),(420,600),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(30,210),(600,210),self.gridcolour,self.thickness)
        cv2.line(self.mygame,(30,420),(600,420),self.gridcolour,self.thickness)
        cv2.rectangle(self.mygame,(670,400),(800,530),(23,13,4),2)
        cv2.rectangle(self.mygame,(820,400),(950,530),(23,13,4),2)
        cv2.circle(self.mygame,(735,465),45,self.Ocolour,self.thickness) # O
        cv2.line(self.mygame,(850,430),(920,500),self.Xcolour,self.thickness) # X
        cv2.line(self.mygame,(920,430),(850,500),self.Xcolour,self.thickness) # X
        cv2.putText(self.mygame,f'Player {self.playerSelection}',(610,100),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),2)
        cv2.putText(self.mygame,f'Computer {self.compSelection}',(780,100),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,255),2)
        cv2.line(self.mygame,(770,80),(770,180),(255,255,255),4)
        cv2.line(self.mygame,(610,120),(980,120),(255,255,255),4)
        cv2.putText(self.mygame,str(self.player),(770-70,160),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.putText(self.mygame,str(self.computer),(770+70,160),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.rectangle(self.mygame,(645,240),(775,300),(15,166,166),-1)
        cv2.rectangle(self.mygame,(795,240),(925,300),(12,12,148),-1)
        cv2.putText(self.mygame,'Reset',(665,281),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        cv2.putText(self.mygame,'Quit',(822,281),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    def isGameOver(self,localstate):
        if self.isWinner(localstate):
            return True
        for i in range(3):
            for j in range(3):
                if localstate[i][j]==' ':
                    return False
        return True

    def drawLine(self):
        # horizontal
        if self.gamestate[0][0]==self.gamestate[0][1] and self.gamestate[0][1]==self.gamestate[0][2] and self.gamestate[0][0]!=' ':
            if self.playerSelection==self.gamestate[0][0]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105-50,105),(_,105), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[1][0]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[1][2] and self.gamestate[1][1]!=' ':
            if self.playerSelection==self.gamestate[1][1]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105-50,315),(_,315), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[2][0]==self.gamestate[2][1] and self.gamestate[2][1]==self.gamestate[2][2] and self.gamestate[2][2]!=' ':
            if self.playerSelection==self.gamestate[2][2]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105-50,525),(_,525), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True

        # vertical
        if self.gamestate[0][0]==self.gamestate[1][0] and self.gamestate[1][0]==self.gamestate[2][0] and self.gamestate[0][0]!=' ':
            if self.playerSelection==self.gamestate[0][0]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(105,105-50),(105,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[0][1]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[2][1] and self.gamestate[1][1]!=' ':
            if self.playerSelection==self.gamestate[1][1]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(315,105-50),(315,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[0][2]==self.gamestate[1][2] and self.gamestate[1][2]==self.gamestate[2][2] and self.gamestate[2][2]!=' ':
            if self.playerSelection==self.gamestate[2][2]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(525,105-50),(525,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
                
        # diagonals
        if self.gamestate[0][0]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[1][1]==self.gamestate[2][2] and self.gamestate[0][0]!=' ':
            if self.playerSelection==self.gamestate[0][0]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(_,_),(_,_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True
        if self.gamestate[2][0]==self.gamestate[1][1] and self.gamestate[1][1]==self.gamestate[0][2] and self.gamestate[1][1]!=' ':
            if self.playerSelection==self.gamestate[1][1]:
                self.player+=1
                self.playermove=True
            else:
                self.computer+=1
                self.playermove=False
            for _ in range(105-50,525+50,2):
                cv2.line(self.mygame,(_,525+105-_),(_,525+105-_), self.wincolor,16)
                cv2.imshow('Tic Tac Toe AI',self.mygame)
                cv2.waitKey(1)
            cv2.waitKey(400)
            return True

    # is somebody winner
    def isWinner(self,localstate):
        # horizontal
        if localstate[0][0]==localstate[0][1] and localstate[0][1]==localstate[0][2] and localstate[0][0]!=' ':
            return True
        if localstate[1][0]==localstate[1][1] and localstate[1][1]==localstate[1][2] and localstate[1][1]!=' ':
            return True
        if localstate[2][0]==localstate[2][1] and localstate[2][1]==localstate[2][2] and localstate[2][2]!=' ':
            return True

        # vertical
        if localstate[0][0]==localstate[1][0] and localstate[1][0]==localstate[2][0] and localstate[0][0]!=' ':
            return True
        if localstate[0][1]==localstate[1][1] and localstate[1][1]==localstate[2][1] and localstate[1][1]!=' ':
            return True
        if localstate[0][2]==localstate[1][2] and localstate[1][2]==localstate[2][2] and localstate[2][2]!=' ':
            return True
                
        # diagonals
        if localstate[0][0]==localstate[1][1] and localstate[1][1]==localstate[2][2] and localstate[0][0]!=' ':
            return True
        if localstate[2][0]==localstate[1][1] and localstate[1][1]==localstate[0][2] and localstate[1][1]!=' ':
            return True

    # the display move function
    def displayMove(self):
        for i in range(3):
            for j in range(3):
                if self.gamestate[i][j]=='O':
                    cv2.circle(self.mygame,(105+210*j,105+210*i),self.Oradius,self.Ocolour,self.thickness)
                elif self.gamestate[i][j]=='X':
                    cv2.line(self.mygame,(50+210*j,50+210*i),(160+210*j,160+210*i),self.Xcolour,self.thickness)
                    cv2.line(self.mygame,(160+210*j,50+210*i),(50+210*j,160+210*i),self.Xcolour,self.thickness)

    # reset the game
    def resetgame(self):
        self.shader()
        for i in range(3):
            for j in range(3):
                self.gamestate[i][j]=' '
        self.displayMove()
        cv2.imshow('Tic Tac Toe AI',self.mygame)
        cv2.waitKey(500)

    # determine best possible move    
    def minimax(self,localstate,depth,isMaximising):
        maxi=-999
        mini=999
        if depth==0 or self.isGameOver(localstate):
            return self.evaluate(localstate)
        
        if isMaximising:
            for i in range(3):
                for j in range(3):
                    if localstate[i][j]==' ':
                        localstate[i][j]=self.compSelection
                        eval=self.minimax(localstate,depth-1, False)
                        localstate[i][j]=' '
                        maxi=max(maxi,eval)
            return maxi

        else:
            for i in range(3):
                for j in range(3):
                    if localstate[i][j]==' ':
                        localstate[i][j]=self.playerSelection
                        eval=self.minimax(localstate,depth-1,True)
                        localstate[i][j]=' '
                        mini=min(mini,eval)
            return mini
        
    # evaluate the score of final position
    def evaluate(self,localstate):
        compscore=0
        # horizontal
        if localstate[0][0]==localstate[0][1] and localstate[0][1]==localstate[0][2]:
            if localstate[0][0]==self.playerSelection:
                compscore-=1
            elif localstate[0][0]==self.compSelection:
                compscore+=1
        if localstate[1][0]==localstate[1][1] and localstate[1][1]==localstate[1][2]:
            if localstate[1][0]==self.playerSelection:
                compscore-=1
            elif localstate[1][0]==self.compSelection:
                compscore+=1
        if localstate[2][0]==localstate[2][1] and localstate[2][1]==localstate[2][2]:
            if localstate[2][0]==self.playerSelection:
                compscore-=1
            elif localstate[2][0]==self.compSelection:
                compscore+=1

        # vertical
        if localstate[0][0]==localstate[1][0] and localstate[1][0]==localstate[2][0]:
            if localstate[0][0]==self.playerSelection:
                compscore-=1
            elif localstate[0][0]==self.compSelection:
                compscore+=1
        if localstate[0][1]==localstate[1][1] and localstate[1][1]==localstate[2][1]:
            if localstate[0][1]==self.playerSelection:
                compscore-=1
            elif localstate[0][1]==self.compSelection:
                compscore+=1
        if localstate[0][2]==localstate[1][2] and localstate[1][2]==localstate[2][2]:
            if localstate[0][2]==self.playerSelection:
                compscore-=1
            elif localstate[0][2]==self.compSelection:
                compscore+=1

        # diagonals
        if localstate[0][0]==localstate[1][1] and localstate[1][1]==localstate[2][2]:
            if localstate[0][0]==self.playerSelection:
                compscore-=2
            elif localstate[0][0]==self.compSelection:
                compscore+=2
        if localstate[2][0]==localstate[1][1] and localstate[1][1]==localstate[0][2]:
            if localstate[2][0]==self.playerSelection:
                compscore-=2
            elif localstate[2][0]==self.compSelection:
                compscore+=2
        return compscore
    
if __name__=='__main__':
    print('All set, the AI will beat you')