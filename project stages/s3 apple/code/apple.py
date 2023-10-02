from settings import * 
from random import choice

class Apple:
	def __init__(self, snake):
		self.pos = pygame.Vector2(5,8)
		self.display_surface = pygame.display.get_surface()
		self.snake = snake
		self.set_pos()

	def set_pos(self):
		available_pos = [pygame.Vector2(x,y) for x in range(COLS) for y in range(ROWS) 
						 if pygame.Vector2(x,y) not in self.snake.body]
		self.pos = choice(available_pos)

	def draw(self):
		rect = pygame.Rect(self.pos.x * CELL_SIZE,self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
		pygame.draw.rect(self.display_surface, 'blue', rect)