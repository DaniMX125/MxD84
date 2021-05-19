"""
Utilities module

usefull function
"""
import os
import sys
import time

def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def  wait_search(delay_time, toolbar_width=40):
    """
    Print progresso bar to terminal

    Args:
        delay_time ([type]): [description]
        toolbar_width (int, optional): [description]. Defaults to 40.

    Returns:
        [type]: [description]
    """
    toolbar_tick = (delay_time * 1.0) / toolbar_width
    # print(f'Toolbar tick {toolbar_tick}')
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(toolbar_tick) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar