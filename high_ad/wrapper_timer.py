

from datetime import datetime
from threading import Thread
from time import sleep
import config


def runtime():
    timer = []
    while(True):
        time_start = datetime.now()
        if(config.digital_read(17)==0):
            timer.append(datetime.now()-time_start)
        print("max:{}\nmin:{}\nmean:{}".format(max(timer),min(timer),mean(timer)))


if __name__=='__main__':
    run_func = Thread(target = runtime)
    run_func.start()
    sleep(10)
    run_func.stop()
    

    


        


