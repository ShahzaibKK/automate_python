#! python3
# mapit.py - Launches a map in the browes using an address from the
# command line or clipboard
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get The Address from Commond
    address = " ".join(sys.argv[1:])
else:
    # Get The Address from Clipboard
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
