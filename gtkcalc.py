import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject
from game import Player, Board, desc, pointsCal
from gtksum import SumGtk


class CalGtk(Player, Gtk.Window):
    def __init__(self, data):
        Gtk.Window.__init__(self, title="Eclipse GTK")

        self.sum = None

        self.P = data
        self.PLen = len(data)
        self.PNum = 0

        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('styles.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider,
        Gtk.STYLE_PROVIDER_PRIORITY_USER)

        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(1000, 500)
        self.set_resizable(False)
        self.connect("destroy", Gtk.main_quit)
        self.calMenu(self.P[0])

        self.show_all()
        Gtk.main()

    def calMenu(self, PNow):
        self.PlayerNow = PNow
        self.BoardNow = Board()
        self.calBox = Gtk.Fixed()

        self.label0 = Gtk.Label(label="Gracz")
        self.label0.get_style_context().add_class("subtitlelabel")

        self.PlayerName = Gtk.Label(label="{}".format(self.PlayerNow.Name))
        self.PlayerName.get_style_context().add_class("subtitlelabel")
        self.PlayerName.get_style_context().add_class("color{}".format(self.PlayerNow.Color))

        self.nex = Gtk.Button.new_with_label("Dalej")
        self.nex.connect("clicked", self.goNex)
        self.nex.set_size_request(200, 50)

        #Mapa galaktyki
        self.label1 = Gtk.Label(label="Mapa galaktyki")
        self.label1.get_style_context().add_class("subtitlelabel")

        self.center = Gtk.ToggleButton.new_with_label("Centrum")
        self.center.get_style_context().add_class("map")
        self.center.connect("clicked", self.changeColor)
        self.center.set_size_request(90, 90)

        #sektor wewnętrzny
        self.w1 = Gtk.ToggleButton.new_with_label("W1")
        self.w1.get_style_context().add_class("map")
        self.w1.connect("clicked", self.changeColor)
        self.w1.set_size_request(50, 50)
        self.w2 = Gtk.ToggleButton.new_with_label("W2")
        self.w2.get_style_context().add_class("map")
        self.w2.connect("clicked", self.changeColor)
        self.w2.set_size_request(50, 50)
        self.w3 = Gtk.ToggleButton.new_with_label("W3")
        self.w3.get_style_context().add_class("map")
        self.w3.connect("clicked", self.changeColor)
        self.w3.set_size_request(50, 50)
        self.w4 = Gtk.ToggleButton.new_with_label("W4")
        self.w4.get_style_context().add_class("map")
        self.w4.connect("clicked", self.changeColor)
        self.w4.set_size_request(50, 50)
        self.w5 = Gtk.ToggleButton.new_with_label("W5")
        self.w5.get_style_context().add_class("map")
        self.w5.connect("clicked", self.changeColor)
        self.w5.set_size_request(50, 50)
        self.w6 = Gtk.ToggleButton.new_with_label("W6")
        self.w6.get_style_context().add_class("map")
        self.w6.connect("clicked", self.changeColor)
        self.w6.set_size_request(50, 50)

        #sektor zewnętrzny
        self.z1 = Gtk.ToggleButton.new_with_label("Z1")
        self.z1.get_style_context().add_class("minimap")
        self.z1.connect("clicked", self.changeColor)
        self.z1.set_size_request(40, 40)
        self.z2 = Gtk.ToggleButton.new_with_label("Z2")
        self.z2.get_style_context().add_class("minimap")
        self.z2.connect("clicked", self.changeColor)
        self.z2.set_size_request(40, 40)
        self.z3 = Gtk.ToggleButton.new_with_label("Z3")
        self.z3.get_style_context().add_class("minimap")
        self.z3.connect("clicked", self.changeColor)
        self.z3.set_size_request(40, 40)
        self.z4 = Gtk.ToggleButton.new_with_label("Z4")
        self.z4.get_style_context().add_class("minimap")
        self.z4.connect("clicked", self.changeColor)
        self.z4.set_size_request(40, 40)
        self.z5 = Gtk.ToggleButton.new_with_label("Z5")
        self.z5.get_style_context().add_class("minimap")
        self.z5.connect("clicked", self.changeColor)
        self.z5.set_size_request(40, 40)
        self.z6 = Gtk.ToggleButton.new_with_label("Z6")
        self.z6.get_style_context().add_class("minimap")
        self.z6.connect("clicked", self.changeColor)
        self.z6.set_size_request(40, 40)
        self.z7 = Gtk.ToggleButton.new_with_label("Z7")
        self.z7.get_style_context().add_class("minimap")
        self.z7.connect("clicked", self.changeColor)
        self.z7.set_size_request(40, 40)
        self.z8 = Gtk.ToggleButton.new_with_label("Z8")
        self.z8.get_style_context().add_class("minimap")
        self.z8.connect("clicked", self.changeColor)
        self.z8.set_size_request(40, 40)
        self.z9 = Gtk.ToggleButton.new_with_label("Z9")
        self.z9.get_style_context().add_class("minimap")
        self.z9.connect("clicked", self.changeColor)
        self.z9.set_size_request(40, 40)
        self.z10 = Gtk.ToggleButton.new_with_label("Z10")
        self.z10.get_style_context().add_class("minimap")
        self.z10.connect("clicked", self.changeColor)
        self.z10.set_size_request(40, 40)
        self.z11 = Gtk.ToggleButton.new_with_label("Z11")
        self.z11.get_style_context().add_class("minimap")
        self.z11.connect("clicked", self.changeColor)
        self.z11.set_size_request(40, 40)
        self.z12 = Gtk.ToggleButton.new_with_label("Z12")
        self.z12.get_style_context().add_class("minimap")
        self.z12.connect("clicked", self.changeColor)
        self.z12.set_size_request(40, 40)

        #Obrzeża
        self.label2 = Gtk.Label(label="Obrzeża")
        self.label2.get_style_context().add_class("subtitlelabel")
        adj1 = Gtk.Adjustment(0, 0, 20, 1, 1, 0)
        self.os = Gtk.VScale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj1)
        self.os.set_value_pos(Gtk.PositionType.RIGHT)
        self.os.set_size_request(180, 20)
        self.os.set_digits(0)

        #technologie
        self.label3 = Gtk.Label(label="Technologie")
        self.label3.get_style_context().add_class("subtitlelabel")
        self.label31 = Gtk.Label(label="Technologie wojskowe")
        self.label31.get_style_context().add_class("nlabel")
        self.label32 = Gtk.Label(label="Technologie naukow")
        self.label32.get_style_context().add_class("nlabel")
        self.label33 = Gtk.Label(label="Technologie cywilne")
        self.label33.get_style_context().add_class("nlabel")

        adjt1 = Gtk.Adjustment(0, 0, 7, 1, 1, 0)
        adjt2 = Gtk.Adjustment(0, 0, 7, 1, 1, 0)
        adjt3 = Gtk.Adjustment(0, 0, 7, 1, 1, 0)
        self.t1 = Gtk.VScale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjt1)
        self.t1.set_value_pos(Gtk.PositionType.RIGHT)
        self.t1.set_size_request(180, 20)
        self.t1.set_digits(0)
        self.t2 = Gtk.VScale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjt2)
        self.t2.set_value_pos(Gtk.PositionType.RIGHT)
        self.t2.set_size_request(180, 20)
        self.t2.set_digits(0)
        self.t3 = Gtk.VScale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjt3)
        self.t3.set_value_pos(Gtk.PositionType.RIGHT)
        self.t3.set_size_request(180, 20)
        self.t3.set_digits(0)

        #dodatkowe technologie
        self.label4 = Gtk.Label(label="Technologie dodatkowe")
        self.label4.get_style_context().add_class("subtitlelabel")
        self.st1 = Gtk.CheckButton.new_with_label("Dodatkowe fundusze na edukację")
        self.st1.get_style_context().add_class("nlabel")
        self.st2 = Gtk.CheckButton.new_with_label("Krąg centralny")
        self.st2.get_style_context().add_class("nlabel")
        self.st3 = Gtk.CheckButton.new_with_label("Rządy na odległość")
        self.st3.get_style_context().add_class("nlabel")
        self.st4 = Gtk.CheckButton.new_with_label("Telewizja wojskowa")
        self.st4.get_style_context().add_class("nlabel")

        #Emblematy
        a1 = Gtk.ListStore(int, str)
        a2 = Gtk.ListStore(int, str)
        a3 = Gtk.ListStore(int, str)
        a4 = Gtk.ListStore(int, str)
        for k in range(5):
            a1.append([k, str(k)])
            a2.append([k, str(k)])
            a3.append([k, str(k)])
            a4.append([k, str(k)])
        self.e1 = Gtk.ComboBox.new_with_model(a1)
        renderer_text = Gtk.CellRendererText()
        self.e1.pack_start(renderer_text, True)
        self.e1.add_attribute(renderer_text, "text", 0)
        self.e1.set_active(0)
        self.e1.set_size_request(100, 20)
        self.e2 = Gtk.ComboBox.new_with_model(a2)
        renderer_text = Gtk.CellRendererText()
        self.e2.pack_start(renderer_text, True)
        self.e2.add_attribute(renderer_text, "text", 0)
        self.e2.set_active(0)
        self.e2.set_size_request(100, 20)
        self.e3 = Gtk.ComboBox.new_with_model(a3)
        renderer_text = Gtk.CellRendererText()
        self.e3.pack_start(renderer_text, True)
        self.e3.add_attribute(renderer_text, "text", 0)
        self.e3.set_active(0)
        self.e3.set_size_request(100, 20)
        self.e4 = Gtk.ComboBox.new_with_model(a4)
        renderer_text = Gtk.CellRendererText()
        self.e4.pack_start(renderer_text, True)
        self.e4.add_attribute(renderer_text, "text", 0)
        self.e4.set_active(0)
        self.e4.set_size_request(100, 20)

        self.le1 = Gtk.Label("Emblemat 1")
        self.le1.get_style_context().add_class("nlabel")
        self.le2 = Gtk.Label("Emblemat 2")
        self.le2.get_style_context().add_class("nlabel")
        self.le3 = Gtk.Label("Emblemat 3")
        self.le3.get_style_context().add_class("nlabel")
        self.le4 = Gtk.Label("Emblemat 4")
        self.le4.get_style_context().add_class("nlabel")

        self.men = self.createMenu()

        self.calBox.put(self.men, 0, 0)

        self.calBox.put(self.label0, 730, 310)
        self.calBox.put(self.PlayerName, 730, 350)
        self.calBox.put(self.nex, 730, 400)
        self.calBox.put(self.label1, 40, 10)

        self.calBox.put(self.center, 170, 170)

        self.calBox.put(self.w1, 190, 110)
        self.calBox.put(self.w2, 270, 150)
        self.calBox.put(self.w3, 270, 230)
        self.calBox.put(self.w4, 190, 270)
        self.calBox.put(self.w5, 110, 150)
        self.calBox.put(self.w6, 110, 230)

        self.calBox.put(self.z1, 195, 65)
        self.calBox.put(self.z2, 270, 90)
        self.calBox.put(self.z3, 330, 140)
        self.calBox.put(self.z4, 345, 195)
        self.calBox.put(self.z5, 330, 250)
        self.calBox.put(self.z6, 270, 300)
        self.calBox.put(self.z7, 195, 325)
        self.calBox.put(self.z8, 120, 300)
        self.calBox.put(self.z9, 60, 250)
        self.calBox.put(self.z10, 45, 195)
        self.calBox.put(self.z11, 60, 140)
        self.calBox.put(self.z12, 120, 90)

        self.calBox.put(self.label2, 40, 360)
        self.calBox.put(self.os, 80, 420)

        self.calBox.put(self.label3, 450, 10)
        self.calBox.put(self.label31, 450, 50)
        self.calBox.put(self.label32, 450, 110)
        self.calBox.put(self.label33, 450, 170)

        self.calBox.put(self.t1, 450, 80)
        self.calBox.put(self.t2, 450, 140)
        self.calBox.put(self.t3, 450, 200)

        self.calBox.put(self.label4, 450, 260)
        self.calBox.put(self.st1, 450, 300)
        self.calBox.put(self.st2, 450, 330)
        self.calBox.put(self.st3, 450, 360)
        self.calBox.put(self.st4, 450, 390)

        self.calBox.put(self.e1, 830, 50)
        self.calBox.put(self.e2, 830, 110)
        self.calBox.put(self.e3, 830, 170)
        self.calBox.put(self.e4, 830, 230)
        self.calBox.put(self.le1, 730, 55)
        self.calBox.put(self.le2, 730, 115)
        self.calBox.put(self.le3, 730, 175)
        self.calBox.put(self.le4, 730, 235)

        self.add(self.calBox)

    def goNex(self, arg):
        if self.PNum == 0:
            self.Score = list()
        self.PNum += 1
        if self.PNum < self.PLen:
            self.savePlayer(self.Score)
            self.PlayerName.get_style_context().remove_class("color{}".format(self.PlayerNow.Color))
            self.PlayerNow = self.P[self.PNum]
            self.PlayerName.set_text(self.PlayerNow.Name)
            self.PlayerName.get_style_context().add_class("color{}".format(self.PlayerNow.Color))
            self.resetMap()
        else:
            self.savePlayer(self.Score)
            self.close()
            self.sum = SumGtk(self.Score)

    def changeColor(self, source):
        if source.get_active():
            source.get_style_context().add_class("map{}".format(self.PlayerNow.Color))
            if source.get_label()[0] == "Z":
                for x in range(12):
                    if source.get_label()[1:] == str(x + 1):
                        self.BoardNow.z[x] = 1
                        self.PlayerNow.Hexs[2] += 1
            elif source.get_label()[0] == "W":
                for x in range(6):
                    if source.get_label()[1:] == str(x + 1):
                        self.BoardNow.w[x] = 1
                        self.PlayerNow.Hexs[1] += 1
            else:
                self.BoardNow.c = 1
                self.PlayerNow.Hexs[0] = 1
        else:
            source.get_style_context().add_class("map")
            if source.get_label()[0] == "Z":
                for x in range(12):
                    if source.get_label()[1:] == str(x + 1):
                        self.BoardNow.z[x] = 0
                        self.PlayerNow.Hexs[2] -= 1
            elif source.get_label()[0] == "W":
                for x in range(6):
                    if source.get_label()[1:] == str(x + 1):
                        self.BoardNow.w[x] = 0
                        self.PlayerNow.Hexs[1] -= 1
            else:
                self.BoardNow.c = 0
                self.PlayerNow.Hexs[0] = 0

    def savePlayer(self, Score):
        #Obrzeża
        self.PlayerNow.Hexs[3] = self.os.get_value()
        self.os.set_range(0, self.os.get_adjustment().get_upper() - self.os.get_value())
        self.os.set_value(0)

        #Technologie
        self.PlayerNow.Techs[0] = self.t1.get_value()
        self.t1.set_value(0)
        self.PlayerNow.Techs[1] = self.t2.get_value()
        self.t2.set_value(0)
        self.PlayerNow.Techs[2] = self.t3.get_value()
        self.t3.set_value(0)

        #Technologie specjalne
        if self.st1.get_active():
            self.PlayerNow.Stechs[0] = 1
            self.st1.set_active(False)
        if self.st2.get_active():
            self.PlayerNow.Stechs[1] = 1
            self.st2.set_active(False)
        if self.st3.get_active():
            self.PlayerNow.Stechs[2] = 1
            self.st3.set_active(False)
        if self.st4.get_active():
            self.PlayerNow.Stechs[3] = 1
            self.st4.set_active(False)

        #Emblematy
        self.PlayerNow.Emb[0] = int(self.e1.get_active())
        self.e1.set_active(0)
        self.PlayerNow.Emb[1] = int(self.e2.get_active())
        self.e2.set_active(0)
        self.PlayerNow.Emb[2] = int(self.e3.get_active())
        self.e3.set_active(0)
        self.PlayerNow.Emb[3] = int(self.e4.get_active())
        self.e4.set_active(0)

        #liczenie punktów
        self.PlayerNow.points = pointsCal(self.PlayerNow)
        Score.append(self.PlayerNow)

    def resetMap(self):
        ###MAP
        #SEKJA ZEWNĘTRZNA
        if self.BoardNow.z[0] == 1:
            self.z1.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[0] = 0
        if self.BoardNow.z[1] == 1:
            self.z2.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[1] = 0
        if self.BoardNow.z[2] == 1:
            self.z3.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[2] = 0
        if self.BoardNow.z[3] == 1:
            self.z4.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[3] = 0
        if self.BoardNow.z[4] == 1:
            self.z5.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[4] = 0
        if self.BoardNow.z[5] == 1:
            self.z6.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[5] = 0
        if self.BoardNow.z[6] == 1:
            self.z7.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[6] = 0
        if self.BoardNow.z[7] == 1:
            self.z8.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[7] = 0
        if self.BoardNow.z[8] == 1:
            self.z9.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[8] = 0
        if self.BoardNow.z[9] == 1:
            self.z10.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[9] = 0
        if self.BoardNow.z[10] == 1:
            self.z11.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[10] = 0
        if self.BoardNow.z[11] == 1:
            self.z12.set_sensitive(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[11] = 0
        #SEKCJA WEWNĘTRZNA
        if self.BoardNow.w[0] == 1:
            self.w1.set_sensitive(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[0] = 0
        if self.BoardNow.w[1] == 1:
            self.w2.set_sensitive(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[1] = 0
        if self.BoardNow.w[2] == 1:
            self.w3.set_sensitive(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[2] = 0
        if self.BoardNow.w[3] == 1:
            self.w4.set_sensitive(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[3] = 0
        if self.BoardNow.w[4] == 1:
            self.w5.set_sensitive(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[4] = 0
        if self.BoardNow.w[5] == 1:
            self.w6.set_sensitive(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[5] = 0
        #Centrum
        if self.BoardNow.c == 1:
            self.center.set_sensitive(False)
            self.PlayerNow.Hexs[0] = 0
            self.BoardNow.c = 0

    def createMenu(self):
        self.menuBar = Gtk.MenuBar()
        self.infoMenu = Gtk.Menu()
        self.info = Gtk.MenuItem("Info")
        self.action = Gtk.MenuItem("Opis aplikacji")
        self.action.connect("activate", self.showInfo)
        self.info.set_submenu(self.infoMenu)
        self.infoMenu.append(self.action)
        self.menuBar.append(self.info)

        return self.menuBar

    def showInfo(self, arg):
        self.infoWidget = Gtk.Window()
        self.infoWidget.set_title("Opis aplikacji")
        self.infoWidget.set_position(Gtk.WindowPosition.CENTER)
        self.infoWidget.set_default_size(300, 100)
        self.infoWidget.set_resizable(False)
        infoText = Gtk.Label(label=desc.Opis)
        infoText.set_line_wrap(True)
        infoText.set_max_width_chars(48)
        infoText.set_margin_top(0)

        box = Gtk.HBox()
        box.pack_start(infoText, True, True, 0)
        self.infoWidget.add(box)
        self.infoWidget.show_all()