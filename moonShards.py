#-------------------------------------------------------------------------------
# Name:        Moon Shards
# Purpose: A 2D adventure game that tells the story of Khaled. Go on a text
# adventure with gameplay elements added to make it more enjoyable.
#
# Author:      Eugene Cho
#
# Created:     16-01-2016
# Copyright:   (c) Eugene 2016
#-------------------------------------------------------------------------------



import pygame
import random
from math import pi

# Define some colors
BLACK         = (0, 0, 0)
WHITE         = (255, 255, 255)
GREEN         = (28, 117, 31)
DARK_GREEN  = (24,97,10)
RED           = (255, 0, 0)
GRAY          = (61, 60, 53)
YELLOW        = (237, 214, 38)
CEMENT        = (125, 85, 45)
BROWN         = (110, 74, 38)
TAN           = (161, 143, 125)
CEMENT_TIP    = (143, 93, 43)
MOON_LIGHT    = (227, 225, 204)
LIGHTER_BLACK = (1, 1, 1)
SMOKE_GRAY    = (159, 160, 161)
RAIN_GRAY     = (152,166,171)


pygame.init()

# Set the width and height of the screen [width, height]
size = (960, 540)
screen = pygame.display.set_mode(size)

#Set caption as game title.
pygame.display.set_caption("Moon Shards")

#Load images that will be needed throughout the game.
background_image = pygame.image.load("starrynight.jpg").convert()
moonCharacterImage = pygame.image.load("moonCharacter.png").convert_alpha()
moonSun = pygame.image.load("moonSun.png").convert_alpha()
pixie = pygame.image.load("pixie.png").convert_alpha()




# Create an empty array for rain (main menu)
rain_list = []
# Loop 150 times and add a rain drop in a random x,y position (main menu)
for i in range(150):
    x = random.randrange(-400, 960)
    y = random.randrange(0, 540)
    rain_list.append([x, y])


#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# These are all drawing functions that will be used throughout the game. Mostly in the main menu.
#==================================================================================================================================================#
def drawBackground(screen,x,y):
    pygame.draw.rect(screen,(0,0,0), [x,y,960,540],0)

def drawMoon(screen,x,y):
        # draw moon.
        pygame.draw.ellipse(screen, MOON_LIGHT, [x,y,150,150], 0)
        pygame.draw.ellipse(screen, (0,0,0), [x+50,y-10,150,150], 0)
        pygame.draw.ellipse(screen, BLACK, [x+35,y+60,11.25,11.25], 2)
        pygame.draw.ellipse(screen, BLACK, [x+40,y+62.5,5.25,5.25], 2)
        pygame.draw.line(screen, BLACK, [x+46, y+95], [x+57.5, y+90], 2)

def drawSun(screen,x,y):
    pygame.draw.ellipse(screen, YELLOW, [x,y,100,100], 0)
    pygame.draw.line(screen, YELLOW, [x+10, y+100], [x-20, y+150], 2)
    pygame.draw.line(screen, YELLOW, [x+80, y+100], [x+110, y+150], 2)
    pygame.draw.line(screen, YELLOW, [x+110, y+50], [x+170, y+50], 2)
    pygame.draw.line(screen, YELLOW, [x-15, y+50], [x-70, y+50], 2)
    pygame.draw.line(screen, YELLOW, [x+130, y-50], [x+90, y], 2)
    pygame.draw.line(screen, YELLOW, [x-35, y-50], [x, y], 2)

def drawUFO(screen,x_ufo,y):
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo+60,y,80,90],  pi/2,     pi, 2)
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo+60,y,80,90],     0,   pi/2, 2)
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)),   [x_ufo+60,y,80,90],3*pi/2,   2*pi, 2)
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)),  [x_ufo+60,y,80,90],    pi, 3*pi/2, 2)
    pygame.draw.ellipse(screen, GRAY, [x_ufo,y+55,200,50], 0)
    pygame.draw.ellipse(screen, GRAY, [x_ufo+60,y,80,90], 0)
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo,y+55,200,50],  pi/2,     pi, 2)
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo,y+55,200,50],     0,   pi/2, 2)
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)),   [x_ufo,y+55,200,50],3*pi/2,   2*pi, 2)
    pygame.draw.arc(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)),  [x_ufo,y+55,200,50],    pi, 3*pi/2, 2)
    pygame.draw.circle(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo+35,y+80], 15)
    pygame.draw.circle(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo+80,y+80], 15)
    pygame.draw.circle(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo+125,y+80], 15)
    pygame.draw.circle(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), [x_ufo+170,y+80], 15)

