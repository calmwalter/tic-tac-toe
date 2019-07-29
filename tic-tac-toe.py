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
from tree import *
import random
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
        '''
        if someone win return 1,else if its equal return 2, else return 0
        '''
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
            # iswin = self.judge_win(x, y)
            # if iswin == 1:
            #     self.step = 0
            #     self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            # if iswin == 2:
            #     self.step = 0
            #     self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def restart(self):
        self.step = 0
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


class tic_tac_toe:
    def __init__(self,alpha,discount_factor):
        self.step = 0
        self.states_tree = Tree(None)
        self.alpha = alpha
        self.discount_factor = discount_factor

    def strategy_pi(self, current_node):
        '''
        random choose or choose the most significant
        '''
        if random.randint(1, 10) < 8:
            # get the smost significant strategy
            maxaction = 0
            for action in current_node.actions:
                if current_node[action] > current_node[maxaction]:
                    maxaction = action
            return maxaction
        else:
            # get the random choosed strategy
            return random.choice(current_node.actions)

    def Q_function(self, q, maxq, alpha, discount_factor, reward):
        return q+(1-alpha)(reward+discount_factor*maxq-q)

    def run(self):
        game = GAME()
        head_node = Node(None, None)
        tree = Tree(head_node)
        episode = 0
        while episode < 500:

            pos = self.strategy_pi(tree.head_node)
            y = pos // 3
            x = pos % 3
            game.put_chess(x, y)
            node = Node(tree.head_node, pos)
            tree.insert(tree.head_node, node)
            current_node = node
            # if the game not end
            iswin = game.judge_win(x, y) 
            while iswin == 0:
                # continue to go next step
                pos = self.strategy_pi(tree.head_node)
                y = pos//3
                x = pos % 3
                game.put_chess(x, y)
                node = Node(current_node, pos)
                tree.insert(current_node, node)
                current_node = node
                iswin = game.judge_win(x, y)

            # if the game end:
            # use Q function update every node use trace back
            # if win, reward 100
            # if lose, reward -100
            # if equal, reward 10
            end_node = len(current_node.states)%2
            temp = current_node.states[len(current_node.states)-1]
            current_node = current_node.parent_node
            while current_node != tree.head_node:
                q = current_node.actions[temp]
                maxq = tree.find_max_actions(current_node)
                if iswin == 1:
                    if len(current_node.states)%2 == end_node:
                        current_node.actions[temp]=self.Q_function(q,maxq,self.alpha,self.discount_factor,100)
                    else:
                        current_node.actions[temp]=self.Q_function(q,maxq,self.alpha,self.discount_factor,-100)
                elif iswin == 2:
                    current_node.actions[temp]=self.Q_function(q,maxq,self.alpha,self.discount_factor,10)
                temp = current_node.states[len(current_node.states)-1]
                current_node = current_node.parent_node
                        
            # restart the game
            game.restart()


if __name__ == "__main__":
    newGame = GAME()
    newGame.run()
