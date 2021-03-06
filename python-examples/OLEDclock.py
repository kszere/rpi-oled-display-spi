#IMPORT POTRZEBNYCH BIBLIOTEK
import gaugette.ssd1306
import time
import sys

#USTAWIENIE ZMIENNYCH
RESET_PIN = 5 #(GPIO 24)
DC_PIN    = 4 #(GPIO 23)

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

offset = 0

#DOPOKI PRAWDA, WYKONUJ:
while True:

    if offset == 0:
        text = time.strftime("%A")
        led.draw_text2(0,0,text,2)
        text = time.strftime("%e %b %Y")
        led.draw_text2(0,16,text,2)
        text = time.strftime("%X")
        led.draw_text2(0,32+4,text,3)
        led.display()
        time.sleep(1)
    else:
        time.sleep(1)

    #PRZEWIJANIE ZAWARTOSCI
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.01)
