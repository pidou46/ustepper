# drv8825 driver
from machine import Pin, PWM, Timer
import micropython, sys
import time

micropython.alloc_emergency_exception_buf(100)

class Stepper:
    def __init__(self, dirPin, stepPin, msPin):
        self.dirPin=dirPin
        self.stepPin=PWM(stepPin, freq=0, duty=0)
        self.msPin=msPin #microstep pin M0
        #M0,M1,M2,ms
        self.PrepNextRun_ref=self.PrepNextRun
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

    def FirstRun(self):
        print("FirstRun: %s"%time.ticks_us())
        self.stepPin.duty(32)
        self.PrepNextRun(0)
        self.Run(0)

    def PrepNextRun(self,t):
        print("PrepNextRun: %s"%time.ticks_us())
        try:
            self.ms=self.timeTable[self.index][0]
            self.p=self.timeTable[self.index][3]
            self.index+=1
        except:
            self.stepPin.duty(0)
            print("Motor have been stopped...")
            self.tim.deinit()
            

    #cela fonctionne masi devrait etre optimiser : http://docs.micropython.org/en/latest/reference/isr_rules.html
    def Run(self, t):
        self.msPin=self.ms
        self.tim.init(period=self.p, mode=Timer.ONE_SHOT, callback=self.Run)
        micropython.schedule(self.PrepNextRun_ref,0)

if __name__ == '__main__':
    test=Stepper(Pin(0, Pin.OUT),Pin(2),Pin(3))
    test.FirstRun()
    while True:
        print('meanwhile...')
        time.sleep(1)

#290696176  
#292696529  2000353
#312696887  20000358
#314697197  2000310
#avec une compensation de 1_ms la deviation est d'environ:
#300_us a chaque changement de palier
        
