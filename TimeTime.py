import time
import datetime

def read_speed(start,end,page):
    v = (end - start) / page
    return v

start_input = input("please enter 's' to start !\n")

if start_input == 's':
    starttime = datetime.datetime.now()

print('Timer is running, please read the book!')
end_input = input("please enter 'e' to end the time!\n")

if end_input == 'e':
    endtime = datetime.datetime.now()
    print('timer is stop!')

page = input('How many page have you read?\n')



speed = read_speed (starttime,endtime,int(page))
print('your read speed is ',speed)



