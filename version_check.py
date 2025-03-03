import pygame
from OpenGL.GL import *

# Initialize Pygame
pygame.init()

# Set up an OpenGL display mode
display = (800, 600)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

# Get OpenGL version
opengl_version = glGetString(GL_VERSION)
print(f"OpenGL Version: {opengl_version}")

# Get OpenGL vendor and renderer
vendor = glGetString(GL_VENDOR)
renderer = glGetString(GL_RENDERER)
print(f"Vendor: {vendor}")
print(f"Renderer: {renderer}")

# Clean up
pygame.quit()