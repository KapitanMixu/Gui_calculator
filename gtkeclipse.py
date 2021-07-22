import gi

import game

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject
from game import Player
from gtkcalc import CalGtk


class EclipseGtk(Player, Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Eclipse GTK")
        self.next = None
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
        self.introMenu()

        self.show_all()
        Gtk.main()

    def introMenu(self):
        self.introBox = Gtk.Fixed()
        self.titlelabel = Gtk.Label(label="Eclipse kalkulator")
        self.titlelabel.get_style_context().add_class("titlelabel")
        self.pnames = Gtk.Label(label="Nazwy graczy")
        self.pnames.get_style_context().add_class("subtitlelabel")
        self.pnum = Gtk.Label(label="Liczba graczy")
        self.pnum.get_style_context().add_class("subtitlelabel")
        self.pn1 = Gtk.Label(label="Nazwa gracza nr. 1")
        self.pn1.get_style_context().add_class("nlabel")
        self.pn2 = Gtk.Label(label="Nazwa gracza nr. 2")
        self.pn2.get_style_context().add_class("nlabel")
        self.pn3 = Gtk.Label(label="Nazwa gracza nr. 3")
        self.pn3.get_style_context().add_class("nlabel")
        self.pn4 = Gtk.Label(label="Nazwa gracza nr. 4")
        self.pn4.get_style_context().add_class("nlabel")

        self.p1 = Gtk.Entry()
        self.p1.set_width_chars(15)
        self.p1.set_max_length(15)
        self.p2 = Gtk.Entry()
        self.p2.set_width_chars(15)
        self.p2.set_max_length(15)
        self.p3 = Gtk.Entry()
        self.p3.set_width_chars(15)
        self.p3.set_max_length(15)
        self.p4 = Gtk.Entry()
        self.p4.set_width_chars(15)
        self.p4.set_max_length(15)
        a = Gtk.ListStore(int, str)
        a.append([2, "2"])
        a.append([3, "3"])
        a.append([4, "4"])
        self.pn = Gtk.ComboBox.new_with_model(a)
        renderer_text = Gtk.CellRendererText()
        self.pn.pack_start(renderer_text, True)
        self.pn.add_attribute(renderer_text, "text", 0)
        self.pn.set_entry_text_column(1)
        self.pn.connect("changed", self.pNumberChange)
        self.pn.set_active(0)
        self.pn.set_size_request(200, 50)


        self.next = Gtk.Button.new_with_label("Dalej")
        self.next.connect("clicked", self.goNext)
        self.next.set_size_request(200, 50)

        self.men = self.createMenu()

        self.introBox.put(self.men, 0, 0)
        self.introBox.put(self.titlelabel, 350, 10)
        self.introBox.put(self.pnames, 200, 100)
        self.introBox.put(self.pnum, 750, 100)
        self.introBox.put(self.pn1, 200, 200)
        self.introBox.put(self.pn2, 200, 250)
        self.introBox.put(self.pn3, 200, 300)
        self.introBox.put(self.pn4, 200, 350)
        self.introBox.put(self.p1, 350, 195)
        self.introBox.put(self.p2, 350, 245)
        self.introBox.put(self.p3, 350, 295)
        self.introBox.put(self.p4, 350, 345)
        self.introBox.put(self.pn, 750, 200)
        self.introBox.put(self.next, 750, 300)
        self.add(self.introBox)

    def pNumberChange(self, index):
        a = index.get_active() + 2
        if a < 3:
            self.p3.set_sensitive(False)
            self.p3.set_text("")
        else:
            self.p3.set_sensitive(True)
        if a < 4:
            self.p4.set_sensitive(False)
            self.p4.set_text("")
        else:
            self.p4.set_sensitive(True)

    def goNext(self, arg):
        Players = list()
        p1 = Player()
        p1.Name = self.p1.get_text()
        if p1.Name == "":
            p1.Name = "Gracz niebieski"
        p1.Color = "blue"
        Players.append(p1)
        p2 = Player()
        p2.Name = self.p2.get_text()
        if p2.Name == "":
            p2.Name = "Gracz czerwony"
        p2.Color = "red"
        Players.append(p2)
        if int(self.pn.get_active() + 2) >= 3:
            p3 = Player()
            p3.Name = self.p3.get_text()
            if p3.Name == "":
                p3.Name = "Gracz fioletowy"
            p3.Color = "purple"
            Players.append(p3)
        if int(self.pn.get_active() + 2) >= 4:
            p4 = Player()
            p4.Name = self.p4.get_text()
            if p4.Name == "":
                p4.Name = "Gracz zielony"
            p4.Color = "green"
            Players.append(p4)

        self.close()
        self.next = CalGtk(Players)

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
        infoText = Gtk.Label(label=game.desc.Opis)
        infoText.set_line_wrap(True)
        infoText.set_max_width_chars(48)
        infoText.set_margin_top(0)

        box = Gtk.HBox()
        box.pack_start(infoText, True, True, 0)
        self.infoWidget.add(box)
        self.infoWidget.show_all()
