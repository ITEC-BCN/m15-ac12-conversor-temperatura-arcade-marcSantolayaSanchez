def menu():
    global opcio_usuari
    opcio_usuari = game.ask_for_number("     1 = Fahrenheit,          2 = Centígrads", 1)
    return opcio_usuari
def salutacio(opcio: number):
    if opcio == 1:
        game.show_long_text("Calcular Fahrenheit ", DialogLayout.TOP)
        calculo_usuarioF = game.ask_for_number("Pon un numero que quieras calcular a Fahrenheit",4)
        resultadoF = Math.round((calculo_usuarioF * 9/5 + 32) * 100) / 100 
        game.show_long_text(resultadoF, DialogLayout.BOTTOM)
    elif opcio == 2:
        game.show_long_text("Calcular Centígrads", DialogLayout.TOP)
        calculo_usuarioC = game.ask_for_number("Pon un numero que quieras calcular a Centígrads",4)
        resultadoC = Math.round((calculo_usuarioF - 32* 5/9)  * 100) / 100
        game.show_long_text(resultadoC, DialogLayout.BOTTOM)
    else:
        game.show_long_text("Opció no vàlida", DialogLayout.BOTTOM)
    salutacio(menu())
opcio_usuari = 0
# MAIN DE LA APP
scene.set_background_image(scene.background_image())
salutacio(menu())