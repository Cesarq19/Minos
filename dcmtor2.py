from machine import Pin, I2C, PWM
import time


class DCMotor:      
  def __init__(self, in1, in2,in3,in4, pwm1,pwm2, min_duty=750, max_duty=1023):
        self.in1=in1
        self.in2=in2
        self.in3=in3
        self.in4=in4

        self.pwm1=pwm1
        self.pwm2=pwm2
        self.min_duty = min_duty
        self.max_duty = max_duty

  def forward(self,speed):
        self.speed=speed
        self.pwm1.duty(self.duty_cycle(self.speed))
        self.pwm2.duty(self.duty_cycle(self.speed))
        self.in1.value(1)
        self.in2.value(0)
        self.in3.value(1)
        self.in4.value(0)
        print("adelante")

  def backward(self,speed):
        self.speed=speed
        self.pwm1.duty(self.duty_cycle(self.speed))
        self.pwm2.duty(self.duty_cycle(self.speed))
        self.in1.value(0)
        self.in2.value(1)
        self.in3.value(0)
        self.in4.value(1)
        print("atras")

  def turn_left(self,speed):
        self.speed=speed
        self.pwm1.duty(self.duty_cycle(self.speed))
        self.pwm2.duty(self.duty_cycle(self.speed))
        self.in1.value(0)
        self.in2.value(1)
        self.in3.value(1)
        self.in4.value(0)

  def turn_right(self,speed):
        self.speed=speed
        self.pwm1.duty(self.duty_cycle(self.speed))
        self.pwm2.duty(self.duty_cycle(self.speed))
        self.in1.value(1)
        self.in2.value(0)
        self.in3.value(0)
        self.in4.value(1)

  def stop(self):
        self.pwm1.duty(0)
        self.pwm2.duty(0)
        print("para")
        
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle