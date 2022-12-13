import numpy as np
import gym
from gym import spaces
import pygame
from pygame import display, time, init
from pygame.event import pump
from pygame.surfarray import array3d
import cv2
import random

"""
Bengünur Baş 
17290010 
Bitirme Projesi 
CATastrophe Game - Oyunun Kurgusu : Kedinin karşısına çıkan balıklardan korunarak ya da onları
vurarak hayatta kalması gerekiyor.  

"""
class Fish():
    img_list = [pygame.image.load("src/images/fish1.png"), 
                pygame.image.load("src/images/fish2.png"),
                pygame.image.load("src/images/fish3.png"),
                pygame.image.load("src/images/fish4.png"),
                pygame.image.load("src/images/fish5.png"),
                pygame.image.load("src/images/fish6.png")]
    
    def __init__(self, enemy_list, spaceship):
        self.velx = random.randint(-2,2)
        self.vely = .5
        self.img = Fish.img_list[0]
        self.image_index = 0
        self.image_mask = pygame.mask.from_surface(self.img)
        self.new_location(enemy_list, spaceship)

    def new_location(self, enemy_list, spaceship):
        new_spot = True
        while new_spot:
            new_spot = False
            self.x = random.randint(70, 500 - 70)
            self.y = random.randint(10, 150)
            for enemy in enemy_list:
                if self == enemy:
                    pass
                else:
                    #new_spot = hit(self.x, self.y, enemy.x, enemy.y)
                    if hit_pixel(self, enemy):
                        # If it hit something go back and start over
                        continue
            if hit_pixel(spaceship, self):
                continue    
            else:
                break
        self.velx = random.randint(-2,2)

    def speed_up(self):
        if abs(self.velx) > 25:
            #self.vely += .5
            #self.velx += random.randint(0, 1)
            pass
        else:
            pass
            #self.velx += random.randint(1, 2)
            #self.vely += random.randint(0, 1)
        if self.image_index < len(self.img_list) - 1:
            self.image_index += 1
            self.img = self.img_list[self.image_index]
            self.image_mask = pygame.mask.from_surface(self.img)

class EnemyWave():
    def __init__(self, count, spaceship):
        self.enemy_list = []
        for i in range(count):
            self.enemy_list.append(Fish(self.enemy_list, spaceship))

    def check(self, screen, bullet, spaceship):
        score_tracker = 0
        for enemy in self.enemy_list:
            screen.blit(enemy.img, (int(enemy.x), int(enemy.y)))

            # Check for wall hit
            if enemy.x > 500 - enemy.img.get_rect().size[0] or enemy.x <= 0:
                # Flip direction
                enemy.velx *= -1  
                enemy.x += enemy.velx
                if enemy.x > 500:
                    enemy.x = 500
                elif enemy.x <= 0:
                    enemy.x = 0

            enemy.x += enemy.velx
            enemy.y += enemy.vely
            if enemy.y > 500:
                enemy.y = 0
                enemy.velx = random.randint(0,2)
                enemy.vely = .5
                #enemy.velx += .25
                #enemy.vely += .25
            if bullet.shoot:
                if hit_pixel(bullet, enemy):
                    bullet.shoot = False
                    score_tracker += 1
                    enemy.new_location(self.enemy_list, spaceship)
                    enemy.speed_up()
                bullet.move(screen)

            if hit_pixel(enemy, spaceship):
                return -1

        return score_tracker


def hit (ojb1x, obj1y, obj2x, obj2y):
    dist = math.sqrt(math.pow(ojb1x-obj2x, 2)+math.pow(obj1y-obj2y, 2))
    if dist < 34:
        return True
    else:
        return False


def hit_pixel(object1, object2):

    offset = (int(object2.x - object1.x), int(object2.y - object1.y))
    point = object1.image_mask.overlap(object2.image_mask, offset)

    if point:
        return True
    return False


class SpaceCAT():
    def __init__(self):
        self.vel = 9
        self.x = 250
        self.y = 400
        self.move_x = 0
        self.move_y = 0
        self.img = pygame.image.load("src/images/cat1.png")
        self.image_mask = pygame.mask.from_surface(self.img)

    def check_move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_x -= self.vel
            if event.key == pygame.K_RIGHT:
                self.move_x += self.vel
            if event.key == pygame.K_UP:
                self.move_y -= self.vel
            if event.key == pygame.K_DOWN:
                self.move_y += self.vel
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                self.move_x = 0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                self.move_y = 0

    def move(self, screen):
        width_bound = 500 - self.img.get_rect().size[0]
        height_bound = 500 - self.img.get_rect().size[1]

        if self.x + self.move_x < width_bound and self.x + self.move_x > 0:
            self.x += self.move_x
        if self.y + self.move_y < height_bound and self.y + self.move_y > 0:
            self.y += self.move_y
    
    def show(self, screen):
        screen.blit(self.img, (int(self.x),int(self.y)))


