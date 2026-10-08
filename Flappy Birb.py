import pygame
from sys import exit
from random import randint

#IMPORTANT STUFF
pygame.init()
screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption('Flappy Bird: 26BEC0428')
clock = pygame.time.Clock()

##FONTS
font_1 = pygame.font.Font('Fonts/Pixeltype.ttf', 200)
font_2 = pygame.font.Font('Fonts/Pixeltype.ttf', 100)
font_3 = pygame.font.Font('Fonts/Pixeltype.ttf', 70)
font_4 = pygame.font.Font('Fonts/Pixeltype.ttf', 50)

#sfxs
sfx_jump = pygame.mixer.Sound('Audio/jump.mp3')
sfx_jump.set_volume(0.07)
sfx_death = pygame.mixer.Sound('Audio/DEATH.mp3')
sfx_death.set_volume(0.85)

#MISC GAME VARIABLES
##Values

player_gravity = 1    #CHANGE TO MAKE GAME WAY MORE HECTIC
player_sprite_angle = 0
player_accel = 0

score = 0
Pipe_2 = 0

Pipe_Offset_Height = (150, 100, 75, 50, 25, 0, -25, -50, -75, -100)
Pipe_Offset_Difficulty = (0, 25, 35, 50, 70)


##Text

Remark = 'Hello! To make this, I had to learn pygame from scratch in two days.'
Remark_2 = 'However, this was a very fun experience, and I hope you enjoy!'
Remark_3 = 'Note: No AI was used to make this, nor was any existing code copied...'

NameReg = '''DHRUV SWAMINATHAN: 26BEC0428'''

Start_req = 'Press SPACEBAR to begin'

Game_Over = 'YOU LOSE'
Try_Again = 'RESTART'
Back = 'BACK TO MENU'
Quit = 'QUIT'
    
##FLAGS

###Game Loop Control
Menu_Flag = True
Game_Flag = False
Credit_Flag = False
Back_Flag = False
Quit_Flag = False
Restart_Flag = False
Game_Start_Flag = False
Game_Over_Flag = False

###Pipe Difficulty Control
Pipe_Spawn_Flag = True
Pipe_Spawn_Flag_2 = False
Pipe_2_Move_Flag = False

###Music Flags
Game_Over_Music_Flag = False
Game_Start_Music_Flag = True
Menu_Music_Flag = True

###Misc Flags
Score_Flag = True


#Colours

Dark_Grey = (40,40,40)
Black = (0,0,0)

#TEXTURES, SPRITES AND TEXT:
##BG

screen_background_sky = pygame.image.load('Graphics/Sky.png')
screen_background_ground = pygame.image.load('Graphics/ground.png')

##Player

player_sprite_rest = pygame.image.load('Graphics/Flappy bird/birb.png').convert_alpha()

##Obstales

obstacle_pipe_grnd = pygame.transform.flip(pygame.image.load('Graphics/Pipe.png').convert_alpha(), False, True)
obstacle_pipe_clng = pygame.image.load('Graphics/Pipe.png').convert_alpha()

##TEXTS
###MENU

menu_text_title = font_1.render('FLAPPY BIRD', False, 'Red')
menu_text_start = font_2.render('BEGIN', False, 'Black')
menu_text_credits = font_2.render('CREDITS', False, 'Black')

###CREDITS

credits_text_name = font_2.render(NameReg, False, 'Black')
credits_text_remarks_1 = font_3.render(Remark, False, 'White')
credits_text_remarks_2 = font_3.render(Remark_2, False, 'White')
credits_text_remarks_3 = font_3.render(Remark_3, False, 'White')
credits_text_back = font_4.render('Back', False, 'Green')

###GAME START AND GAME OVER

game_text_start = font_3.render(Start_req, False, 'Red')
Game_Over_text_Title = font_1.render(Game_Over, False, 'Red')
Game_Over_text_Back = font_2.render(Back, False, 'White')
Game_Over_text_Restart = font_2.render(Try_Again, False, 'White')
Game_Over_text_Quit = font_2.render(Quit, False, 'White')

#RECTANGLES

##Ground

ground_rect_grnd = screen_background_ground.get_rect(center = (700, 800))
ground_rect_clng = screen_background_ground.get_rect(center = (700, 0))
ground_rect_grnd_2 = screen_background_ground.get_rect(topleft = (1401, 700))
ground_rect_clng_2 = screen_background_ground.get_rect(topleft = (1401, -100))

##SKY

sky_rect_1 = screen_background_sky.get_rect(topleft = (0,100))
sky_rect_2 = screen_background_sky.get_rect(topleft = (1401, 100))

