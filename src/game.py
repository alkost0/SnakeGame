from .infrastructure import Infrastructure
from .snake import Snake
from .utils import *
from .constants import *


class Game:

    def __init__(self, infrastructure: Infrastructure) -> None:
        self.infrastructure = infrastructure
        head = gen_center_element()
        self.snake = Snake(head)
        self.apple = gen_apple(self.snake)
        self.tick_counter = 0
        self.snake_speed_delay = INITIAL_SPEED_DELAY
        self.is_running = True
        self.is_game_over = False

    def process_events(self) -> None:
        if self.infrastructure.is_quit_event():
            self.is_running = False #выход из цикла
        new_direction = self.infrastructure.get_pressed_key()
        if new_direction is not None:
            self.snake.set_direction(new_direction) #подвинули змейку вводом клавиатуры

    def update_state(self) -> None:
        if self.is_game_over:
            return
        self.tick_counter += 1
        if not self.tick_counter % self.snake_speed_delay:  #время обновить наше состояние
            head = self.snake.get_new_head()                #вычисляем новую голову
            if is_good_head(head, self.snake):
                self.snake.enqueue(head)                    #добавили новый кубик (голову) к змейке
                if head == self.apple:                      #означает, что яблоко съели
                    self.score += 1
                    self.apple = gen_apple(self.snake)
                else:
                    self.snake.dequeue()                    #убираем элемент
            else:                                           #когда врезались
                self.is_game_over = True

    def render(self) -> None:
        self.infrastructure.fill_screen()                   #стираем все, что было нарисовано
        for e in self.snake.deque:
            self.infrastructure.draw_element(e, SNAKE_COLOR)
        self.infrastructure.draw_element(self.apple, APPLE_COLOR)
        self.infrastructure.draw_score(self.score)
        if self.is_game_over:
            self.infrastructure.draw_game_over()
        self.infrastructure.update_and_tick()

    def loop(self):
        while self.is_running:
            self.process_events()
            self.update_state()
            self.render()
        self.infrastructire.quit()

