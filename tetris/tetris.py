import pyglet
import gametypes
      
WIDTH = 800
HEIGHT = 600
BOARD_X = 445
BOARD_Y = 13     
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 24

window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_vsync(False)

###### load resources ######

backgroundImage = pyglet.resource.image('background.jpg')
blocksImage = pyglet.resource.image('block.png')
gametypes.TetrominoType.classInit(blocksImage, BLOCK_SIZE)

###### init game state ######

board = gametypes.Board(BOARD_X, BOARD_Y, GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE)
infoDisplay = gametypes.InfoDisplay(window)
input = gametypes.Input()
game = gametypes.Game(board, infoDisplay, input, backgroundImage)
            
@window.event
def on_key_press(symbol, modifiers):
    input.processKeypress(symbol, modifiers)
               
@window.event
def on_text_motion(motion):
    input.processTextMotion(motion)

@window.event
def on_draw():
    # don't need to window.clear() because the whole window gets redrawn in game.draw()
    game.draw()    
  
def update(dt):
    game.update()
        
pyglet.clock.schedule_interval(update, 1/60.0)        
pyglet.app.run()