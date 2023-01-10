import time
print("Current Time is: ")
def timer():
    string = time.strftime('%H : %M : %S %p')
    print(string,end='\r')
    time.sleep(1)
    timer()
timer()