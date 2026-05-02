<h1>Physical Assembly Instructions</h1>
Building Shortcuit from scratch is incredibly rewarding. If this is your first hardware project, take your time, keep your soldering iron clean, and make sure your work space is well ventilated!

### Tools Required
<ul>
  <li>Soldering Iron (with a standard tip and a flat tip for inserts, if available)</li>
  <li>Solder (60/40 rosin core or lead-free)</li>
  <li>Flush cutters (for trimming diode legs)</li>
  <li>Hex screwdriver(for M2 screws)</li>
  <li>tweezers (helpful for placing diodes)</li>
</ul>

---

### Phase 1: Soldering the Low-Profile Components
Always solder the shortest components first so the board lays flat on your deskwhen flipped over.

 1. **The Diodes** bend the legs of your 9 diodes and insert them into the PCB
    > **CRITICAL:** Diodes are directional! make sure the black line(the cathode) on the physical glass diode matches the line on the PCB footprint. Since our code uses 'COL2ROW'
, getting this backward means the key won't register. solder them and trim the excess legs with flush cutters.
2. **the Resistors:** solder the two 4.7k resistors. these aren't strictly directional, so you can place them either way. (Even if you aren't using OLED screen yet, adding these keeps the board future-proof!).

### Phase 2: Mounting the microcontroller
1. **The Raspberry Pi Pico W:** we are surface-mounting the Pico W using its castelleated "half-moon" edges.
>  **CRITICAL:** the Pico w will be solder to the bottom side of the board, ensure the Pico W is facing the opening side so we can use its 'BOOTSEL' button.
2. **Tack and Solder:** Tack down one corner pad with a bit of solder to hold the Pico strictly in place. then, carefully solder the remaining required GPI0, GND, and 3v3 pads by heating 
