# NightLite
A light powered by a Raspberry Pi that adjusts its brightness based on how bright/dark it is.

## Running
Run the following command in the terminal when you are in the same directory as the program: ```sudo python3 main.py```.

## The Wiring
### Assuming you are using a half-size breadboard (I'm not sure if the sizes make a difference) that is placed vertically, with a1 being in the top left:
---
- Female to Male Jumper Wire: GND -> f5
- Female to Male Jumper Wire: 17 -> b1
- Female to Male Jumper Wire: 22 -> b4
- 1k Ohm Resistor: d1 -> f1
- 1k Ohm Resistor: d4 -> f4
- 330 nF Capacitor: h4 (-) -> j5 (+)
- Photoresistor: j1 -> j4
- Female to Male Jumper Wire: 18 -> a10
- Female to Male Jumper Wire: GND -> a17
- 1k Ohm Resistor: c10 -> c15
- White LED: e15 (+) -> e17 (-)
---
### Double-check your wiring. It's really easy to mix up this stuff, and I do it all the time too. If you find something wrong with this wiring, please let me know immediately in the issues section.

## How It Works

We measure the resistance by first discharging everything in the capacitor. Then we want to charge the capacitor with the current coming through the photoreistor. The capacitor will fill faster if it is brighter. So that means we can figure out the light level by checking how fast the capacitor fills up. For one time constant (1 Tau), the capacitor will rise to approximately 63.2% of the original input/charge voltage. The time constant (1 Tau) can also be expressed as the value of the resistance multiplied by the value of the capacitance. So that gives us, with Tau being T: T = time * 0.33 * 1000 * 0.632, which is the equation used in the program.
