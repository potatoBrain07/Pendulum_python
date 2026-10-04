
#main.py

import sys
import pygame
import math
from physics import *

def create_pendulum(x, y, x_bob, y_bob, length, radius):
    pygame.draw.line(screen, (230,230,230), (x-200,y), (x+200,y), width=2)
    pygame.draw.line(screen, (140,140,140), (x,y), (x_bob, y_bob), width=2)
    pygame.draw.circle(screen, (255,223,0), (x_bob, y_bob), radius)

def render_text(info, x, y):
    for i in range(len(info)):
        screen.blit(FONT_1.render(f"{info[i][0]}={round(info[i][1],4)}", True, (230,230,230)), (x, y + i * 30))

pygame.init()
screen = pygame.display.set_mode((1600, 600))
running = True

clock = pygame.time.Clock()
t=0
dt=0.01

#constants
FONT_1 = pygame.font.SysFont("monospace",20)
LENGTH = 400
g = 10
BOB_RADIUS = 20
ANGULAR_FREQ = math.sqrt(g/LENGTH)
A = math.pi/3

theta_real = A
omega_real =0.0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((11,11,11))

    #calculations
    theta, omega, alpha = small_angle_pendulum(A, t, ANGULAR_FREQ)
    x_bob = 400 + LENGTH * math.sin(theta)
    y_bob = 75 + LENGTH * math.cos(theta)

    theta_real, omega_real, alpha_real = rk4_step(theta_real, omega_real, ANGULAR_FREQ, dt)
    x_bob_real = 1200 + LENGTH * math.sin(theta_real)
    y_bob_real = 75 + LENGTH * math.cos(theta_real)

    t+=dt

    #rendering the objects
    create_pendulum(400, 75, x_bob, y_bob, LENGTH, BOB_RADIUS)
    create_pendulum(1200, 75, x_bob_real, y_bob_real, LENGTH, BOB_RADIUS)

    #rendering text
    render_text([["\u0398", theta], ["\u03c9", omega], ["\u03b1", alpha], ["t", t]], 650,75)
    render_text([["\u0398", theta_real], ["\u03c9", omega_real], ["\u03b1", alpha_real], ["t", t]], 1450,75)
    pygame.display.update()

