from pynput.mouse import Button, Controller
from pynput import mouse
from tqdm import tqdm
import time
xinput=[]
yinput=[]
windowconst=1.2486 # 윈도우 화면 확대 설정_125%

## scan position
def on_click(x, y, button, pressed):
    global xinput, yinput
    if pressed:
        xinput.append(x)
        yinput.append(y)
    if not pressed:
        # Stop listener
        return False

# read 처음 좌표, 확인 3개
for i in range(4):
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

# 잘 됐는지 확인
print('xinput : ',xinput)
print('yinput : ',yinput)

# macro 실행
mouse_drag = Controller()

## windowconst 만큼 나눠줌
for i in range(len(xinput)):
    xinput[i]=xinput[i]/windowconst
    yinput[i] =yinput[i]/windowconst
count=int(input()) # 몇회 할지 입력받으면 실행

# t: 확인간 간격
t=[0.2,2.9,0.1]

for i in tqdm(range(count)):
    mouse_drag.position = (xinput[0], yinput[0])  # input 위치로 이동
    for j in range(10):
        mouse_drag.click(Button.right, 1)
        time.sleep(0.57)

    for j in range(3):
        mouse_drag.position = (xinput[j+1], yinput[j+1])  # 확인 위치로 이동
        time.sleep(0.2)
        mouse_drag.click(Button.left, 1)
        time.sleep(t[j])
    time.sleep(0.5)