BGRects = (ground_rect_clng,
           ground_rect_clng_2,
           ground_rect_grnd,
           ground_rect_grnd_2,
           sky_rect_1,
           sky_rect_2)

##Player

player_rect = player_sprite_rest.get_rect(center = (200, 400))

##Obstacles

obstacle_pipe_clng_rect = obstacle_pipe_clng.get_rect(topleft = (1531, 0))
obstacle_pipe_grnd_rect = obstacle_pipe_grnd.get_rect(topleft = (1531, 600))

obstacle_pipe_grnd_rect_2 = obstacle_pipe_grnd.get_rect(topleft = (2331, 600))
obstacle_pipe_clng_rect_2 = obstacle_pipe_clng.get_rect(topleft = (2331, 0))


OBSTACLES = (obstacle_pipe_clng_rect,      #HASH TO REMOVE COLLISION
             obstacle_pipe_grnd_rect,
             obstacle_pipe_clng_rect_2,
             obstacle_pipe_grnd_rect_2,
             ground_rect_clng,
             ground_rect_clng_2,
             ground_rect_grnd,
             ground_rect_grnd_2)


menu_text_title_rect = menu_text_title.get_rect(center = (700, 100))
menu_text_start_rect = menu_text_start.get_rect(center = (700, 300))
menu_text_credits_rect = menu_text_credits.get_rect(center = (700, 500))

credits_text_name_rect = credits_text_name.get_rect(center = (700, 100))
credits_text_remarks_rect = credits_text_remarks_1.get_rect(center = (700, 400))
credits_text_remarks_rect_2 = credits_text_remarks_2.get_rect(topleft = credits_text_remarks_rect.bottomleft)
credits_text_remarks_rect_3 = credits_text_remarks_3.get_rect(topleft = credits_text_remarks_rect_2.bottomleft)
credits_text_back_rect = credits_text_back.get_rect(bottomleft = (10, 700))

game_text_start_rect = game_text_start.get_rect(center = (700,400))

game_over_text_title_rect = Game_Over_text_Title.get_rect(center = (700,100))
game_over_text_back_rect = Game_Over_text_Back.get_rect(center = (700, 700))
game_over_text_restart_rect = Game_Over_text_Restart.get_rect(center = (700, 300))
game_over_text_quit_rect = Game_Over_text_Quit.get_rect(center = (700, 500))


#GAME LOOP: MENU

