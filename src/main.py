# import knihoven a modulů
from pyray import *
from raylib import *
from player.snake_player import *
from obstacle.egg_obstacle import *

# konstanty
WIN_WIDTH = 800
WIN_HEIGHT = 600

# řízení herního stavu
class Game_Context:
    def __init__(self, state, snake, egg):
        self.state = state
        self.snake = snake
        self.egg = egg
        self.score = 0

class Game_StateStart:
    def execute(self, context):
        if is_key_pressed(KEY_SPACE):
            context.score = 0
            return context.state[1]
        else:
            if is_key_pressed(KEY_SPACE):
                return context.state[1]
            else:
                draw_text("Press Space start", 250, 300, 30, GREEN)
                return context.state[0]

class Game_StateRun:
    def is_snake_edge_colision(self, snake):
        head_position = snake.head_position()
        if head_position.x <= 0 or head_position.x >= WIN_WIDTH - snake.size.x:
            return True
        elif head_position.y <= 40 or head_position.y >= WIN_HEIGHT - snake.size.y:
            return True
        else:
            return False

    def is_snake_self_colision(self, snake):
        head_position = snake.head_position()
        for node in snake.node_chain[1:]:
            if self.is_collision(head_position, snake.size, node, snake.size):
                return True

        return False

    def is_collision(self, obj1_pos, obj1_size, obj2_pos, obj2_size):
        if obj1_pos.x < obj2_pos.x + obj2_size.x and \
                obj1_pos.x + obj1_size.x > obj2_pos.x and \
                obj1_pos.y < obj2_pos.y + obj2_size.y and \
                obj1_pos.y + obj1_size.y > obj2_pos.y:
            return True
        else:
            return False

    def is_egg_on_snake(self, egg, egg_size, snake):
        for node in snake.node_chain:
            if self.is_collision(node, snake.size, egg, egg_size) is True:
                return True
        return False

    def reloc_egg(self, egg, snake):
        while True:
            egg.position = context.egg.reloc_position()
            if self.is_egg_on_snake(egg.position, egg.size, snake) is False:
                break

    def execute(self, context):
        if is_key_pressed(KEY_UP):
            context.snake.turn_up()
        elif is_key_pressed(KEY_DOWN):
            context.snake.turn_down()
        elif is_key_pressed(KEY_LEFT):
            context.snake.turn_left()
        elif is_key_pressed(KEY_RIGHT):
            context.snake.turn_right()    

        context.snake.move()
        context.snake.draw()

        if self.is_snake_edge_colision(context.snake) or self.is_snake_self_colision(context.snake):
            return context.state[2]
        else:
            if self.is_collision(
                    context.snake.head_position()
                    , context.snake.size
                    , context.egg.position
                    , context.egg.size) is True:
                context.score += 1
                self.reloc_egg(context.egg, context.snake)
                context.snake.append_node()
            else:
                context.egg.draw()

            return context.state[1]

class Game_StateGameOver:
    def execute(self, context):
        if is_key_pressed(KEY_SPACE):
            context.score = 0
            context.snake.reset()
            context.egg.position = context.egg.reloc_position()
            return context.state[1]
        else:
            context.snake.draw()
            draw_text("Game Over", 320, 300, 30, RED)
            return context.state[2]

class Game:
    def __init__(self, init_state, context):
        self.game_state = init_state
        self.context = context

    def execute(self):
        draw_fps(10, 10)
        draw_text("score: " + str(self.context.score), 600, 10, 20, BLACK)
        draw_line(0, 40, WIN_WIDTH, 40, BLACK)
        self.game_state = self.game_state.execute(self.context)

# inicializace okna
init_window(WIN_WIDTH, WIN_HEIGHT, "Snake")
set_target_fps(10)

# inicializace herního stavu
gs_start = Game_StateStart()
gs_run = Game_StateRun()
gs_game_over = Game_StateGameOver()

snake = Snake_Player(Vector2(400, 300), Vector2(20, 20), GRAY)
egg = Egg_Obstacle(Vector2(0, 40), Vector2(WIN_WIDTH, WIN_HEIGHT), Vector2(20, 20), RED)

context = Game_Context([gs_start, gs_run, gs_game_over], snake, egg)
game = Game(gs_start, context)

# vykreslovací smyčka
while window_should_close() is False:
    begin_drawing()
    clear_background(WHITE)
    game.execute()
    end_drawing()

# korektní ukončení programu
close_window()






