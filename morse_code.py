'''
Created by Natalya Morales
July 29, 2024
Program that uses buttons as Morse code to print a word
'''
from hub import port, button, light_matrix, sound
import color_sensor, color, runloop

# Diccionario para convertir de código Morse a letras
diccionario = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

async def main():
    arreglo_palabra = []
    codigo_morse = ""
    arreglo_morse = []
    print("Introduce letras en código Morse con los botones. Usa el sensor de color para finalizar la palabra.")
    print("Botón izquierdo: punto (.), Botón derecho: raya (-)")

    while True:
        if button.pressed(button.LEFT):
            await sound.beep(440, 100, 100)
            arreglo_morse.append(".")
            print(". agregado")
            await runloop.sleep_ms(1500) # Evitar múltiples registros por una sola pulsación

        elif button.pressed(button.RIGHT):
            await sound.beep(440, 500, 100)
            arreglo_morse.append("-")
            print("- agregado")
            await runloop.sleep_ms(1500) # Evitar múltiples registros por una sola pulsación

        # Comprobar si se ha detectado el color rojo (final de palabra)
        elif color_sensor.color(port.B) == color.YELLOW:
            codigo_morse = ''.join(arreglo_morse)
            print(codigo_morse)
            arreglo_morse.clear()
            if codigo_morse in diccionario:
                letra = diccionario[codigo_morse]
                arreglo_palabra.append(letra)
                print(letra)
                light_matrix.write(letra)
            else:
                print("Código Morse inválido. Por favor, inténtalo de nuevo.")

            codigo_morse = ""
            await runloop.sleep_ms(1500) # Esperar un poco para evitar múltiples detecciones

        # Si se ha detectado el color rojo nuevamente, finalizar la palabra
        if color_sensor.color(port.B) == color.RED and not codigo_morse:
            break

    palabra_completa = ''.join(arreglo_palabra)
    print("La palabra completa es:", palabra_completa)
    light_matrix.write(palabra_completa)

runloop.run(main())