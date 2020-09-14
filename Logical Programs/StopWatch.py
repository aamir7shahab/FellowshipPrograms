import time
from math import floor


class StopWatch:

    @staticmethod
    def startTime():
        start = time.time()
        return start

    @staticmethod
    def stopTime():
        stop = time.time()
        return stop

    @staticmethod
    def elapsedTime(start, end):
        elapsedTime = (end - start)
        return elapsedTime

    @staticmethod
    def formatTime(timeInSec):
        mins = timeInSec // 60
        sec = timeInSec % 60
        hour = mins // 60
        mins = mins % 60
        millSec = (sec - floor(sec)) * 1000
        print()
        print(f'{int(hour):2} hrs: {int(mins):2} mins: {floor(sec):2} secs: {floor(millSec):3} msec')
        print()


if __name__ == '__main__':
    input('Press Enter to Start the Watch')
    start = StopWatch.startTime()
    input('Press Enter to Stop the Watch')
    end = StopWatch.stopTime()
    StopWatch.formatTime(StopWatch.elapsedTime(start, end))
