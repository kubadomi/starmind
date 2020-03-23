import pygame, time, random

pygame.init()

good = 0
wrong = 0
place = 0
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
aqua = (0, 255, 255)
green = (0,220,0)
bright_green = (0, 255, 0)
blue = (0,0,200)
yellow = (220, 220, 0)
bright_yellow = (255,255,0)
pink = (235, 172, 183)
bright_pink = (255, 192, 203)
orange = (235, 115, 0)
bright_orange = (255, 140, 0)
bright_blue = (0,0,255)
bright_red = (255,0,0)
bezowy = (240, 248, 255)
grey = (131, 139, 139)
bright_grey = (193, 205, 205)
bright_gre = (180, 190, 190)

i = 0
j = 0
k = 0
pp = 0
zm = [grey, grey, grey, grey]
zm2 = [grey, grey, grey, grey]
w = [grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey]
zm1 = [grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey]
line = [50, 150, 215, 280, 345, 410, 475, 540, 605, 630]
column = [40, 102, 164, 226, 295, 321, 347, 373]

colors = [green, blue, red, yellow, pink, orange]
color_number = 4

display_width = 500
display_height = 780
gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay1 = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('mastermind')
clock = pygame.time.Clock()
gameIcon = pygame.image.load('leb.jpg')
pygame.display.set_icon(gameIcon)
menu_sound = pygame.mixer.Sound("DesiJourney.wav")
win_sound = pygame.mixer.Sound("strings.wav")
lose_sound = pygame.mixer.Sound("strings4.wav")
game_sound = pygame.mixer.Sound("strings3.wav")


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)


def quitgame():
    pygame.quit()
    quit()


def color1():
    global i
    global zm
    zm[i] = green
    #print("jest kolor")
    if i == 4:
        i = 3


def color2():
    global i
    global zm
    zm[i] = blue
    #print("jest kolor")
    if i == 4:
        i = 3


def color3():
    global i
    global zm
    zm[i] = red
    #print("jest kolor")
    if i == 4:
        i = 3


def color4():
    global i
    global zm
    zm[i] = yellow
    #print("jest kolor")
    if i == 4:
        i = 3


def color5():
    global i
    global zm
    zm[i] = pink
    #print("jest kolor")
    if i == 4:
        i = 3


def color6():
    global i
    global zm
    zm[i] = orange
    #print("jest kolor")
    if i == 4:
        i = 3

def colorreset1():
    global i
    global zm
    zm[0] = grey
    #print("mamy to")
    i = 0

def colorreset2():
    global i
    global zm
    zm[1] = grey
    #print("mamy to")
    i = 1

def colorreset3():
    global i
    global zm
    zm[2] = grey
    #print("mamy to")
    i = 2

def colorreset4():
    global i
    global zm
    zm[3] = grey
    #print("mamy to")
    i = 3

