import numpy as np
import pygame
import sys
import math


COLOR = (23, 32, 53)
COLOR1 = (213, 21, 52)
COLOR2 = (32, 54, 67)

BLACK = (0, 0, 0)


ROW = 6
COL = 7

def create_board():
    board = np.zeros((ROW, COL))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    for c in range(COL-3):
        for r in range(ROW):
            # HORIZONTAL
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3]:
                return True

            # VERTICAL
    for c in range(COL):
            for r in range(ROW-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True


            # POSITIVE DIAGONAL
    for c in range(COL-3):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

            # NEGATIVE DIAGONAL
    for c in range(COL-3):
        for r in range(3, ROW):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    for c in range(COL):
        for r in range(ROW):
            pygame.draw.rect(screen, COLOR, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COL):
        for r in range(ROW):
            if board[r][c] == 1: 
                pygame.draw.circle(screen, COLOR1, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, COLOR2, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100 
game_font = pygame.font.SysFont('Monospace', 75)

width = COL * SQUARESIZE
height = (ROW+1) * SQUARESIZE

size = (width, height)
RADIUS = (SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size) 
draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, COLOR1, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, COLOR2, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        win_font = game_font.render('Player1 wins!!', 1 ,COLOR1)
                        screen.blit(win_font, (40, 10))
                        game_over = True
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        win_font = game_font.render('Player2 wins!!', 1, COLOR2)
                        screen.blit(win_font, (40,10))
                        game_over = True
            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(2000)