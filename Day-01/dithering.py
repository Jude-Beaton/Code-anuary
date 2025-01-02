import pygame
from PIL import Image, ImageOps
img = Image.open("data/Tiger512.jpg")
# img = ImageOps.grayscale(inp)
pixel_map = img.load()
img_data = img.tobytes()
img_dimensions = img.size
pixels = list(img.getdata())

pygame.init()
pygame_surface = pygame.image.fromstring(img_data, img_dimensions, "RGB")
screen = pygame.display.set_mode((1024, 512))

def ind(x, y, w):
    return x + y * w

def initialise():   
   
    pygame.display.set_caption("Dithering")
    screen.blit(pygame_surface, (0, 0))
    pygame.display.flip()

def processImage():
    img2 = Image.new('RGB', (512, 512), color='black')
    w = img_dimensions[0]
    for y in range (0, img_dimensions[1]-1):
        for x in range (1, img_dimensions[0]-1):

            # pixels = list(img.getdata())
            pix = pixels[ind(x, y, w)]
            oldR = pix[0]
            oldG = pix[1]
            oldB = pix[2]

            factor = 1

            newR = int(round(factor * oldR / 255) * (255/factor))
            newG = int(round(factor * oldG / 255) * (255/factor))
            newB = int(round(factor * oldB / 255) * (255/factor))

            pixel_map[x, y] = (newR, newG, newB)

            errR = oldR - newR
            errG = oldG - newG
            errB = oldB - newB

            index = ind(x+1, y, w)
            c = pixels[index]
            r = c[0]
            g = c[1]
            b = c[2]
            r = int(r + errR * 7/16.0)
            g = int(g + errG * 7/16.0)
            b = int(b + errB * 7/16.0)
            pixels[index] = (r, g, b)
            pixel_map[x+1, y] = (r, g, b)


            index = ind(x-1, y+1, w)
            c = pixels[index]
            r = c[0]
            g = c[1]
            b = c[2]
            r = int(r + errR * 3/16.0)
            g = int(g + errG * 3/16.0)
            b = int(b + errB * 3/16.0)
            pixels[index] = (r, g, b)
            pixel_map[x-1, y+1] = (r, g, b)

            index = ind(x, y+1, w)
            c = pixels[index]
            r = c[0]
            g = c[1]
            b = c[2]
            r = int(r + errR * 5/16.0)
            g = int(g + errG * 5/16.0)
            b = int(b + errB * 5/16.0)
            pixels[index] = (r, g, b)
            pixel_map[x, y+1] = (r, g, b)


            index = ind(x+1, y+1, w)
            c = pixels[index]
            r = c[0]
            g = c[1]
            b = c[2]
            r = int(r + errR * 1/16.0)
            g = int(g + errG * 1/16.0)
            b = int(b + errB * 1/16.0)
            pixels[index] = (r, g, b)
            pixel_map[x+1, y+1] = (r, g, b)

            # img2.putpixel((x, y), pix)

    image2_surface = pygame.image.fromstring(img.tobytes(), img_dimensions, "RGB")
    screen.blit(image2_surface, (512, 0))
    pygame.display.flip()
    img.save("data/out.jpg")
    
    # img2_data = img2.tobytes()
    # img2_dimensions = img2.size
    # image2_surface = pygame.image.fromstring(img2_data, img2_dimensions, "RGB")
    # screen.blit(image2_surface, (200, 0))
    # pygame.display.flip()

def main():

    initialise()

    processImage()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

    pygame.quit()

if __name__ == '__main__': 
    main()