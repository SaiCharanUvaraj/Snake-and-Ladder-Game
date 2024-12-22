#naming the pieces with the name "Yellow" and "blue"
player1="Yellow"
player2="blue"
players=[player1,player2]

#Impoting and initialising pygame module
import pygame
pygame.init()

#Loading the background sounds
from pygame import mixer
mixer.init() 
opening_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\Snakes and ladders game openning sound.mp3")
winning_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\winning sound.wav")
game_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\Snakes and ladders game sound.mp3")
clicking_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\mouse clicking sound.mp3")
misclicking_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\mouse misclicking sound.wav")
snake_attack_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\negative result sound.wav")
ladder_rise_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\positive result sound.wav")
notification_sound=mixer.Sound("D:\\Snake and Ladder\\audios\\notification sound.wav")

#Initialising the colours
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
dark_gray=(100,100,100)
light_gray=(130,130,130)
white=(255,255,255)
yellow=(255,255,0)
orange=(255,155,0)
blue=(0,0,255)

#Creating a display screen
screen_length,screen_width=1000,700
screen=pygame.display.set_mode((screen_length,screen_width))
pygame.display.set_caption("Snakes and ladders")

#printing a blank screen for a second
screen.fill(black)
pygame.display.update()
pygame.time.delay(1000)

#Printing the title screen with background sound
screen.fill(red)
image=pygame.image.load("D:\\Snake and Ladder\\images\\snakes and ladders game openning picture.webp")
image = pygame.transform.scale(image,(900,600))
screen.blit(image,(50,50))
pygame.display.update()
disturbance="no"
opening_sound.play()
while disturbance=="no":
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            disturbance="yes"
            opening_sound.stop()
            clicking_sound.play()
        if event.type==pygame.KEYDOWN:
            disturbance="yes"
            opening_sound.stop()
            clicking_sound.play()
        if event.type==pygame.QUIT:
            pygame.quit()
    if pygame.mixer.get_busy()==False:
        opening_sound.play()

#printing a blank screen for a second
screen.fill(black)
pygame.display.update()
pygame.time.delay(50)

#creating snake and ladder text numbers 
step=0
initial_numbers=[100,81,80,61,60,41,40,21,20,1]
numbers_text=[]
for initial_number in initial_numbers:
    if initial_number in [100,80,60,40,20]:
        final_number=initial_number+(-9)-1
        step=-1
    if initial_number in [81,61,41,21,1]:
        final_number=initial_number+(+9)+1
        step=+1
    for number in range(initial_number,final_number,step):
        numbers_text=numbers_text+["  "+str(number)]

#creating the position points for the number text ,player1 text and player2 text in the grid boxes
number_text_points,player1_text_points,player2_text_points=[],[],[] #list of points of number texts,player1 text,player2 text
number_number_text_points_dict={}   #dict of number text with respective number text points
number_text_player1_points_dict={}  #dict of number text points with respective player1 text points
number_text_player2_points_dict={}  #dict of number text points with respective player2 text points
for p in range(0,700,70):
    for q in range(0,700,70):
        number_text_points=number_text_points+[(q,p)]
        player1_text_points=player1_text_points+[((q+50),p)]
        player2_text_points=player2_text_points+[((q+50),(p+50))]
        number_text_player1_points_dict[(q,p)]=(q+50,p)
        number_text_player2_points_dict[(q,p)]=(q+50,p+50)
for a in range(0,100,1):
    number_number_text_points_dict[numbers_text[a]]=number_text_points[a]

#finding the points under dice button
dice_points=[]
x_dice,y_dice=720,70
dice_len,dice_wid=70,70
for x in range(x_dice,x_dice+dice_len+1,1):
    for y in range(y_dice,y_dice+dice_wid+1,1):
        dice_points=dice_points+[(x,y)]

#defining the player1 and player2 piece text
font=pygame.font.SysFont("Times new Roman",20)
player1_gray=font.render("X",True,yellow,light_gray) #player1_black : small "x" for placing in the game board
player1_black=font.render("x",True,yellow)           #player1_gray  : Capital "X" for placing in the pieces box
player2_gray=font.render("X",True,blue,light_gray) #player2_black : small "x" for placing in the game board
player2_black=font.render("x",True,blue)           #player2_gray  : Capital "X" for placing in the pieces box

