def on_button_pressed_a():
    kukla.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    kukla.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

kukla: game.LedSprite = None
kukla = game.create_sprite(2, 4)
balon = game.create_sprite(randint(0, 4), 0)
süre = 1000
game.set_score(0)
game.set_life(5)

def on_forever():
    global süre
    basic.pause(süre)
    balon.change(LedSpriteProperty.Y, 1)
    basic.pause(süre)
    if kukla.is_touching(balon):
        game.add_score(1)
        balon.set(LedSpriteProperty.Y, 0)
        balon.set(LedSpriteProperty.X, randint(0, 4))
        if süre > 250:
            süre += -50
    elif balon.get(LedSpriteProperty.Y) == 4:
        game.remove_life(1)
        balon.set(LedSpriteProperty.Y, 0)
        balon.set(LedSpriteProperty.X, randint(0, 4))
basic.forever(on_forever)
