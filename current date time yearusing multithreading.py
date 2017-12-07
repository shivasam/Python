from threading import Thread
import time

def timer(delay, repeat):
    #while repeat<5:
        time.sleep(delay)
        print(time.ctime(time.time()))
        #repeat += 1
    #print 'completed'
def main():
    t1 = Thread(target=timer, args=(1, 3))
    t2 = Thread(target=timer, args=(2, 3))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
