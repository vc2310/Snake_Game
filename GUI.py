## @file GUI.py
#  @Author Vaibhav Chadha | Andy Hameed
#  @brief A library for common functions used for displaying text and buttons
#  @details Used in modules that display text and buttons
#  @date 11/09/2018

import pygame, sys

## @brief A method to create a button
#  @details This method will make a box on the interface
#  @param surface The background (surface) the box should be made on
#  @param color The color of the button to be made
#  @param Rect The coordinate of the button with the length and width
#  @param width The width of the sides of button
def button(Surface, color,Rect,width):
  pygame.draw.rect(Surface, color,Rect,width)

## @brief A method to display text
#  @details This function will print the text on the interface
#  @param text The text to be printed
#  @param fontStyle The font Style of the text to be displayed
#  @param fontSize The size of the text written
#  @param color The color of the text
#  @param coord The coordinate at which the text should start displaying
#  @param surface The background (surface) the text should be printed on
def text(text,fontStyle,fontSize,color,coord,surface):
  font = pygame.font.SysFont(fontStyle,fontSize)
  text = font.render(text,True,color)
  surface.blit(text,coord)

## @brief A method to display downloaded text using .ttf files
#  @details This function will print the text on the interface
#  @param text The text to be printed
#  @param fontName The name of the font/ttf file 
#  @param fontSize The size of the text written
#  @param color The color of the text
#  @param coord The coordinate at which the text should start displaying
#  @param surface The background (surface) the text should be printed on
def custom_text(text,fontName,fontSize,color,coord,surface):
  font = pygame.font.Font(fontName,fontSize)
  text = font.render(text,True,color)
  surface.blit(text,coord)
