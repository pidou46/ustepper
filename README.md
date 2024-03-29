# ustepper
micropython asynchronious driver for stepper motor via step/dir driver

This code is splitted in to steps:

1/ schedule a mouvement given a steps quantity, speed set point in Hz (steps/s) and acceleration steps/second square

2/ run the scheduled mouvement

## Scheduling:

The aim of this step is to compute a time table of the mouvement, this time table will be used later by Running function to actualy make the motor mouvement.

Here it is a graphic plot of a very short mouvement time table:


![Mouvemet profile 01](MvtProfile_01.png)

The acceleration parameter is not a real angular acceleration expressed in rad/s^2.
It's aquind of progressive change in speed rate.
It's based on change in microstepping setting at constant time intervals


## Running:

  The step pin of the driver is feeded at constant speed using the mcu's hardware PWM.
A Timer is used to stop the movement at the theorical position based on time spent.
The experiments I have made prouve that delay of the Timer is quite small and consitant at 1_ms, so it can be compensated.

Optionaly, the microsteping capacity of the driver is used to implement:
- speed ramp up (acceleration)
- smooth mouvement
- higher precision


Testing:
testing is made with:
- esp32 and esp8266, should work also with stm32 since (https://github.com/micropython/micropython/pull/5254)
- micropython firmware (official)
- drv8825 driver (should also work with other step/dir drivers like A4988)
- 2 x phases (four wires) stepper motor


