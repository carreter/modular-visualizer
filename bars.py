from typing import List
import pygame
import numpy as np

class VisualizerBars():
    '''
    Set of visualizer bars which can be set to an array of heights.
    '''
    def __init__(self, screen: pygame.Surface, x: float, y: float, width: float, height: float, n_bars: int = 10, 
        color: pygame.Color = pygame.Color(255,255,255)) -> None:

        self.screen = screen
        self.n_bars = n_bars
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

        self._create_bars()

    def _create_bars(self) -> None:
        '''
        Create the bar rect objects and place them in their respective positions
        '''
        bar_width = self.width / self.n_bars
        self.bars = []
        for i in range(self.n_bars):
            self.bars.append(pygame.Rect(self.x + i * bar_width, self.y, bar_width, 0))

    def draw(self, heights: List[float]) -> pygame.Rect:
        '''
        Draw the visualizer rectangles at the given heights
        '''
        for i in range(self.n_bars):
            self.bars[i].height = heights[i]
            pygame.draw.rect(self.screen, self.color, self.bars[i])

        return self.rect
            

