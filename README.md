# XavPad
XavPad is a 4x3 key macropad which uses KMK. I made this to help me be more productive.

## Features:
- 12 keys
- Simple case
- Dual layers 

## CAD Model:
The entire case fits together with 4 M3 screws.
The case has 2 seperate pieces: The Bottom and Sides, and the Top.

<img src=assets/cad.png alt="Schematic" width="500"/>

## PCB:
I made my PCB in KiCad

Schematic

<img src=assets/schematic.png alt="Schematic" width="500"/>

PCB

<img src=assets/pcb.png alt="Schematic" width="500"/>

## Firmware:
My hackpad uses [KMK](https://github.com/KMKfw/kmk_firmware) firmware.

- Swap between the 2 layers by double pressing the bottom left key
- The first layer are number pad 0-9
- The second layer are F1-12

For now it uses KMK but later on I might switch to QMK and add VIA support.

## BOM:
- 12x Cherry MX Switches
- 12x DSA Keycaps 
- 4x M3x16mm screws
- 12x through-hole 1N4148 Diodes
- 1x XIAO RP2040
- 1x Case (2 pieces)