def check():
    global pp
    global i
    global j
    global good
    global wrong
    global place
    global chosen
    global w
    global zm2
    global zm
    win = 0
    #check zm[0]
    if zm[0] == chosen[0]:
        good += 1
    elif zm[0] == chosen [1] or zm[0] == chosen[2] or zm[0] == chosen[3]:
        place += 1
    else:
        wrong += 1
    #check zm[1]
    if zm[1] == chosen[1]:
        good += 1
    elif zm[1] == chosen [0] or zm[1] == chosen[2] or zm[1] == chosen[3]:
        place += 1
    else:
        wrong += 1
    #check zm[2]
    if zm[2] == chosen[2]:
        good += 1
    elif zm[2] == chosen [0] or zm[2] == chosen[1] or zm[2] == chosen[3]:
        place += 1
    else:
        wrong += 1
    #check zm[3]
    if zm[3] == chosen[3]:
        good += 1
    elif zm[3] == chosen [0] or zm[3] == chosen[1] or zm[3] == chosen[2]:
        place += 1
    else:
        wrong += 1

    print("good:", good, "wrong:", wrong, "place:", place)

    for zz in range(pp, good+pp):
        w[zz] = white
    for zz in range(pp+good, good+wrong+pp):
        w[zz] = black
    for zz in range(pp+good+wrong, good+wrong+place+pp):
        w[zz] = bright_gre
    pp += 4

    for l in range(0, 4):
        zm1[j] = zm[l]
        j += 1
        if zm[0] == chosen[0] and zm[1] == chosen[1] and zm[2] == chosen[2] and zm[3] == chosen[3]:
            zm2[0] = chosen[0]
            zm2[1] = chosen[1]
            zm2[2] = chosen[2]
            zm2[3] = chosen[3]
            win = 2
        if pp >= 32:
            zm2[0] = chosen[0]
            zm2[1] = chosen[1]
            zm2[2] = chosen[2]
            zm2[3] = chosen[3]
        zm[l] = grey

    i = 0
    pygame.display.update()
    if win == 2:
        pygame.display.update()
        win = 3
    if win == 3:
        pygame.mixer.Sound.play(win_sound)
        pygame.mixer.music.stop()
        message_display("You won!")
        good = 0
        wrong = 0
        place = 0
        j = 0
        pp = 0
        i = 0

    if pp >= 32:
        pygame.mixer.Sound.play(lose_sound)
        pygame.mixer.music.stop()
        message_display("You lost!")
        good = 0
        wrong = 0
        place = 0
        j = 0
        pp = 0
        i = 0

    good = 0
    wrong = 0
    place = 0


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",17)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def menu():
    global w
    global zm
    global zm1
    global zm2
    global chosen
    global i
    global j
    global pp
    chosen = random.sample(colors, color_number)
    print(chosen)
    pygame.mixer.music.load('DesiJourney.wav')
    pygame.mixer.music.play(-1)
    intro1 = True
    while intro1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(aqua)
        largeText = pygame.font.Font("freesansbold.ttf", 60)
        TextSurf, TextRect = text_objects("Mastermind", largeText)
        TextRect.center = ((display_width/2), (display_height/6))
        gameDisplay.blit(TextSurf, TextRect)

        button("New Game", 200, 250, 100, 50, blue, bright_blue, game)
        button("Instruction", 200, 400, 100, 50, blue, bright_blue, instruction)
        button("Quit", 200, 550, 100, 50, red, bright_red, quitgame)

        zm = [grey, grey, grey, grey]
        zm2 = [grey, grey, grey, grey]
        w = [grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey,
             grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey]
        zm1 = [grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey,
               grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey, grey]
        i = 0
        j = 0
        pp = 0
        pygame.display.flip()


def pas():
    pass


