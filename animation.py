import turtle
import math

class WaveAnimation:
    def __init__(self, frequency):
        self.frequency = frequency
        self.period = 1 / frequency

        # Create the turtle screen and set it up
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=400)
        self.screen.title("Wave Animation")
        self.screen.bgcolor("black")

        # Create the turtle object
        self.wave = turtle.Turtle()
        self.wave.speed(0)
        self.wave.color("white")
        self.wave.width(3)

    def draw_wave(self):
        x = 0
        while True:
            # Calculate the y-coordinate based on a sine function
            y = 100 * math.sin(2 * math.pi * self.frequency * x)

            # Move the turtle to the calculated coordinates
            self.wave.goto(x, y)

            # Increment x
            x += 0.1

            # Clear the wave after one period
            if x > self.period:
                self.wave.clear()
                x = 0

    def start_animation(self):
        # Call the draw_wave method to start the animation
        self.draw_wave()

        # Keep the turtle window open
        turtle.mainloop()

# Create an instance of the WaveAnimation class with a frequency of 5 Hz
animation = WaveAnimation(5)
animation.start_animation()
