from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

app = Ursina()

# variable to hold surface mesh
surface = Entity(scale=100, scale_y=50, collision=True)

# main update loop
def update():
    player.y += held_keys['space'] * 1
    player.y -= held_keys['shift'] * 1

def input(key):
    if key == 'escape':
        player.disable()
        fb = FileBrowser(file_types=('.png'), enabled=True, selection_limit=1)
        fb.on_submit = on_submit

    if key == 'r':
        player.x = 0
        player.y = 0
        player.z = 0

# actions on file submit
fb = FileBrowser(file_types=('.png'), enabled=True, selection_limit=1)

def on_submit(path):
    path = os.path.relpath(path[0])
    surface.model = Terrain(str(path), skip=1)
    # check if there is a color image present
    color_path = path[:-4] + '-color.png'
    if os.path.exists(color_path):
        surface.texture = str(color_path)
    else:
        surface.texture = str(path)         # use same image to texture surface
    surface.y = -50                        # put below origin so camera always starts above
    player.enable()

fb.on_submit = on_submit

Sky()

# camera control
player = FirstPersonController(speed=50, gravity=0, collider='box')
player.disable()
#EditorCamera()

# generic settings
mouse.visible = True
window.title = 'First-person AFM'
window.borderless = False        
window.fullscreen = False        
window.exit_button.visible = True
window.fps_counter.enabled = True

# run the app
if __name__ == "__main__":
    app.run()