def drawBuilding(screen,x,y):
    # draw main building outline.
    pygame.draw.rect(screen,GRAY,[x,y,435,315],0)

    # draw windows with lights on, (some will be filled with black for lights off)
    x_offset = 0
    y_offset = 0
    for i in range (12):
        pygame.draw.rect(screen,YELLOW, [x+30+x_offset,y+35+y_offset,52.5,75],0)
        x_offset += 112.5
        if x_offset == 450:
            y_offset+=112.5
            x_offset = 0

    # draw building windows with lights off
    pygame.draw.rect(screen,BLACK, [x+30,y+35,52.5,75],0)
    pygame.draw.rect(screen,BLACK, [x+255,y+147.5,52.5,75],0)
    pygame.draw.rect(screen,BLACK, [x+142.5,y+260.5,52.5,75],0)
    pygame.draw.rect(screen,BLACK, [x+367.5,y+260.5,52.5,75],0)

def drawCurtains(screen,x,y):
    # draw curtains.
    pygame.draw.rect(screen,BROWN, [x,y,47,60],0)
    pygame.draw.rect(screen,BROWN, [x-224,y+225.5,45.5,60],0)
    line_y_offset = 0
    for i in range (5):
        pygame.draw.line(screen, BLACK, [x-1.9, y+line_y_offset], [x+46.1, y+line_y_offset], 3)
        pygame.draw.line(screen, BLACK, [x-225.9, y+225.5+line_y_offset], [x-179.9, y+225.5+line_y_offset], 3)
        line_y_offset += 15
def drawChimney(screen,x,y):
    # draw chimney
    pygame.draw.rect(screen,BROWN, [x,y,22.5,15],0)
    pygame.draw.rect(screen,CEMENT, [x+22.5,y,22.5,15],0)
    pygame.draw.rect(screen,TAN, [x,y-15,22.5,15],0)
    pygame.draw.rect(screen,BROWN, [x+22,y-15,22.5,15],0)
    pygame.draw.rect(screen,BROWN, [x,y-30,22.5,15],0)
    pygame.draw.rect(screen,CEMENT, [x+22,y-30,22.5,15],0)
    pygame.draw.rect(screen,TAN, [x,y-45,22.5,15],0)
    pygame.draw.rect(screen,BROWN, [x+22,y-45,22.5,15],0)
    pygame.draw.rect(screen,CEMENT_TIP, [x-5,y-50,53,22.5],0)

def drawMotelSign(screen,x,y):
    # draw motel sign
    pygame.draw.rect(screen,CEMENT_TIP, [x,y,9,112.5],0)
    pygame.draw.rect(screen,CEMENT_TIP, [x+175,y,9,112.5],0)
    pygame.draw.rect(screen,MOON_LIGHT, [x+9,y,166,75],0)

    # draw text on the sign
    font = pygame.font.SysFont('Times New Roman', 20, True, False)
    fontTwo = pygame.font.SysFont('Times New Roman', 16, True, False)


    motelSign_1 = font.render("Moon Shards",True, BLACK)
    screen.blit(motelSign_1, [x+32, y+7])

    motelSign_2 = fontTwo.render("By: Eugene Cho",True,BLACK)
    screen.blit(motelSign_2, [x+32, y+40])

    instructions = fontTwo.render("Press space to start the game. Press q to quit.",True,(255, 255, 255))
    screen.blit(instructions, [x-50, y-50])




def drawPulley(screen,x,y):
    # draw pulleys in windows
    pygame.draw.line(screen, BLACK, [x, y], [x, y+52], 1)
    pygame.draw.ellipse(screen, BLACK, [x-2.5,y+52,7,7], 1)
    pygame.draw.line(screen, BLACK, [x+223, y+112], [x+223, y+164], 1)
    pygame.draw.ellipse(screen, BLACK, [x+220.5,y+164,7,7], 1)

