# Importieren der notwendigen Module aus PyQt6 für UI-Elemente und Ereignisverarbeitung
from PyQt6.QtCore import QRect, Qt, QDateTime, QTimer
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QLabel, QPushButton

# Importieren einer benutzerdefinierten Klasse TemplateRoom, die als Basis für diesen spezifischen Raum dient
from TemplateRoom import TemplateRoom


# Definition der Klasse QrCode, die von TemplateRoom erbt
class TestRaum(TemplateRoom):
    def __init__(self, parent=None):
        # Aufruf des Konstruktors der Elternklasse, um die Basisklasseninitialisierung durchzuführen
        super(TestRaum, self).__init__(parent)

        # Verbergen des Exit-Buttons in diesem speziellen Raum
        self.show_exit_button(False)

        # Initialisieren des Raumes mit einem spezifischen Bild
        self.init_room("weis.png")

        # Festlegen der Position und Größe eines UI-Elements, das vermutlich einen Sprechblasenbereich darstellt
        self.offset_balloon_x = 750
        self.offset_balloon_y = 20
        self.offset_balloon_width = 180
        self.offset_balloon_length = 650

        # Festlegen der Position und Größe des "Mundes", möglicherweise für eine Sprechblase
        self.set_offset_mouth(787, 271, 50, 150)

        # Definition der Hitboxen, die interaktive Bereiche repräsentieren, um mit Türen im Raum zu interagieren
        self.hitbox_door_1 = QRect(5, 215, 350, 600)
        self.append_hitbox(self.hitbox_door_1)


        # Eine weitere Hitbox, die eine Schaltfläche für Vorwärts- oder Weiteraktionen darstellt
        self.hitbox_forward = QRect(1270, 150, 100, 25)
        self.append_hitbox(self.hitbox_forward)

        # Interne Zähler, die verwendet werden, um den Dialogfortschritt zu steuern
        self.__counter = 0

        # Eine spezielle Hitbox für ein Easter Egg
        self.hitbox_easter_egg = QRect(740, 410, 35, 35)

        # Initialisieren der Textzeilen, die in der Benutzeroberfläche angezeigt werden
        self.text_line_1 = ""
        self.text_line_2 = "Hallo und herzlich willkommen,"
        self.text_line_3 = "zum Tag der offenen Tür am 16. März 2024"
        self.text_line_4 = "im SBS Herzogenaurach."
        self.text_line_5 = ""
        self.text_line_6 = "                                    weiter"

#------------------------------------------------------------------------------------------------------

        # Einfügen eines Labels mit einem Willkommens-Text
        self.welcome_label = QLabel("Willkommen im TestRaum!", self)
        self.welcome_label.setGeometry(100, 100, 300, 50)  # Setze die Position und Größe des Labels
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Zentriere den Text im Label
        self.welcome_label.setStyleSheet(
            "background-color: lightgrey; color: black; font-size: 20px;")  # Stil des Labels
# ------------------------------------------------------------------------------------------------------

        #Button hinzufügen
        self.action_button = QPushButton("Aktion ausführen", self)
        self.action_button.setGeometry(500, 800, 200, 50)  # Position und Größe des Buttons
        #self.action_button.clicked.connect(self.button_action)  # Verbindung des Buttons mit einer Funktion
        #self.action_button.setEnabled(False)  # Button initial deaktivieren

    #def button_action(self):
        #print("Button wurde geklickt")
# ------------------------------------------------------------------------------------------------------


        # MP3-Button hinzufügen
        self.mp3_button = QPushButton("Play MP3", self)
        self.mp3_button.setGeometry(600, 400, 150, 50)  # Angenommene Position und Größe
        #self.mp3_button.clicked.connect(self.play_mp3_file)  # Verbindung des Buttons mit der play_mp3_file Funktion

    #def play_mp3_file(self):
        #self.play_sound("TemplateRoom.mp3")