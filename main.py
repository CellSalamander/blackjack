import pygame
import math

HEIGHT , WIDTH = 1000,1400
pygame.init()

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Orbit")

bodies = [
    {"name": "Sun", "mass": 1.989e30, "radius": 80, "distance": 0, "color": (255, 255, 0)},
    {"name": "Mercury", "mass": 3.30e23, "radius": 5, "distance": 50, "color": (200, 200, 200)},
    {"name": "Venus", "mass": 4.87e24, "radius": 9, "distance": 80, "color": (255, 220, 180)},
    {"name": "Earth", "mass": 5.97e24, "radius": 10, "distance": 110, "color": (0, 102, 255)},
    {"name": "Mars", "mass": 6.42e23, "radius": 7, "distance": 160, "color": (255, 80, 20)},
    {"name": "Jupiter", "mass": 1.90e27, "radius": 30, "distance": 400, "color": (204, 153, 102)},
]

planets = []
Sun = None
G = 6.674e-11
PIXEL_TO_METER = 1e9
TIME_SCALE = 1000000

class Body:

    def __init__(self,name,mass,radius,distance,color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance = distance
        self.color = color
        
        self.x = WIDTH//2
        self.y = HEIGHT//2

        self.r = 0
        self.angle = 0
        self.v = 0
    
    def draw_body(self):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    
    
    def get_v(self):
        self.r = Sun.radius + self.distance + self.radius
        self.v = (G * Sun.mass / (self.r*PIXEL_TO_METER))**0.5
        

    def move(self):
        self.get_v()
        
        dt = 1 / 60 
        pixels_per_frame = (self.v*dt*TIME_SCALE)/PIXEL_TO_METER

        self.angle += pixels_per_frame/self.r

        self.x = Sun.radius+WIDTH//2 + math.cos(self.angle) * self.distance
        self.y = Sun.radius+HEIGHT//2 + math.sin(self.angle) * self.distance



    
def fill_bodies(bodies):

    global Sun 

    for body in bodies:

        name = body["name"]
        mass = body["mass"]
        radius = body["radius"]
        distance  = body["distance"]
        color = body["color"]
        
        if body["name"] == "Sun":
            Sun = Body(name,mass,radius,distance,color)
        else:
            planet = Body(name,mass,radius,distance,color)
            planets.append(planet)
    
def draw_planets():

    for planet in planets:
        planet.draw_body()
            

def main():

    fill_bodies(bodies)

    run = True
    clock = pygame.time.Clock()
    while run:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        win.fill((0,0,0))

        Sun.draw_body()

        for planet in planets:
            planet.move()

        draw_planets()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()