def drawPerson(screen,x,y):
    # draw person.
    pygame.draw.ellipse(screen, BLACK, [x,y,30,30], 0)
    pygame.draw.line(screen, BLACK, [x+13.5, y+30], [x+13.5, y+66], 2)
    pygame.draw.line(screen, BLACK, [x+12, y+45], [x-11, y+10], 2)
    pygame.draw.line(screen, BLACK, [x+15, y+45], [x+38, y+10], 2)

def drawSmoke(screen,x,y):
    # draw smoke coming out of chimney
    pygame.draw.arc(screen, SMOKE_GRAY, [x,y,1100,200],2,pi, 80)


def drawMoonShard(screen,x,y):
    pygame.draw.ellipse(screen, SMOKE_GRAY, [x,y,50,50], 0)
    pygame.draw.ellipse(screen, BLACK, [x+10,y+13,11.25,11.25], 2)
    pygame.draw.ellipse(screen, BLACK, [x+13.5,y+16,5.25,5.25], 2)
    pygame.draw.ellipse(screen, BLACK, [x+28,y+13,11.25,11.25], 2)
    pygame.draw.ellipse(screen, BLACK, [x+31.5,y+16,5.25,5.25], 2)
    pygame.draw.line(screen, BLACK, [x+10, y+35], [x+38, y+35], 1)


#========================================================================================================================#




#set the moon co-ordinate for the gameplay.
moon_y = 480
#set a variable equal to zero for the future speed of the moon in gameplay.
moon_y_speed = 0

#set a variable for the stage of the game.
gameStage = 0

#set a variable for a substage within the game stage.
subStage = 0



#open text file to read the dialogue in the game.
text = open('text.txt','r')

#set the dialogue list to a variable
textlist = text.readlines()


#set a variable for the stage background x-coordinate, namely for the gameplay stage.
stageBackground_x = 0
#set a variable for the stage background y-coordinate, namely for the credits stage.
stageBackground_y = 0

#set a variable for the moon in the gameplay stage. This is for the end of the stage when the moon moves off the screen to the right.
moon_collect_x = 0



#create an empty list for the fairy spawn point x-coordinate
randomListX = []

#append the list with the random fairy spawn point x-coordinate
for i in range(200):
    randomListX.append(random.randint(540,19000))

#create an empty list for the fairy spawn point y-coordinate
randomListY = []

#append the list with the random fairy spawn point y-coordinate
for i in range(200):
    randomListY.append(random.randint(0,490))




#create an empty list for the moons' x-coordinate in the credit stage.
randomMoonX = []
#append the list with random integers from 0-900 (screen width while not going outside the screen.)
for i in range (10):
    randomMoonX.append(random.randint(0,900))

#create an empty list for the moons' y-coordinate in the credit stage.
randomMoonY = []
#append the list with random integers from 0-900 (screen height while not going outside the screen.)
for i in range (10):
    randomMoonY.append(random.randint(0,500))




#music list for stages throughout the game.
musicList = ["musicBox.ogg","mountainMusic.ogg","forestMusic.ogg","forestMusic.ogg","credits.ogg"]

#default music selection set to -1 beacuse each stage adds + 1 to the music selection.
musicSelect = -1

#default font. this is changed throughout the game though.
font = pygame.font.SysFont('Times New Roman', 20, True, False)

#load and play the first music piece of the game before going into the music list for later stages.
pygame.mixer.music.load("rainy.wav")
pygame.mixer.music.play()



# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        #if the user presses the key down.
        elif event.type == pygame.KEYDOWN:

            #speed for moon movement in the gameplay (stage 4)
            if event.key == pygame.K_UP:

                moon_y_speed = -10
            elif event.key == pygame.K_DOWN:
                moon_y_speed = 10







        # User let up on a key
        elif event.type == pygame.KEYUP:

            #set speed to 0 if the user presses neither the up or down key.
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                moon_y_speed = 0

            #The space button triggers the gameStages and sub stages for various parts of the game.
            #These commands were down with keyup instead of keydown. This is because there was a conflict with using keydown and having
            #consecutive commands with the same key.
            elif event.key == pygame.K_SPACE:
                #move substage when needed
                if gameStage ==1 and subStage <1 or gameStage == 2 and subStage <10 or gameStage == 3 and subStage<4 or gameStage == 4 and subStage==0 or gameStage == 5 and subStage == 0 or gameStage == 6 and subStage == 0:
                    subStage+=1
                #do nothing during these stages even if space is KEYUP
                elif gameStage == 4 and subStage == 1 or gameStage == 5 and subStage == 1 or gameStage == 6 and subStage == 1:
                    subStage+=0
                #everywhere else, game stage is changed therefore, change music also and reset substage back to 0
                else:
                    gameStage+=1
                    musicSelect+=1
                    subStage = 0

                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(musicList[musicSelect])
                    pygame.mixer.music.play()

            #q and r keys are used throughout the game for restarting the level and quitting the game altogether.
            # the gamestage and subtage requirements in the if statement indicates the stages where quit and restart are used.
            elif event.key == pygame.K_q and gameStage == 6 or gameStage == 0:
                done = True
            elif event.key == pygame.K_q and gameStage == 5 and subStage == 1:
                done = True

            elif event.key == pygame.K_r and gameStage == 6:
                    gameStage = 4
                    stageBackground_x = 0



    # --- Game logic should go here
    # i.e calculations for positions, variable updates

    #add the speed to moon_y to reposition the moon in the gameplay
    moon_y += moon_y_speed



    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    #set background image.

    # --- Drawing code should go here



    #first game stage
    if gameStage == 0:
    #draw the opening menu screen
        drawBackground(screen,0,0)
        drawMoon(screen,10,10)
        drawSun(screen,800,620-10)
        drawBuilding(screen,525,225)
        drawPulley(screen,680,260)
        drawPerson(screen,678,380)
        drawSmoke(screen,830,64)
        drawMotelSign(screen,550,113)
        drawChimney(screen,830,210)
        drawCurtains(screen,783.9,260)

    #draw rain in the opening menu screen.
    # Process each rain drop in the list
        for i in range(len(rain_list)):

            # Draw the rain drop
            pygame.draw.line(screen, RAIN_GRAY, rain_list[i], [rain_list[i][0]+3, rain_list[i][1]+3], 1)


            # Move the rain drop down 2 pixels and right 2 pixels (make rain diagonal).
            rain_list[i][1] += 2
            rain_list[i][0] += 2

            # If the rain drop has moved off the bottom of the screen
            if rain_list[i][1] > 540:
                # Reset it just above the top and before the start on the left side.
                y = random.randrange(-50, -10)
                rain_list[i][1] = y
                # Give it a new x position
                x = random.randrange(-400, 960)
                rain_list[i][0] = x

#========================================================================================================================#

    #second game stage
    if gameStage == 1:

        #first substage of the second game stage. This logic applies to the rest of the substages per gameStage.
        if subStage == 0:


            screen.fill(BLACK)
            #this whole sequence of code is to blit the text from the textfile list accordingly.
            #the a variable is used to discriminate which lines to blit and which not to.
            a = 0
            height = 0
            for line in textlist:
                    a+=1
                    height += 20
                    if a <9:
                        line = line[:-1]
                        sentence = font.render(line,True,WHITE)
                        screen.blit(moonSun, [350, 100])

                        screen.blit(sentence, [50, height])
        #Second substage of the second game stage
        if subStage == 1:
                screen.fill(BLACK)
            #this whole sequence of code is to blit the text from the textfile list accordingly.
            #the a variable is used to discriminate which lines to blit and which not to.
                a = 0
                height = 0
                for line in textlist:
                        a+=1
                        if 9<a<14:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(moonSun, [350, 100])

                            screen.blit(sentence, [50, height])


#========================================================================================================================#

    if gameStage == 2:
        background_image = pygame.image.load("townMap1.jpg").convert()
        screen.blit(background_image, [0, 0])
        if subStage == 0:
            #this whole sequence of code is to blit the text from the textfile list accordingly.
            #the a variable is used to discriminate which lines to blit and which not to.
                a = 0
                height = 0

                for line in textlist:
                        a+=1
                        if a ==15:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 1:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 16:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 2:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 17:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 3:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 18:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 4:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 19:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 5:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 20:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 6:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 21:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 7:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 22:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 8:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 23:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 9:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 24:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])
        if subStage == 10:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 25:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                        screen.blit(moonCharacterImage, [325, 75])



