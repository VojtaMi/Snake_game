import time
from turtle import Turtle
from segment import Segment, Direction
import utils

# constants
STEP_SIZE = 4
SNAKE_SPEED = 0.1
GRID_SIZE = 20


class SnakeBody:
    def __init__(self):
        self.head = Segment()
        self.tail = self.head
        self.pin_segment(GRID_SIZE)
        self.head_switch = Direction.RIGHT
        self.snake_animation = SnakeAnimation(self)

    def pin_segment(self, grid_size):
        new_tail = Segment()
        self.tail.pin(new_tail, grid_size)
        self.tail = new_tail

    def turn(self, direction):
        heading = self.head.heading()
        if (heading == Direction.UP or heading == Direction.DOWN) and (
                direction == Direction.LEFT or direction == Direction.RIGHT):
            self.head_switch = direction
        elif (heading == Direction.LEFT or heading == Direction.RIGHT) and (
                direction == Direction.UP or direction == Direction.DOWN):
            self.head_switch = direction

    def _pass_directions(self):
        later_segment = self.tail
        earlier_segment = later_segment.previous_segment
        while earlier_segment:
            later_segment.setheading(earlier_segment.heading())
            later_segment = earlier_segment
            earlier_segment = earlier_segment.previous_segment

    def _move_all_segments(self, grid_size):
        current_segment = self.head
        while current_segment:
            current_segment.forward(grid_size)
            current_segment = current_segment.next_segment

    def move(self, grid_size, screen):
        self.head.setheading(self.head_switch)
        self.snake_animation.animate(screen)
        self._move_all_segments(grid_size)
        self._pass_directions()

    def segments_positions(self):
        positions = []
        index_segment = self.head
        while index_segment:
            positions.append(index_segment.pos())
            index_segment = index_segment.next_segment
        return positions

    def collision(self):
        # collision with border wall
        if abs(self.head.xcor()) > (280 + 1) or abs(self.head.ycor()) > (280 + 1):
            return True
        # collision with own body
        body_segment = self.tail
        while body_segment is not self.head:
            if utils.check_proximity(body_segment.pos(), self.head.pos()):
                return True
            body_segment = body_segment.previous_segment
        return False



class SnakeAnimation:
    def __init__(self, snake):
        self.draw_body_turtle = DrawTurtle()
        self.draw_tail_turtle = DrawTurtle()
        self.draw_head_turtle = DrawTurtle()
        self.snake = snake

    def animate(self, screen):
        self._draw_static_body()

        frames = int(GRID_SIZE / STEP_SIZE)
        for frame in range(frames):
            self._animate_tail_movement(frame)
            self._animate_head_movement(frame)
            screen.update()
            time.sleep(SNAKE_SPEED / frames)

    def _draw_static_body(self):
        # draws a line from the new tail position to the old head position
        self.draw_body_turtle.clear()
        self.draw_body_turtle.penup()

        from_segment = self.snake.tail.previous_segment
        self.draw_body_turtle.goto(from_segment.pos())
        self.draw_body_turtle.pendown()

        while from_segment is not self.snake.head:
            self.draw_body_turtle.setheading(from_segment.heading())
            self.draw_body_turtle.forward(GRID_SIZE)
            from_segment = from_segment.previous_segment

    def _animate_tail_movement(self, frame):
        new_tail_pos = self.snake.tail.previous_segment.pos()
        complement_fraction_distance = GRID_SIZE - (STEP_SIZE * frame)

        self.draw_tail_turtle.clear()
        self.draw_tail_turtle.penup()
        self.draw_tail_turtle.goto(new_tail_pos)
        self.draw_tail_turtle.pendown()
        self.draw_tail_turtle.setheading(self.snake.tail.heading())
        self.draw_tail_turtle.back(complement_fraction_distance)

    def _animate_head_movement(self, frame):
        fraction_distance = STEP_SIZE * frame
        self.draw_head_turtle.clear()
        self.draw_head_turtle.showturtle()
        # grow head
        self.draw_head_turtle.penup()
        self.draw_head_turtle.goto(self.snake.head.pos())
        self.draw_head_turtle.pendown()
        self.draw_head_turtle.setheading(self.snake.head.heading())
        self.draw_head_turtle.forward(fraction_distance)

    def wipe_snake(self):
        self.draw_body_turtle.clear()
        self.draw_head_turtle.clear()
        self.draw_tail_turtle.clear()
        self.draw_head_turtle.hideturtle()


class DrawTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(20)
        self.pencolor("blue")
        self.fillcolor("purple")
        self.shape("triangle")
        self.turtlesize(1.7)
        self.hideturtle()
