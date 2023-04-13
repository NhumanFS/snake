import pygame
import random
from os import path

pygame.init()
pygame.display.set_caption("game")

color1 = (172, 255, 120)
color2 = (255, 120, 226)
color3 = (255, 217, 120)
color4 = (178, 255, 120)
color5 = (163, 120, 255)
speed = 15

width = 800
hight = 600
fps = 5
clock = pygame.time.Clock()
snake_block = 30
snake_step = 30

screen = pygame.display.set_mode((width, hight))
imj_dir = path.join(path.dirname(__file__),
                    "F:\психушка\music\img")
music_dir = path.join(path.dirname(__file__),
                      "F:\психушка\music\music")
bg = pygame.image.load(path.join(imj_dir, "Fon_grass4.jpg")).convert()
bg = pygame.transform.scale(bg, (width, hight))
pygame.mixer.music.load(path.join(music_dir, "Intense.mp3"))
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
am = pygame.mixer.Sound(path.join(music_dir, "apple_bite.ogg"))
am.set_volume(0.5)
bg_rect = bg.get_rect()
snake_head = [pygame.image.load(path.join(imj_dir, "HeadB.png")).convert(),
              pygame.image.load(path.join(imj_dir, "HeadL.png")).convert(),
              pygame.image.load(path.join(imj_dir, "HeadR.png")).convert(),
              pygame.image.load(path.join(imj_dir, "HeadT.png")).convert()]

snake_tail = [pygame.image.load(path.join(imj_dir, "taildown.png")).convert(),
              pygame.image.load(path.join(imj_dir, "tailleft.png")).convert(),
              pygame.image.load(path.join(imj_dir, "tailright.png")).convert(),
              pygame.image.load(path.join(imj_dir, "tailup.png")).convert()]


def draw_head(i, snakelist):
    snake_head_imj = snake_head[i]
    snake_head1 = pygame.transform.scale(
        snake_head_imj, (snake_block, snake_block))
    snake_head1.set_colorkey(color2)
    snake_head_rect = snake_head1.get_rect(
        x=snakelist[-1][0], y=snakelist[-1][1])
    # x=snakelist[-1][0], y=snakelist[-1][1])
    screen.blit(snake_head1, snake_head_rect)


def draw_tail(i, snakelist):
    snake_tail_imj = snake_tail[i]
    snake_tail1 = pygame.transform.scale(
        snake_tail_imj, (snake_block, snake_block))
    snake_tail1.set_colorkey(color2)
    snake_tail_rect = snake_tail1.get_rect(
        x=snakelist[0][0], y=snakelist[0][1])
    # x=snakelist[0][0], y=snakelist[0][1])
    screen.blit(snake_tail1, snake_tail_rect)


def creat_message(message, color, x, y, fontname, size):
    fontstyle = pygame.font.SysFont(fontname, size)
    message = fontstyle.render(message, True, color)
    screen.blit(message, [x, y])


def eating_check(xcor, ycor, foodx, foody):
    if foodx - snake_block <= xcor <= foodx+snake_block:
        if foody - snake_block <= ycor <= foody+snake_block:
            return True
    else:
        return False


def gameloop():

    i = 0
    gameclose = False
    x1 = width / 2
    y1 = hight / 2
    x1change = 0
    y1change = 0
    lenght = 2
    snakelist = []
    foodx = random.randrange(0, width-snake_block)
    foody = random.randrange(0, hight-snake_block)

    food = [pygame.image.load(path.join(imj_dir, "f_1.png")).convert(),
            pygame.image.load(path.join(imj_dir, "f_2.png")).convert(),
            pygame.image.load(path.join(imj_dir, "f_3.png")).convert(),
            pygame.image.load(path.join(imj_dir, "f_4.png")).convert(),
            pygame.image.load(path.join(imj_dir, "f_5.png")).convert(),
            pygame.image.load(path.join(imj_dir, "f_6.png")).convert(),
            pygame.image.load(path.join(imj_dir, "f_7.png")).convert()]

    food1 = pygame.transform.scale(
        random.choice(food), (snake_block, snake_block))
    food1.set_colorkey(color2)
    foodrect = food1.get_rect(x=foodx, y=foody)
    run = True

    while run:

        while gameclose:
            screen.fill(color1)
            creat_message("you failed", color2,
                          200, 200, "comicsans", 50)
            creat_message("q for exit, c for retry",
                          color2, 10, 300, "comicsans", 25)
            creat_message(
                f"your score {lenght-2}", color2, 0, 0, "comicsans", 25)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        gameclose = False
                    elif event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1change = - snake_step
                    y1change = 0
                    i = 1
                elif event.key == pygame.K_RIGHT:
                    x1change = snake_step
                    y1change = 0
                    i = 2
                elif event.key == pygame.K_UP:
                    y1change = - snake_step
                    x1change = 0
                    i = 3
                elif event.key == pygame.K_DOWN:
                    y1change = snake_step
                    x1change = 0
                    i = 0
        if x1 >= width or x1 <= 0 or y1 >= hight or y1 <= 0:
            gameclose = True
        x1 += x1change
        y1 += y1change
        screen.fill(color1)
        screen.blit(bg, bg_rect)
        screen.blit(food1, foodrect)
        snake_head = [x1, y1]
        snakelist.append(snake_head)
        if len(snakelist) > lenght:
            del snakelist[0]
        for x in snakelist[1:]:
            body = pygame.image.load(
                path.join(imj_dir, "body.png")).convert()
            snake = pygame.transform.scale(body, (snake_block, snake_block))
            snake.set_colorkey(color2)
            screen.blit(body, (x[0], x[1]))
        draw_head(i, snakelist)
        draw_tail(i, snakelist)
        creat_message(
            f"your score {lenght-2}", color2, 0, 0, "comicsans", 25)
        pygame.display.update()
        if eating_check(x1, y1, foodx, foody):
            foodx = random.randrange(0, width-snake_block)
            foody = random.randrange(0, hight-snake_block)

            food = [pygame.image.load(path.join(imj_dir, "f_1.png")).convert(),
                    pygame.image.load(path.join(imj_dir, "f_2.png")).convert(),
                    pygame.image.load(path.join(imj_dir, "f_3.png")).convert(),
                    pygame.image.load(path.join(imj_dir, "f_4.png")).convert(),
                    pygame.image.load(path.join(imj_dir, "f_5.png")).convert(),
                    pygame.image.load(path.join(imj_dir, "f_6.png")).convert(),
                    pygame.image.load(path.join(imj_dir, "f_7.png")).convert()]

            food1 = pygame.transform.scale(
                random.choice(food), (snake_block, snake_block))
            food1.set_colorkey(color2)
            foodrect = food1.get_rect(x=foodx, y=foody)
            lenght+1
            am.play()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


gameloop()
