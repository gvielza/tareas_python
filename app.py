import wx
import wx.adv
import sqlite3


class MiVentana(wx.Frame):
    def __init__(self, *args, **kw):
        super(MiVentana, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # Crear un BoxSizer horizontal
        box_sizer_horizontal = wx.BoxSizer(wx.HORIZONTAL)
        box_sizer_vertical=wx.BoxSizer(wx.VERTICAL)

        lista_tareas = wx.StaticText(panel, label="Lista de tareas")
        tarea = wx.TextCtrl(panel, size=(300, 30))
        fecha = wx.adv.DatePickerCtrl(panel,style=wx.adv.CAL_SHOW_HOLIDAYS)
        #fecha1=wx.DateTimeCtrl(panel, style=wx.adv.DP_DROPDOWN | wx.adv.DP_SHOWCENTURY)
        #hora = wx.adv.TimePickerCtrl(panel)
        boton_agregar=wx.Button(panel, label="Agregar")
        boton_agregar.Bind(wx.EVT_BUTTON, lambda event: self.agregar_tarea(event, tarea.GetValue(), fecha.GetValue()))

        #Agregar un tipo de letra distinta al por defecto
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        lista_tareas.SetFont(font)

        # Agregar algunos elementos al BoxSizer (por ejemplo, botones)
        box_sizer_vertical.Add(lista_tareas, 0, wx.ALIGN_CENTER | wx.TOP, 10)

        box_sizer_horizontal.AddSpacer(10)
        box_sizer_horizontal.Add(tarea, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_horizontal.AddSpacer(10)
        box_sizer_horizontal.Add(fecha, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_horizontal.AddSpacer(10)
        box_sizer_horizontal.Add(boton_agregar, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_horizontal.AddSpacer(10)

        box_sizer_vertical.Add(box_sizer_horizontal)

        # Establecer el BoxSizer en el panel
        panel.SetSizer(box_sizer_vertical)

        # Cambiar la posición del BoxSizer ajustando el tamaño mínimo
        box_sizer_vertical.SetMinSize((200, -1))  # Puedes ajustar el valor según tus necesidades

        # Configuraciones adicionales para la ventana
        self.SetSize((520, 300))
        self.SetTitle('Lista de tareas')
        self.Centre()

    def agregar_tarea(self, event,  tarea,fecha):
        print(f"La tarea es: {tarea} y la fecha es: {fecha.Format('%Y-%m-%d')}")  # Imprime la tarea y la fecha (  tarea+ fecha)



if __name__ == '__main__':
    app = wx.App()
    frame = MiVentana(None)
    frame.Show()
    app.MainLoop()
