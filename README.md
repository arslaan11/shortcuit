# Shortcuit
Shortcuit is a 9 key macropad with a rotary encoder. It uses KMK fireware

It is one of my projects for Hackclub Fallout
<img width="1920" height="867" alt="SHORTCUIT NO BG" src="https://github.com/user-attachments/assets/411d5ada-049e-4684-b9a6-dae1c53c8ca7" />

# The Motivation Behind Shortcuit
Shortcuit was boarn out of the Hack Club Fallout event. I've always been comfortable in the digital realm. Writing code and designing interfaces but i wanted to challenge myself to bring something into the physical world.

This was honestly my first ever hardware project. I wanted to learn the entire stack: from routing my first PCB in KiCad and figuring out the electronics, to 3D printing a custom shell and writing the KMK firmware. The goal wasn't just to build a macro pad, but to demystify the hardware engineering process for myself. It was a steep learning curve, but turning a digital schematic into a physical tool i use everyday made it entirely worth it.

# Features:
<ul>
 <li> EC11 Rotary encoder for volume controller or whatever you want</li>
 <li> 9 keys</li>
</ul>

# PCB
Here's my PCB! It was made in KiCad. 
<img width="1045" height="587" alt="Schematic" src="https://github.com/user-attachments/assets/02ebcd9f-80d4-4e46-b340-e6d06981f211" />
<h2>Schematic</h2>
<img width="901" height="724" alt="Screenshot 2026-04-20 174359" src="https://github.com/user-attachments/assets/092bb3eb-e3bd-4340-98f5-c9c8f80610d3" />
<h2>PCB</h2>
I used MX_CHERRY for the keyswitch footprint
# Firmware Overview
Shortcuit uses KMK firmware for everything
<ul>
 <li> the rotary encoder changes volume and press to mute</li>
 <li> the 9 keys currently open steam,github,Obs software and etc but you should change them for your prefer apps,games or website</li>
</ul>

# Case
The case was designed in fusion with the help of [@NoseF](https://github.coom/NoseFa).
the case is designed to be oprinted in two pieces. the top plate and thee sides are deesigned to be printed in one piece and the bottom plate attaches with M2 screws to heated inserts in the top plate. the dial and the keycaps was made to be 3d printable as well. the case also has logos of Hack Club and Fallout(The event this was made for.)
The materials that will be used for the print are orange(#FF8C37) PLA+ and the keycaps will be made of Red(#EC3750)PLA+. here are the specific [Fusion files](./Fusion%20files/).
<img width="1920" height="867" alt="SHORTCUIT NO BG" src="https://github.com/user-attachments/assets/411d5ada-049e-4684-b9a6-dae1c53c8ca7" />
Special thanks to oskar(Hack Club slack @NoseF) for helping me with the case design.

# BOM:
<ul>
 <li> 1x RasberryPi Pico W</li>
 <li> 9x Cherry MX Switches </li>
 <li> 9x keycaps </li>
 <li> 2X Resistor 4.7k </li>
 <li> 1x EC11 Rotary Encoder</li>
 <li> 1x case (printed parts)</li>
</ul>

# Extra 
Honestly this was my first ever hardware project. you can imagine how it went but in the end it turned out fine 