#========================================================================================================================#


    if gameStage == 3:
        #change and blit the background image to forest.
        background_image = pygame.image.load("forestOne.png").convert()
        screen.blit(background_image, [0, 0])

        if subStage == 0:

                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 27:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                screen.blit(moonCharacterImage, [325, 75])
        if subStage == 1:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 28:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                screen.blit(moonCharacterImage, [325, 75])
        if subStage == 2:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 29:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                screen.blit(moonCharacterImage, [325, 75])
        if subStage == 3:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 30:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                screen.blit(moonCharacterImage, [325, 75])
        if subStage == 4:
                a = 0
                height = 0
                #this whole sequence of code is to blit the text from the textfile list accordingly.
                #the a variable is used to discriminate which lines to blit and which not to.
                for line in textlist:
                        a+=1
                        if a == 31:
                            height += 20
                            line = line[:-1]
                            sentence = font.render(line,True,WHITE)
                            screen.blit(sentence, [50, height])
                screen.blit(moonCharacterImage, [325, 75])



#========================================================================================================================#

    if gameStage == 4:

        if subStage == 0:
            #background image for this stage
            screen.blit(background_image, [0-stageBackground_x, 0])
            background_image = pygame.image.load("forestLevel.jpg").convert()

            #instructions
            text = font.render("Avoid the evil fairies. Use Up and Down arrows to move. Press space to start.",True,WHITE)
            screen.blit(text,[150,150])

        #substage with actual gameplay.
        if subStage == 1:
            #if the x_coordinate of the location of the last background image is not 1, keep scrolling the background.
            if 1082*18-stageBackground_x != 1:

                stageBackground_x += 5

            #if the x_coordinate of the last background reaches 0, stop moving the background, and move the moon off the screen to the right.
            elif 1082*18-stageBackground_x == 1:
                moon_collect_x +=5

            #Blit the background image side to side 18 times to create a scrolling level.
            screen.blit(background_image, [0-stageBackground_x, 0])
            screen.blit(background_image, [1082-stageBackground_x,0])
            screen.blit(background_image, [1082*2-stageBackground_x,0])
            screen.blit(background_image, [1082*3-stageBackground_x,0])
            screen.blit(background_image, [1082*4-stageBackground_x,0])
            screen.blit(background_image, [1082*5-stageBackground_x,0])
            screen.blit(background_image, [1082*6-stageBackground_x,0])

            screen.blit(background_image, [1082*7-stageBackground_x,0])
            screen.blit(background_image, [1082*8-stageBackground_x,0])
            screen.blit(background_image, [1082*9-stageBackground_x,0])
            screen.blit(background_image, [1082*10-stageBackground_x,0])
            screen.blit(background_image, [1082*11-stageBackground_x,0])
            screen.blit(background_image, [1082*12-stageBackground_x,0])
            screen.blit(background_image, [1082*13-stageBackground_x,0])
            screen.blit(background_image, [1082*14-stageBackground_x,0])
            screen.blit(background_image, [1082*15-stageBackground_x,0])
            screen.blit(background_image, [1082*16-stageBackground_x,0])
            screen.blit(background_image, [1082*17-stageBackground_x,0])
            screen.blit(background_image, [1082*18-stageBackground_x,0])


            #draw player's moon accordingly to the location.
            drawMoonShard(screen,50+moon_collect_x,moon_y)


            #create sprite. This is to create and invisible hit box for the player-controlled moon.
            moonBox = pygame.sprite.Sprite()
            moonBox.rect = pygame.Rect(50+moon_collect_x,moon_y ,50, 50)
            moonBox.image = pygame.Surface((50, 50))
            moonBox.image.fill((0,0,0,0))


            for i in range (len(randomListX)):
                    #create sprite. This is to create and invisible hit box for the fairies.
                    player = pygame.sprite.Sprite()

                    player.rect = pygame.Rect(randomListX[i]-stageBackground_x, randomListY[i],40, 40)


                    player.image = pygame.Surface((40, 40))

                    player.image.fill((0, 0, 0,0))


                    #blit the fairy according to the random integers assigned to the random lists. This location applys to the hitboxes too.
                    screen.blit(pixie, [randomListX[i]-stageBackground_x, randomListY[i]])

                    #if the two hitboxes collide, it is sent to stage 6, which is game-over.
                    if pygame.sprite.collide_rect(player, moonBox):
                        gameStage = 6






            #if the player makes it to the end, and the moon moves off the screen, set to subStage 2,
            if 50 + moon_collect_x>960:
                subStage+=1

            #These are the walls that will prevent the player moon from moving outside the screen.
            if moon_y > 490:
                moon_y = 490

            if moon_y<0:
                moon_y = 0
        #Congratulatory substage.
        if subStage == 2:
            screen.blit(background_image, [0, 0])

            #moons are drawn randomly to celebrate the re-unification of the moon-shards.
            for i in range (10):

                drawMoonShard(screen,randomMoonX[i],randomMoonY[i])

            #Change the fonts appropriately for congratulatory text.
            font = pygame.font.SysFont('Calibri', 30, True, False)
            fontTwo = pygame.font.SysFont('Calibri', 30, True, False)
            text = font.render("Congratulations, you won the game and re-united the moon shards!!!",True,WHITE)
            textTwo =fontTwo.render("Press space to roll the credits!.",True,WHITE)
            screen.blit(text,[50,150])
            screen.blit(textTwo,[50,225])



