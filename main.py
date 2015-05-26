# -*- coding: utf-8 -*-
"""
Display a nice and quiet aquarium into your shell.

Usage:
    main.py

"""

##########
# IMPORT #
##########
import curses

########
# MAIN #
########
def _main_():
    screen = _init()
    try:
        screen.addstr("TEST DE LA MORT!!!")
        screen.refresh()
        while True:
            c = screen.getch()
            if c == ord('q'):
                _quit(screen)
                print('ok')
                break
            else:
                screen.addstr("BOOM")
                screen.refresh()
    except BaseException as bug_report:
        _quit(screen)
        print("Ça bug!")
        print(bug_report)

#############
# FUNCTIONS #
#############
def _init():
    screen = curses.initscr()  # New screen initialization
    curses.start_color()       # Allow to use colors
    curses.noecho()            # No display of keyboard
    curses.cbreak()            # Will react directly to the key
    screen.keypad(True)
    return screen

def _quit(screen):
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()

##########
# LAUNCH #
##########
_main_()
