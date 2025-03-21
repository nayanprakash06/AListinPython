from machine import Pin, PWM
enA = PWM(Pin(15))
in1 = Pin(12,Pin.OUT)
in2 = Pin (13,Pin.OUT)

enA.freq(1000)
enA.duty(512)

while True :
    in1.value(1)
    in2.value(0)
    time.sleep(2)
    in1.value (0)
    in2.value(1)
    time.sleep(2)
# Write your code here :-)
#Practise of repo for section B

print("hello world")
//go for lunch

gouri_list=["no"]


          10 more mins for lunch 


