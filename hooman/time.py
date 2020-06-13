import time


class Timer:
    def __init__(self, callback, seconds=0, minutes=0):
        self.callback = callback
        self.length = seconds + (minutes * 60)
        self.start_time = time.time()
        self.finsished = False

    def update(self):
        if time.time() - self.start_time >= self.length:
            self.finsished = True
            if self.callback is not None:
                self.callback()
            return True
        return False

    def __str__(self):
        return "Timer: %d seconds remaining" % (
            self.length - (time.time() - self.start_time)
        )

    def __bool__(self):
        return self.finsished
