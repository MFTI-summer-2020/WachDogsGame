#################################
#ЕСЛИ ХОТИТЕ ЧТО-ТО ИЗМЕНИТЬ ПРЕДУПРЕДИТЕ МЕНЯ!!!!
#################################
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Mario")
padOn = False
x = 50
y = 425
width = 40
height = 60
speed = 5

isJump = False
jumpCount = 10
pygame.joystick.init()

my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
	joysticks.append(pygame.joystick.Joystick(i))
	joysticks[-1].init()

run = True
while  run:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_p] and padOn == False:
		padOn = True
		print("True")

	if keys[pygame.K_o] and padOn == True:
		padOn = False
		print("False")
	if padOn == True:

		if my_joystick.get_hat(0) == (-1, -1):
			x -= speed
			y += speed
		if my_joystick.get_hat(0) == (1, 1):
			x += speed
			y -= speed
		if my_joystick.get_hat(0) == (-1, 1):
			x -= speed
			y -= speed
		if my_joystick.get_hat(0) == (1, -1):
			x += speed
			y += speed
		if my_joystick.get_hat(0) == (-1, 0):
			x -= speed
		if my_joystick.get_hat(0) == (1, 0):
			x += speed
		if  my_joystick.get_hat(0) == (0, 1):
			y -= speed
		if my_joystick.get_hat(0) == (0, -1):
			y += speed





	if keys[pygame.K_LEFT] and x > 5:
		x -= speed

	if keys[pygame.K_RIGHT] and x < 500	 - width - 5:
		x += speed
	if not(isJump):
		if keys[pygame.K_UP] and y > 5:
			y -= speed
		if keys[pygame.K_DOWN] and y < 500 - height - 15:
			y += speed
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= - 10:
			y -= (jumpCount ** 2) / 2
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10



	win.fill((0,0,0))
	pygame.draw.rect(win, (0, 0, 255), (x, int(y), width, height))
	pygame.display.update()	


pygame.quit()			
