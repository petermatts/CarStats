""""""

from operator import itemgetter

####################################################################################################

# Timing Constands

class Timing:
    IMPLICIT_WAIT = 5 # seconds
    SLEEP = 2 # seconds

    BAD_LINK = 5 # seconds
    TIMEOUT = 120 # seconds
    NO_SUCH_ELEMENT = 10 # seconds
    CLICK_INTERCEPTED = 30 # second

####################################################################################################

# Scraper Results

class Results:
    GOOD = 1
    INTIAL = 0
    BAD = -1

    BAD_LINK = -1 # change this to not match general
    REQUEST_TIMEOUT = -2
    SELENIUM_TIMEOUT = -3
    SELENIUM_NO_SUCH_ELEMENT = -4
    SELENIUM_CLICK_INTERCEPTED = -5

####################################################################################################

#

####################################################################################################

