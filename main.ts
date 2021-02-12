input.onButtonPressed(Button.A, function () {
    kukla.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    kukla.change(LedSpriteProperty.X, 1)
})
let kukla: game.LedSprite = null
kukla = game.createSprite(2, 4)
let balon = game.createSprite(randint(0, 4), 0)
let süre = 1000
game.setScore(0)
game.setLife(5)
basic.forever(function () {
    basic.pause(süre)
    balon.change(LedSpriteProperty.Y, 1)
    basic.pause(süre)
    if (kukla.isTouching(balon)) {
        game.addScore(1)
        balon.set(LedSpriteProperty.Y, 0)
        balon.set(LedSpriteProperty.X, randint(0, 4))
        if (süre > 250) {
            süre += -50
        }
    } else if (balon.get(LedSpriteProperty.Y) == 4) {
        game.removeLife(1)
        balon.set(LedSpriteProperty.Y, 0)
        balon.set(LedSpriteProperty.X, randint(0, 4))
    }
})