#========================================================================================================================#


    #credits stage
    if gameStage == 5:
        if subStage == 0:

            #the credits background will keep moving upwards by 3 pixels until the last one reaches the top.
            #when it reaches the top, send to substage 2.
            if 720*5-stageBackground_y ==0:
                stageBackground_y+= 0
                subStage+=1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        done = True
            else:
                stageBackground_y+= 3

            #change and blit background images one above the other to create a scrolling effect.
            background_image = pygame.image.load("credits.jpg").convert()
            screen.blit(background_image, [0, 0-stageBackground_y])
            screen.blit(background_image, [0, 720-stageBackground_y])
            screen.blit(background_image, [0, 720*2-stageBackground_y])
            screen.blit(background_image, [0, 720*3-stageBackground_y])
            screen.blit(background_image, [0, 720*4-stageBackground_y])
            screen.blit(background_image, [0, 720*5-stageBackground_y])

            #change font appropriately for the credits.
            font = pygame.font.SysFont('Calibri', 30, True, False)
            creditsOne = font.render("Produced by: Eugene Cho",True,DARK_GREEN)
            creditsTwo = font.render("Directed by: Eugene Cho",True,DARK_GREEN)
            creditsThree = font.render("Programming by: Eugene Cho",True,DARK_GREEN)
            creditsFour = font.render("Music Selection by: Eugene Cho",True,DARK_GREEN)
            creditsFive = font.render("Written by: Eugene Cho",True,DARK_GREEN)
            creditsSix = font.render("Inspired by: Mr. Henin",True,DARK_GREEN)

            screen.blit(creditsOne,[300,540 - stageBackground_y])
            screen.blit(creditsTwo,[300,540*2 - stageBackground_y])
            screen.blit(creditsThree,[300,540*3 - stageBackground_y])
            screen.blit(creditsFour,[300,540*4 - stageBackground_y])
            screen.blit(creditsFive,[300,540*5 - stageBackground_y])
            screen.blit(creditsSix,[300,540*6 - stageBackground_y])

        #final victory screen, press q to quit the game altogether.
        if subStage == 1:
            screen.blit(background_image, [0, 0])
            font = pygame.font.SysFont('Calibri', 25, True, False)
            victory = font.render("You have won. Press q to quit.",True,DARK_GREEN)

            screen.blit(victory,[150,150])



#========================================================================================================================#
    #game-over stage the user will be sent to if they get hit by a fairy.

    if gameStage == 6:
        screen.fill(BLACK)

        #change font to appropriate parameters for gameover stage.
        #blit the game-over text.
        font = pygame.font.SysFont('Calibri', 85, True, False)
        fontTwo = pygame.font.SysFont('Calibri', 55, True, False)
        gameOver = font.render("GAME OVER",True,WHITE)
        gameOverTwo = fontTwo.render("Press q to exit OR r to restart the level",True,WHITE)
        screen.blit(gameOver,[50,150])
        screen.blit(gameOverTwo,[50,225])




    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
