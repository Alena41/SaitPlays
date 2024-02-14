import subprocess

import pygame
import random
import time


class ReactionTimeTest:

    def __init__(self):
        pygame.init()
        self.result_file = open("res_txt/Klicker_res.txt", "a")
        # Принимаем размеры экрана
        screen_info = pygame.display.Info()
        self.width, self.height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height))

        button_size = (50, 50)

        self.close_button_image = pygame.image.load('foto/exites.png')
        self.close_button_image = pygame.transform.scale(
            self.close_button_image,
            button_size)
        self.close_button_rect = self.close_button_image.get_rect()
        self.close_button_rect.topleft = (5, 5)

        self.blue_screen()

    def too_soon_screen(self):
        self.screen.fill((50, 50, 155))
        font = pygame.font.Font(None, 100)
        text = font.render("Click too soon", True,
                           (255, 255, 255))
        self.screen.blit(text,
                         (self.width // 2 - text.get_width() // 2,
                          self.height // 2 - text.get_height() // 2))
        pygame.display.flip()

    def blue_screen(self):
        self.screen.fill((50, 50, 155))
        font = pygame.font.Font(None, 100)
        text = font.render("Reaction time test", True,
                           (255, 255, 255))
        self.screen.blit(text,
                         (self.width // 2 - text.get_width() // 2,
                          self.height // 2 - text.get_height() // 2))
        pygame.display.flip()

    def red_screen(self):
        self.screen.fill((155, 0, 0))
        font = pygame.font.Font(None, 100)
        text = font.render("Wait for green", True,
                           (255, 255, 255))
        self.screen.blit(text,
                         (self.width // 2 - text.get_width() // 2,
                          self.height // 2 - text.get_height() // 2))
        pygame.display.flip()

    def green_screen(self):
        self.screen.fill((0, 155, 20))
        font = pygame.font.Font(None, 100)
        text = font.render("Click!", True, (255, 255, 255))
        self.screen.blit(text,
                         (self.width // 2 - text.get_width() // 2,
                          self.height // 2 - text.get_height() // 2))
        pygame.display.flip()

    def result_screen(self, result):
        self.screen.fill((0, 155, 20))
        font = pygame.font.Font(None, 100)
        text = font.render(f"{result} ms", True,
                           (255, 255, 255))
        self.screen.blit(text,
                         (self.width // 2 - text.get_width() // 2,
                          self.height // 2 - text.get_height() // 2))
        pygame.display.flip()
        self.result_file.write(str(result) + "\n")

    def open_main_screen(self):
        subprocess.run(["python", "main.py"])

    def run(self):
        start = True
        self.is_running = True

        while start and self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.red_screen()

                    if self.close_button_rect.collidepoint(event.pos):
                        self.is_running = False
                        pygame.quit()
                        self.open_main_screen()

                    running = True
                    is_red = True

                    while running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False

                            elif (event.type == pygame.MOUSEBUTTONDOWN
                                  and is_red):
                                running = False
                                self.too_soon_screen()

                            elif (event.type == pygame.MOUSEBUTTONDOWN
                                  and not is_red):
                                running = False
                                result = int((time.time() - result) * 1000)
                                self.result_screen(result)

                            if not self.is_running:
                                running = False

                        if random.randint(0, 100) == 1:
                            self.green_screen()
                            result = time.time()
                            is_red = False

                        pygame.time.wait(30)
            self.screen.blit(self.close_button_image, self.close_button_rect)
            pygame.display.flip()
        self.result_file.close()
        pygame.quit()


if __name__ == "__main__":
    reaction_time_test = ReactionTimeTest()
    reaction_time_test.run()
