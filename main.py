@namespace
class SpriteKind:
    Boton = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Nivel
    if otherSprite == BotonCelcius and controller.A.is_pressed():
        Nivel = 1
        manejo_nivel()
    if otherSprite == BotonFahreinheit and controller.A.is_pressed():
        Nivel = 2
        manejo_nivel()
sprites.on_overlap(SpriteKind.player, SpriteKind.Boton, on_on_overlap)

def inicio(opcio: number):
    if opcio == 1:
        game.show_long_text("Calcular Fahrenheit ", DialogLayout.TOP)
        calculo_usuarioF = game.ask_for_number("Pon un numero que quieras calcular a Fahrenheit", 4)
        resultadoF = Math.round((calculo_usuarioF * 9 / 5 + 32) * 100) / 100
        game.show_long_text(resultadoF, DialogLayout.BOTTOM)
    elif opcio == 2:
        game.show_long_text("Calcular Centígrads", DialogLayout.TOP)
        calculo_usuarioC = game.ask_for_number("Pon un numero que quieras calcular a Centígrads", 4)
        resultadoC = Math.round((calculo_usuarioC - 32 * 5 / 9) * 100) / 100
        game.show_long_text(resultadoC, DialogLayout.BOTTOM)
    else:
        game.show_long_text("Opció no vàlida", DialogLayout.BOTTOM)
