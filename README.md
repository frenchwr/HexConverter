# HexConverter

![hex converter](/images/screenshot.jpg "HexConverter")  

This utilitiy listens for command-C's on a Mac keyboard, and when triggered checks the clipboard
for strings beginning with the **0x** hexadecimal prefix, converting any hex codes
it encounters to decimal and binary. The result is presented in a simple dialog box
(see image below). The tool will convert as many hex codes as it identifies on the screen.
Note that the script does NOT listen to mouse actions, so will not pick up changes
to the clipboard via the right-click option. 

## Dependencies

* Mac OS (only tested on 10.15 to date)
* Python (only tested on 3.7.4 to date)
* [Pynput](https://pypi.org/project/pynput/) Python package (install with `pip install pynput`)

## Running

This script can be run from the Mac terminal app (Applications -> Terminal.app).

```
python cmd-c-listener.py
```

or:

```
chmod +x cmd-c-listener.py
./cmd-c-listener.py 
```

No output will be produced at startup. You may leave the program running
in its own tab (I hope to improve this in the future - see the TODO list below). 

## TODO

* Add support for Windows/Linux
* Add tooling/documentation to run at startup
* Add support for accepting decimal or binary encoding input  
* Add regex for removing potential spurious characters appended to hex string

