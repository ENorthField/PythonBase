all_big=all_small=big_mouse=small_mouse=1
x,day=10,0
while True:
    x-=(big_mouse+small_mouse)
    big_mouse*=2
    small_mouse/=2
    day+=1
    if x<=0:
        print(day)
        break
    all_big+=big_mouse
    all_small+=small_mouse
x=(10-all_big-all_small)
all_big+=x*big_mouse/(big_mouse+small_mouse)
all_small+=x*small_mouse/(big_mouse+small_mouse)
print(f'大老鼠挖了{all_big}尺，小老鼠挖了{all_small}尺')
