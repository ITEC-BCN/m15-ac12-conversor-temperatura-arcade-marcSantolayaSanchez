function menu(): number {
    
    opcio_usuari = game.askForNumber("     1 = Fahrenheit,          2 = Centígrads", 1)
    return opcio_usuari
}

function salutacio(opcio: number) {
    let calculo_usuarioF: number;
    let resultadoF: number;
    let calculo_usuarioC: number;
    let resultadoC: number;
    if (opcio == 1) {
        game.showLongText("Calcular Fahrenheit ", DialogLayout.Top)
        calculo_usuarioF = game.askForNumber("Pon un numero que quieras calcular a Fahrenheit", 4)
        resultadoF = Math.round((calculo_usuarioF * 9 / 5 + 32) * 100) / 100
        game.showLongText(resultadoF, DialogLayout.Bottom)
    } else if (opcio == 2) {
        game.showLongText("Calcular Centígrads", DialogLayout.Top)
        calculo_usuarioC = game.askForNumber("Pon un numero que quieras calcular a Centígrads", 4)
        resultadoC = Math.round((calculo_usuarioF - 32 * 5 / 9) * 100) / 100
        game.showLongText(resultadoC, DialogLayout.Bottom)
    } else {
        game.showLongText("Opció no vàlida", DialogLayout.Bottom)
    }
    
    salutacio(menu())
}

let opcio_usuari = 0
//  MAIN DE LA APP
scene.setBackgroundImage(scene.backgroundImage())
salutacio(menu())
