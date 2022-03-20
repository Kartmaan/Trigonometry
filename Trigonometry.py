__author__ = "Kartmaan"
__version__ = "1.0"

import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1024, 800 #1024, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trigonometry')

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
    """ Function calculating the distance between 
    two pairs of x,y coordinates.
    
    The function returns an int value.
    
    Example:
    getDistance((141, 400), (512, 400))
    >>> 371
    """
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
    adj = ((187, 400), (512, 400))
    hyp = ((512, 400), (187, 109))

    Each pair of coordinates is then used to calculate 
    the distance between them (getDistance())

    These distances correspond to the lengths of the two segments, 
    thus making it possible to calculate the angle

    getAngle(((187,400), (512, 400)), ((512, 400), (187, 109)))
    >>> 41.81
    """
    adj = getDistance(adj[0], adj[1]) # Adjacent side measurement
    hyp = getDistance(hyp[0], hyp[1]) # Hypotenuse measurement
    angle = math.acos(adj/hyp) # Angle measurement
    angle = math.degrees(angle) # Conversion to degree
    return round(angle, 2)

def writeDistance(p1, p2, pos, axis="x", side1=(0,0), side2=(0,0)):
    """ Function that inscribes and places the length of the 
    segments on the surface so as not to overlap the figure.
    
    p1 and p2 are tuples corresponding to the coordinates 
    of the two points of each segment
    
    "pos" is a tuple containing the coordinates of the cursor, 
    which are also the coordinates of point A 
    (which therefore follows the cursor). 
    This variable makes it possible to determine in real time 
    on which part of the surface the point A is located 
    and thus to adjust the positioning of the texts so 
    that they do not encroach on the figure

    "axis" can take the value of "x" or "y", 
    it determines on which axis the correction of the 
    placement of the text must be done.
    - axis="x" : Passage between the left side (side1) 
    and right side (side2) of the surface
    - axis="y" : Passage between the top side (side1) 
    and bottom side (side2) of the surface

    side1/side2: x,y adjustment of text placement depending 
    on which side of the surface you are on. By default 
    the text is displayed on the center point of the segment, 
    these adjustments allow to correct the positioning 
    for a better visibility
    """

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
    """Function inscribing and placing angles on the surface 
    so as not to overlap the figure 
    
    p1, p2 and p3 are the coordinates of the 3 points 
    of the right triangle. 
    p2 is the point on which the angle will be calculated.
    
    "pos" is a tuple containing the coordinates of the cursor, 
    which are also the coordinates of point A 
    (which therefore follows the cursor). 
    This variable makes it possible to determine in real time 
    on which part of the surface the point A is located 
    and thus to adjust the positioning of the texts so 
    that they do not encroach on the figure.

    "axis" can take the value of "x" or "y", 
    it determines on which axis the correction of the 
    placement of the text must be done.
    - axis="x" : Passage between the left side (side1) 
    and right side (side2) of the surface
    - axis="y" : Passage between the top side (side1) 
    and bottom side (side2) of the surface

    side1/side2 : x,y adjustment of text placement depending 
    on which side of the surface we are on. By default the text 
    is displayed on the coordinates of the point, 
    these adjustments allow to correct the positioning 
    for a better visibility
    """
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

    # Introductory sentences
    # The instructions appear only once before 
    # entering the main loop
    intro_txt = "Left click and move the cursor"
    intro_txt = font.render(intro_txt, True, "black")
    intro_txt_rect = intro_txt.get_rect()

    instruc_txt = "Left click again to stop/retrieve the transformation"
    instruc_txt = font.render(instruc_txt, True, "black")
    instruc_txt_rect = instruc_txt.get_rect()

    window.blit(intro_txt, ((WIDTH/2)-(intro_txt_rect[2]/2), (HEIGHT/4)-intro_txt_rect[3]-10), intro_txt_rect)
    window.blit(instruc_txt, ((WIDTH/2)-(instruc_txt_rect[2]/2), (HEIGHT/4)), instruc_txt_rect)

    while run: # Main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click
                if pygame.mouse.get_pressed()[0]: #Left click
                    if move == False: # Tranformation OFF
                        move = True # Transformation ON
                    else:
                        move = False # Transformation OFF

            if event.type == pygame.MOUSEMOTION: # When cursor move
                if move:
                    window.fill("white")
                    pygame.draw.line(window, "black", (0, HEIGHT/2), (WIDTH, HEIGHT/2))
                    pygame.draw.circle(window, "black", (WIDTH/2, HEIGHT/2), 5)

                    pos = pygame.mouse.get_pos() # Cursor (x,y) coordinates
                    pygame.draw.line(window, "red", (WIDTH/2, HEIGHT/2), pos)
                    pygame.draw.line(window, "blue", pos, (pos[0], HEIGHT/2))

                    # Coordinates of the 3 points of the right triangle
                    point_O = (WIDTH/2, HEIGHT/2)
                    point_A = pos
                    point_B = (pos[0], HEIGHT/2)

                    # Placing red points at the center of each segment
                    cent1 = getCenter(point_A, point_B)
                    cent2 = getCenter(point_A, point_O)
                    cent3 = getCenter(point_B, point_O)
                    pygame.draw.circle(window, "red", cent1, 4)
                    pygame.draw.circle(window, "red", cent2, 4)
                    pygame.draw.circle(window, "red", cent3, 4)

                    # Writing points on the surface (O, A, B)
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