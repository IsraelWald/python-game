import math
import pygame
from pygame.locals import *

pygame.init()
screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)

# keys = W, A, S, D
keys = [False, False, False, False]
player_pos = [100, 100]


def load(filename):
	return pygame.image.load(f"resources/images/{filename}")


# Load Images
player = load("dude.png")
grass = load("grass.png")
castle = load("castle.png")

while True:
	screen.fill(0)
	# Draw castles

	for x in range(screen_size[0] // grass.get_width() + 1):
		for y in range(screen_size[1] // grass.get_height() + 1):
			screen.blit(grass, (x * 100, y * 100))
	counter = 30
	while True:
		if counter == 345 + 105:
			break
		screen.blit(castle, (0, counter))
		counter += 105
	# Rotate player to face mouse
	position = pygame.mouse.get_pos()
	angle = math.atan2(
		position[1] - (player_pos[1] + 32), position[0] - (player_pos[0] + 26)
	)
	player_angle = pygame.transform.rotate(player, 360 - angle * 57.29)
	playerpos1 = (
		player_pos[0] - player_angle.get_rect().width / 2,
		player_pos[1] - player_angle.get_rect().height / 2,
	)
	screen.blit(player_angle, playerpos1)
	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				keys[0] = True
			elif event.key == pygame.K_s:
				keys[1] = True
			elif event.key == pygame.K_d:
				keys[2] = True
			elif event.key == pygame.K_a:
				keys[3] = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				keys[0] = False
			elif event.key == pygame.K_s:
				keys[1] = False
			elif event.key == pygame.K_d:
				keys[2] = False
			elif event.key == pygame.K_a:
				keys[3] = False
	if keys[0]:
		player_pos[1] -= 5
	if keys[1]:
		player_pos[1] += 5
	if keys[2]:
		player_pos[0] += 5
	if keys[3]:
		player_pos[0] -= 5