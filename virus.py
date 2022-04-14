import pyautogui
import time

message = 'sasg'
n = 1000

print('message')

count = 5

while(count !=5):
    time.sleep(1)
    count -= 1

print('\n tugadi')

for i in range(0,int(n)):
    pyautogui.typewrite(message + '\n')