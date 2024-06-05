from time import sleep
from random import random
from clint.textui import progress

from pyfiglet import figlet_format


def twilio_intro():
    ''' Fun intro print statement '''

    # fun print statement
    print(figlet_format('Welcome to Twilio Academy', font='small'))

    return


def progress_bar():

    for i in progress.dots(range(20)):
        sleep(random() * 0.2)

    return

# https://github.com/tqdm/tqdm#documentation
# this is a fun progress bar


