import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 1024, 800 #1024, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font(None,20) # Default font, size 20

window.fill("white")
pygame.draw.line(window, "black", (0, HEIGHT/2), (WIDTH, HEIGHT/2))
pygame.draw.circle(window, "black", (WIDTH/2, HEIGHT/2), 5)

center_txt = "O"
center_txt = font.render(center_txt, True, "black")
center_txt_rect = center_txt.get_rect()
window.blit(center_txt, (WIDTH/2 - 5, HEIGHT/2 + 5), center_txt_rect)

def update():
    pygame.display.update()

def getDistance(p1, p2):
    dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return int(dist)

def getCenter(p1, p2):
    center = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    return center

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def writeDistance(p1, p2, pos, side1=(0,0), side2=(0,0), axis="x"):
    dist_txt = str(getDistance(p1, p2))
    dist_txt = font.render(dist_txt, True, "black")
    dist_txt_rect = dist_txt.get_rect()
    center = getCenter(p1, p2)

    if axis == "x":
        if pos[0] <= WIDTH/2:
            window.blit(dist_txt, (center[0]+side1[0], center[1]+side1[1]), dist_txt_rect)
        else:
            window.blit(dist_txt, (center[0]+side2[0], center[1]+side2[1]), dist_txt_rect)

    if axis == "y":
        if pos[1] <= HEIGHT/2:
            window.blit(dist_txt, (center[0]+side1[0], center[1]+side1[1]), dist_txt_rect)
        else:
            window.blit(dist_txt, (center[0]+side2[0], center[1]+side2[1]), dist_txt_rect)

def run():
    run = True
    clock = pygame.time.Clock()
    fps = 30
    clock.tick(fps)
    move = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click
                if pygame.mouse.get_pressed()[0]: #Left click
                    if move == False:
                        move = True
                    else:
                        move = False

            if event.type == pygame.MOUSEMOTION: # When cursor move
                if move:
                    window.fill("white")
                    pygame.draw.line(window, "black", (0, HEIGHT/2), (WIDTH, HEIGHT/2))
                    pygame.draw.circle(window, "black", (WIDTH/2, HEIGHT/2), 5)

                    pos = pygame.mouse.get_pos()
                    pygame.draw.line(window, "red", (WIDTH/2, HEIGHT/2), pos)
                    pygame.draw.line(window, "blue", pos, (pos[0], HEIGHT/2))

                    point_O = (WIDTH/2, HEIGHT/2)
                    point_A = pos
                    point_B = (pos[0], HEIGHT/2)

                    cent1 = getCenter(point_A, point_B)
                    cent2 = getCenter(point_A, point_O)
                    cent3 = getCenter(point_B, point_O)
                    pygame.draw.circle(window, "red", cent1, 4)
                    pygame.draw.circle(window, "red", cent2, 4)
                    pygame.draw.circle(window, "red", cent3, 4)

                    # POINT O
                    center_txt = "O"
                    center_txt = font.render(center_txt, True, "black")
                    center_txt_rect = center_txt.get_rect()
                    window.blit(center_txt, (WIDTH/2 - 5, HEIGHT/2 + 5), center_txt_rect)

                    # POINT A
                    pointA_txt = "A"
                    pointA_txt = font.render(pointA_txt, True, "black")
                    pointA_txt_rect = pointA_txt.get_rect()
                    if pos[1] <= (HEIGHT/2):
                        window.blit(pointA_txt, (pos[0]-5, pos[1]-15), pointA_txt_rect)
                    else:
                        window.blit(pointA_txt, (pos[0]-5, pos[1]+15), pointA_txt_rect)
                    
                    # POINT B
                    pointB_txt = "B"
                    pointB_txt = font.render(pointB_txt, True, "black")
                    pointB_txt_rect = pointB_txt.get_rect()
                    if pos[1] <= (HEIGHT/2): # UPPER HALF
                        window.blit(pointB_txt, (pos[0]-5, HEIGHT/2 + 5), pointB_txt_rect)

                    else: # LOWER HALF
                        if pos[0] <= (WIDTH/2): # LEFT HALF
                            window.blit(pointB_txt, (pos[0]-5, HEIGHT/2 - 15), pointB_txt_rect)
                        else : # RIGHT HALF
                            window.blit(pointB_txt, (pos[0]-5, HEIGHT/2 - 15), pointB_txt_rect)

                    writeDistance(point_B, point_O, pos, axis="y", side1=(-8,13), side2=(-8,-20))
                    writeDistance(point_B, point_A, pos, axis="x", side1=(-30,0), side2=(10,0))
                    writeDistance(point_O, point_A, pos, axis="x", side1=(20,-5), side2=(-35,-5))

        update()

    pygame.quit()

if __name__ == "__main__":
    run()