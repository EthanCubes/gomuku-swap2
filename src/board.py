import pygame
import global_data as gD
import random

def place_stone(x_pos, y_pos, player):
    gD.boardPositions[y_pos][x_pos] = player
    gD.currentPlayer *= -1

def user_place_stone():
    if pygame.mouse.get_pressed(3)[0]:
        mouse_pos = pygame.mouse.get_pos()
        grid_x = round(mouse_pos[0]/45) - 1
        grid_y = round(mouse_pos[1]/45) - 1
        if grid_x > 14:
            grid_x = 14
        if grid_y > 14:
            grid_y = 14
        if gD.boardPositions[grid_y][grid_x] == 0:
            place_stone(grid_x, grid_y, gD.currentPlayer)

def render():
    gD.screen.fill("peru")
    if gD.currentPlayer == -1:
        pygame.draw.circle(gD.screen, (0, 0, 0), (697, 23), 5)
    else:
        pygame.draw.circle(gD.screen, (255, 255, 255), (697, 23), 5)
    
    pygame.draw.circle(gD.screen, (0, 0, 0), (360, 360), 10)

    for i in range(15):
        pygame.draw.line(gD.screen, (0, 0, 0), (45, 45 + i * 45), (675, 45 + i * 45), round(45 / 12))
    for i in range(15):
        pygame.draw.line(gD.screen, (0, 0, 0), (45 + i * 45, 45), (45 + i * 45, 675), round(45 / 12))

    for y in range(15):
        y_pos = 45 + 45*y
        for x in range(15):
            x_pos = 45 + 45*x
            if gD.boardPositions[y][x] == 1:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            if gD.boardPositions[y][x] != 0:
                pygame.draw.circle(gD.screen, color, (x_pos, y_pos), 20)

def generate_start_pos():
    stone1 = [None, None]
    stone1[0] = random.randint(5, 9)
    stone1[1] = random.randint(5, 9)

    stone2 = [None, None]
    position_valid = False
    while not position_valid:
        stone2[0] = random.randint(5, 9)
        stone2[1] = random.randint(5, 9)
        if stone2 != stone1:
            position_valid = True
    
    stone3 = [None, None]
    position_valid = False
    while not position_valid:
        stone3[0] = random.randint(5, 9)
        stone3[1] = random.randint(5, 9)
        if stone3 != stone1 and stone3 != stone2:
            position_valid = True

    gD.boardPositions[stone1[1]][stone1[0]] = -1
    gD.boardPositions[stone2[1]][stone2[0]] = 1
    gD.boardPositions[stone3[1]][stone3[0]] = -1