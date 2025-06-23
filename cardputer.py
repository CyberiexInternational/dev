file_name = 'cckeyboard.py'
author = 'dissy', 'Peter Stöck'
kb_version = '01.00.00'
date = '16.04.2024'


import os, sys, io
import M5
from M5 import *
from hardware import *


# globale Variablen
kb_buffer = ''              # Puffer für die eingegebenen Werte
kb_buf_max_len = None       # Max. Pufferlänge

kb_input_box = None

# Keyboard Instanz initialisieren
kb = MatrixKeyboard()

# Schreibt Text in ein Widgets.Labell und zeigt es an
def update_box(val, box):
    box.setText(str(val))
    box.setVisible(True)


# Löscht das letzte Zeichen
def kb_delete():
    global kb_buffer
    l = len(kb_buffer)
    if l < 1:
        return
    x = l - 1
    kb_buffer = kb_buffer[:x]
    update_box(kb_buffer, kb_input_box)
    Speaker.tone(1000, 50)


# Bearbeitet die Eingabe von Enter
def kb_enter():
    global kb_aktive
    kb_aktive = False
    Speaker.tone(2000, 100)

# ISR
def kb_pressed_event(kb_0):
    global kb_buffer
    # Puffer voll?
    l = len(kb_buffer)
    if l > kb_buf_max_len:
        kb_buffer = ''
        update_box(kb_buffer, kb_input_box)
        Speaker.tone(1000, 750)
    # Tastendruck holen auswerten und ggf. an den Puffer anhängen
    keyCode = kb.get_key()
    if keyCode==8:                # 8 is the Delete key
        kb_delete()
    elif keyCode==9:              # 9 is the Tab key, which we will just ignore
        Speaker.tone(3000, 50)
    elif keyCode==13:             # 13 is the Enter key
        kb_enter()
    else:
        keyChar = ''
        keyChar = chr(keyCode)
        kb_buffer = (str(kb_buffer) + str(keyChar))
        Speaker.tone(3000, 50)
    update_box(kb_buffer, kb_input_box)
    
# Startet die Keyboardabfrage
def kb_input(message, msg_box, input_box, buf_len):
    global kb_aktive, kb_buffer, kb_msg_box, kb_input_box, kb_buf_max_len
    update_box(message, msg_box)
    kb_input_box = input_box
    kb_buffer = ''
    update_box(kb_buffer, kb_input_box)
    kb_buf_max_len = buf_len    
    kb_aktive = True 
    while kb_aktive:
        M5.update()
        kb.tick()
    return kb_buffer

# Keyboard ISR zuweisen
kb.set_callback(kb_pressed_event)

# Nun ist alles ist bereit

# Demo

def test_run():
    Widgets.setRotation(1)

    lab_msg = Widgets.Label("---", 10, 30, 1.0, 0xffffff, 0x0, Widgets.FONTS.DejaVu18)
    lab_input = Widgets.Label("---", 10, 60, 1.0, 0xffffff, 0x0, Widgets.FONTS.DejaVu24)

    lab_msg.setVisible(True)
    lab_input.setVisible(True)

    inp = ' '
    while inp:
        inp = ''
        inp = kb_input('Test-Eingabe:', lab_msg, lab_input, 13)
        print(inp)
    
if __name__ == '__main__':
    test_run()

Z.Z. müsst Ihr es aus dem Browser kopieren und in einen Editor einfügen. Dort unter dem Namen cckeyboard.py abspeichern.
Wenn Ihr das Modul direkt startet wird eine Demo ausgeführt, mit Ihr es testen könnt.

Keycode Konstanten
Da die eingebauten Keycode-Konstanten nicht funktionieren, habe ich ein eigenes Modul geschrieben.
Es erfordert den Präfix keycodes anstatt KeyCode. Das kann aber durch ändern des Filenamen oder einer entsprechenden Import-Anweisung (siehe Code) geändert werden.

# keycodes.py
# use: import keycodes as KeyCode

KEYCODE_BACKSPACE = const(8)
KEYCODE_TAB = const(9)
KEYCODE_ENTER = const(13)
KEYCODE_ESC = const(27)
KEYCODE_SPACE = const(32)
KEYCODE_DEL = const(8)
KEYCODE_LEFT = const(180)
KEYCODE_RIGHT = const(183)
KEYCODE_UP = const(181)
KEYCODE_DOWN = const(182)