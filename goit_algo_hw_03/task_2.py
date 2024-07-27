import turtle
import sys
import os

def setup_turtle():
    window = turtle.Screen()
    window.bgcolor("white")
    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("blue")
    return snowflake

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        for angle in [60, -120, 60, 0]:
            koch_curve(t, length, level - 1)
            t.left(angle)

def draw_koch_snowflake(t, x, y, length, level):
    t.penup()
    t.goto(x - length/2, y + length/(2*3**0.5))
    t.pendown()
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def parse_arguments():
    if len(sys.argv) < 2:
        script_name = os.path.basename(sys.argv[0])
        print(f"Usage: python3 {script_name} <recursion_level>")
        sys.exit(1)
    return int(sys.argv[1])

def main():
    level = parse_arguments()
    length = 300.0

    snowflake = setup_turtle()
    draw_koch_snowflake(snowflake, 0, 0, length, level)
    
    snowflake.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()