import subprocess
import sys
import pygame
import random


class VisualMemoryTest:
    def __init__(self):
        pygame.init()
        # Принимаем размеры экрана
        screen_info = pygame.display.Info()
        self.width, self.height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height))

        # обои на весь экран
        self.background_image = pygame.image.load("foto/poslefon.jpg")
        self.background_image = (pygame.transform.scale
                                 (self.background_image,
                                  (self.width, self.height)))

        self.clock = pygame.time.Clock()
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        self.sequence = []
        self.user_input = []
        self.current_level = 0
        self.correct_sequences = 0
        self.running = True

        # Кнопка выхода на главный экран
        self.button_image = pygame.image.load("foto/exites.png")
        self.button_image = pygame.transform.scale(self.button_image,
                                                   (50, 50))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.bottomleft = (self.width - 50, 60)

    # генерируем цвета
    def generate_sequence(self):
        self.sequence = [random.choice(self.colors) for _ in
                         range(self.current_level + 3)]

    # расположение генирирующихся цветов, и время для запоминания
    def display_sequence(self):
        for i, color in enumerate(self.sequence):
            pygame.draw.rect(self.screen, color,
                             (20 + 70 * i, 300, 60, 60))
        pygame.display.update()
        pygame.time.wait(10000)

    # кнопки для обозначения цвета, и счётчик
    def draw_buttons(self):
        for i, color in enumerate(self.colors):
            pygame.draw.rect(self.screen, color,
                             (470 + 130 * i, 530, 100, 100))

        font = pygame.font.Font(None, 36)
        text = font.render(f'Ваш счёт: {self.correct_sequences}',
                           True, (0, 0, 0))
        self.screen.blit(text, (20, 20))
        self.screen.blit(self.button_image, self.button_rect)

        pygame.display.update()

    # нажатие кнопок по координатам выдаёт соответсвующий цвет и кнопка выхода
    def handle_input(self):
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run(["python", "main.py"])
                x, y = pygame.mouse.get_pos()
                if y >= 530:
                    if 470 <= x < 600:
                        self.user_input.append(
                            self.colors.index(self.colors[0]))
                    elif 605 <= x < 710:
                        self.user_input.append(
                            self.colors.index(self.colors[1]))
                    elif 720 <= x < 830:
                        self.user_input.append(
                            self.colors.index(self.colors[2]))

    # если проигрыш, счётчик -1
    def decrease_score(self):
        if self.correct_sequences > 0:
            self.correct_sequences -= 1

    # основной цикл с движухой
    def run(self):
        pygame.init()
        while self.running:
            self.screen.blit(self.background_image, (0, 0))
            self.draw_buttons()
            self.handle_input()
            if len(self.user_input) == len(self.sequence):
                if self.user_input == [self.colors.index(color)
                                       for color in self.sequence]:
                    self.current_level += 1
                    self.correct_sequences += 1
                    if self.current_level >= 17:
                        win_game = WIN(self.correct_sequences)
                        win_game.run()
                        self.running = False
                    else:
                        self.generate_sequence()
                        self.display_sequence()
                        self.user_input = []
                else:
                    self.decrease_score()
                    self.running = False
                    rip_game = RIP(self.correct_sequences)
                    rip_game.run()

            self.clock.tick(60)
        pygame.quit()


# класс если пользователь ввёл неверную последовательность
class RIP:
    def __init__(self, score):
        # размеры окна
        screen_info = pygame.display.Info()
        self.width, self.height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.running = True
        self.score = score

        # кнопка попробовать снова
        self.button_image = pygame.image.load("foto/md_5aaeb1e070494.jpg")
        self.button_image = pygame.transform.scale(self.button_image,
                                                   (150, 150))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.center = (self.width // 2, self.height // 2)

        # кнопка вернуться на главный экран
        self.button1 = pygame.image.load("foto/homes.png")
        self.button1 = pygame.transform.scale(self.button1, (150, 150))
        self.button_rect1 = self.button1.get_rect()
        self.button_rect1.center = (self.width // 2, 550)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    self.return_game()
                    self.running = False
                elif self.button_rect1.collidepoint(event.pos):
                    self.close_pygame()

    # возвращение на главный экран
    def close_pygame(self):
        pygame.quit()
        subprocess.run(["python", "main.py"])

    # возвращение в игру
    def return_game(self):
        return_game = VisualMemoryTest()
        return_game.run()
        pygame.quit()

    # сохранение счётчика
    def save_score(self):
        with open("res_txt/score.txt", "a") as file:
            file.write(str(self.score) + "\n")

    # основной движ
    def run(self):
        self.save_score()
        while self.running:
            self.handle_input()
            self.screen.fill((180, 0, 10))
            self.screen.blit(self.button_image, self.button_rect)
            self.screen.blit(self.button1, self.button_rect1)

            font = pygame.font.Font(None, 36)
            text = font.render(f'Ваш результат: {self.score}',
                               True, (255, 255, 255))
            self.screen.blit(text, (20, 20))

            pygame.display.update()

        pygame.quit()


# класс если пользователь победил
class WIN:
    def __init__(self, score):
        # создание окна
        screen_info = pygame.display.Info()
        self.width, self.height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.running = True
        self.score = score

        self.button_image = pygame.image.load("foto/md_5aaeb1e070494.jpg")
        self.button_image = pygame.transform.scale(self.button_image,
                                                   (150, 150))
        self.button_rect = self.button_image.get_rect()
        self.button_rect.center = (self.width // 2, self.height // 2)

        self.button1 = pygame.image.load("foto/homes.png")
        self.button1 = pygame.transform.scale(self.button1, (150, 150))
        self.button_rect1 = self.button1.get_rect()
        self.button_rect1.center = (self.width // 2, 550)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    self.return_game()
                    self.running = False
                elif self.button_rect1.collidepoint(event.pos):
                    self.close_pygame()

    # возврат в игру
    def return_game(self):
        return_game = VisualMemoryTest()
        return_game.run()
        pygame.quit()

    # возвращение на главный экран
    def close_pygame(self):
        pygame.quit()
        subprocess.run(["python", "main.py"])

    # Сохранение счётчика
    def save_score(self):
        with open("res_txt/score.txt", "a") as file:
            file.write(str(self.score) + "\n")

    # основной движ
    def run(self):
        self.save_score()
        while self.running:
            self.handle_input()
            self.screen.fill((0, 200, 0))

            font = pygame.font.Font(None, 36)
            text = font.render(f'Ваш результат: {self.score}',
                               True, (255, 255, 255))
            self.screen.blit(text, (20, 20))

            self.screen.blit(self.button_image, self.button_rect)
            self.screen.blit(self.button1, self.button_rect1)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = VisualMemoryTest()
    game.run()
    sys.exit()
