c = color(0)
x = 0
y = 100
speed = 1

def setup():
  size(200,200);

def draw():
  background(255);
  move();
  display();

def move():
  global x
  x = x + speed;
  if (x > width):
    x = 0;

def display():
  fill(c);
  rect(x,y,30,10);
