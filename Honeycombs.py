import subprocess

import pygame
import random
import math

SQRT3 = math.sqrt(3)
ORANGE = (247, 187, 57)
YELLOW = (250, 230, 115)
ALMOSTWHITE = (255, 240, 150)
BACKGROUND = (235, 185, 105)
EDGE = (180, 115, 63)
DISTANCE = 10
DELAY = 300


class Honeycomb:
    def __init__(self):
        pygame.init()
        # создание окна
        screen_info = pygame.display.Info()
        self.WIDTH, self.HEIGHT = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Кнопка выхода на главный экран
        self.button_image = pygame.image.load("foto/exites.png")
        self.button_image = pygame.transform.scale(self.button_image,
                                                   (50, 50))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.bottomleft = (self.WIDTH - 50, 60)

    # счётчик игры
    def ShowScore(self, score):
        rect = pygame.Rect(0, 0, self.WIDTH / 2 - 100, self.HEIGHT / 6)
        self.screen.fill(BACKGROUND, rect)
        font = pygame.font.Font(None, 70)
        text = font.render(f"Your score: {score}", True,
                           ALMOSTWHITE)
        self.screen.blit(text,
                         (self.WIDTH // 4 - text.get_width() // 2,
                          self.HEIGHT // 8 - text.get_height() // 2))
        self.screen.blit(self.button_image, self.button_rect)
        pygame.display.flip()

    # создаёт соты
    def CreateHoneycombs(self):
        self.screen.fill(BACKGROUND)
        x_0 = self.WIDTH // 2
        y_0 = self.HEIGHT // 2
        honeycombs = []
        honeycombs.append(Polygon(x_0, y_0, EDGE))
        dist = DISTANCE + 2 * honeycombs[0].side_size * SQRT3 / 2
        honeycombs.append(
            Polygon(x_0 - SQRT3 / 2 * dist, y_0 - 1 / 2 * dist, EDGE))
        honeycombs.append(Polygon(x_0, y_0 - dist, EDGE))
        honeycombs.append(
            Polygon(x_0 + SQRT3 / 2 * dist, y_0 - 1 / 2 * dist, EDGE))
        honeycombs.append(
            Polygon(x_0 + SQRT3 / 2 * dist, y_0 + 1 / 2 * dist, EDGE))
        honeycombs.append(Polygon(x_0, y_0 + dist, EDGE))
        honeycombs.append(
            Polygon(x_0 - SQRT3 / 2 * dist, y_0 + 1 / 2 * dist, EDGE))
        self.DrawHoneycombs(honeycombs)
        return honeycombs

    # отрисовывает соты
    def DrawHoneycombs(self, honeycombs):
        for i in range(len(honeycombs)):
            honeycombs[i].Draw(self.screen)
            new_polygon = Polygon(honeycombs[i].x, honeycombs[i].y, ORANGE,
                                  100)
            new_polygon.Draw(self.screen)
        pygame.display.update()

    # показывает последовательность подсветки сот для игрока
    def ShowSequence(self, sequence, honeycombs):
        pygame.event.pump()
        for i in sequence:
            new_polygon = Polygon(honeycombs[i].x, honeycombs[i].y, YELLOW,
                                  100)
            new_polygon.Draw(self.screen)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(DELAY)
            self.DrawHoneycombs(honeycombs)
            pygame.event.pump()
            pygame.time.delay(DELAY)


    # запускает игровой цикл, проверяет правильность
    # нажатия игрока и определяет окончание игры
    def Run(self):
        score = 0
        game_over = False
        snd1 = pygame.mixer.Sound("songs/snd1.wav")
        snd3 = pygame.mixer.Sound("songs/snd3.wav")
        honeycombs = self.CreateHoneycombs()
        sequence = [random.randint(0, 6)]
        queue = [sequence[0]]
        self.ShowScore(score)
        self.ShowSequence(sequence, honeycombs)
        print(sequence)

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        pygame.quit()
                        subprocess.run(["python", "main.py"])
                    x, y = pygame.mouse.get_pos()
                    if not honeycombs[queue[-1]].Popal(x, y):
                        pygame.mixer.Sound.play(snd3)
                        pygame.event.pump()
                        pygame.time.delay(4 * DELAY)
                        game_over = True
                        Restart.RestartScreen(self, score)
                        restart_button = Button(self.WIDTH // 2 - 50,
                                                self.HEIGHT // 2 + 30,
                                                100, 50,
                                                ALMOSTWHITE)
                        restart_button.Draw(self.screen)
                        restart_button.DrawButtonText(self.screen)
                        pygame.display.update()
                        if game_over:
                            break
                    else:
                        pygame.mixer.Sound.play(snd1)
                        queue.pop()
                        if len(queue) == 0:
                            sequence.append(random.randint(0, 6))
                            self.ShowScore(score + 1)
                            self.ShowSequence(sequence, honeycombs)
                            queue = sequence.copy()
                            queue.reverse()
                            print(sequence)
                            score += 1

            if game_over:
                with open("res_txt/sota_res.txt", "a") as file:
                    file.write(str(score) + "\n")

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    restart_button.CheckIfClicked(pos)
                    if restart_button.clicked:
                        self.Run()
                    if self.button_rect1.collidepoint(event.pos):
                        pygame.quit()
                        subprocess.run(["python", "main.py"])


# проверяет, была ли нажата кнопка "Restart"
# и перезапускает игру при необходимости
class Restart:
    def init(self):
        pygame.init()
        screen_info = pygame.display.Info()
        self.WIDTH, self.HEIGHT = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    # выводит окно с сообщением о конце игры и показывает счет игрока
    def RestartScreen(self, score):
        self.screen.fill(BACKGROUND)

        self.button1 = pygame.image.load("foto/homes.png")
        self.button1 = pygame.transform.scale(self.button1, (150, 150))
        self.button_rect1 = self.button1.get_rect()
        self.button_rect1.center = (self.WIDTH // 2, 550)

        font = pygame.font.Font(None, 80)
        text = font.render(f"Game over! Your score: {score}", True,
                           ALMOSTWHITE)
        self.screen.blit(text,
                         (self.WIDTH // 2 - text.get_width() // 2,
                          self.HEIGHT // 2 - text.get_height() // 2))
        self.screen.blit(self.button1, self.button_rect1)

        pygame.display.update()


# представляет точку на плокости
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# представляет вектор
class Vector:
    def __init__(self, point_a: Point, point_b: Point):
        self.x = point_b.x - point_a.x
        self.y = point_b.y - point_a.y


# вычисляет векторное произведение двух векторов
def VectorProduct(a: Vector, b: Vector):
    return a.x * b.y - a.y * b.x


# создание сот
class Polygon:
    def __init__(self, x, y, color, side_size=125):
        self.x = x
        self.y = y
        self.color = color
        self.clicked = False
        self.side_size = side_size

    # возвращает координаты вершин шестиугольника
    def PolygonPoint(self, number):
        if (number == 0):
            return Point(-self.side_size / 2 + self.x,
                         SQRT3 * self.side_size / 2 + self.y)
        if (number == 1):
            return Point(self.side_size / 2 + self.x,
                         SQRT3 * self.side_size / 2 + self.y)
        if (number == 2):
            return Point(self.side_size + self.x, self.y)
        if (number == 3):
            return Point(self.side_size / 2 + self.x,
                         -SQRT3 * self.side_size / 2 + self.y)
        if (number == 4):
            return Point(-self.side_size / 2 + self.x,
                         -SQRT3 * self.side_size / 2 + self.y)
        if (number == 5):
            return Point(-self.side_size + self.x, self.y)

    # рисует шестиугольник на экране
    def Draw(self, screen):
        coordinades = []
        for i in range(6):
            point = self.PolygonPoint(i)
            coordinades.append((point.x, point.y))
        pygame.draw.polygon(screen, self.color, coordinades)

    # проверяет, попал ли клик игрока внутрь шестиугольника
    def Popal(self, x, y):
        for i in range(6):
            a = self.PolygonPoint(i)
            b = self.PolygonPoint((i + 1) % 6)
            c = Point(x, y)
            if VectorProduct(Vector(a, b), Vector(a, c)) > 0:
                return False
        return True


# создание кнопки в окне смерти
class Button:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.clicked = False
        self.width = x + 15
        self.height = y + 15

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    # текст на кнопке
    def DrawButtonText(self, screen):
        self.screen = screen
        font = pygame.font.Font(None, 30)
        text = font.render("Restart", True, EDGE)
        self.screen.blit(text, (self.width, self.height))

    def CheckIfClicked(self, pos):
        if self.rect.collidepoint(pos):
            self.clicked = True
        else:
            self.clicked = False


visual_memory_honeycombs_test = Honeycomb()
visual_memory_honeycombs_test.Run()
