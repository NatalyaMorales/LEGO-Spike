'''
Created by Natalya Morales
July 24, 2024
Program to introduce movement of Spike
'''
from hub import light_matrix, port, motion_sensor
import runloop, motor_pair, color_sensor, color, distance_sensor, math

async def main():
    motor_pair.pair(motor_pair.PAIR_1,port.C,port.D)

    ### DETECTAR COLOR E IR PARA ATRÁS
    '''
    while True:
        if color_sensor.color(port.B) != color.BLACK:
            motor_pair.move_for_degrees(motor_pair.PAIR_1,200,0,velocity=200)
        else:
            await motor_pair.move_for_degrees(motor_pair.PAIR_1,2000,0,velocity=-200)
    '''

    ### DETECTAR DISTANCIA Y DETENERSE
    '''
    while True:
        if distance_sensor.distance(port.E) > 10:
            motor_pair.move_for_degrees(motor_pair.PAIR_1,200,0,velocity=200)
        else:
            motor_pair.stop(motor_pair.PAIR_1)
    '''

    # GIRAR SOBRE SU PROPIO EJE
    '''
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)

    while True:
        if motion_sensor.tilt_angles()[0] > 1600:
            motor_pair.stop(motor_pair.PAIR_1)
        else:
            motor_pair.move(motor_pair.PAIR_1,100)
    '''
    # SEGUIMIENTO DE ÁNGULO: DA UN GIRO 90° Y CAMINA RECTO
    '''
    while True:
        if motion_sensor.tilt_angles()[0] <= 900:
            motor_pair.move(motor_pair.PAIR_1,-25)
        elif motion_sensor.tilt_angles()[0] >= 900:
            motor_pair.move(motor_pair.PAIR_1,25)
    '''

    #await runloop.sleep_ms(200)

runloop.run(main())