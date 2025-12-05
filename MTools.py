import pygame
import time
from termcolor import colored
import random



class Color(object):
    """
    Shortcuts for basic RGB (r,g,b) values.
    """
    def __init__(self):
        self.red = (255,0,0)
        self.orange = (255,128,0)
        self.yellow = (255,255,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.purple = (153,0,153)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.grey = (64,64,64)
        self.dark_grey = (32,32,32)

class Input_Box(object):
    """
    Creates a simple input box that can be placed anywhere on the screen\n
    :param screen: The surface to be displayed on.
    :param color: A tuple, (active_color, inactive_color)
    :param rect: The dimensions of the input box, (x,y,w,h)
    :param padding: A tuple, the x and y padding, (x_padding, y_padding)
    :param font: The font components, (font, text_size)
    :param minimum_width: The minimum length horizontally of the input box
    """
    def __init__(self, screen, color=(), rect=(), padding=(5,5), font=(None, 32), minimum_width=200):
        self.surface = screen
        self.font = pygame.font.Font(font[0], font[1])
        self.active_color = color[0]
        self.inactive_color = color[1]
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]
        self.x_pad = padding[0]
        self.y_pad = padding[1]
        self.min_w = minimum_width
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.active = False
        self.text = ""
    def __str__(self):
        return(self.text)
    def draw(self):
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(self.surface, self.active_color if self.active else self.inactive_color, self.rect)
        pygame.draw.rect(self.surface, self.inactive_color if self.active else self.active_color, self.rect, 3)
        txt_surface = self.font.render(self.text, True, self.inactive_color)
        self.surface.blit(txt_surface, (self.x+self.x_pad,self.y+self.y_pad))
        self.w = max(self.min_w,txt_surface.get_width()+10)
    def check_box(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    returnable = self.text
                    self.text = ""
                    return(returnable)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        
        
print(f"\n{colored("Thank you for using MTools.", "light_cyan")}",
      f"\n\\\\",
      f"\n \\\\",
      f"\n  \\\\====== {colored("1", "blue")}{colored(".0.0", "light_cyan")}",
      f"\n   \\\\",
      f"\n    \\\\==== {colored("made by Maguire\n\n","magenta")}")
