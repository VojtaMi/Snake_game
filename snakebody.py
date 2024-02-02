import time
from turtle import Turtle
from segment import Segment, Direction

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

    def _animate_snake_movement(self, screen):
        # draw main body
        draw_body_turtle = DrawTurtle()
        draw_body_turtle.hideturtle()
        draw_body_turtle.penup()

        from_segment = self.tail.previous_segment
        draw_body_turtle.goto(from_segment.pos())
        draw_body_turtle.pendown()
        # draw main body
        while from_segment is not self.head:
            draw_body_turtle.setheading(from_segment.heading())
            draw_body_turtle.forward(GRID_SIZE)
            from_segment = from_segment.previous_segment

        steps = int(GRID_SIZE / STEP_SIZE)
        new_tail_pos = self.tail.previous_segment.pos()

        draw_ht_turtle = DrawTurtle()
        for i in range(steps):
            fraction_distance = STEP_SIZE * i
            complement_fraction_distance = GRID_SIZE - (STEP_SIZE * i)
            # shorten tail
            draw_ht_turtle.penup()
            draw_ht_turtle.goto(new_tail_pos)
            draw_ht_turtle.pendown()
            draw_ht_turtle.setheading(self.tail.heading())
            draw_ht_turtle.back(complement_fraction_distance)

            # grow head
            draw_ht_turtle.penup()
            draw_ht_turtle.goto(self.head.pos())
            draw_ht_turtle.pendown()
            draw_ht_turtle.setheading(self.head.heading())
            draw_ht_turtle.forward(fraction_distance)

            # display fractional shift
            draw_ht_turtle.penup()
            screen.update()
            time.sleep(SNAKE_SPEED / steps)
            draw_ht_turtle.clear()

        draw_body_turtle.clear()
        draw_body_turtle.hideturtle()
        draw_ht_turtle.hideturtle()

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
        self._animate_snake_movement(screen)
        self._move_all_segments(grid_size)
        self._pass_directions()


class DrawTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(20)
        self.pencolor("blue")
        self.fillcolor("purple")
        self.shape("triangle")
        self.turtlesize(1.7)

