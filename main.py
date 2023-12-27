from datetime import datetime
import dearpygui.dearpygui as dpg

fecha_actual=datetime.now()
anno=fecha_actual.year
dpg.create_context()
viewport=dpg.create_viewport(title='Tareas', width=600, height=600)
date_picker_id = None

def on_date_selected(sender, app_data):
    year = app_data["year"]+1900
    month = app_data["month"]+1
    day = app_data["month_day"]
    selected_date = datetime(year, month, day)
    print(f"Fecha {year} ,  month {month} , day {day}")

with dpg.window(label="Tareas", width=600, height=600):
    dpg.add_input_text(width=300, height=30)
    #dpg.add_button(label="fecha", pos=(310, 27),callback=show_hide_date_picker)
    fecha_id=dpg.add_date_picker(default_value={"month_day": 1, "month": 11, "year": 123},pos=(310, 27))
    dpg.add_button(label="Agregar", pos=(500, 27), callback=lambda : on_date_selected(None, dpg.get_value(fecha_id)))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()