#for designing yes and no buttons
font=pygame.font.SysFont("Times new Roman",20)
yes_button=font.render("Yes",True,green,light_gray)
no_button=font.render("No",True,red,light_gray)

#finding the points under the yes button
yes_button_points=[]
for a in range(750,800):
    for b in range(560,590):
        yes_button_points=yes_button_points+[(a,b)]

#finding the points under the no button
no_button_points=[]
for a in range(900,950):
    for b in range(560,590):
        no_button_points=no_button_points+[(a,b)]

#finding the points under the restart button
restart_button_points=[]
for a in range(900,1000):
    for b in range(0,51):
        restart_button_points=restart_button_points+[(a,b)]

#function for snake positions
def snakes():
    #loading the snake image and placing it in the board   
    image=pygame.image.load("D:\\Snake and Ladder\\images\\snake image.png")
        #for 1st snake
    screen.blit(image,(80,5)) #at 99
        #for 2nd snake
    snake2=pygame.transform.rotate(image,270)
    snake2=pygame.transform.scale(snake2,(290,290))
    screen.blit(snake2,(350,150)) #at 72
        #for snake 3
    snake3=pygame.transform.rotate(image,320)
    snake3=pygame.transform.scale(snake3,(400,400))
    screen.blit(snake3,(150,300)) #at56
        #for snake 4
    snake4=pygame.transform.rotate(image,260)
    snake4=pygame.transform.scale(snake4,(300,300))
    screen.blit(snake4,(330,0)) #at92
        #for snake 5
    snake5=pygame.transform.rotate(image,270)
    snake5=pygame.transform.scale(snake5,(250,250))
    screen.blit(snake5,(70,70))#85
        #for snake 6
    snake6=pygame.transform.rotate(image,290)
    snake6=pygame.transform.scale(snake6,(300,200))
    screen.blit(snake6,(0,420))#38
        #snke 7
    snake7=pygame.transform.rotate(image,300)
    snake7=pygame.transform.scale(snake7,(320,300))
    screen.blit(snake7,(500,350)) #at50

#function for ladders positions
def ladders():
    #loading the ladder image
    ladder=pygame.image.load("D:\\Snake and Ladder\\images\\ladder image.png")
        #for ladder1
    ladder1=pygame.transform.scale(ladder,(190,420))
    screen.blit(ladder1,(130,0)) #at44
        #for ladder2
    ladder2=pygame.transform.scale(ladder,(180,420))
    screen.blit(ladder2,(490,70)) #at32
        #for ladder3
    ladder3=pygame.transform.rotate(ladder,25)
    ladder3=pygame.transform.scale(ladder3,(300,300))
    screen.blit(ladder3,(-20,370)) #at18
        #for ladder4
    ladder4=pygame.transform.rotate(ladder,190)
    ladder4=pygame.transform.scale(ladder4,(200,300))
    screen.blit(ladder4,(300,400)) #at7

#function for default game screen
def default_game_screen():
    
    #filling the screen initially by black colour
    screen.fill(black)

    #creating a small dice box at the right corner
    pygame.draw.rect(screen,dark_gray,(700,0,300,210))

    #designing the dice button 
    font=pygame.font.SysFont("Times new Roman",30)
    text_surface=font.render("  Die",True,black,white)
    x_dice,y_dice=720,70
    dice_len,dice_wid=75,70
    pygame.draw.rect(screen,white,(x_dice,y_dice,dice_len,dice_wid))
    screen.blit(text_surface,(720,88)) 
    pygame.draw.rect(screen,black,(x_dice,y_dice,dice_len,dice_wid),5)

    #designing the restart button
    pygame.draw.rect(screen,white,(900,0,100,50))
    font=pygame.font.SysFont("Times new Roman",26)
    text_surface=font.render("  Restart",True,black,white)
    screen.blit(text_surface,(900,10))
    pygame.draw.rect(screen,black,(900,0,100,50),5)
    
    #creating a pieces box to show pieces and their turns
    pygame.draw.rect(screen,light_gray,(700,210,300,140))

    #placing the pieces for the piece box and title for pieces box in i/o box
    font=pygame.font.SysFont("Times new Roman",30)
    text_surface=font.render(" Pieces",True,black,light_gray) 
    screen.blit(text_surface,(700,210))
    screen.blit(player1_gray,(800,280))
    screen.blit(player2_gray,(900,280))

    #for creating event message box 
    pygame.draw.rect(screen,dark_gray,(700,350,300,70))

    #for creating a notification box
    pygame.draw.rect(screen,light_gray,(700,420,300,280))
    
    #loading the ladder image and placing it in the board
    ladders()

    #loading the snake image and placing it in the board   
    snakes()
        
    #for adding the number text according to the positions
    for a in range(0,100,1):
        text=numbers_text[a]
        position=number_text_points[a]
        font=pygame.font.SysFont("Times new Roman",15)
        text_surface=font.render(text,True,green)
        text_surface.set_alpha(500)
        screen.blit(text_surface,position)

    #for drawing 10*10 grid lines on the board
    for a in range(0,701,70):
        pygame.draw.line(screen,red,(0,a),(700,a),3)
        pygame.draw.line(screen,red,(a,0),(a,700),3)

