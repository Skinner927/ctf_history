This was a fun one. I haven't done a USB capture dump before as I was always afraid they may be too difficult: they're really not!

Basically, filter on `usb.capdata` and see who's spitting out the most data. 

Long story short, stick this filter in: `usb.device_address == 21 && usb.dst == "host"`

You'll see device DESCRIPTOR Response DEVICE that lets us know deivce `21` is a Kinesis keyboard. Brand doesn't really matter here, just that we're dealing with a keyboard that speaks generic HID protocol (seen in the `CONFIGURATION` block. 

The new Wireshark on mac doesn't let you dump data easily (or I'm too stupid to figure it out), so use tshark to dump it.

```
tshark -r intercept_3dcea34fd7056a4cc2c1934dd07e4d1fed0bc0683b05b24741a999d1273339da.pcapng -Tfields -e usb.capdata -Y 'usb.device_address == 21 && usb.dst == "host" && usb.capdata' | grep -v '00:00:00:00:00:00:00:00' >  dump2.txt
```

Dump all the packet data for our keyboard and remove the null messages.

Basically each message looks like:

`[modifier, reserved, Key1, Key2, Key3, Key4, Key6, Key7]`

[https://docs.mbed.com/docs/ble-hid/en/latest/api/md_doc_HID.html](https://docs.mbed.com/docs/ble-hid/en/latest/api/md_doc_HID.html)

And a list of keymaps is found here on page 54: 
[http://www.usb.org/developers/hidpage/Hut1_12v2.pdf](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf) p.54

I made a lookup table in `keys.py`. Probably derived from someone else's code. 

Then I decode the message with `read.py` to get:
`gidIKY[LEFT_BRACE][COMMA]j0[MINUS]p1v3[SEMICOLON][MINUS]x[comma]3O7t[MINUS]4LT[comma]4t5[RIGHT_BRACE]`

Which cleaned up is:
`gidIKY[,j0-p1v3:-x,3O7t-4LT,4t5]`

Which doesn't make sense but you can see the format of the key is close. After farting around, I thought maybe the user was typing in dvorak and the OS was swapping key codes instead of the keyboard.

`dvorak-layout.png` is the layout for this specific model of keyboard and sure enough, after flipping the letters by hand, the proper key appeared. 





