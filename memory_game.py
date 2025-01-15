'''
Created by Natalya Morales
Agust 05, 2024
Program that creates a memory game with lights
'''
from hub import light_matrix, port, sound
import random
import runloop, color_sensor, color, color_matrix

# Función para generar una secuencia de colores
def generar_secuencia(length, numeros_base):
    secuencia = [random.choice(numeros_base) for _ in range(length)]
    return secuencia

# Función para mostrar la secuencia al jugador
async def mostrar_secuencia(secuencia):
    level = len(secuencia) - 3
    print("Nivel ", level)
    light_matrix.write(str(level))
    for color in secuencia:
        color_matrix.set_pixel(port.D, 1, 1, (color, 10))
        await runloop.sleep_ms(1000)
        color_matrix.clear(port.D)
        await runloop.sleep_ms(500)

# Función  Main
async def main():
    length = 4
    numeros_base = [3, 6, 7, 9]
    print("Bienvenido al juego de memoria!")
    print("Ve la secuencia de colores y repite la secuencia con los bloques en el sensor")
    await runloop.sleep_ms(1000)
    # Se genera la secuencia
    secuencia = generar_secuencia(length, numeros_base)

    # Se muestra la secuencia en color matrix
    print("Secuencia generada: ", secuencia)
    await mostrar_secuencia(secuencia)
    await runloop.sleep_ms(1000)
    await sound.beep(440, 1000, 100)

    i = 0 # Inicialización del contador
    result = []

    # Se guardan en una lista los colores del usuario
    while True:
        if color_sensor.color(port.B) in numeros_base:
            result.append(color_sensor.color(port.B)) # Se agrega a result el color
            print(result[i])

            if result[i] == secuencia[i]: # Color correcto
                light_matrix.show_image(light_matrix.IMAGE_HAPPY)
                await sound.beep(440, 100, 100)
                await runloop.sleep_ms(1000)
                i += 1 # Se actualiza el contador
                light_matrix.clear()
            else: # Color incorrecto
                light_matrix.show_image(light_matrix.IMAGE_SAD)
                await runloop.sleep_ms(1000)
                break

        if i >= length:
            length += 1
            if length > 8: # Termina el programa al llegar al nivel 5
                light_matrix.write("Ganaste!")
                await runloop.sleep_ms(1000)
                break
            else:
                # Se reinician el contador y las listas
                i = 0
                secuencia.clear()
                result.clear()
                # Se genera la secuencia
                secuencia = generar_secuencia(length, numeros_base)

                # Se muestra la secuencia en color matrix
                print("Secuencia generada: ", secuencia)
                await mostrar_secuencia(secuencia)
                await runloop.sleep_ms(1000)
                await sound.beep(440, 1000, 100)

    # Se comparan la lista con
    print(result)

runloop.run(main())