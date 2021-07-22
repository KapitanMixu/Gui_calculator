import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject
from game import Player, Board, desc, pointsCal


class SumGtk(Player, Gtk.Window):
    def __init__(self, data):
        Gtk.Window.__init__(self, title="Eclipse GTK")

        self.S = data
        self.SLen = len(data)
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
        self.sumMenu(self.S)

        self.show_all()
        Gtk.main()

    def sumMenu(self, Score):
        self.sumBox = Gtk.Fixed()
        self.sumlabel = Gtk.Label(label="Wyniki")
        self.sumlabel.get_style_context().add_class("titlelabel")
        self.g1 = Gtk.Label(label="1. miejsce")
        self.g1.get_style_context().add_class("sumlabel")
        self.g2 = Gtk.Label(label="2. miejsce")
        self.g2.get_style_context().add_class("sumlabel")
        self.g3 = Gtk.Label(label="")
        self.g3.get_style_context().add_class("sumlabel")
        self.g4 = Gtk.Label(label="")
        self.g4.get_style_context().add_class("sumlabel")

        self.player1 = Gtk.Label(label="")
        self.player1.get_style_context().add_class("sumlabel")
        self.player2 = Gtk.Label(label="")
        self.player2.get_style_context().add_class("sumlabel")
        self.player3 = Gtk.Label(label="")
        self.player3.get_style_context().add_class("sumlabel")
        self.player4 = Gtk.Label(label="")
        self.player4.get_style_context().add_class("sumlabel")

        self.pkt1 = Gtk.Label(label="")
        self.pkt1.get_style_context().add_class("sumlabel")
        self.pkt2 = Gtk.Label(label="")
        self.pkt2.get_style_context().add_class("sumlabel")
        self.pkt3 = Gtk.Label(label="")
        self.pkt3.get_style_context().add_class("sumlabel")
        self.pkt4 = Gtk.Label(label="")
        self.pkt4.get_style_context().add_class("sumlabel")

        self.men = self.createMenu()

        self.sumBox.put(self.men, 0, 0)

        self.sumBox.put(self.sumlabel, 450, 20)
        self.sumBox.put(self.g1, 150, 120)
        self.sumBox.put(self.g2, 150, 190)
        self.sumBox.put(self.g3, 150, 260)
        self.sumBox.put(self.g4, 150, 330)
        self.sumBox.put(self.player1, 350, 120)
        self.sumBox.put(self.player2, 350, 190)
        self.sumBox.put(self.player3, 350, 260)
        self.sumBox.put(self.player4, 350, 330)
        self.sumBox.put(self.pkt1, 650, 120)
        self.sumBox.put(self.pkt2, 650, 190)
        self.sumBox.put(self.pkt3, 650, 260)
        self.sumBox.put(self.pkt4, 650, 330)

        self.add(self.sumBox)
        self.getScore(Score)

    def getScore(self, S):
        S.sort(key=lambda x: x.points, reverse=True)
        self.player1.set_text(self.S[0].Name)
        self.player1.get_style_context().add_class("color{}".format(self.S[0].Color))
        self.pkt1.set_text("{} pkt.".format(S[0].points))
        self.player2.set_text(self.S[1].Name)
        self.player2.get_style_context().add_class("color{}".format(self.S[1].Color))
        self.pkt2.set_text("{} pkt.".format(S[1].points))
        if len(S) >= 3:
            self.g3.set_text("3. miejsce")
            self.player3.set_text(self.S[2].Name)
            self.player3.get_style_context().add_class("color{}".format(self.S[2].Color))
            self.pkt3.set_text("{} pkt.".format(S[2].points))
        if len(S) == 4:
            self.g4.set_text("4. miejsce")
            self.player4.set_text(self.S[3].Name)
            self.player4.get_style_context().add_class("color{}".format(self.S[3].Color))
            self.pkt4.set_text("{} pkt.".format(S[3].points))

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