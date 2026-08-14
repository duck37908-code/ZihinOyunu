import math, random
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.widget import Widget

class IllusionGameWidget(Widget):
    def __init__(self, **kwargs):
        super(IllusionGameWidget, self).__init__(**kwargs)
        self.num_points, self.current_shape, self.angle_y, self.rotation_speed = 600, 0, 0.0, 0.03
        self.points = self.create_shape(self.current_shape)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def create_shape(self, shape_type):
        pts = []
        if shape_type == 0:
            for _ in range(self.num_points):
                angle = random.uniform(0, 2 * math.pi)
                pts.append([120 * math.cos(angle), random.uniform(-150, 150), 120 * math.sin(angle)])
        elif shape_type == 1:
            for _ in range(self.num_points):
                z = random.uniform(-140, 140)
                phi = random.uniform(0, 2 * math.pi)
                r_slice = math.sqrt(140**2 - z**2)
                pts.append([r_slice * math.cos(phi), r_slice * math.sin(phi), z])
        elif shape_type == 2:
            half = 100
            for _ in range(self.num_points):
                face = random.randint(0, 5)
                u, v = random.uniform(-half, half), random.uniform(-half, half)
                if face == 0: pts.append([half, u, v])
                elif face == 1: pts.append([-half, u, v])
                elif face == 2: pts.append([u, half, v])
                elif face == 3: pts.append([u, -half, v])
                elif face == 4: pts.append([u, v, half])
                else: pts.append([u, v, -half])
        return pts

    def on_touch_down(self, touch):
        self.current_shape = (self.current_shape + 1) % 3
        self.points = self.create_shape(self.current_shape)
        return True

    def update(self, dt):
        self.canvas.clear()
        cx, cy = self.width / 2, self.height / 2
        self.angle_y += self.rotation_speed
        cos_a, sin_a = math.cos(self.angle_y), math.sin(self.angle_y)
        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=(0, 0), size=(self.width, self.height))
            Color(1, 1, 1, 1)
            for pt in self.points:
                rx = pt[0] * cos_a + pt[2] * sin_a
                Ellipse(pos=(cx + rx - 2, cy + pt[1] - 2), size=(4, 4))

class MainApp(App):
    def build(self): return IllusionGameWidget()

if __name__ == "__main__": MainApp().run()
  
