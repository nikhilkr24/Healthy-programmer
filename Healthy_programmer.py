from pygame import mixer
from datetime import datetime
from time import time

def musicplay(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)

    while True:
        input_of_user=input()
        if input_of_user==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylog.txt","a") as op:
        op.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    water_sec=30*60
    eye_sec=45*60
    exercise_sec=90*60

    while True:
        if time()-init_water>water_sec:
            print("Water dirinking time. Enter 'drank' to stop the alarm")
            musicplay('water.mp3','drank')
            init_water=time()
            log_now("Drank water at")

        if time()-init_eyes>eye_sec:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm")
            musicplay('eyes.mp3','doneeyes')
            init_eyes=time()
            log_now("Eyes Relaxed at")

        if time()-init_exercise>exercise_sec:
            print("Physical activity time. Enter 'donephy' to stop the alarm")
            musicplay('physical.wav','donephy')
            init_exercise=time()
            log_now("Physical activity done at")



