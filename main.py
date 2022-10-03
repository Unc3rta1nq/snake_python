import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
font_style = pygame.font.SysFont("bahnschrift", 25)
clock = pygame.time.Clock()


class Snake:
    def __init__(self, snake_speed):
        self.snake_block = 10
        self.snake_speed = snake_speed
        self.snake_list = []
        self.snake_Head = []
        self.length_of_snake = 1
        self.x1 = 300
        self.y1 = 200
        self.game_end = False
        self.game_lose = False

    def our_snake(self):
        for x in self.snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], self.snake_block, self.snake_block])


class Food:

    def __init__(self):
        self.foodx = round(random.randrange(0, dis_width-10) / 10.0) * 10.0
        self.foody = round(random.randrange(0, dis_height-10) / 10.0) * 10.0

    def respawn_food(self):
        self.foodx = round(random.randrange(0, dis_width-10) / 10.0) * 10.0
        self.foody = round(random.randrange(0, dis_height-10) / 10.0) * 10.0


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2.5, dis_height / 2.25])


def game_loop():
    s = Snake(15)  # set fps(named as snake_speed)
    f = Food()
    x1_change = 0
    y1_change = 0

    while not s.game_end:
        while s.game_lose:
            dis.fill(red)
            message("You Lost!", white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s.game_end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change == s.snake_block:
                        continue
                    x1_change = -s.snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change == -s.snake_block:
                        continue
                    x1_change = s.snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change == s.snake_block:
                        continue
                    y1_change = -s.snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change== -s.snake_block:
                        continue
                    y1_change = s.snake_block
                    x1_change = 0

        if s.x1 >= dis_width or s.x1 < 0 or s.y1 >= dis_height or s.y1 < 0:
            s.game_lose = True
        s.x1 += x1_change
        s.y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [f.foodx, f.foody, s.snake_block, s.snake_block])
        s.snake_Head = []
        s.snake_Head.append(s.x1)
        s.snake_Head.append(s.y1)
        s.snake_list.append(s.snake_Head)
        if len(s.snake_list) > s.length_of_snake:
            del s.snake_list[0]

        for x in s.snake_list[:-1]:
            if x == s.snake_Head:
                s.game_lose = True

        s.our_snake()

        pygame.display.update()

        if s.x1 == f.foodx and s.y1 == f.foody:
            f.respawn_food()
            s.length_of_snake += 1

        clock.tick(s.snake_speed)
    pygame.quit()
    quit()


def main():
    game_loop()


if __name__ == "__main__":
    main()
