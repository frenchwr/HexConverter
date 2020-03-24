#!/usr/bin/env python 
from pynput import keyboard
import subprocess
from time import sleep

hex_prefix = "0x"
spurious_character = ":"
CLIPBOARD_UPDATE_DELAY_SECS = 0.2

def tokenize_clipboard():
    return subprocess.run('/usr/bin/pbpaste',stdout=
            subprocess.PIPE).stdout.decode().strip().split()

def sanitize_clipboard():
    subprocess.run("/bin/echo \'\' | /usr/bin/pbcopy &> /dev/null", 
            shell=True)

def get_hexcode_string(matching_string):
    matching_string = matching_string.replace(hex_prefix,'')
    # TODO: add regex to remove other spurious characters 
    #       that may be appended on hex output
    if spurious_character in matching_string:
        matching_string = matching_string.replace(
                spurious_character,'')
    return matching_string

def is_valid_hex(test_str):
    try:
        int(test_str, 16)
        return True
    except ValueError:
        print("Invalid hex code "+test_str)
        return False

def get_display_string(hex_str):
    str1 = "Hex encoding: {0}\n\n".format(hex_str)
    str2 = "Decimal encoding: {0}\n\n".format(int(hex_str, 16))
    str3 = "Binary encoding: {0}".format(bin(int(hex_str, 16))[2:])
    return str1 + str2 + str3 

def get_osascript_cmd(hex_str):
    display_text = get_display_string(hex_str)
    str1 = "/usr/bin/osascript -e \'Tell application \"System Events\" to display dialog \""
    str2 = "\" with title \"Hex Converter\"\' &> /dev/null"
    return str1 + display_text + str2

def show_dialog(hex_str):
    subprocess.run(get_osascript_cmd(hex_str), shell=True)

def on_activate():
    sleep(CLIPBOARD_UPDATE_DELAY_SECS) # give clipboard time to update
    tokens = tokenize_clipboard()
    found_valid_hex = False
    for token in tokens:
        if hex_prefix in token:
            hex_code_str = get_hexcode_string(token)
            if is_valid_hex(hex_code_str):
                found_valid_hex = True
                show_dialog(hex_code_str)
    if found_valid_hex:
        sanitize_clipboard()

def for_canonical(f):
    return lambda k: f(listener.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<cmd>+c'),
    on_activate)

# Collect events until released
with keyboard.Listener(on_press=for_canonical(hotkey.press),
                       on_release=for_canonical(hotkey.release)) as listener:
    listener.join()