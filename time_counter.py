import time as tm

class Timer():

    def __init__(self, seconds):
        self.seconds = seconds
        print('you have {} seconds'.format(seconds))

    def timer(self):
        start_time = tm.time()
        print('tick')
        print(tm.time())
        tm.sleep(self.seconds -((tm.time() - start_time) % self.seconds))


if __name__ == '__main__':

    #creates Timer object called timey - 5 is seconds and can be replaced
    timey = Timer(5)
   
    #executes timer function 5 times in this example
    for each in range(5):
        timey.timer()
