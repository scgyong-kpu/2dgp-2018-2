from pico2d import *
import game_framework

class Button:
    def __init__(self, normal, selected, x, y):
        self.normalImage = load_image(normal)
        self.selectedImage = load_image(selected)
        self.x, self.y = x, y
        self.selected = False
    def draw(self):
        if self.selected:
            self.selectedImage.draw(self.x, self.y)
        else:
            self.normalImage.draw(self.x, self.y)
    def hits(self, x, y):
        hw, hh = self.normalImage.w // 2, self.normalImage.h // 2
        if x < self.x - hw: return False
        if x > self.x + hw: return False
        if y < self.y - hh: return False
        if y > self.y + hw: return False
        return True

buttons = []
def selectButton(b):
    size = len(buttons)
    for i in range(size):
        if buttons[i] == b:
            print(str(i) + ' has been selected')
            buttons[i].selected = True
        else:
            buttons[i].selected = False

def handle_events():
    global boy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        elif e.type == SDL_MOUSEMOTION:
            x, y = e.x, get_canvas_height() - e.y
            for b in buttons:
                if b.hits(x, y):
                    selectButton(b)

def enter():
    global buttons
    buttons.append(Button('check_n.png', 'check_p.png', 200, 300))
    buttons.append(Button('check_n.png', 'check_p.png', 400, 300))
    buttons.append(Button('check_n.png', 'check_p.png', 600, 300))

def draw():
    clear_canvas()
    for b in buttons:
        b.draw()
    update_canvas()

def update():
    delay(0.03)

# fill here

def exit():
    pass

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]  
    open_canvas()
    game_framework.run(current_module)
    close_canvas()
