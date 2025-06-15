import pygame

pygame.init()
screen=pygame.display.set_mode((288,512))

def creat_pipe():#creats new pipe
    new_pipe=pipe.get_rect(midtop=(144,256))
    return new_pipe
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes
# def draw_pipes(pipes):
    #for pipe in pipes:
        #screen.blit(pipe)

floor_surface = pygame.image.load('graphics/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0


pygame.display.set_caption("flappy bird")
clock=pygame.time.Clock()

#background

background=pygame.image.load("graphics/background-day.png")
background_rect=background.get_rect(center=(288/2,512/2))

#creating base
floor_sur=pygame.image.load("graphics/base.png")
floor_sur=pygame.transform.scale2x(floor_sur)
floor_x=0

bird=pygame.image.load("graphics/bird/yellowbird-midflap.png")
bird_angle=0
bird=pygame.transform.rotozoom(bird,bird_angle,1.2)

bird_x_pos=50
bird_y_pos=(512-100)/2
bird_rect=bird.get_rect(center=(bird_x_pos,bird_y_pos))
gravity=0

game_active=False

base = pygame.image.load("graphics/base.png").convert()





#starting screen
starting_screen=pygame.image.load("graphics/message.png")
starting_screen_rect=starting_screen.get_rect(center=(288/2,512/2))
start2=pygame.image.load("graphics/background-night.png")

#pipe
pipe=pygame.image.load("graphics/pipe/pipe-green.png")

pipe=pygame.transform.scale2x(pipe)



pipe_list=[]
SPAWNPIPE=pygame.USEREVENT 
pygame.time.set_timer(SPAWNPIPE,1200)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()




        if game_active == True:
            if event.type==pygame.KEYDOWN:

                if event.key   ==pygame.K_SPACE:
                    gravity=-10
                    bird_angle = 0
                    print("gay")
            if event.type==SPAWNPIPE:
                pipe_list.append(creat_pipe())

                print("fdff")

        else:
            screen.blit(start2,(0,0))
            screen.blit(starting_screen, starting_screen_rect)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("hhh")
                    gravity=0
                    bird_x_pos = 50
                    bird_y_pos = (512 - 100) / 2

                    game_active=True





    if game_active==True:
        screen.blit(background,background_rect)
        #screen.blit(base,base_rect)

        bird_angle = bird_angle + 10
        screen.blit(bird, (bird_x_pos,bird_y_pos))

        bird_y_pos=bird_y_pos+gravity
        gravity=gravity+1
        screen.blit(floor_sur,(floor_x,400 ))

        pipe_list= move_pipes(pipe_list)



        if bird_y_pos >= 400:
            game_active = False
            print("qqq")

        # # Floor
        floor_x -= 1

        if floor_x <= -376:
            floor_x= 0

    pygame.display.update()
    clock.tick(60)
