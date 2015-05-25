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
    curses.beep()
    screen.addstr("Test")
    screen.refresh()

    _quit(screen)

#############
# FUNCTIONS #
#############
def init():
    screen = curses.initscr()  # New screen initialization
    curses.start_color()       # Allow to use colors
    curses.noecho()            # No display of keyboard
    curses.cbreak()            # Will react directly to the key
    screen.keypad(True)

def _quit(screen):
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()

##########
# LAUNCH #
##########
_main_()
