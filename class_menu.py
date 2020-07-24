import pygame
import ctypes

pygame.init()

num = 1  # ???????
main_menu = True  # ????
cnopk_on = False  # ????????

user32 = ctypes.windll.user32
USER_SCREEN_W, USER_SCREEN_H = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

BUTTON_W = USER_SCREEN_W * 0.75
BUTTON_H = 100


class Button(pygame.sprite.Sprite):
	def __init__(self, text, x, y, width = BUTTON_W, height = BUTTON_H ):
		super().__init__()
		self.text = text
		self.width = width
		self.height = height
		self.image = pygame.Surface((self.width, self.height))
		self.rect = self.image.get_rect(x = x, y = y)
		self.active = False
		self.activeColor = (0, 255, 0)
		self.baseColor = (0, 0, 255)


	def update(self, *args):
		if self.active:
			self.image.fill(self.activeColor)
		else:
			self.image.fill(self.baseColor)




class Menu():
	def __init__(self, win):
		self.win = win #Экран для отрисовки

		self.activeButton = 0  # Бывшая переменная num, какая кнопка сейчас активна
		self.buttons= [		Button("button1", 50, 50),
							Button("button2", 50, 50+BUTTON_H +100),
						]


	def update(self):
		self.win.fill((56,67,128))


		for b in self.buttons:
			b.update()
			self.win.blit(b.image, b.rect)
		pygame.display.update()

	def up(self):
		if self.activeButton != 0:
			self.buttons[self.activeButton].active = False
			self.activeButton-=1
			self.buttons[self.activeButton].active = True

	def down(self):
		if self.activeButton +1 !=len(self.buttons):
			self.buttons[self.activeButton].active = False
			self.activeButton+=1
			self.buttons[self.activeButton].active = True


	# def main_menu(self):
	# 	"""
	# 	ЧТО ДЕЛАЕТ ФУНКЦИЯ
	#
	# 	:return:
	# 	"""
	#
	# 	pygame.draw.rect(self.win, (0, 255, 0), (
	# 			(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))

	# 	event = pygame.event.get()
	# 	keys = pygame.key.get_pressed()
	#
	# 	if keys[pygame.K_UP]:
	# 		num -= 1
	# 	if keys[pygame.K_DOWN]:
	# 		num += 1
	#
	# 	if num == 4:
	# 		num = 3
	# 	elif num == 0:
	# 		num = 1
	#
	# 	if num == 1:
	# 		pygame.draw.rect(self.win, (0, 255, 0), (
	# 			(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# 		pygame.draw.rect(self.win, (0, 0, 255),
	# 						 ((USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
	# 		pygame.draw.rect(self.win, (0, 0, 255), (
	# 			(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# 	elif num == 2:
	# 		pygame.draw.rect(self.win, (0, 0, 255), (
	# 			(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# 		pygame.draw.rect(self.win, (0, 255, 0),
	# 						 ((USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
	# 		pygame.draw.rect(self.win, (0, 0, 255), (
	# 			(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# 	elif num == 3:
	# 		pygame.draw.rect(self.win, (0, 0, 255), (
	# 			(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# 	pygame.draw.rect(self.win, (0, 255, 0),
	# 					 ((USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
	# 	pygame.draw.rect(self.win, (0, 255, 0), (
	# 		(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	#
	#
	# if keys[pygame.K_RIGHT]:
	# 	if num == 1:
	# 		main_menu = False
	# 	elif num == 2:
	# 		pygame.draw.rect(self.win, (0, 0, 0), (
	# 			(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# pygame.draw.rect(self.win, (0, 0, 0),
	# 				 ((USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
	# pygame.draw.rect(self.win, (0, 0, 0), (
	# 	(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# menu_op(self.win)
	#
	#
	# def menu_op(win):
	# 	menu_op1 = True
	# 	numOp = 1
	# 	self.win = win
	# 	while menu_op1:
	# 		event = pygame.event.get()
	# 		keys = pygame.key.get_pressed()
	# 		if keys[pygame.K_UP]:
	# 			numOp -= 1
	# 		if keys[pygame.K_DOWN]:
	# 			numOp += 1
	#
	# 		if numOp == 3:
	# 			numOp = 2
	# 		elif numOp == 0:
	# 			numOp = 1
	#
	# 		if numOp == 1:
	# 			pygame.draw.rect(self.win, (0, 255, 0), (
	# 				(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# 			pygame.draw.rect(self.win, (0, 0, 255),
	# 							 ((USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
	# 		elif numOp == 2:
	# 			pygame.draw.rect(self.win, (0, 0, 255), (
	# 				(USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2 - menuButton1x), menuButton1x, menuButton1y))
	# 			pygame.draw.rect(self.win, (0, 255, 0),
	# 							 ((USER_SCREEN_W / 2 - menuButton1y), (USER_SCREEN_H / 2), menuButton1x, menuButton1y))
	#
	# 		pygame.time.delay(60)
	# 		pygame.display.update()