#calling the default game screen function
default_game_screen()

#updating the screen
pygame.display.update()

#game function
def game():
    
    #pre initialising the variables
    global player1_black,player2_black
    pre_player1_text_point=pre_player2_text_point=()
    location1=location2=0
    entry1=entry2=""
    player_no=-1
    dice_outcome=0
    game=game_continue=game_close=game_replay=continued_game=game_restart=""

    #for background music
    game_sound.play()
    
    #game loop
    while True:
        
        #finding the active player
        if continued_game!="yes":
            if dice_outcome!=1:
                if player_no==1:
                    player_no=-1
                player_no=player_no+1
                active_player=players[player_no]
        if continued_game=="yes":
            continued_game=""
        
        #for background sound
            if pygame.mixer.get_busy()==False:
                game_sound.play()

        #for highligting the current player
        font=pygame.font.SysFont("Times new Roman",40)
        if active_player==player1:
            player1_gray=font.render("X",True,yellow,light_gray)
            screen.blit(player1_gray,(800,280))  
        if active_player==player2:
            font=pygame.font.SysFont("Times new Roman",40)
            player2_gray=font.render("X",True,blue,light_gray)
            screen.blit(player2_gray,(900,280))
        pygame.display.update()

        #loop for getting inputs from keyboard and mouse
        mouse_point=()
        dice_roll=""
        while True:

            #for background sound
            if pygame.mixer.get_busy()==False:
                game_sound.play()

            #for getting the events
            for event in pygame.event.get():
                
                #for mouse events
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_point=pygame.mouse.get_pos()
                    
                    #for getting response for dice
                    if mouse_point in dice_points:
                        clicking_sound.play()
                        dice_roll="yes"
                        break
                    
                    #for getting response for restart
                    elif mouse_point in restart_button_points:
                        clicking_sound.play()
                        pygame.time.delay(700)
                        pygame.mixer.pause()
                        notification_sound.play()
                        text="      Do you want to restart?"
                        font=pygame.font.SysFont("Times new Roman",25)
                        notification=font.render(text,True,white,light_gray)
                        screen.blit(notification,(700,490))
                        screen.blit(yes_button,(750,560))
                        screen.blit(no_button,(900,560))
                        for a in range(0,701,70):
                            pygame.draw.line(screen,red,(0,a),(700,a),3)
                            pygame.draw.line(screen,red,(a,0),(a,700),3)
                        pygame.display.update()

                        #to accept mouse inputs from the user for the notification     
                        mouse_point=()
                        game_continue=game_restart=""
                        while True:
                            for event in pygame.event.get():
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    mouse_point=pygame.mouse.get_pos()
                                    if mouse_point in yes_button_points:
                                        clicking_sound.play()
                                        game_restart="yes"
                                        pygame.draw.rect(screen,light_gray,(700,420,300,280))
                                        break
                                    elif mouse_point in no_button_points:
                                        clicking_sound.play()
                                        game_continue="yes"
                                        pygame.draw.rect(screen,light_gray,(700,420,300,280))
                                        pygame.mixer.unpause()
                                        break
                                    else:
                                        misclicking_sound.play()
                                if event.type==pygame.KEYDOWN:
                                    misclicking_sound.play()
                            if mouse_point in yes_button_points or mouse_point in no_button_points:
                                break

                    #for misclicking sound
                    else:
                        misclicking_sound.play()

                #for quit button events
                if event.type==pygame.QUIT:
                    clicking_sound.play()
                    pygame.time.delay(700)
                    pygame.mixer.pause()
                    notification_sound.play()
                    text="   Do you want to continue?"
                    font=pygame.font.SysFont("Times new Roman",25)
                    notification=font.render(text,True,white,light_gray)
                    screen.blit(notification,(700,490))
                    screen.blit(yes_button,(750,560))
                    screen.blit(no_button,(900,560))
                    for a in range(0,701,70):
                        pygame.draw.line(screen,red,(0,a),(700,a),3)
                        pygame.draw.line(screen,red,(a,0),(a,700),3)
                    pygame.display.update()

                    #to accept mouse inputs from the user for the notification     
                    mouse_point=()
                    game_continue=game_close=""
                    while True:
                        for event in pygame.event.get():
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                mouse_point=pygame.mouse.get_pos()
                                if mouse_point in yes_button_points:
                                    clicking_sound.play()
                                    game_continue="yes"
                                    pygame.draw.rect(screen,light_gray,(700,420,300,280))
                                    pygame.mixer.unpause()
                                    break
                                elif mouse_point in no_button_points:
                                    clicking_sound.play()
                                    game_close="yes"
                                    break
                                else:
                                    misclicking_sound.play()
                            if event.type==pygame.KEYDOWN:
                                misclicking_sound.play()
                        if mouse_point in yes_button_points or mouse_point in no_button_points:
                            break

                #for keyboard events
                if event.type==pygame.KEYDOWN:
                    misclicking_sound.play()
                    
            if mouse_point in dice_points or game_continue=="yes"or game_close=="yes" or game_restart=="yes":
                break
            
        if game_continue=="yes":
            game_continue=""
            continued_game="yes"
            continue
        if game_restart=="yes":
            return "restart"
        if game_close=="yes":
            return "close"

        #rolls a die through random function
        if dice_roll=="yes":
            import random
            dice_outcome=random.randint(1,6)

            #printing the die image next to the dice button  showing the output   
            x_dice,y_dice=910,70
            dice_len,dice_wid=70,70
            pygame.draw.rect(screen,white,(x_dice,y_dice,dice_len,dice_wid))
            pygame.draw.rect(screen,black,(x_dice,y_dice,dice_len,dice_wid),3)
            #for outcome 1
            if dice_outcome==1:
                pygame.draw.circle(screen,red,((x_dice+x_dice+dice_len)/2,(y_dice+y_dice+dice_wid)/2),6)
                if active_player==player1:
                    entry1="yes"
                if active_player==player2:
                    entry2="yes"
            #for outcome 2
            if dice_outcome==2:
                pygame.draw.circle(screen,black,((x_dice+x_dice+dice_len)/2,y_dice+20),5)
                pygame.draw.circle(screen,black,((x_dice+x_dice+dice_len)/2,y_dice+dice_wid-20),5)
            #for outcome 3
            if dice_outcome==3:
                pygame.draw.circle(screen,black,(x_dice+20,(y_dice+y_dice+dice_wid)/2),5)
                pygame.draw.circle(screen,black,((x_dice+x_dice+dice_len)/2,(y_dice+y_dice+dice_wid)/2),5)
                pygame.draw.circle(screen,black,(x_dice+dice_len-20,(y_dice+y_dice+dice_wid)/2),5)
            #for outcome 4
            if dice_outcome==4:
                pygame.draw.circle(screen,black,(x_dice+20,y_dice+20),5)
                pygame.draw.circle(screen,black,(x_dice+dice_len-20,y_dice+dice_wid-20),5)
                pygame.draw.circle(screen,black,(x_dice+20,y_dice+dice_wid-20),5)
                pygame.draw.circle(screen,black,(x_dice+dice_len-20,y_dice+20),5)
            #for outcome 5
            if dice_outcome==5:
                pygame.draw.circle(screen,black,((x_dice+x_dice+dice_len)/2,(y_dice+y_dice+dice_wid)/2),5)
                pygame.draw.circle(screen,black,(x_dice+20,y_dice+20),5)
                pygame.draw.circle(screen,black,(x_dice+dice_len-20,y_dice+dice_wid-20),5)
                pygame.draw.circle(screen,black,(x_dice+20,y_dice+dice_wid-20),5)
                pygame.draw.circle(screen,black,(x_dice+dice_len-20,y_dice+20),5)
            #for outcome 6
            if dice_outcome==6:
                pygame.draw.circle(screen,black,((x_dice+x_dice+dice_len)/2,y_dice+20),5)
                pygame.draw.circle(screen,black,((x_dice+x_dice+dice_len)/2,y_dice+dice_wid-20),5)
                pygame.draw.circle(screen,black,(x_dice+20,y_dice+20),5)
                pygame.draw.circle(screen,black,(x_dice+dice_len-20,y_dice+dice_wid-20),5)
                pygame.draw.circle(screen,black,(x_dice+20,y_dice+dice_wid-20),5)
                pygame.draw.circle(screen,black,(x_dice+dice_len-20,y_dice+20),5)

        #for updating the screen
        pygame.display.update()

        #for delay
        pygame.time.delay(3000)
        
        #for changing the location of the pieces
        if active_player==player1:

            #for checking the piece has entered the board or not
            if entry1=="yes":

                #adding the current location with outcome of the die
                location1=location1+dice_outcome

                #for restricting the overflow of the value of the location
                if location1>100:
                    location1=location1-dice_outcome

                #finding the respective number text point for the the location  
                str_location1="  "+str(location1)
                if str_location1 in number_number_text_points_dict:
                    wanted_number_text_point=number_number_text_points_dict[str_location1]

                #finding the respective position point for player1_text surface
                if wanted_number_text_point in number_text_player1_points_dict:

                    #erasing the previous player1_text
                    if pre_player1_text_point!=():
                        pygame.draw.rect(screen,black,pre_player1_text_point+(20,30))
                    wanted_player1_text_point=number_text_player1_points_dict[wanted_number_text_point]

                    #adding the text in the position
                    screen.blit(player1_black,wanted_player1_text_point)
                    
                    pre_player1_text_point=wanted_player1_text_point
                    
        if active_player==player2:

            #for checking the piece has entered the board or not
            if entry2=="yes":

                #adding the current location with outcome of the die
                location2=location2+dice_outcome

                #for restricting the overflow of the value of the location
                if location2>100:
                    location2=location2-dice_outcome

                #finding the respective number text point for the the location  
                str_location2="  "+str(location2)
                if str_location2 in number_number_text_points_dict:
                    wanted_number_text_point=number_number_text_points_dict[str_location2]

                #finding the respective position point for player2_text surface
                if wanted_number_text_point in number_text_player2_points_dict:

                    #erasing the previous player2_text
                    if pre_player2_text_point!=():
                        pygame.draw.rect(screen,black,pre_player2_text_point+(20,30))
                    wanted_player2_text_point=number_text_player2_points_dict[wanted_number_text_point]
                
                    #adding the text in the position
                    screen.blit(player2_black,wanted_player2_text_point)

                    pre_player2_text_point=wanted_player2_text_point
                
        #for restoring the design of the piece box
                    #"piece" heading for the box
        pygame.draw.rect(screen,light_gray,(700,210,300,140))
        font=pygame.font.SysFont("Times new Roman",30)
        text_surface=font.render(" Pieces",True,black,light_gray) 
        screen.blit(text_surface,(700,210))
                    #player1(yellow) 
        font=pygame.font.SysFont("Times new Roman",20)
        player1_gray=font.render("X",True,yellow,light_gray)
        screen.blit(player1_gray,(800,280))
                    #player2(blue)
        font=pygame.font.SysFont("Times new Roman",20)
        player2_gray=font.render("X",True,blue,light_gray)
        screen.blit(player2_gray,(900,280))

        #for re-drawing 10*10 grid lines on the board
        for a in range(0,701,70):
            pygame.draw.line(screen,red,(0,a),(700,a),3)
            pygame.draw.line(screen,red,(a,0),(a,700),3)

        #updating the screen
        pygame.display.update()

        #for creating the snake attack text
        font=pygame.font.SysFont("Times new Roman",40)
        text="   Snake attack!"
        snake_attack_message=font.render(text,True,red,dark_gray)

        #snake attack effects
        if location1 in [99,72,92,85,56,38,50] or location2 in [99,72,92,85,56,38,50]:
            pygame.time.delay(1000)
            pygame.mixer.pause()
            snake_attack_sound.play()
            screen.blit(snake_attack_message,(710,350))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.draw.rect(screen,dark_gray,(700,350,300,70))
            pygame.mixer.unpause()

        #decreasing the location if there is a snake attack
        if active_player==player1:
            if location1==99:
                location1=54
            elif location1==72:
                location1=35
            elif location1==92:
                location1==65
            elif location1==85:
                location1=59
            elif location1==56:
                location1=6
            elif location1==38:
                location1=19
            elif location1==50:
                location1=10
            else:
                pass
        if active_player==player2:
            if location2==99:
                location2=54
            elif location2==72:
                location2=35
            elif location2==92:
                location2==65
            elif location2==85:
                location2=59
            elif location2==56:
                location2=6
            elif location2==38:
                location2=19
            elif location2==50:
                location2=10
            else:
                pass

        #for creating the rise through ladder text
        font=pygame.font.SysFont("Times new Roman",30)
        text="  Rise through ladder!"
        ladder_rise_message=font.render(text,True,green,dark_gray)

        #ladder rise effects
        if location1 in [44,32,18,7] or location2 in [44,32,18,7]:
            pygame.time.delay(1000)
            pygame.mixer.pause()
            ladder_rise_sound.play()
            screen.blit(ladder_rise_message,(710,350))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.draw.rect(screen,dark_gray,(700,350,300,70))
            pygame.mixer.unpause()

        #increasing the location if there is a ladder rise
        if active_player==player1:
            if location1==44:
                location1=98
            elif location1==32:
                location1=88
            elif location1==18:
                location1==40
            elif location1==7:
                location1=36
            else:
                pass
        if active_player==player2:
            if location2==44:
                location2=98
            elif location2==32:
                location2=88
            elif location2==18:
                location2==40
            elif location2==7:
                location2=35
            else:
                pass

        #updating the screen
        pygame.display.update()

        #for changing the location if there was a snake attack or a ladder rise
        if active_player==player1:

            #for checking the piece has entered the board or not
            if entry1=="yes":
                
                #finding the respective number text point for the the location  
                str_location1="  "+str(location1)
                if str_location1 in number_number_text_points_dict:
                    wanted_number_text_point=number_number_text_points_dict[str_location1]

                #finding the respective position point for player1_text surface
                if wanted_number_text_point in number_text_player1_points_dict:

                    #erasing the previous player1_text
                    if pre_player1_text_point!=():
                        pygame.draw.rect(screen,black,pre_player1_text_point+(20,30))
                    wanted_player1_text_point=number_text_player1_points_dict[wanted_number_text_point]

                    #adding the text in the position
                    screen.blit(player1_black,wanted_player1_text_point)

                    pre_player1_text_point=wanted_player1_text_point
                    
        if active_player==player2:

            #for checking the piece has entered the board or not
            if entry2=="yes":

                #finding the respective number text point for the the location  
                str_location2="  "+str(location2)
                if str_location2 in number_number_text_points_dict:
                    wanted_number_text_point=number_number_text_points_dict[str_location2]

                #finding the respective position point for player2_text surface
                if wanted_number_text_point in number_text_player2_points_dict:

                    #erasing the previous player2_text
                    if pre_player2_text_point!=():
                        pygame.draw.rect(screen,black,pre_player2_text_point+(20,30))
                    wanted_player2_text_point=number_text_player2_points_dict[wanted_number_text_point]
                
                    #adding the text in the position
                    screen.blit(player2_black,wanted_player2_text_point)

                    pre_player2_text_point=wanted_player2_text_point
                
        #for restoring the design of the piece box
                    #"piece" heading for the box
        pygame.draw.rect(screen,light_gray,(700,210,300,140))
        font=pygame.font.SysFont("Times new Roman",30)
        text_surface=font.render(" Pieces",True,black,light_gray) 
        screen.blit(text_surface,(700,210))
                    #player1(yellow) 
        font=pygame.font.SysFont("Times new Roman",20)
        player1_gray=font.render("X",True,yellow,light_gray)
        player1_black=font.render("x",True,yellow,black)
        screen.blit(player1_gray,(800,280))
                    #player2(orange)
        font=pygame.font.SysFont("Times new Roman",20)
        player2_gray=font.render("X",True,blue,light_gray)
        player2_black=font.render("x",True,blue,black)
        screen.blit(player2_gray,(900,280))

        #for re-drawing 10*10 grid lines on the board
        for a in range(0,701,70):
            pygame.draw.line(screen,red,(0,a),(700,a),3)
            pygame.draw.line(screen,red,(a,0),(a,700),3)
        
        #for erasing the die image
        pygame.draw.rect(screen,dark_gray,(x_dice,y_dice,dice_len,dice_wid))
        
        #updating the screen
        pygame.display.update()

        #for displaying the  winning message for the players
        if active_player==player1:

            #checking the player1 location is 100
            if location1==100:

                #playing the winning sound
                game_sound.stop()
                winning_sound.play()
                
                #for time delay
                pygame.time.delay(500)
                
                #printing the winning message 
                text="   "+player1+"  won!"
                Font=pygame.font.SysFont("Times new Roman",40)
                winning_message=Font.render(text,True,yellow,dark_gray)
                screen.blit(winning_message,(710,350))
                game="over"

        #for displaying the  winning message for the players
        if active_player==player2:

            #checking the player1 location is 100
            if location2==100:

                #playing the winning sound
                game_sound.stop()
                winning_sound.play()
                
                #for time delay
                pygame.time.delay(500)
                
                #printing the winning message
                text="   "+player2+"  won !"
                Font=pygame.font.SysFont("Times new Roman",40)
                winning_message=Font.render(text,True,blue,dark_gray)
                screen.blit(winning_message,(710,350))
                game="over"

        #updating the screen
        pygame.display.update()

        #for notification and inputing the decision
        if game=="over":

            #for time delay 
            pygame.time.delay(4000)

            #playing notification sound
            notification_sound.play()

            #creating the notification "Do you want to play again? with yes and no buttons
            text=" Do you want to play again?"
            font=pygame.font.SysFont("Times new Roman",25)
            notification=font.render(text,True,white,light_gray)
            screen.blit(notification,(700,490))
            screen.blit(yes_button,(750,560))
            screen.blit(no_button,(900,560))
            pygame.display.update()

            #redrawing the erased grid lines 
            for a in range(0,701,70):
                pygame.draw.line(screen,red,(0,a),(700,a),3)
                pygame.draw.line(screen,red,(a,0),(a,700),3)
                
            pygame.display.update()
            
            #to accept mouse inputs from the user         
            mouse_point=()
            game_replay=game_close=""
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        mouse_point=pygame.mouse.get_pos()
                        if mouse_point in yes_button_points:
                            clicking_sound.play()
                            game_replay="yes"
                            break
                        elif mouse_point in no_button_points:
                            clicking_sound.play()
                            game_close="yes"
                            break
                        else:
                            misclicking_sound.play()
                    if event.type==pygame.KEYDOWN:
                        misclicking_sound.play()
                if mouse_point in yes_button_points or mouse_point in no_button_points:
                    break
            #returning the function with appropriate messages
            if game_replay=="yes":
                return "replay"
            if game_close=="yes":
                return "close"

        #loading the ladder image and placing it in the board   
        ladders()
        
        #loading the snake image and placing it in the board   
        snakes()

        #for re-adding the number text according to the positions
        for a in range(0,100,1):
            text=numbers_text[a]
            position=number_text_points[a]
            font=pygame.font.SysFont("Times new Roman",15)
            text_surface=font.render(text,True,green)
            text_surface.set_alpha(500)
            screen.blit(text_surface,position)

        #for re-drawing 10*10 grid lines on the board
        for a in range(0,701,70):
            pygame.draw.line(screen,red,(0,a),(700,a),3)
            pygame.draw.line(screen,red,(a,0),(a,700),3)

        #updating the screen
        pygame.display.update()

#loop for calling the game() function        
while True:

    #calling the game() function
    output=game()

    #for restart
    if output=="restart":
        default_game_screen()
        continue

    #for replay
    if output=="replay":
        default_game_screen()
        continue

    #for closing the game
    if output=="close":
        pygame.quit()
        break










