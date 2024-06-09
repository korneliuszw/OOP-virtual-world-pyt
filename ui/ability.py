import dearpygui.dearpygui as dpg

ability_tag = "ability"

def create_ability_status():
    dpg.add_text(tag=ability_tag)

def show_ability_status(ability):
    if ability.is_activated():
        text = "Active"
    elif ability.is_available():
        text = "Ready"
    else:
        text = "On cooldown"
    
    dpg.configure_item(ability_tag, default_value=text)