'''
Created by Natalya Morales
July 31, 2024
Program that makes basics operations detecting colors
'''
from hub import light_matrix, button, port
import runloop, color_sensor, color, force_sensor

# Diccionario para saber las operaciones
diccionario = {
    1: "+", 2: "-", 3: "*", 4: "/"
}
async def main():
    # Variables iniciales
    a = 0
    b = 0
    c = 0
    print("Programa que realiza operaciones entre dos numeros")

    # Se elige la operacion que se va a realizar
    print("\nElige la operación que quieres realizar: ")
    print("1. Suma \n2. Resta \n3. Mutliplicacion \n4. DIvisión\n")

    operacion = 1
    print("Operación actual: 1")
    light_matrix.write("+")

    while True:
        if button.pressed(button.LEFT) and operacion < 4:
            operacion += 1
            await runloop.sleep_ms(1000)
            print("Operación actual: ", operacion)
            light_matrix.write(diccionario[operacion])
        elif button.pressed(button.RIGHT) and operacion > 1:
            operacion -= 1
            await runloop.sleep_ms(1000)
            print("Operación actual: ", operacion)
            light_matrix.write(diccionario[operacion])
        if force_sensor.force(port.F) > 8:
            break

    # Asignar valores con los colores
    await runloop.sleep_ms(1000)
    light_matrix.write("B")
    while True:
        # Se asigna el primer valor a "b"
        if color_sensor.color(port.B) is not color.UNKNOWN and b == 0 and color_sensor.color(port.B) is not color.BLACK:
            b = color_sensor.color(port.B)
            print("b = ", b)
            light_matrix.write(str(b))
            await runloop.sleep_ms(1000)
            light_matrix.write("A")
            await runloop.sleep_ms(1000)
        # Se asigna el segundo valor a "a"
        elif color_sensor.color(port.B) is not color.UNKNOWN and b is not color.UNKNOWN and a == 0 and color_sensor.color(port.B) is not color.BLACK:
            a = color_sensor.color(port.B)
            print("a = ", a)
            await runloop.sleep_ms(1000)
            light_matrix.write(str(a))
        # Sale del programa
        if force_sensor.force(port.F) > 8:
            break

    # Impresión de la suma a + b asignado a "c"
    if operacion == 1:
        c = a + b
        print("La suma de ",a, " + ",b, " = ",c)
    elif operacion == 2:
        c = a - b
        print("La resta de ",a, " - ",b, " = ",c)
    elif operacion == 3:
        c = a * b
        print("La multiplicación de ",a, " * ",b, " = ",c)
    elif operacion == 4:
        c = a / b
        print("La división de ",a, " / ",b, " = ",c)

    light_matrix.write(str(c))


runloop.run(main())