def manejo_nivel():
    global BotonCelcius, BotonFahreinheit, Cursor
    if Nivel == 0:
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffff111fffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffff11111fffffffffff111fffffffffffffffffffffff11111ffffffffff111fffffffffffff111ffffffffffffffff111fffffffffff111fffffffffffffffffff
                        fffffffffffffffffffffffffffffffff11111fffffffff1111fffffffffffffffff11111111111ffffffffff1111ffffffffffff111ffffffffffffffff111fffffffffff1111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffff111111fffffff11111fffffffffffffff1111111111111ffffffffff11111ffffffffff1111ffffffffffffffff111fffffffffff1111ffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff11111fffffff11111fffffffffffffff11111111111ffffffffffff111111fffffffff1111ffffffffffffffff111fffffffffff1111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff1111ffffff111111fffffffffffffff1111fffffffffffffffffffff11111ffffffff111fffffffffffffffff111ffffffffffff111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff11111ffff1111111ffffffffffffff1111ffffffffffffffffffffff111111fffffff111ffffffffffffffff1111ffffffffffff111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff11111ff111111111ffffffffffffff1111fffffffffffffffffffffff11111fffffff111ffffffffffffffff1111ffffffffffff111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff111111111111f111ffffffffffffff111fffffffffffffffffffffffff11111ffffff111ffffffffffffffff111fffffffffffff111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff11111111111ff111ffffffffffffff111ffffffffffffffffffffffffff11111ffff1111ffffffffffffffff111fffffffffffff111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff111111111ffff111ffffffffffffff1111111ffffffffffffffffffffff11111ffff1111ffffffffffffffff111fffffffffffff111ffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff111111111fffff111ffffffffffffff111111111111111ffffffffffffff11111ffff111fffffffffffffffff111fffffffffffff111ffffffffffffffffff
                        ffffffffffffffffffffffffffffffffff1111f111ffffff111ffffffffffffff111111111111111ffffffffffffff111111fff111fffffffffffffffff111ffffffffffff1111ffffffffffffffffff
                        fffffffffffffffffffffffffffffffff1111fffffffffff111ffffffffffffff111ff1111111111ffffffffffffff1111111ff111fffffffffffffffff111ffffffffffff1111ffffffffffffffffff
                        ffffffffffffffffffffffffffffffff11111fffffffffff111ffffffffffffff111ffffffffffffffffffffffffff1111111ff111fffffffffffffffff111fffffffffff1111fffffffffffffffffff
                        fffffffffffffffffffffffffffffff11111ffffffffffff111ffffffffffffff111ffffffffffffffffffffffffff111f1111f111fffffffffffffffff111ffffffffff11111fffffffffffffffffff
                        ffffffffffffffffffffffffffffff11111fffffffffffff1111fffffffffffff111fffffffffffffffffffffffff1111f11111111fffffffffffffffff1111fffffffff11111fffffffffffffffffff
                        ffffffffffffffffffffffffffff111111ffffffffffffff1111fffffffffffff111fffffffffffffffffffffffff1111f11111111fffffffffffffffff1111ffffffff11111ffffffffffffffffffff
                        fffffffffffffffffffffffffff1111111fffffffffffffff111fffffffffffff111fffffffffff11111fffffffff111ffff111111fffffffffffffffff1111fffffff11111fffffffffffffffffffff
                        ffffffffffffffffffffffffff111111fffffffffffffffff111fffffffffffff1111ffffff111111111ffffffff1111fffff11111ffffffffffffffffff1111fffff111111fffffffffffffffffffff
                        fffffffffffffffffff111111111111ffffffffffffffffff111fffffffffffff1111111111111111111fffffff11111fffff11111ffffffffffffffffff11111fff111111ffffffffffffffffffffff
                        fffffffffffffffffff1111111111ffffffffffffffffffff111fffffffffffff1111111111111111ffffffffff1111fffffff1111ffffffffffffffffff111111111111ffffffffffffffffffffffff
                        fffffffffffffffffff111111111ffffffffffffffffffffffffffffffffffffff11111111111ffffffffffffff1111fffffff111ffffffffffffffffffff1111111111fffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111111ffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111fffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2ffffffffff2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222fffffffff2222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222ffffffff22222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222ffffffff224422222ffffffffffffff222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222fffffff224444222fffffffffffff2222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222ffffff2224444422ffffffffffff22222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222fffffff22444444222fffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22422222ffffff2244444442222ffffff22222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff224444222fffff22244444442222fffff22222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22444442222ffff22455444422222fff2224444222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff244444222222ff22455554442222fff2224444222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff4444444222222f24555555422222f22224444422ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2445544422222222455555422222f22224444422ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2445555542222222455555442222222224554422ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2245555544444444455555544442222244555422ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2255555544444445555555544444444455554222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2245555555555555555555555555555555554222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2224555555555555555555555555555555554222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff224555555555555555555555555555555554222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222455555555555555555555555555555554422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222455555555555555555555555555555554422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222455555555555555555555555555555554422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2f222455555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222455555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222445555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222445555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222445555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222445555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222445555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222445555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222445555555555555555555555555555544422fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222444555555555555555555555555555444222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222444555555555555555555555555555444222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222444555555555555555555555555555444222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222444455555555555555555555555554442222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222444455555555555555555555555554442222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222444455555555555555555555555554442222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222444445555555555555555555555544422222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222244445555555555555555555555444222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22224444455555555555555555555444222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222444445555555555555555554442222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222444444555555555555555544422222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22224444444555555555544444222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22224444445555554444444222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222444444444444444422222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222244444442222222222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222222222222222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff22222222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
    BotonCelcius = sprites.create(img("""
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
                    1 7 7 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 7 1 1 1 1 1 1 1 1 1 1 7 7 1
                    1 7 1 1 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 1 1 7 7 7 7 7 7 7 7 7 7 7 1
                    1 7 7 1 1 1 1 1 1 1 1 1 1 7 7 1
                    1 7 7 7 7 7 7 7 7 7 7 7 7 7 7 1
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        """),
        SpriteKind.Boton)
    BotonFahreinheit = sprites.create(img("""
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
                    1 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 1 1 1 1 1 1 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 1 1 1 1 1 1 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 1 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1
                    1 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        """),
        SpriteKind.Boton)
    Cursor = sprites.create(img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . 6 . . . . . . .
                    . . . . . . . 6 6 6 . . . . . .
                    . . . . . . 6 6 6 6 6 . . . . .
                    . . . . . . 6 6 6 6 6 . . . . .
                    . . . . . 6 6 6 6 6 6 6 . . . .
                    . . . . . 6 6 6 6 6 6 6 . . . .
                    . . . . 6 6 6 6 6 6 6 6 6 . . .
                    . . . . . . . 6 6 6 . . . . . .
                    . . . . . . . 6 6 6 . . . . . .
                    . . . . . . . 6 6 6 . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    BotonCelcius.set_position(26, 81)
    BotonFahreinheit.set_position(130, 81)
    Cursor.set_bounce_on_wall(True)
    Cursor.set_stay_in_screen(True)
    controller.move_sprite(Cursor)
    if Nivel == 1:
        inicio(2)
        game.reset()
    elif Nivel == 2:
        inicio(1)
        game.reset()
    else:
        pass
Cursor: Sprite = None
BotonFahreinheit: Sprite = None
BotonCelcius: Sprite = None
Nivel = 0
opcio_usuari = 0
Nivel = 0
manejo_nivel()