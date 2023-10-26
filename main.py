# Importer nødvendige ting

from pyfirmata import *
import time
import os

# Velg brett og start opp brett
board = Arduino("COM5", baudrate=57600)
i = util.Iterator(board)
i.start()


# Definere pins på brettet

button = board.get_pin("d:2:i")

red = board.get_pin("d:9:p")
green = board.get_pin("d:10:p")
blue = board.get_pin("d:11:p")


in_teams_meeting = False

# Sjekke teams kommando
CMD = 'tasklist /fo table /v /fi "imagename eq Teams.exe" /fi "windowtitle eq Meet*"'

# Let etter teams prosessen
def find_teams():
    # Søk etter prossesen som har riktig navn og exe
    p = os.popen(CMD).read().splitlines()

    global in_teams_meeting
    in_teams_meeting = False
    
    for item in p:
        if 'teams.exe' in item.lower():
            in_teams_meeting = True

# Sett fargen på lyset
def setColor(r, g, b):
    red.write(r*0.00392)
    green.write(g*0.00392)
    blue.write(b*0.00392)

# Loop sjekk for alltid
while True:
    find_teams()

    if in_teams_meeting:
        setColor(255, 0, 0)
    else:
        setColor(0, 0, 0)

    if button.read():
        setColor(0, 255, 0)
        time.sleep(10)

    time.sleep(0.1)
