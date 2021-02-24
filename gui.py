from dearpygui.core import *
from dearpygui.simple import *
import main


def check_sarc(sender,data):
    
    print(len(pred))

    with window("Sarcasm Detector"):
        if len(pred) == 0:
            add_spacing(count=12)
            add_separator()
            add_spacing(count=12)

            input_val = get_value("Input")
            pred_text,colour = main.predict(input_val)
            pred.append(pred_text)
            print(len(pred))

            add_text(pred[-1],color=colour)
        else:
            hide_item(pred[-1])
            input_val = get_value("Input")
            pred_text,colour = main.predict(input_val)
            pred.append(pred_text)

            add_text(pred[-1],color=colour)


pred = []
set_main_window_size(720,540)
set_global_font_scale(1.25)
set_style_window_padding(30,30)
set_theme("Gold")

with window("Sarcasm Detector", width=720, height=540):
    print("Success")
    set_window_pos("Sarcasm Detector",0,0)
    add_separator()
    add_spacing(count=12)

    add_text("Enter Sample text",color=[252,160,33])
    add_spacing(count=12)

    add_input_text("Input", width=600)
    add_spacing(count=12)

    add_button("Check", callback=check_sarc)
    


start_dearpygui()