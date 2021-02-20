from dearpygui.core import *
from dearpygui.simple import *

def check_sarc(sender, data):
    with window("Sarcasm Detector"):
        #To be contd...



set_main_window_size(540,720)
set_global_font_scale(1.25)
set_style_window_padding(30,30)
set_theme("Gold")

with window("Sarcasm Detector", width=520, height=677):
    print("Success")
    set_window_pos("Sarcasm Detector",0,0)
    add_separator()
    add_spacing(count=12)

    add_text("Enter Sample text",color=[252,160,33])
    add_spacing(count=12)

    add_input_text("Input", width=400)
    add_spacing(count=12)

    add_button("Check", callback=check_sarc)


start_dearpygui()