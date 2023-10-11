# Library Overview

## Library Selection

For this Exploration Activity, I decided on Pyglet as my library of choice to research on. 

## Pyglet

Pyglet lets you use the game development tools seen in game engines with Python to create your games. Additionally, it is also used for other multimedia applications that can benefit from the useful functionalities of these tools.

## Functionalities

For my sample project, I recreated snake game to demonstrate the functionalities of Pyglet, the modules used are listed below:

1. Initiating the game canvas and update it at an interval using the built-in fucntion `on_draw()` and the `clock` module with `update(dt)`.

```
#create the window
window = window(WINDOW_WIDTH, WINDOW_HEIGHT)

@window.event
def on_draw():
    window.clear()
    draw_something(x, y, size)

def update(dt):
    snake_x += snake_dx
    snake_y += snake_dy

clock.schedule_interval(update, 1/15)

app.run()
```

2. Using the `image` module to create game objects such as the snake, the apple and the obsticles using `image.create()` and then drawing the image to the screen using `blit()`.

```
# draw the shape that is used for the segments of the snake, the apple as well as the obsticles
def draw_square(x, y, size, color = (255, 255, 255, 0)):
    img = image.create(size, size, image.SolidColorImagePattern(color))
    img.blit(x, y)
```

3. Using the built-in function `on_key_press()` and `key` module for event handling.

```
@window.event
def on_key_press(symbol, modifiers):
    global snake_dx, snake_dy

    if symbol == key.LEFT:
        if snake_dx == 0:
            snake_dx = -cell_size
            snake_dy = 0
    elif symbol == key.RIGHT:
        if snake_dx == 0:
            snake_dx = cell_size
            snake_dy = 0
...
```
4. Using the `resource` module to import sound effects into the project and `media` module to play sounnds during the game

```
def update(dt):
    global snake_x, snake_y, apple_x, apple_y, game_over
    
    if game_over_condition():
        game_over = True
        crash.play()
        return

    # Check if apple is eaten
    if snake_x == apple_x and snake_y == apple_y:
        eat.play()

eat = resource.media('sound/eat.mp3', streaming=False)
crash = resource.media('sound/crash.wav', streaming=False)
```

5. Using the `text` module to show players on how to play the game, the score, and the game over text at the end.

```
@window.event
def on_draw():
    window.clear()

    draw_score()

def draw_score():
    score_text = text.Label(f'{len(tail)}', font_size=24, x=window.width//10, y=window.height//1.1, width=window.width, align='center', anchor_x='center', anchor_y='center', multiline=True)

    score_text.draw()
```
## When was Pyglet created

After a little digging on the internet, I have found that there is little information about when Pyglet was first released on Wikipedia or any other online articles/sources. However, upon looking at the license file in the Pyglet open-source repository on github, Pyglet dates back to around 2006 and was first created by Alex Holkner [[1]](https://github.com/pyglet/pyglet/blob/master/LICENSE).

## Why I chose Pyglet

There were really only two options that I had while choosing which Python library to use for my project, which was Pyglet and Pygame [[2]](https://www.pygame.org/wiki/about). While Pygame is the more popular choice among the two, I found Pyglet to be a much more simpler library to understand, learn and write code with, which is the main influence on why I chose this library, especially for a project on a smaller size such as this.

Pyglet is also object-oriented and has more more modern functionalities, such as built-in support for OpenGL [[3]](https://www.opengl.org/) making Pyglet much faster than Pygame.

For the reasons listed above, I decided to use Pyglet as my library of choice.

## Reflection

### influence in learning Python

This experience has helped a lot in familiarizing myself in the Python language and its syntax. And learning how to use import and use libraries. Additionally, not only did I had the chance to try out the functionalities of the `Pyglet` library, I also made use of other common Python libraries such as `itertools` and `random` for my program.

### Overall experience

My overall exprience with Pyglet was very good. After reading the documentation, I was comfortable with the library functionalities and started to focus more on the logical part of the game. Other online resources [[4]](https://www.youtube.com/playlist?list=PL42MzI01SYj7unM-kMN1nf70smlIsLDc0) have also helped me tremendously in the building process of this program, I'd be lying if I said I did not follow any tutorial on how to build the frame and main functionalities of the game. However, using the already built frame of the snake game, I also gave the app some of my personal touch and implementations, namely making the game more challenging by adding obstacles, as well as showing more texts and using more sounds.

Because of time limitations, there are some more features I haven't had a chance to experiment on as well as optimizing the already existing game logic such as the obstacles in the game. As of now, the obstacle is generated randomly with no limitations, which means that if you're really unlucky, they could literally on top of your snake and make you lose the game instantly. That is why even after handing in this project, I'd still like to work on this project some more in my free time. It really was a fun time putting this all together.

As Python is an extremely popular choice for beginner programmers. I would highly recommend anyone who picked up Python and is interested in game development to tryout Pyglet before moving on to the bigger and more confusing game engines used today.

## References
[1] [https://github.com/pyglet/pyglet/blob/master/LICENSE](https://github.com/pyglet/pyglet/blob/master/LICENSE)

[2] [https://www.pygame.org/wiki/about](https://www.pygame.org/wiki/about)

[3] [https://www.opengl.org/](https://www.opengl.org/)

[4] [Snake game tutorial by Justin Robertson](https://www.youtube.com/playlist?list=PL42MzI01SYj7unM-kMN1nf70smlIsLDc0)


