
import wx
import wx.adv


from base_datos.conexion import Conexion




class MiVentana(wx.Frame):
    def __init__(self, *args, **kw):
        super(MiVentana, self).__init__(*args, **kw)

        panel = wx.Panel(self)

        # Crear un BoxSizer horizontal
        box_sizer_horizontal = wx.BoxSizer(wx.HORIZONTAL)
        box_sizer_vertical=wx.BoxSizer(wx.VERTICAL)
        box_sizer_horizontal_nueva = wx.BoxSizer(wx.HORIZONTAL)

        lista_tareas = wx.StaticText(panel, label="Lista de tareas")
        tarea = wx.TextCtrl(panel, size=(300, 30))
        fecha = wx.adv.DatePickerCtrl(panel,style=wx.adv.CAL_SHOW_HOLIDAYS)
        #hora = wx.adv.TimePickerCtrl(panel)
        boton_agregar=wx.Button(panel, label="Agregar")
        boton_agregar.Bind(wx.EVT_BUTTON, lambda event: self.agregar_tarea(event, tarea.GetValue(), fecha.GetValue()))


        boton_eliminar_tareas = wx.Button(panel, label="Eliminar tareas")
        boton_eliminar_tareas.Bind(wx.EVT_BUTTON, lambda event: self.eliminar_tareas(event))
        #La nueva tarea
        tarea_nueva=wx.StaticText(panel, label="")
        fecha_nueva=wx.StaticText(panel, label="")


        #Agregar un tipo de letra distinta al por defecto
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        lista_tareas.SetFont(font)

        # Agregar algunos elementos al BoxSizer (por ejemplo, botones)
        box_sizer_vertical.Add(lista_tareas, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_vertical.Add(boton_eliminar_tareas, 0, wx.ALIGN_CENTER | wx.TOP, 10)

        box_sizer_horizontal.AddSpacer(10)
        box_sizer_horizontal.Add(tarea, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_horizontal.AddSpacer(10)
        box_sizer_horizontal.Add(fecha, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_horizontal.AddSpacer(10)
        box_sizer_horizontal.Add(boton_agregar, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_horizontal.AddSpacer(10)

        box_sizer_horizontal_nueva.AddSpacer(30)
        box_sizer_horizontal_nueva.Add(fecha_nueva, 0, wx.ALIGN_CENTER | wx.TOP, 10)
        box_sizer_horizontal_nueva.AddSpacer(70)
        box_sizer_horizontal_nueva.Add(tarea_nueva, 0, wx.ALIGN_CENTER | wx.TOP, 10)





        box_sizer_vertical.Add(box_sizer_horizontal)
        box_sizer_vertical.Add(box_sizer_horizontal_nueva, 0, wx.ALIGN_LEFT | wx.TOP, 10)

        # probar checkbox
        check_box = wx.CheckBox(panel, label="Marcar")
        box_h=wx.BoxSizer(wx.HORIZONTAL)
        texto = wx.StaticText(panel, label="Texto")

        box_h.Add(texto, 0, wx.ALIGN_LEFT | wx.TOP, 10)
        tareas_bd=self.obtener_tareas()

        for i in tareas_bd:
            check_box2=wx.CheckBox(panel, label="Marcar")

            box_h.Add(check_box2, 0, wx.ALIGN_LEFT | wx.TOP, 10)
            box_h.Add(i[1], 0, wx.ALIGN_LEFT | wx.TOP, 10)

        box_sizer_vertical.Add(box_h, 0, wx.ALIGN_LEFT | wx.TOP, 10)



        # Establecer el BoxSizer en el panel
        panel.SetSizer(box_sizer_vertical)

        # Cambiar la posición del BoxSizer ajustando el tamaño mínimo
        box_sizer_vertical.SetMinSize((200, -1))  # Puedes ajustar el valor según tus necesidades

        # Configuraciones adicionales para la ventana
        self.SetSize((920, 500))
        self.SetTitle('Lista de tareas')
        self.Centre()
        #Mostrar las tareas de la Base de datos
        self.mostrar_tareas()


    def agregar_tarea(self, event,  tarea,fecha):
        print(f"La tarea es: {tarea} y la fecha es: {fecha.Format('%Y-%m-%d')}")  # Imprime la tarea y la fecha (  tarea+ fecha)
        #tarea_nueva.SetLabel(tarea)
        #fecha_nueva.SetLabel(fecha.Format('%d-%m-%Y'))  # Imprime la fecha (fecha.Format('%Y-%m-%d'))
        nombre_base_de_datos = 'tareas.db'
        conexion=Conexion(nombre_base_de_datos)
        conexion.crear_tabla_tareas()
        conexion.insertar_tarea(tarea, fecha.Format('%Y-%m-%d'))

        conexion.cerrar_conexion()
        self.reiniciar_app()


    def eliminar_tareas(self, event):
        base_datos='./tareas.db'
        conexion=Conexion(base_datos)
        conexion.eliminar_tareas()
        conexion.cerrar_conexion()
        self.reiniciar_app()

    def mostrar_tareas(self):
        nombre_base_de_datos = 'tareas.db'
        conexion = Conexion(nombre_base_de_datos)
        tareas = conexion.obtener_tareas()

        box_tareas_vertical = wx.BoxSizer(wx.VERTICAL)

        panel_tareas = wx.Panel(self)
        panel_tareas.SetPosition((10, 120))




        for tarea in tareas:
            print(tarea[1])
            box_tareas_horizontal = wx.BoxSizer(wx.HORIZONTAL)
            check_box = wx.CheckBox(panel_tareas, label="")


            static_text_fecha = wx.StaticText(panel_tareas, label=tarea[2])
            static_text_tarea = wx.StaticText(panel_tareas, label=tarea[1])

            imagen_editar = wx.Image('src/editar2.png', wx.BITMAP_TYPE_PNG)
            btn_editar = wx.BitmapButton(panel_tareas, bitmap=wx.Bitmap(imagen_editar))

            imagen_eliminar = wx.Image('src/eliminar2.png', wx.BITMAP_TYPE_PNG)
            btn_eliminar = wx.BitmapButton(panel_tareas, bitmap=wx.Bitmap(imagen_eliminar))



            btn_editar.Bind(wx.EVT_BUTTON, lambda event: self.editar_tarea(event, static_text_tarea, static_text_fecha))

            box_tareas_horizontal.Add(static_text_fecha, 0, wx.ALL, 10)
            box_tareas_horizontal.Add(static_text_tarea, 0, wx.ALL, 10)
            box_tareas_horizontal.Add(btn_editar, 0, wx.ALL, 10)
            box_tareas_horizontal.Add(btn_eliminar, 0, wx.ALL, 10)
            box_tareas_horizontal.Add(check_box, 0, wx.ALL, 10)


            box_tareas_vertical.Add(box_tareas_horizontal, 0, wx.ALL, 1)



        # Establece el wx.BoxSizer vertical como el Sizer del panel
        panel_tareas.SetSizerAndFit(box_tareas_vertical)
        conexion.cerrar_conexion()
    def reiniciar_app(self):
        self.Destroy()
        app = wx.App()
        frame = MiVentana(None)
        frame.Show()
        app.MainLoop()

    def redimensionar_imagen(self, bitmap, ancho, alto):
        image = bitmap.ConvertToImage()
        image = image.Scale(ancho, alto, wx.IMAGE_QUALITY_HIGH)
        return wx.Bitmap(image)

    def editar_tarea(self, event, static_text_tarea, static_text_fecha):
        print("La tarea es: " + static_text_tarea.GetLabel() + " y la fecha es: " + static_text_fecha.GetLabel())

    def obtener_tareas(self):
        base_datos='./tareas.db'
        conexion=Conexion(base_datos)
        tareas = conexion.obtener_tareas()
        conexion.cerrar_conexion()
        return tareas



if __name__ == '__main__':
    app = wx.App()
    frame = MiVentana(None)
    frame.Show()
    app.MainLoop()