def instruction():
    intro1 = True
    while intro1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(aqua)
        largeText = pygame.font.Font("freesansbold.ttf", 40)
        TextSurf, TextRect = text_objects("Instruction", largeText)
        TextRect.center = ((display_width/2), (display_height/12))
        gameDisplay.blit(TextSurf, TextRect)


        largText = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 18)
        largeeText = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 25)
        TextSurf, TextRect = text_objects("Mastermind is a simple board game.", largText)
        TextRect.center = ((display_width/2), (display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("The main goal of this game is to guess 4 out of 6", largText)
        TextRect.center = ((display_width/2), (display_height/4+25))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("randomly selected colours.", largText)
        TextRect.center = ((display_width/2), (display_height/4+50))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("On the right side, you can pick them and put to input line.", largText)
        TextRect.center = ((display_width/2), (display_height/4+75))
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("You can cancel your pick by clicking on them in the input line.", largText)
        TextRect.center = ((display_width/2), (display_height/4+100))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("If you think that you are ready to guess, click 'check' button.", largText)
        TextRect.center = ((display_width/2), (display_height/4+125))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("The colors in result column mean:", largText)
        TextRect.center = ((display_width/2), (display_height/4+150))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("White - good color on the right spot", largText)
        TextRect.center = ((display_width/2), (display_height/4+175))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Black - wrong color", largText)
        TextRect.center = ((display_width/2), (display_height/4+200))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Grey - good color on the wrong spot", largText)
        TextRect.center = ((display_width/2), (display_height/4+225))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("You win the game if you guess all the 4 colors.", largText)
        TextRect.center = ((display_width/2), (display_height/4+250))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("But you lose the game if you won't, after 8 tries.", largText)
        TextRect.center = ((display_width/2), (display_height/4+275))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("Good luck! Become the mastermind!", largeeText)
        TextRect.center = ((display_width/2), (display_height/4+320))
        gameDisplay.blit(TextSurf, TextRect)

        button("menu", 370, 690, 100, 60, red, bright_red, menu)

        pygame.display.update()
        clock.tick(15)


def game():

    pygame.mixer.music.load('strings3.wav')
    pygame.mixer.music.play(-1)
    intro1 = True
    while intro1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(aqua)


        smallText = pygame.font.Font("freesansbold.ttf", 20)
        TextSurf, TextRect = text_objects("Answer:", smallText)
        TextRect.center = (80, 30)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Your tries:", smallText)
        TextRect.center = (90, 130)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Input:", smallText)
        TextRect.center = (70, 690)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Pick:", smallText)
        TextRect.center = (430, 130)
        gameDisplay.blit(TextSurf, TextRect)

        smalText = pygame.font.Font("freesansbold.ttf", 17)
        TextSurf, TextRect = text_objects("Results:", smalText)
        TextRect.center = (330, 150)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("#1", smallText)
        TextRect.center = (20, line[1]+31)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("#2", smallText)
        TextRect.center = (20, line[2]+31)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("#3", smallText)
        TextRect.center = (20, line[3]+31)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("#4", smallText)
        TextRect.center = (20, line[4]+31)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("#5", smallText)
        TextRect.center = (20, line[5]+31)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("#6", smallText)
        TextRect.center = (20, line[6]+31)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("#7", smallText)
        TextRect.center = (20, line[7]+31)
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("#8", smallText)
        TextRect.center = (20, line[8]+31)
        gameDisplay.blit(TextSurf, TextRect)


        smaText = pygame.font.Font("freesansbold.ttf", 15)
        TextSurf, TextRect = text_objects("<To start a new game,", smaText)
        TextRect.center = (400, line[0])
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("go back to menu>", smaText)
        TextRect.center = (400, line[0]+17)
        gameDisplay.blit(TextSurf, TextRect)


        button("", column[0], line[0], 60, 60, zm2[0], zm2[0], pas)
        button("", column[1], line[0], 60, 60, zm2[1], zm2[1], pas)
        button("", column[2], line[0], 60, 60, zm2[2], zm2[2], pas)
        button("", column[3], line[0], 60, 60, zm2[3], zm2[3], pas)

        button("", column[0], line[1], 60, 60, zm1[0], zm1[0], pas)
        button("", column[1], line[1], 60, 60, zm1[1], zm1[1], pas)
        button("", column[2], line[1], 60, 60, zm1[2], zm1[2], pas)
        button("", column[3], line[1], 60, 60, zm1[3], zm1[3], pas)
        button("", column[0], line[2], 60, 60, zm1[4], zm1[4], pas)
        button("", column[1], line[2], 60, 60, zm1[5], zm1[5], pas)
        button("", column[2], line[2], 60, 60, zm1[6], zm1[6], pas)
        button("", column[3], line[2], 60, 60, zm1[7], zm1[7], pas)
        button("", column[0], line[3], 60, 60, zm1[8], zm1[8], pas)
        button("", column[1], line[3], 60, 60, zm1[9], zm1[9], pas)
        button("", column[2], line[3], 60, 60, zm1[10], zm1[10], pas)
        button("", column[3], line[3], 60, 60, zm1[11], zm1[11], pas)
        button("", column[0], line[4], 60, 60, zm1[12], zm1[12], pas)
        button("", column[1], line[4], 60, 60, zm1[13], zm1[13], pas)
        button("", column[2], line[4], 60, 60, zm1[14], zm1[14], pas)
        button("", column[3], line[4], 60, 60, zm1[15], zm1[15], pas)
        button("", column[0], line[5], 60, 60, zm1[16], zm1[16], pas)
        button("", column[1], line[5], 60, 60, zm1[17], zm1[17], pas)
        button("", column[2], line[5], 60, 60, zm1[18], zm1[18], pas)
        button("", column[3], line[5], 60, 60, zm1[19], zm1[19], pas)
        button("", column[0], line[6], 60, 60, zm1[20], zm1[20], pas)
        button("", column[1], line[6], 60, 60, zm1[21], zm1[21], pas)
        button("", column[2], line[6], 60, 60, zm1[22], zm1[22], pas)
        button("", column[3], line[6], 60, 60, zm1[23], zm1[23], pas)
        button("", column[0], line[7], 60, 60, zm1[24], zm1[24], pas)
        button("", column[1], line[7], 60, 60, zm1[25], zm1[25], pas)
        button("", column[2], line[7], 60, 60, zm1[26], zm1[26], pas)
        button("", column[3], line[7], 60, 60, zm1[27], zm1[27], pas)
        button("", column[0], line[8], 60, 60, zm1[28], zm1[28], pas)
        button("", column[1], line[8], 60, 60, zm1[29], zm1[29], pas)
        button("", column[2], line[8], 60, 60, zm1[30], zm1[30], pas)
        button("", column[3], line[8], 60, 60, zm1[31], zm1[31], pas)

        button("", column[0], 710, 60, 60, zm[0], bright_grey, colorreset1)
        button("", column[1], 710, 60, 60, zm[1], bright_grey, colorreset2)
        button("", column[2], 710, 60, 60, zm[2], bright_grey, colorreset3)
        button("", column[3], 710, 60, 60, zm[3], bright_grey, colorreset4)

        button("", 410, 150, 60, 60, green, bright_green, color1)
        button("", 410, 241, 60, 60, blue, bright_blue, color2)
        button("", 410, 332, 60, 60, red, bright_red, color3)
        button("", 410, 423, 60, 60, yellow, bright_yellow, color4)
        button("", 410, 514, 60, 60, pink, bright_pink, color5)
        button("", 410, 605, 60, 60, orange, bright_orange, color6)

        button("", column[4], line[1] + 17.5, 25, 25, w[0], w[0], pas)
        button("", column[5], line[1] + 17.5, 25, 25, w[1], w[1], pas)
        button("", column[6], line[1] + 17.5, 25, 25, w[2], w[2], pas)
        button("", column[7], line[1] + 17.5, 25, 25, w[3], w[3], pas)
        button("", column[4], line[2] + 17.5, 25, 25, w[4], w[4], pas)
        button("", column[5], line[2] + 17.5, 25, 25, w[5], w[5], pas)
        button("", column[6], line[2] + 17.5, 25, 25, w[6], w[6], pas)
        button("", column[7], line[2] + 17.5, 25, 25, w[7], w[7], pas)
        button("", column[4], line[3] + 17.5, 25, 25, w[8], w[8], pas)
        button("", column[5], line[3] + 17.5, 25, 25, w[9], w[9], pas)
        button("", column[6], line[3] + 17.5, 25, 25, w[10], w[10], pas)
        button("", column[7], line[3] + 17.5, 25, 25, w[11], w[11], pas)
        button("", column[4], line[4] + 17.5, 25, 25, w[12], w[12], pas)
        button("", column[5], line[4] + 17.5, 25, 25, w[13], w[13], pas)
        button("", column[6], line[4] + 17.5, 25, 25, w[14], w[14], pas)
        button("", column[7], line[4] + 17.5, 25, 25, w[15], w[15], pas)
        button("", column[4], line[5] + 17.5, 25, 25, w[16], w[16], pas)
        button("", column[5], line[5] + 17.5, 25, 25, w[17], w[17], pas)
        button("", column[6], line[5] + 17.5, 25, 25, w[18], w[18], pas)
        button("", column[7], line[5] + 17.5, 25, 25, w[19], w[19], pas)
        button("", column[4], line[6] + 17.5, 25, 25, w[20], w[20], pas)
        button("", column[5], line[6] + 17.5, 25, 25, w[21], w[21], pas)
        button("", column[6], line[6] + 17.5, 25, 25, w[22], w[22], pas)
        button("", column[7], line[6] + 17.5, 25, 25, w[23], w[23], pas)
        button("", column[4], line[7] + 17.5, 25, 25, w[24], w[24], pas)
        button("", column[5], line[7] + 17.5, 25, 25, w[25], w[25], pas)
        button("", column[6], line[7] + 17.5, 25, 25, w[26], w[26], pas)
        button("", column[7], line[7] + 17.5, 25, 25, w[27], w[27], pas)
        button("", column[4], line[8] + 17.5, 25, 25, w[28], w[28], pas)
        button("", column[5], line[8] + 17.5, 25, 25, w[29], w[29], pas)
        button("", column[6], line[8] + 17.5, 25, 25, w[30], w[30], pas)
        button("", column[7], line[8] + 17.5, 25, 25, w[31], w[31], pas)


        button("check", 305, 710, 60, 60, bright_grey, grey, check)
        button("menu", 390, 710, 100, 60, red, bright_red, menu)

        pygame.display.update()
        clock.tick(15)


menu()
instruction()
game()
pygame.quit()
quit()