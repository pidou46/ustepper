# drv8825 driver
from machine import Pin, PWM, Timer
import time

class Stepper:
    def __init__(self, dirPin, stepPin, msPin):
        self.dirPin=dirPin
        self.stepPin=PWM(stepPin, freq=0, duty=0)
        self.msPin=msPin #microstep pin M0
        #M0,M1,M2,ms
        self.timeTable=[(1,0,0,1999),(0,0,0,19999),(1,0,0,1999)]
        self.tim=Timer(-1)
        self.freq=1000
        self.index=0

    #travel (in steps), speed (in steps / seconds)
    def Schedule(self, travel, speed):
        #converti les steps en millisecondes en tenant compte
        #cree une rampe d'acceleration / deceleration par paliers
        #en utilisant les microsteps
        #integre une compensation du temps du retard moyen du Timer (1_ms)
        
        #for i in  
        #    self.timeTable[]int(steps/self.freq)*1000)
        pass
    
    def Run(self, t):
        self.stepPin.duty(32)
        try:
            print(time.ticks_ms())
            self.msPin=self.timeTable[self.index][0]
            self.tim.init(period=self.timeTable[self.index][3], mode=Timer.ONE_SHOT, callback=self.Run)
            self.index+=1
        except:
            self.stepPin.duty(0)

if __name__ == '__main__':
    test=Stepper(Pin(0, Pin.OUT),Pin(2),Pin(3))
    test.Spin(0)
    while True:
        print('meanwhile...')
        time.sleep(1)
