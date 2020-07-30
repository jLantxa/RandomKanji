#!/usr/bin/env python3

import random
import sys
import time
from timeit import default_timer as timer

import pygame

PATH = "kanji.txt"
RTK1_NUM_KANJI = 2200

def get_list(limit):
    with open(PATH, 'r', encoding='utf8') as file:
        line = file.readline()
        return line[:limit]

if __name__ == "__main__":
    limit = RTK1_NUM_KANJI
    if (len(sys.argv) == 2):
        limit = int(sys.argv[1])
    kanjilist = get_list(limit)

    width, height = 250, 250
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Kanji')
    pygame.font.init()
    myfont = pygame.font.SysFont('ipamincho', 200)

    start_time = 0
    interval = 2
    running = True
    while running:
        now = timer()
        if (now - start_time > interval):
            n = random.randint(0, limit-1)
            textsurface = myfont.render(kanjilist[n], True, (0x00, 0x00, 0x00))
            w = textsurface.get_width()
            h = textsurface.get_height()

            screen.fill((255, 255, 255))
            screen.blit(textsurface,(int((width - w)/2), int((height - h)/2)))
            pygame.display.update()
            start_time = timer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time.sleep(0.33)
