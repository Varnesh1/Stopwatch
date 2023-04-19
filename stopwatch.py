import time

seconds = int(input('How many seconds do you want?'))



        


def countdownTimer(seconds):
    while seconds > 0:
        minute = int(seconds / 60)
        sec = int(seconds % 60)
        timer = f'{minute} min : {sec} sec '
        print(timer)
        time.sleep(1)
        seconds -= 1
        

    


countdownTimer(int(seconds))



