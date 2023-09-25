import pygame
import random 

pygame.font.init()

# Global Vars
s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# Shape Formats

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
    ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 225, 0), (225, 0, 0), (0, 225, 225), (225, 225, 0), (255, 165, 0), (0, 0, 225), (128, 0, 128)]


class Piece():
      def __init__(self, x, y, shape) :
            self.x = x
            self.y = y
            self.shape = shape
            self.color = shape_colors[shapes.index(shape)]
            self.rotation = 0


def create_grid(locked_pos={}):
      grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if (j, i) in locked_pos:
                        c = locked_pos[j, i]
                        grid[i][j] = c
      return grid

def convert_shape_format(shape):
      positions = []
      formate = shape.shape[shape.rotation % len(shape.shape)]

      for i, line in enumerate(formate):
            row = list(line)
            for j, column in enumerate(row):
                  if column == '0':
                        positions.append((shape.x + j, shape.y + i))
            
      for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

      return positions


def valid_space(shape, grid):
      accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
      accepted_pos = [j for sub in accepted_pos for j in sub]

      formatted = convert_shape_format(shape)
      
      for pos in formatted:
            if pos not in accepted_pos:
                  if pos[1] > -1:
                        return False
      return True


def check_lost(positions):
      for pos in positions:
            _, y = pos
            if y < 1:
                  return True
      return False


def get_shape():
      return Piece(5, 0, random.choice(shapes))


def draw_text_middle(surface, text, size, color):
      font = pygame.font.SysFont('comicsans', size, bold=True)
      label = font.render(text, 1, color)

      surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2.5 - (label.get_height()/2)))

def draw_text_lower_middle(surface, text, size, color):
      font = pygame.font.SysFont('comicsans', size, bold=True)
      label = font.render(text, 1, color)

      surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), top_left_y + play_height/2 - (label.get_height()/2)))

def update_score(nscore):
      score = max_score()

      with open('Tetris_score.txt', 'w') as f:
            if int(score) > nscore:
                  f.write(str(score))
            else:
                  f.write(str(nscore))


def max_score():
      with open('Tetris_score.txt', 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()

      return score

def draw_grid(surface, grid):
      sx = top_left_x
      sy = top_left_y

      for i in range(len(grid)):
            pygame.draw.line(surface, (128, 128, 128), (sx, sy + i*block_size,), (sx + play_width, sy + i*block_size))
            for j in range(len(grid[i])):
                  pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy), (sx + j*block_size, sy + play_height))


def clear_rows(grid, locked):
      inc = 0
      for i in range(len(grid)-1, -1, -1):
            row = grid[i]
            if (0, 0, 0) not in row:
                  inc += 1
                  idx = i
                  for j in range(len(row)):
                        try:
                              del locked[(j, i)]
                        except:
                              continue
      if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                  x, y = key
                  if y < idx:
                        newKey = (x, y + inc)
                        locked[newKey] = locked.pop(key)

      return inc

def draw_next_shape(surface, shape):
      font = pygame.font.SysFont('comicsans', 30)
      label = font.render('Next shape', 1, (255, 255, 255))

      sx = top_left_x + play_width + 50
      sy = top_left_y + (play_height/2 - 100)
      formate = shape.shape[shape.rotation % len(shape.shape)]

      for i, line in enumerate(formate):
            row = list(line)
            for j, column in enumerate(row):
                  if column == '0':
                        pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

      surface.blit(label, (sx, sy - 45))


def draw_window(surface, grid, score=0, last_score=0):
      surface.fill((0, 0, 0))

      pygame.font.init()
      font = pygame.font.SysFont('comicsans', 60)
      label = font.render('Tetris', 1, (225, 225, 225))
      surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))

      # Current Score
      font1 = pygame.font.SysFont('comicsans', 30)
      label1 = font1.render(f'Score: {score}', 1, (225, 225, 225))
      sx = top_left_x + play_width + 50
      sy = top_left_y + (play_height/2 - 100)
      surface.blit(label1, (sx + 10, sy + 130))

      # Last Score
      label1 = font1.render(f'HighScore: {last_score}', 1, (225, 225, 225))

      sx1 = top_left_x - 200
      sy1 = top_left_y + 200
      surface.blit(label1, (sx1, sy1))


      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

      pygame.draw.rect(surface, (225, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)

      draw_grid(surface, grid)

def main(surface):
      last_score = max_score()
      locked_position = {}
      grid = create_grid(locked_position)

      change_piece = False
      run = True
      current_piece = get_shape()
      next_piece = get_shape() 
      clock = pygame.time.Clock()
      fall_time = 0
      fall_speed = 0.2
      level_time = 0
      score = 0

      while run:
            grid = create_grid(locked_position)
            fall_time += clock.get_rawtime()
            level_time += clock.get_rawtime()
            clock.tick()

            if level_time/1000 > 5:
                  level_time = 0
                  if fall_speed > 0.3:
                        fall_speed -= 0.005

            if fall_time/1000 > fall_speed:
                  fall_time = 0
                  current_piece.y += 1
                  if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                        change_piece = True

            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        run = False
                        pygame.display.quit()

                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                              current_piece.rotation += 1
                              if not(valid_space(current_piece, grid)):
                                    current_piece.rotation -= 1
                        if event.key == pygame.K_DOWN:
                              current_piece.y += 1
                              if not(valid_space(current_piece, grid)):
                                    current_piece.y -= 1
                        if event.key == pygame.K_LEFT:
                              current_piece.x -= 1
                              if not(valid_space(current_piece, grid)):
                                    current_piece.x += 1
                        if event.key == pygame.K_RIGHT:
                              current_piece.x += 1
                              if not(valid_space(current_piece, grid)):
                                    current_piece.x -= 1

            shape_pos = convert_shape_format(current_piece)

            for i in range(len(shape_pos)):
                  x, y = shape_pos[i]
                  if y > -1:
                        grid[y][x] = current_piece.color

            if change_piece:
                  for pos in shape_pos:
                        p = (pos[0], pos[1])
                        locked_position[p] = current_piece.color
                  current_piece = next_piece
                  next_piece = get_shape()
                  change_piece = False
                  score += clear_rows(grid, locked_position) * 10                  

            draw_window(surface, grid, score, last_score)
            draw_next_shape(surface, next_piece)
            pygame.display.update()

            if check_lost(locked_position):
                  draw_text_middle(surface, 'YOU LOST!!', 80, (225, 225, 225))
                  pygame.display.update()
                  pygame.time.delay(1500)
                  run = False
                  update_score(score)

def main_menu(win):
      run = True
      while run:
            win.fill((0, 0, 0))
            draw_text_middle(win, 'Press any key to start!', 40, (225, 225, 225))
            pygame.display.update()
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        run = False
                  if event.type == pygame.KEYDOWN:
                        main(win)
      pygame.display.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')

main_menu(win)