class Laser():

    def __init__(self):
        self.x = 250
        self.y = -100
        self.shoot = False
        self.img = pygame.image.load("src/images/laser.png")
        self.image_mask = pygame.mask.from_surface(self.img)


    def sound(self):
        pass
        # self.laser.play()

    def check_move(self, event, ship_x, ship_y):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not self.shoot:
                    self.sound()
                    self.x = ship_x + 32 - (self.img.get_rect().size[0] / 2 )
                    self.y = ship_y - self.img.get_rect().size[1]
                    self.shoot = True

    def move(self, screen):
        if self.y < 0:
            self.shoot = False
            self.y = -100
        else:
            self.y -= 3
            #screen.blit(self.img, (self.x, self.y))

    def show(self, screen):
        if self.shoot:
            screen.blit(self.img, (self.x, self.y))


class CATastrophe(gym.Env):

  def __init__(self):
    pygame.init()
    super(CATastrophe, self).__init__()

    self.fps = 30
    self.fps_clock = time.Clock()
    self.WIDTH = 500
    self.HEIGHT = 500
    base_y = 500
    self.history = []
    for i in range(0, 6):
      self.history.append(np.zeros((84, 84)))
    
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    display.set_caption('CATastrophe')
    self.screen.fill((0, 0, 0))
    n_actions = 18
    self.action_space = spaces.Discrete(n_actions)
    self.observation_space = spaces.Box(low=0, high=255, shape=(252, 84, 1), dtype=np.uint8)

  def reset(self):
    self.history_frame = np.zeros((84, 84))
    self.history_frame2 = np.zeros((84, 84))
    self.screen.fill((0, 0, 0))
    self.spaceshipCat = SpaceCAT()
    self.Laser = Laser()
    self.enemy_wave = EnemyWave(5, self.spaceshipCat)
    self.score = 0
    image = self.pre_processing(array3d(display.get_surface()))
    return image

  def step(self, action):
    scoreholder = self.score
    self.screen.fill((0, 0, 0))
    pump()
    reward = -0.001
    done = False

    if action == 2 or action == 6 or action == 10 or action == 11 or action == 14 or action == 15:
        self.spaceshipCat.move_y -= self.spaceshipCat.vel
    if action == 3 or action == 7 or action == 12 or action == 13 or action == 16 or action == 17:
        self.spaceshipCat.move_y += self.spaceshipCat.vel
    if action == 5 or action == 9 or action == 11 or action == 13 or action == 15 or action == 17:
        self.spaceshipCat.move_x -= self.spaceshipCat.vel
    if action == 4 or action == 8 or action ==10 or action == 12 or action == 14 or action == 16:
        self.spaceshipCat.move_x += self.spaceshipCat.vel
    # Atış Yapmak için olan eylemler .
    if action == 1 or action == 6 or action == 7 or action == 8 or action == 9 or action == 14 or action == 15 or action == 16 or action == 17:
        if self.Laser.shoot == False:
            self.Laser.x = self.spaceshipCat.x + 32 - (self.Laser.img.get_rect().size[0] / 2 )
            self.Laser.y = self.spaceshipCat.y - self.Laser.img.get_rect().size[1]
            self.Laser.shoot = True
            reward -= 0.001
        
    self.spaceshipCat.move(self.screen)
    self.spaceshipCat.move_x = 0
    self.spaceshipCat.move_y = 0

    result = self.enemy_wave.check(self.screen, self.Laser, self.spaceshipCat)
    if result >= 0:
        reward += result
        self.score += result
    else:
        done = True
        reward = -2
        self.__init__()

    self.Laser.show(self.screen)
    self.spaceshipCat.show(self.screen)
    image = array3d(display.get_surface())
    info = {'score': scoreholder}
    self.fps_clock.tick(self.fps)
    display.update()
    return self.pre_processing(image), reward, done, info

  def render(self):

    # Score Göster 
    font = pygame.font.SysFont("comicsans", 40)
    showscore = font.render(f"Score: {self.score}", True, (255, 255, 255))
    self.screen.blit(showscore, (self.WIDTH - 10 - showscore.get_width(), 10))  

    # Görüntüyü güncelle 
    display.update()

  def close(self):
    pass

  def pre_processing(self, image):
    image = cv2.cvtColor(cv2.resize(image, (84, 84)), cv2.COLOR_BGR2GRAY)              # Treshold 
    _, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
    image = image / 255
    
    del self.history[0]
    self.history.append(image)

    image = np.concatenate((self.history[-5], self.history[-3], image), axis=0)
 
    image = np.expand_dims(image, axis=-1)

    return image