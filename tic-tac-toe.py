'''
this file is the achieve of the tic-tac-toe game using reinforcement learning

analysis:
state:the state of the game
action:the next action of the current state
reward:when a game finish, reward every state if win, else punish every state

'''
import sys
import pygame
import numpy as np
'''
the game UI

draw the game board
the action of drop game chess
the judge of the game end
restart the game
'''


class GAME:
    def __init__(self):
        # game board
        pygame.init()
        self.screen = pygame.display.set_mode((3*200, 3*200))
        pygame.display.update()
        self.step = 0
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # print(event.pos)
                    x = event.pos[0]//200
                    y = event.pos[1]//200
                    self.put_chess(x, y)
            self.screen.fill((255, 255, 255))
            for i in range(4):
                pygame.draw.line(self.screen, (0, 0, 0),
                                 [0, i*200], [3*200, i*200], 5)
                pygame.draw.line(self.screen, (0, 0, 0),
                                 [i*200, 0], [i*200, 3*200], 5)
            for i in range(3):
                for j in range(3):
                    if self.board[j][i] != 0:
                        if self.board[j][i] % 2 == 0:
                            # circle
                            pygame.draw.circle(self.screen, (255, 0, 0), [
                                               100+j*200, 100+i*200], 100, 10)
                        else:
                            # cross
                            pygame.draw.line(self.screen, (0, 0, 255),
                                             [200*j, 200*i], [200*(j+1), 200*(i+1)], 10)
                            pygame.draw.line(self.screen, (0, 0, 255),
                                             [200*j, 200*(i+1)], [200*(j+1), 200*i], 10)

            pygame.display.update()

    def judge_win(self, x, y):
        chess = self.board[x][y] % 2
        cnt = 0
        i = x
        j = y
        while i != -1:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                i -= 1
            else:
                break
        i = x+1
        while i != 3:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                i += 1
            else:
                break
        if cnt == 3:
            return 1

        cnt = 0
        i = x
        j = y
        while j != -1:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                j -= 1
            else:
                break
        j = y+1
        while j != 3:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                j += 1
            else:
                break
        if cnt == 3:
            return 1

        cnt = 0
        i = x
        j = y
        while i != -1 and j != -1:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                i -= 1
                j -= 1
            else:
                break
        i = x+1
        j = y+1
        while i != 3 and j != 3:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                i += 1
                j += 1
            else:
                break
        if cnt == 3:
            return 1

        cnt = 0
        i = x
        j = y
        while i != 3 and j != -1:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                i += 1
                j -= 1
            else:
                break
        i = x-1
        j = y+1
        while i != -1 and j != 3:
            if self.board[i][j] != 0 and self.board[i][j] % 2 == chess:
                cnt += 1
                i -= 1
                j += 1
            else:
                break
        if cnt == 3:
            return 1

        for row in self.board:
            for column in row:
                if column == 0:
                    return 0
        return 2

    def put_chess(self, x, y):
        if self.board[x][y] == 0:
            self.step += 1
            self.board[x][y] = self.step
            iswin = self.judge_win(x, y)
            if iswin == 1:
                self.step = 0
                self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            if iswin == 2:
                self.step = 0
                self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


if __name__ == "__main__":
    newGame = GAME()
    newGame.run()