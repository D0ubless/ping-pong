from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 300:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_r2(self):
        keys = key.get_pressed()
        if keys[K_KP5] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_KP2] and self.rect.y < win_height - 450:
            self.rect.y += self.speed
    def update_l2(self):
        keys = key.get_pressed()
        if keys[K_y] and self.rect.y > 300:
            self.rect.y -= self.speed
        if keys[K_h] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 450:
            self.rect.y += self.speed


#создание экрана
back = ('background.png')
win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(back), (win_width, win_height))

game = True
finish = False
clock = time.Clock()


#спрайты   
racket1 = Player('left_racket.png', 30, 75, 4, 50, 100)
racket2 = Player('left_racket.png', 30, 375, 4, 50, 100)
racket3 = Player('right_racket.png', 730, 75, 4, 50, 100)
racket4 = Player('right_racket.png', 730, 375, 4, 50, 100)
ball = GameSprite('ball.png', 380, 150, 4, 35, 35)
ball2 = GameSprite('ball.png', 380, win_height - 150, 4, 35, 35)



font.init()
font = font.Font(None, 35)
lose1 = font.render('КОМАНДА 1 ПРОИГРАЛА', True, (0, 0, 180))
lose2 = font.render('КОМАНДА 2 ПРОИГРАЛА', True, (0, 0, 180))


speed_x1 = 9
speed_y1 = 9
speed_x2 = 9
speed_y2 = 9


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_l2()
        racket3.update_r2()
        racket4.update_r()
        ball.rect.x += speed_x1
        ball.rect.y += speed_y1
        ball2.rect.x += speed_x2
        ball2.rect.y += speed_y2  

        if sprite.collide_rect(racket1, ball) and speed_x1 < 0:
            speed_x1 *= -1
        if sprite.collide_rect(racket2, ball2) and speed_x2 < 0:
            speed_x2 *= -1
        if sprite.collide_rect(racket3, ball) and speed_x1 > 0:
            speed_x1 *= -1
        if sprite.collide_rect(racket4, ball2) and speed_x2 > 0:
            speed_x2 *= -1

        if ball.rect.y > 250 or ball.rect.y < 0:
            speed_y1 *= -1
        if ball2.rect.y > win_height - 40 or ball2.rect.y < 300:
            speed_y2 *= -1

        if ball.rect.x < 0 or ball2.rect.x < 0:
            finish = True
            window.blit(lose1, (250, 290))
  
        if ball.rect.x > win_width or ball2.rect.x > win_width:
            finish = True
            window.blit(lose2, (250, 290))

        racket1.reset()
        racket2.reset()
        racket3.reset()
        racket4.reset()
        ball.reset()
        ball2.reset()
        


    display.update()
    clock.tick(60)
