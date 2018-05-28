import cocos.layer
import cocos.scene
import cocos.text
import cocos.sprite
import cocos.euclid as eu
import numpy as np

import mainmenu


class GameLayer(cocos.layer.Layer):
    is_event_handler = True
    PERSON = 1
    COMPUTER = -1

    def __init__(self, difficulty, hud_layer):
        super(GameLayer, self).__init__()
        self.difficulty = difficulty
        self.levelDepth = self.difficulty*2+2
        self.hud = hud_layer
        self.square = 75
        self.row = 8
        self.column = 8
        self.height = 8*self.square
        self.width = 8*self.square
        self.table = np.arange(self.row*self.column).reshape(self.row, self.column)

        for x in range(0, self.column+1):
            line = cocos.draw.Line((x*self.square, 0), (x*self.square, self.height), (255, 0, 255, 255))
            self.add(line)
        
        for y in range(0, self.row+1):
            line = cocos.draw.Line((0, y*self.square), (self.width, y*self.square), (255, 0, 255, 255))
            self.add(line)
        
        # disk sprite
        self.disk = [[None for i in range(self.column)] for j in range(self.row)]

        for y in range(0, self.row):
            for x in range(0, self.column):
                centerPt = eu.Vector2(x*self.square + self.square/2, y*self.square + self.square/2)
                self.disk[y][x] = cocos.sprite.Sprite('assets/ball.png', position = centerPt, color = (255, 255, 255))
                self.add(self.disk[y][x])
        
        self.setup()
        self.turn = GameLayer.PERSON
        self.schedule(self.update)
    
    def setup(self):
        for y in range(0, self.row):
            for x in range(0, self.column):
                self.table[y][x] = 0
        
        self.table[3][3] = GameLayer.PERSON
        self.table[3][4] = GameLayer.COMPUTER
        self.table[4][3] = GameLayer.COMPUTER
        self.table[4][4] = GameLayer.PERSON
    
    def update(self, dt):
        computer = 0
        person = 0

        for y in range(0, self.row):
            for x in range(0, self.column):
                if self.table[y][x] == GameLayer.COMPUTER:
                    self.disk[y][x].color = (255, 255, 255)
                    self.disk[y][x].visible = True
                    computer += 1
                elif self.table[y][x] == GameLayer.PERSON:
                    self.disk[y][x].color = (0, 0, 0)
                    self.disk[y][x].visible = True
                    person += 1
                else:
                    self.disk[y][x].visible = False
        # decision on outcome
    
    # check position
    def isPossible(self, x, y, turn, board):
        rtnList = list()
        if board[y][x] != 0:
            return rtnList # table

        for dirX in range(-1, 2):
            for dirY in range(-1, 2):
                if dirX == 0 and dirY == 0:
                    continue
                if x+dirX < 0 or x+dirX >= self.column:
                    continue
                if y+dirY < 0 or y+dirY >= self.row:
                    continue

                xList = list()
                yList = list()
                if dirX == 0:
                    for yy in range(y + dirY*2, self.row*dirY, dirY):
                        if yy < 0 or yy >= self.row:
                            break
                        xList.append(x)
                        yList.append(yy)

                bDetected = False
                revList = []
                if board[y+dirY][x+dirX] == turn*-1: # 상대방 돌이면
                    revList.append((x+dirX, y+dirY))
                    for xx, yy in zip(xList, yList):
                        if board[xx][yy] == 0:
                            break
                        elif board[xx][yy] == turn:
                            bDetected == True
                            break
                        elif board[xx][yy] == turn*-1:
                            revList.append((xx, yy))
                    if(bDetected == False):
                        revList = []

                rtnList += revList
        return rtnList

    # computer turn
    def computer(self):
        pass
    
    # minimax
    def minimax(self, player):
        pass
    
    def maxMove(self, board, depth, alpha, beta):
        pass
        
    def minMove(self, board, depth, alpha, beta):
        pass
    
    def boardScore(self, board):
        pass
    
    # move list
    def getMoves(self, turn, board):
        pass


class HUD(cocos.layer.Layer):
    def __init__(self):
        super(HUD, self).__init__()
        w, h = cocos.director.director.get_window_size()


def new_game():
    pass


def game_over():
    pass
