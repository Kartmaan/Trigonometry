import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1024, 800 #1024, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font(None,20) # Default font, size 20

# Initialisation before run
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
    """ Function to find the center between two x,y coordinates

    p1 and p2 are tuples
    p1 = (x,y) of first point
    p2 = (x,y) of second point

    The function returns a tuple

    Example:
    getCenter((141, 400), (512,400))
    >>> (326.5, 400)
    """
    center = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    return center

def getAngle(adj, hyp):
    """ Function to calculate an angle from the 
    lengths of 2 segments  
    
    adj and hyp are 2 tuples each containing 2 tuples 
    corresponding to the x,y coordinates of a segment
    example : 
    adj = ((141, 400), (512,400))
    hyp = ((512, 400), (141, 121))

    Each pair of coordinates is then used to calculate 
    the distance between them
    example:
    getDistance((141, 400), (512, 400))
    >>> 371

    These distances correspond to the lengths of the two segments, 
    thus making it possible to calculate the angle
    """
    adj = getDistance(adj[0], adj[1])
    hyp = getDistance(hyp[0], hyp[1])
    angle = math.acos(adj/hyp)
    angle = math.degrees(angle)
    return round(angle, 2)

def writeDistance(p1, p2, pos, axis="x", side1=(0,0), side2=(0,0)):
    dist_txt = str(getDistance(p1, p2))
    dist_txt = font.render(dist_txt, True, "cyan4")
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

def writeAngle(p1, p2, p3, pos, axis="x", side1=(0,0), side2=(0,0)):
    angle_txt = str(getAngle((p1, p2), (p2, p3)))+"°"
    angle_txt = font.render(angle_txt, True, "darkorange3")
    angle_txt_rect = angle_txt.get_rect()

    if axis == "x":
        if pos[0] <= WIDTH/2: # LEFT
            window.blit(angle_txt, (p2[0]+side1[0], p2[1]+side1[1]), angle_txt_rect)
        else: # RIGHT
            window.blit(angle_txt, (p2[0]+side2[0], p2[1]+side2[1]), angle_txt_rect)

    if axis == "y":
        if pos[1] <= HEIGHT/2: # TOP
            window.blit(angle_txt, (p2[0]+side1[0], p2[1]+side1[1]), angle_txt_rect)
        else: # DOWN
            window.blit(angle_txt, (p2[0]+side2[0], p2[1]+side2[1]), angle_txt_rect)

def run():
    run = True
    clock = pygame.time.Clock()
    fps = 30
    clock.tick(fps)
    move = False

    #print(getDistance((141, 400), (512, 400)))
    print(getCenter((141, 400), (512,400)))

    # Introductory sentences
    intro_txt = "Left click and move the cursor"
    intro_txt = font.render(intro_txt, True, "black")
    intro_txt_rect = intro_txt.get_rect()

    instruc_txt = "Left click again to stop/retrieve the transformation"
    instruc_txt = font.render(instruc_txt, True, "black")
    instruc_txt_rect = instruc_txt.get_rect()

    window.blit(intro_txt, ((WIDTH/2)-(intro_txt_rect[2]/2), (HEIGHT/4)-intro_txt_rect[3]-10), intro_txt_rect)
    window.blit(instruc_txt, ((WIDTH/2)-(instruc_txt_rect[2]/2), (HEIGHT/4)), instruc_txt_rect)

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

                    # Placing points at the center of segments
                    cent1 = getCenter(point_A, point_B)
                    cent2 = getCenter(point_A, point_O)
                    cent3 = getCenter(point_B, point_O)
                    pygame.draw.circle(window, "red", cent1, 4)
                    pygame.draw.circle(window, "red", cent2, 4)
                    pygame.draw.circle(window, "red", cent3, 4)

                    # POINT O (static)
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

                    # Show segment length
                    writeDistance(point_B, point_O, pos, axis="y", side1=(-8,13), side2=(-8,-20))
                    writeDistance(point_B, point_A, pos, axis="x", side1=(-30,0), side2=(10,0))
                    writeDistance(point_O, point_A, pos, axis="x", side1=(20,-5), side2=(-35,-5))

                    # Show angles
                    writeAngle(point_B, point_A, point_O, pos, axis="y", side1=(-15,-30), side2=(-15,30))
                    writeAngle(point_B, point_O, point_A, pos, axis="x", side1=(0,-20), side2=(-35,-20))

        update()

    pygame.quit()

if __name__ == "__main__":
    run()