import time

from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()


@tl.job(interval=timedelta(seconds=2))
def sample_job_every_2s():
    print ("2s job current time : {}".format(time.ctime()))


@tl.job(interval=timedelta(seconds=5))
def sample_job_every_5s():
    print ("5s job current time : {}".format(time.ctime()))


@tl.job(interval=timedelta(seconds=10))
def sample_job_every_10s():
    print ("10s job current time : {}".format(time.ctime()))


tl.start()

while True:
    time.sleep(20)
    tl.stop()
    break