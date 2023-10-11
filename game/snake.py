from pyglet import app
from pyglet.window import Window
from pyglet import image
from pyglet import clock
from pyglet.window import key
from pyglet import resource
from pyglet import media
from pyglet import text
from itertools import cycle
from random import randint

# Width and Height of the window screen
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
# The size of each of the blocks/segments used to make the snake, the apple and the obsticles
CELL_SIZE = 20
# Maximum number of obsticles generated
MAX_OBSTACLE = 5
# Maximum number of blocks/segments for each obsticles
MAX_OBSTACLE_SEGMENT = 4
# The rate at which the screen updates, this also means how fast your snake will move
REFRESH_RATE = 1/13

window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
window.set_caption("Snake")

@window.event
def on_draw():
    window.clear()

    # Draw the obstacles
    for blocks in obstacle:
        for coords in blocks:
            draw_square(coords[0], coords[1], cell_size, color = (255, 215, 130, 0))
    # Draw the apple
    draw_square(apple_x, apple_y, cell_size, color = (255, 0, 0, 0))
    # Draw the snake's tail
    for coords in tail:
        draw_square(coords[0], coords[1], cell_size, color = (15, 110, 40, 0))
    # Draw the snake's head
    draw_square(snake_x, snake_y, cell_size, color = (23, 163, 60, 0))

    if game_over:
        draw_game_over()
    
    if idle:
        draw_guide()

    draw_score()

def new_game():
    global snake_x, snake_y, snake_dx, snake_dy, tail, apple_x, apple_y, obstacle, game_over, idle

    # Start the snake in the middle
    snake_x = window.width // cell_size // 2 * cell_size
    snake_y = window.height // cell_size // 2 * cell_size

    snake_dx, snake_dy = 0, 0
    tail = []
    obstacle = []

    apple_x, apple_y = 0, 0
    # Place the apple randomly
    place_apple()

    # Place the obstacles randomly
    place_obstacle()

    game_over = False
    idle = True

# draw the shape that is used for the segments of the snake as well as the apple
def draw_square(x, y, size, color = (255, 255, 255, 0)):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x, y)

# place the apple on a random coordinate
def place_apple():
    global apple_x, apple_y
    apple_x = randint(0, (window.width // cell_size) - 1) * cell_size
    apple_y = randint(0, (window.height // cell_size) - 1) * cell_size

def place_obstacle():
    global obstacle

    obstacle_x, obstacle_y = 0, 0
    direction = 0

    for i in range (MAX_OBSTACLE):
        obstacle_x = randint(0, (window.width // cell_size) - 1) * cell_size
        obstacle_y = randint(0, (window.height // cell_size) - 1) * cell_size
        obstacle.append([])
        obstacle[0].append((obstacle_x, obstacle_y))
        for j in range(MAX_OBSTACLE_SEGMENT - 1):
            direction = randint(1, 4)
            if direction == 1:
                obstacle_x += -cell_size
            elif direction == 2:
                obstacle_x += cell_size
            elif direction == 3:
                obstacle_y += cell_size
            elif direction == 4:
                obstacle_y += -cell_size
            obstacle[0].append((obstacle_x, obstacle_y))

def draw_guide():
    guide_text = text.Label('(Press any arrow keys to start)', font_size=20,
                            x=window.width//2, y=window.height//2 - (1.5 * cell_size), width=window.width, align='center',
                            anchor_x='center', anchor_y='center', multiline=True)
    guide_text.draw()
    

def draw_game_over():
    game_over_text = text.Label(f'Score: {len(tail)}\n(Press space to restart)', font_size=24,
                                x=window.width//2, y=window.height//2, width=window.width, align='center',
                                anchor_x='center', anchor_y='center', multiline=True)
    game_over_text.draw()

def draw_score():
    score_text = text.Label(f'{len(tail)}', font_size=24,
                                x=window.width//10, y=window.height//1.1, width=window.width, align='center',
                                anchor_x='center', anchor_y='center', multiline=True)
    score_text.draw()

@window.event
def on_key_press(symbol, modifiers):
    global snake_dx, snake_dy, game_over, idle

    if (symbol == key.LEFT or symbol == key.RIGHT or symbol == key.UP or symbol == key.DOWN):
        idle = False

    if not game_over:
        if symbol == key.LEFT:
            if snake_dx == 0:
                snake_dx = -cell_size
                snake_dy = 0
        elif symbol == key.RIGHT:
            if snake_dx == 0:
                snake_dx = cell_size
                snake_dy = 0
        elif symbol == key.UP:
            if snake_dy == 0:
                snake_dx = 0
                snake_dy = cell_size
        elif symbol == key.DOWN:
            if snake_dy == 0:
                snake_dx = 0
                snake_dy = -cell_size
    else:
        if symbol == key.SPACE:
            new_game()

def update(dt):
    global snake_x, snake_y, apple_x, apple_y, game_over
    
    if game_over:
        return
    
    if game_over_condition():
        game_over = True
        crash.play()
        return

    # Add a new tail segment behind the head
    tail.append((snake_x, snake_y))

    # Update the position of the snake's head
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if apple is eaten
    if snake_x == apple_x and snake_y == apple_y:
        eat.play()
        place_apple()
        obstacle.clear()
        place_obstacle()
    else:
        # Remove the new tail segment if the apple is not eaten
        tail.pop(0)


def game_over_condition():
    # Collision with edge
    condition1 = snake_x + snake_dx < 0 or snake_x + snake_dx > window.width - cell_size or snake_y + snake_dy < 0 or snake_y + snake_dy > window.height - cell_size
    # Collision with tail
    condition2 = (snake_x, snake_y) in tail
    # Collision with obstacles
    condition3 = False
    for blocks in obstacle:
        if (snake_x, snake_y) in blocks:
            condition3 = True
    return condition1 or condition2 or condition3

# Sounds used in the game
eat = resource.media('sound/eat.mp3', streaming=False)
crash = resource.media('sound/crash.wav', streaming=False)
bgm = resource.media('sound/bgm.mp3')
playlist = cycle([bgm])

player = media.Player()
player.queue(playlist)
player.play()

# Width and height of a snake segment
cell_size = CELL_SIZE

new_game()

clock.schedule_interval(update, REFRESH_RATE)

app.run()