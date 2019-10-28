# drv8825 driver
from machine import Pin, PWM, Timer
import time

class Stepper:
    def __init__(self, dirPin, stepPin, msPin):
        self.dirPin=dirPin
        self.stepPin=PWM(stepPin, freq=0, duty=0)
        self.msPin=msPin #microstep pin M0
        #M0,M1,M2,ms
        self.timeTable=[(1,0,0,2000),(0,0,0,20000),(1,0,0,2000)]
        self.tim=Timer(-1)
        self.freq=1000
        self.index=0

    #travel (in steps), speed (in steps / seconds)
    def Schedule(self, travel, speed):
        #converti les steps en millisecondes en tenant compte
        #cree une rampe d'acceleration / deceleration par paliers
        #en utilisant les microsteps
        
        #for i in  
        #    self.timeTable[]int(steps/self.freq)*1000)
        pass

    #integre une compensation du temps du retard moyen du Timer (1_ms)
    def Run(self, t):
        self.stepPin.duty(32)
        try:
            print(time.ticks_ms())
            self.msPin=self.timeTable[self.index][0]
            self.tim.init(period=(self.timeTable[self.index][3])-1, mode=Timer.ONE_SHOT, callback=self.Run)
            self.index+=1
        except:
            self.stepPin.duty(0)

if __name__ == '__main__':
    test=Stepper(Pin(0, Pin.OUT),Pin(2),Pin(3))
    test.Run(0)
    while True:
        print('meanwhile...')
        time.sleep(1)

#290696176	
#292696529	2000353
#312696887	20000358
#314697197	2000310
#avec une compensation de 1_ms la deviation est d'environ:
#300_us a chaque changement de palier
        
