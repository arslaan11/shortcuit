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
2. **Tack and Solder:** Tack down one corner pad with a bit of solder to hold the Pico strictly in place. then, carefully solder the remaining required GPI0, GND, and 3v3 pads by heating the half-moon edge and the PCB pad simultaneously.

### Phase 3: The Plate & Switches (The "Sandwich" Step)
1. **Snap Switches to the Plate:** take your top plate of your case. snap all 9 akko creamy yellow pro switches firmly into the square cutouts.
2. **attach the pcb.** Carefully line up the metal pins of all 9 switches with the holes on your soldered PCB. gently push the PCB onto the switches pins until it is sitting flush against the plastic center pegs of the switches.
3. **Solder the switches:** Flip the whole assembly over and solder 18 switch pins to the PCB.
4. **The Rotary Encoder:** Insert the EC11 rotary encoder into its slot, ensure it is sitting perfectly straight, and solder its pins and the large structural mounting legs.

### phase 4: Threaded Inserts & Final Case Assembly
To give the case a premium, reuseable closure, we use brass heat-set inserts instead of threading screws directly into plastic.

1. **Install M2 Heated Inserts:** Heat up ypur soldering iron to around 200°C (390°F). place a brass M2 insert over the mounting hole on the inside of the 3D printed top .plate. Gently press the tip of the iron into the insert, The heat will melt the PLA+ just enough for the insert to slide in. push it until it is perfectly flush with the plastic, then pull the iron straight out and let it cool for a minute.
2. **close the case:** Place the bottom plate over the assembly, line up the holes with your newly installed brass inserts.
3. **Screw it together:** Use your M2 screws to firmly attach the bottom plate to the top plate. Do not overtighten!
4. **The Finishing Touches:** Push your red custom keycaps onto your switches, and slide your printed (or aluminum) know onto the rotary encoder.

### Last Step
**Install the firmware using the guide and then enjoy**
