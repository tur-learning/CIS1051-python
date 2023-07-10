import pygame
import shelve

class Session():
    pygame.init()
    font = pygame.font.Font(None, 36)
    score = 0.
    def __init__(self, window_x, window_y):
        # Hide cursor here
        pygame.mouse.set_visible(False)
        self.fps = pygame.time.Clock()
        # Window size
        self.window_x = window_x
        self.window_y = window_y
        # Initializing game window
        pygame.display.set_caption("Exploring Space")
        self.game_window = pygame.display.set_mode((self.window_x, self.window_y))
        self.filename = 'game_session'

    def increase_score():
        Session.score += 100.

    def draw_score(self):
        score_surface = Session.font.render("Score: " + str(Session.score), 
                                            True, 'white')
        self.game_window.blit(score_surface, (10, 10))

    def game_over(self):
        surface = Session.font.render("GAME OVER: You have been killed", 
                                      True, 'red')
        self.game_window.blit(surface, ((self.window_x-surface.get_width())//2, 50))

    def save(self):
        pass

    def load(self):
        db = shelve.open(self.filename)
        return db
