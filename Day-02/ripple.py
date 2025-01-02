import pygame
import numpy

cols = 200
rows = 200

current = numpy.zeros((cols, rows))
previous = numpy.zeros((cols, rows))

damping = 0.9

# for i in range(1, cols - 1):
#     for j in range(1, rows - 1):
#         current[i][j] = 100;
#         previous[i][j] = 100;

previous[100][100] = 255

pygame.init()
screen = pygame.display.set_mode((cols, rows))
pygame.display.set_caption("Ripples")


def main():

    global current
    global previous

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pixel_array = pygame.PixelArray(screen)
        for i in range(1, cols - 1):
            for j in range(1, rows - 1):
                current[i][j] = (previous[i-1][j] + previous[i+1][j] + \
                                 previous[i][j-1] + previous[i][j+1] ) / 2 - current[i][j]
                current[i][j] *= damping
                
                pix = max(0, min(current[i][j]*255, 255))
                # print(int(pix*255))
                pixel_array[i, j] = (int(pix), int(pix), int(pix))
  
        
        pixel_array.close()
        pygame.display.flip()

        

        temp = current.copy()
        current = previous.copy()
        previous = temp.copy()
        

    pygame.quit()

if __name__ == '__main__': 
    main()