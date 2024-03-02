import time
from turtle import Turtle
from segment import Segment, Direction
import utils

# constants
GRID_SIZE = 20

# smaller number = faster snake (less time between frames)
SNAKE_SPEED = 0.1


class SnakeBody:
    def __init__(self):
        """ creates a snake of two segments facing right"""
        self.head = Segment()
        self.tail = self.head
        self.pin_segment(GRID_SIZE)
        self.head_switch = Direction.RIGHT
        self.snake_animation = SnakeAnimation(self)

    def pin_segment(self, grid_size):
        """ Adds a new segment behind the snake's tail """
        new_tail = Segment()
        self.tail.pin(new_tail, grid_size)
        self.tail = new_tail

    def turn(self, direction):
        """
        If possible, changes the snake's direction
        :param direction: change of direction defined by user keyboard input
        """
        # current heading of snake
        heading = self.head.heading()

        # if snake is heading up or down, change is possible to left or right
        if (heading == Direction.UP or heading == Direction.DOWN) and (
                direction == Direction.LEFT or direction == Direction.RIGHT):
            self.head_switch = direction
        # if snake is heading left or right, change is possible up or down
        elif (heading == Direction.LEFT or heading == Direction.RIGHT) and (
                direction == Direction.UP or direction == Direction.DOWN):
            self.head_switch = direction

    def _pass_directions(self):
        """ When snakes moves by one grid, segments directions are updated"""
        # from tail to head (excluding), segments get direction of the segment that was in front of them
        later_segment = self.tail
        earlier_segment = later_segment.previous_segment
        while earlier_segment:
            later_segment.setheading(earlier_segment.heading())
            later_segment = earlier_segment
            earlier_segment = earlier_segment.previous_segment

    def _move_all_segments(self, grid_size):
        """ Move all segments one grid size in their direction"""
        current_segment = self.head
        while current_segment:
            current_segment.forward(grid_size)
            current_segment = current_segment.next_segment

    def move(self, grid_size, screen):
        """ Handle all processes of snake movement"""
        self.head.setheading(self.head_switch)
        self.snake_animation.animate(screen)
        self._move_all_segments(grid_size)
        self._pass_directions()

    def segments_positions(self):
        """
        Iterates over all segments of snake body to save their screen location
        :return: list of positions
        """
        positions = []
        index_segment = self.head
        while index_segment:
            positions.append(index_segment.pos())
            index_segment = index_segment.next_segment
        return positions

    def collision(self):
        """ Checks for snake collision with the wall or with its body"""

        # collision with border wall
        if abs(self.head.xcor()) > (280 + 1) or abs(self.head.ycor()) > (280 + 1):
            return True

        # collision with own body
        body_segment = self.tail
        while body_segment is not self.head:
            if utils.same_grid(body_segment.pos(), self.head.pos()):
                return True
            body_segment = body_segment.previous_segment
        return False


class SnakeAnimation:
    """ Displays the snake movement by splitting its move into fractional frames"""
    def __init__(self, snake):
        self.draw_body_turtle = DrawTurtle()
        self.draw_tail_turtle = DrawTurtle()
        self.draw_head_turtle = DrawTurtle()
        self.snake = snake

    def animate(self, screen):
        """ displays fractional movements of head and tail, defines inner static body section"""

        # inner static section is drawn only once per animation
        self._draw_static_body()

        # number of animation frames = 1 frame for every pixel
        frames = GRID_SIZE

        # displays a fractional change for a time
        for frame in range(frames):
            self._animate_tail_movement(frame)
            self._animate_head_movement(frame)
            screen.update()
            time.sleep(SNAKE_SPEED / frames)

    def _draw_static_body(self):
        """
        Draws a line from the new tail position to the old head position
            new tail position = where the tail is going to be at the end of animation
            old head position = where the head is at the beginning of animation
        """
        self.draw_body_turtle.clear()
        self.draw_body_turtle.penup()

        # new tail position is the position of the segment in front of the tail segment
        from_segment = self.snake.tail.previous_segment
        self.draw_body_turtle.goto(from_segment.pos())
        self.draw_body_turtle.pendown()

        # write a line following the segments to the "old head"
        while from_segment is not self.snake.head:
            self.draw_body_turtle.setheading(from_segment.heading())
            self.draw_body_turtle.forward(GRID_SIZE)
            from_segment = from_segment.previous_segment

    def _animate_tail_movement(self, frames):
        """ For every frame draw a smaller tail"""

        new_tail_pos = self.snake.tail.previous_segment.pos()
        # tail length is smaller by each frame
        complement_fraction_distance = GRID_SIZE - frames

        self.draw_tail_turtle.clear()
        self.draw_tail_turtle.penup()
        self.draw_tail_turtle.goto(new_tail_pos)
        self.draw_tail_turtle.pendown()
        self.draw_tail_turtle.setheading(self.snake.tail.heading())
        self.draw_tail_turtle.back(complement_fraction_distance)

    def _animate_head_movement(self, frames):
        """
        For every frame put head a bit forward
            head goes forward and snake's "neck" gets a bit longer
        """
        fraction_distance = frames
        self.draw_head_turtle.clear()
        self.draw_head_turtle.showturtle()
        # make "neck" longer, the head is at the top of the neck represented by the turtle
        self.draw_head_turtle.penup()
        self.draw_head_turtle.goto(self.snake.head.pos())
        self.draw_head_turtle.pendown()
        self.draw_head_turtle.setheading(self.snake.head.heading())
        self.draw_head_turtle.forward(fraction_distance)

    def wipe_snake(self):
        """ Remove snake from the screen"""
        self.draw_body_turtle.clear()
        self.draw_head_turtle.clear()
        self.draw_tail_turtle.clear()
        self.draw_head_turtle.hideturtle()


class DrawTurtle(Turtle):
    """
    Object to draw snake's body
    Draws a blue line, the turtle is purple and triangular, visible only for head
    """
    def __init__(self):
        super().__init__()
        self.pensize(20)
        self.pencolor("blue")
        self.fillcolor("purple")
        self.shape("triangle")
        self.turtlesize(1.7)
        self.hideturtle()
