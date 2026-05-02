import usb_hid
import storage
import board
import digitalio

#--- COMFIGURATION ---
# We'll use one of your keys as a 'safety switch' to prevent the device from acting as a keyboard when you dont want it to. Change this to the key you want to use as a safety switch.
row_pin = board.GP2
col_pin = board.GP5

# Setup the pins to check for a press
row = digitalio.DigitalInOut(row_pin)
row.direction = digitalio.Direction.INPUT
row.value = False

col = digitalio.DigitalInOut(col_pin)
col.direction = digitalio.Direction.INPUT
col.pull = digitalio.Pull.UP

# --- LOGIC ---
# If the button is not pressed (value is true due to Pull.UP), hide the drive.
# If you HOLD the top-left key while plugging it in, the drive will appear.
if col.value:
    storage.disable_usb_drive()

# --- CUSTOMIZATION ---
# This renames the device in your 'Device and Printer' menu.
new_name = "Shortcuit macro pad"
storage.remount("/", False)
m = storage.getmount("/")
m.label = "SHORTCUIT"
storage.remount("/", True)
usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.MOUSE, usb_hid.Device.CONSUMER_CONTROL))