while True:
    
    
    #####################
    
    
    Menu_Music_Flag = True
    Game_Start_Music_Flag = True
    Game_Over_Music_Flag = True
    
    if Menu_Music_Flag:
        pygame.mixer.music.load('Audio/music.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(loops=-1)
        
    while Menu_Flag:           
        
        #BLITS
        ##BG
        screen.blit(screen_background_sky, (0,100))
        screen.blit(screen_background_ground, ground_rect_grnd)
        screen.blit(screen_background_ground, ground_rect_clng)
        screen.blit(player_sprite_rest, player_rect)
        
        #Button Checks
        credit_hover = False
        start_hover = False
        mouse_pos = pygame.mouse.get_pos()
        if menu_text_start_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, 'Grey', menu_text_start_rect)
            start_hover = True
            
        elif menu_text_credits_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, 'Grey', menu_text_credits_rect)
            credit_hover = True
            
        #TEXT
        screen.blit(menu_text_title, menu_text_title_rect)
        screen.blit(menu_text_start, menu_text_start_rect)
        screen.blit(menu_text_credits, menu_text_credits_rect)
        
        #QUIT CONDITION & EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if credit_hover == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Credit_Flag = True
                    Menu_Flag = False
                    
            elif start_hover == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Game_Flag = True
                    Menu_Flag = False
                    pygame.mixer.music.stop()
                    
        pygame.display.update()
        clock.tick(60)
            
        
    #####################
    
    
    pygame.mixer.music.set_volume(0.15)
    
    while Credit_Flag:
        
        screen.fill(Dark_Grey)
        screen.blit(credits_text_name, credits_text_name_rect)
        screen.blit(credits_text_remarks_1, credits_text_remarks_rect)
        screen.blit(credits_text_remarks_2, credits_text_remarks_rect_2)
        screen.blit(credits_text_remarks_3, credits_text_remarks_rect_3)
        screen.blit(credits_text_back, credits_text_back_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        #QUIT CONDITION & EVENT LOOP
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if credits_text_back_rect.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Menu_Flag = True
                    Credit_Flag = False

        
        pygame.display.update()
        clock.tick(60)
                      
        
    ######################
    
    
    while Game_Flag:
         
        if Game_Start_Flag and Game_Start_Music_Flag:
            pygame.mixer.music.load('Audio/Path of Pain.mp3')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(loops=-1)
            Game_Start_Music_Flag = False
            
        #LOOP VARIABLES
        Keys = pygame.key.get_pressed()

        
    
        #SCORE:
        game_score = f"Score = {score}"
        game_text_score = font_3.render(game_score, False, 'Green')
        
        #BLITS
        #BG
        if Game_Start_Flag == False:
            screen.blit(screen_background_sky, (0,100))
            screen.blit(screen_background_ground, ground_rect_grnd)
            screen.blit(screen_background_ground, ground_rect_clng)
            screen.blit(game_text_start, game_text_start_rect)
            screen.blit(game_text_score, (1100, 50))
            screen.blit(game_text_start, game_text_start_rect)
            screen.blit(game_text_score, (1100, 50))
            
            
        #MOVEMENT:
        if Keys[pygame.K_SPACE] and Game_Start_Flag == False:
            Game_Start_Flag = True
            
        if Game_Start_Flag:
            
            if Pipe_Spawn_Flag:
                
                Pipe_Offset_Value = Pipe_Offset_Height[randint(0, 8)]
                obstacle_pipe_clng_rect.top -= Pipe_Offset_Value
                obstacle_pipe_grnd_rect.top = (obstacle_pipe_clng_rect.bottom + 250 - Pipe_Offset_Difficulty[randint(0,4)])
                Pipe_Spawn_Flag = False
                
            if Pipe_Spawn_Flag_2:
                
                Pipe_Offset_Value = Pipe_Offset_Height[randint(0, 8)]
                obstacle_pipe_clng_rect_2.top -= Pipe_Offset_Value
                obstacle_pipe_grnd_rect_2.top = (obstacle_pipe_clng_rect_2.bottom + 250 - Pipe_Offset_Difficulty[randint(0,4)])
                Pipe_Spawn_Flag_2 = False
                
            #BLITS
            screen.blit(screen_background_sky, sky_rect_1)
            screen.blit(screen_background_sky, sky_rect_2)
            screen.blit(obstacle_pipe_grnd, obstacle_pipe_grnd_rect)
            screen.blit(obstacle_pipe_clng, obstacle_pipe_clng_rect)
            screen.blit(obstacle_pipe_grnd, obstacle_pipe_grnd_rect_2)
            screen.blit(obstacle_pipe_clng, obstacle_pipe_clng_rect_2)
            screen.blit(screen_background_ground, ground_rect_grnd)
            screen.blit(screen_background_ground, ground_rect_grnd_2)
            screen.blit(screen_background_ground, ground_rect_clng)
            screen.blit(screen_background_ground, ground_rect_clng_2)
            screen.blit(game_text_score, (1100, 50))
            
            #BG ANIMATIONS
            ##SKY
            sky_rect_1.left -= 5
            sky_rect_2.left -= 5
            if sky_rect_1.left < -1401:
                sky_rect_1.left = 1401
            elif sky_rect_2.left < -1401:
                sky_rect_2.left = 1401
                
            ##GROUND AND CEILING
            ground_rect_grnd.left -= 7
            ground_rect_clng.left -= 7
            ground_rect_clng_2.left -= 7
            ground_rect_grnd_2.left -= 7
            
            if ground_rect_grnd.right < 1:
                ground_rect_grnd.left = 1401
            elif ground_rect_grnd_2.right < 1:
                ground_rect_grnd_2.left = 1401
            if ground_rect_clng.right < 1:
                ground_rect_clng.left = 1401
            elif ground_rect_clng_2.right < 1:
                ground_rect_clng_2.left = 1401
                
            #OBSTACLE
            obstacle_pipe_clng_rect.left -= 7
            obstacle_pipe_grnd_rect.left -= 7
            
            if obstacle_pipe_clng_rect.right <= 0:
                obstacle_pipe_clng_rect.topleft = (1531,0)
                obstacle_pipe_grnd_rect.topleft = (1531,600)
                
                Pipe_Spawn_Flag = True
                Pipe_2 += 1
                
            if Pipe_2 == 2:
                Pipe_2_Move_Flag = True
                
            if Pipe_2_Move_Flag == True:
                obstacle_pipe_clng_rect_2.left -= 7
                obstacle_pipe_grnd_rect_2.left -= 7
                
            if obstacle_pipe_clng_rect_2.right <= 0:
                obstacle_pipe_clng_rect_2.topleft = (1531, 0)
                obstacle_pipe_grnd_rect_2.topleft = (1531, 600)
                Pipe_Spawn_Flag_2 = True
                
                
            #HitBoxes: UNhash to display hitboxes
            # pygame.draw.rect(screen, 'Red', player_rect)
            # pygame.draw.rect(screen, 'Red', obstacle_pipe_clng_rect)
            # pygame.draw.rect(screen, 'Red', obstacle_pipe_grnd_rect)
            # pygame.draw.rect(screen, 'Blue', obstacle_pipe_grnd_rect_2)
            # pygame.draw.rect(screen, 'Blue', obstacle_pipe_clng_rect_2)

            
            #JUMP
            if Keys[pygame.K_SPACE]:
                if player_accel >= -4:
                    player_accel = -16
                    player_sprite_angle = 60
                    sfx_jump.play()
                    
            #VERTICAL POS
            player_accel += player_gravity
            player_rect.bottom += player_accel
        
            ##PLAYER
            player_sprite_rotate = pygame.transform.rotate(player_sprite_rest, player_sprite_angle)
            screen.blit(player_sprite_rotate, player_rect)
            if player_sprite_angle >= -50:    
                player_sprite_angle -= 3
                
            #Collision
            if player_rect.collidelist(OBSTACLES) != -1:
                Game_Over_Flag = True
                Game_Start_Flag = False
                sfx_death.play()
                pygame.mixer.music.stop()
                continue
                
            #Score Calc
            if obstacle_pipe_clng_rect.centerx == 203:
                score += 1
                Score_Flag = False
            elif obstacle_pipe_clng_rect_2.centerx in (203,205):
                score += 1
           
                
        ########################################

        
        #GAME OVER SCREEN CONDITION        
        if Game_Over_Flag:
            mouse_pos = pygame.mouse.get_pos()
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
             
        #GAME OVER SCREEN        
        if Game_Over_Flag:
            
            if Game_Over_Music_Flag:
                pygame.mixer.music.load('Audio/Last Surprise.mp3')
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(loops=-1, start=46.0)
                Game_Over_Music_Flag = False
            
            Back_Flag = False
            Quit_Flag = False
            Restart_Flag = False
            
            screen.fill(Black)
            screen.blit(Game_Over_text_Title, game_over_text_title_rect)
            screen.blit(game_text_score, (600, 150))
            
            ##BACK CONDITION
            if game_over_text_back_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, 'Grey', game_over_text_back_rect)
                if pygame.mouse.get_pressed()[0]: Back_Flag = True    
            screen.blit(Game_Over_text_Back, game_over_text_back_rect)
            
            ##QUIT CONDITION
            if game_over_text_quit_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, 'Grey', game_over_text_quit_rect)
                if pygame.mouse.get_pressed()[0]: Quit_Flag = True  
            screen.blit(Game_Over_text_Quit, game_over_text_quit_rect)
            
            ##RESTART CONDITION
            if game_over_text_restart_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, 'Grey', game_over_text_restart_rect)
                if pygame.mouse.get_pressed()[0]: Restart_Flag = True
            screen.blit(Game_Over_text_Restart, game_over_text_restart_rect)
            
            #CONDITION CHECKS
            if Back_Flag == True:
                Menu_Flag = True
                Game_Flag = False
                
                sky_rect_1.topleft = (0, 100)
                sky_rect_2.topleft = (1401, 100)
                ground_rect_grnd.center = (700, 800)
                ground_rect_clng.center = (700, 0)
                ground_rect_clng_2.topleft = (1401, -100)
                ground_rect_grnd_2.topleft = (1401, 700)
                player_rect.center = (200,400)
                obstacle_pipe_clng_rect.topleft =  (1531, 0)
                obstacle_pipe_grnd_rect.topleft = (1531, 600)
                obstacle_pipe_grnd_rect_2.topleft = (2231, 600)
                obstacle_pipe_clng_rect_2.topleft = (2231, 0)
                Game_Over_Flag = False
                
            elif Quit_Flag:
                pygame.quit()
                exit()
                
            elif Restart_Flag:
                
                sky_rect_1.topleft = (0, 100)
                sky_rect_2.topleft = (1401, 100)
                ground_rect_grnd.center = (700, 800)
                ground_rect_clng.center = (700, 0)
                ground_rect_clng_2.topleft = (1401, -100)
                ground_rect_grnd_2.topleft = (1401, 700)
                player_rect.center = (200,400)
                obstacle_pipe_clng_rect.topleft =  (1531, 0)
                obstacle_pipe_grnd_rect.topleft = (1531, 600)
                obstacle_pipe_grnd_rect_2.topleft = (2231, 600)
                obstacle_pipe_clng_rect_2.topleft = (2231, 0)
                
                Game_Start_Flag = False
                Game_Over_Flag = False
        
        pygame.display.update()
        clock.tick(60)
                

    #UPDATE AND CLOCK
    pygame.display.update()
    clock.tick(60)
    
    