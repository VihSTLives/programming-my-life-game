from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal
from PySide6.QtCore import QTimer
from PySide6.QtGui import QFont

class MainWindow(QMainWindow) :
    def __init__(self, player) : 
        super().__init__()

        self.player = player
        self.setWindowTitle("- Programmin My Life -")
        self.resize(1920,1080)

        self.charge_window(MainMenuWindow)
    
    def charge_window(self, window_class) :
        new_window = window_class(self, self.player)
        self.setCentralWidget(new_window)

class Window(QWidget) :
    def __init__(self, main_window, player) :
        super().__init__(main_window)

        self.player = player
        self.main_window = main_window

    def build_hud(self) :
        self.BackgroundStatusBarHealth = QLabel(self)
        self.BackgroundStatusBarHealth.setPixmap(QPixmap("assets/MainGameWindow/BackgroundStatusBar.png"))
        self.BackgroundStatusBarHealth.setScaledContents(True)
        self.BackgroundStatusBarHealth.setGeometry(0, 0, 250, 45)
        self.BackgroundStatusBarThirst = QLabel(self)
        self.BackgroundStatusBarThirst.setPixmap(QPixmap("assets/MainGameWindow/BackgroundStatusBar.png"))
        self.BackgroundStatusBarThirst.setScaledContents(True)
        self.BackgroundStatusBarThirst.setGeometry(0, 40, 250, 45)
        self.BackgroundStatusBarHunger = QLabel(self)
        self.BackgroundStatusBarHunger.setPixmap(QPixmap("assets/MainGameWindow/BackgroundStatusBar.png"))
        self.BackgroundStatusBarHunger.setScaledContents(True)
        self.BackgroundStatusBarHunger.setGeometry(0, 80, 250, 45)
        self.health_bar_max_width = 250
        self.thirst_bar_max_width = 250
        self.hunger_bar_max_width = 250
        self.health_fill = QLabel(self)
        self.health_fill.setPixmap(QPixmap("assets/MainGameWindow/ProgressStatusBarHealth.png"))
        self.health_fill.setScaledContents(True)
        self.health_fill.setGeometry(0, 0, self.health_bar_max_width, 45)
        self.update_status_bar(
            self.health_fill,
            self.player.health,
            self.player.max_health,
            self.health_bar_max_width
        )
        self.thirst_fill = QLabel(self)
        self.thirst_fill.setPixmap(QPixmap("assets/MainGameWindow/ProgressStatusBar.png"))
        self.thirst_fill.setScaledContents(True)
        self.thirst_fill.setGeometry(0, 40, self.thirst_bar_max_width, 45)
        self.update_status_bar(
            self.thirst_fill,
            self.player.thirst,
            self.player.max_thirst,
            self.thirst_bar_max_width
        )
        self.hunger_fill = QLabel(self)
        self.hunger_fill.setPixmap(QPixmap("assets/MainGameWindow/ProgressStatusBar.png"))
        self.hunger_fill.setScaledContents(True)
        self.hunger_fill.setGeometry(0, 80, self.hunger_bar_max_width, 45)
        self.update_status_bar(
            self.hunger_fill,
            self.player.hunger,
            self.player.max_hunger,
            self.hunger_bar_max_width
        )
        font = QFont()
        font.setPointSize(22)
        self.label_health = QLabel("HEALTH", self)
        self.label_health.setStyleSheet("color: white;")
        self.label_health.setFont(font)
        self.label_health.setGeometry(70, 5, 220, 40)
        self.label_thirst = QLabel("THIRST", self)
        self.label_thirst.setStyleSheet("color: white;")
        self.label_thirst.setFont(font)
        self.label_thirst.setGeometry(70, 45, 220, 40)
        self.label_hunger = QLabel("HUNGER", self) 
        self.label_hunger.setStyleSheet("color: white;")
        self.label_hunger.setFont(font)
        self.label_hunger.setGeometry(60, 85, 220, 40)
        self.label_dev_skill = QLabel("Dev Skill: " + str(self.player.dev_skill), self)
        self.label_dev_skill.setStyleSheet("color: white;")
        self.label_dev_skill.setFont(font)
        self.label_dev_skill.setGeometry(40, 120, 300, 40)
        self.label_money = QLabel("Money: $" + str(self.player.money), self)
        self.label_money.setStyleSheet("color: white;")
        self.label_money.setFont(font)
        self.label_money.setGeometry(40, 150, 350, 40)
    
    def update_status_bar(self, bar_fill, current_value, max_value, max_width):
        if current_value < 0:
            current_value = 0
        if current_value > max_value:
            current_value = max_value

        porcentagem = current_value / max_value
        largura = int(max_width * porcentagem)

        bar_fill.setFixedWidth(largura)

    def update_status_hud(self) :
        self.label_dev_skill.setText("Dev Skill: " + str(self.player.dev_skill))
        self.label_money.setText("Money: $" + str(self.player.money))

class MainMenuWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)

        self.build_it()

    
    def build_it(self) :
        self.setWindowTitle("- Main Menu -")
        self.resize(1920, 1080)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/MainMenuWindow/backgroundMainMenu.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 1920, 1080)
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap("assets/MainMenuWindow/logoMainMenu.png"))
        self.logo.setScaledContents(True)
        self.logo_pos_x = 510
        self.logo_pos_y = 120
        self.logo_direction = "CENTER"
        self.logo.setGeometry(self.logo_pos_x, self.logo_pos_y, 900, 350)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(85)
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setFamily("Arial")
        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(460,675,400,100)
        self.play_button.setFont(font)
        self.play_button.setStyleSheet("""
            QPushButton {
                background-color: #1a1a1a;
                color: white;
                font-size: 24px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2a2a2a;
            }
            QPushButton:pressed {
                background-color: #0f0f0f;
            }
            """)
        self.play_button.clicked.connect(lambda : self.main_window.charge_window(MainGameWindow))
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(1060,675,400,100)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("""
            QPushButton {
                background-color: #1a1a1a;
                color: white;
                font-size: 24px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2a2a2a;
            }
            QPushButton:pressed {
                background-color: #0f0f0f;
            }
            """)
        self.exit_button.clicked.connect(QApplication.quit)

    def update_animation(self):
        self.pos_x = self.logo.x()
        self.pos_y = self.logo.y()

        if self.logo_direction == "CENTER" :
            self.logo.move(self.pos_x - 3, self.pos_y - 3)
            self.logo_direction = "LEFT" 
        elif self.logo_direction == "LEFT" :
            self.logo.move(self.pos_x + 3, self.pos_y - 3)
            self.logo_direction = "RIGHT1"
        elif self.logo_direction == "RIGHT1" :
            self.logo.move(self.pos_x + 3, self.pos_y + 3)
            self.logo_direction = "RIGHT2"
        elif self.logo_direction == "RIGHT2" :
            self.logo.move(self.pos_x - 3, self.pos_y + 3)
            self.logo_direction = "CENTER"

class MainGameWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)
    
        self.build_it()
    
    def build_it(self) :
        self.setWindowTitle("- Main Game -")
        self.resize(1920, 1080)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/MainGameWindow/BackgroundMainGame.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 1920, 1080)
        self.blackbase = QLabel(self)
        self.blackbase.setPixmap(QPixmap("assets/MainGameWindow/BlackBase.png"))
        self.blackbase.setScaledContents(True)
        self.blackbase.setGeometry(1460,333,350,400)
        self.bookCase = InteractiveImage(
            "assets/MainGameWindow/BookcaseMainGame.png",
            0, 200, 300, 600,
            self
        )
        self.computer = InteractiveImage(
            "assets/MainGameWindow/ComputerMainGame.png",
            460, 345, 450, 500,
            self
        )
        self.beg = InteractiveImage(
            "assets/MainGameWindow/BegMainGame.png",
            200, 590, 300, 290,
            self
        )
        self.door = InteractiveImage(
            "assets/MainGameWindow/DoorMainGame.png",
            1430, 95, 410, 650,
            self
        )
        self.bed = InteractiveImage(
            "assets/MainGameWindow/BedMainGame.png",
            940, 400, 550, 600,
            self
        )
        self.build_hud()

class StudyWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)
    
        self.build_it()
    
    def build_it(self) :
        self.setWindowTitle("- Study -")
        self.resize(1920, 1080)

class FeedingWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)
    
        self.build_it()
    
    def build_it(self) :
        self.setWindowTitle("- Feeding -")
        self.resize(1920, 1080)

class WorkWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)
    
        self.build_it()
    
    def build_it(self) :
        self.setWindowTitle("- Work -")
        self.resize(1920, 1080)

class SleepingWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)
    
        self.build_it()
    
    def build_it(self) :
        self.setWindowTitle("- Sleeping -")
        self.resize(1920, 1080)

class UniversityWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)
    
        self.build_it()
    
    def build_it(self) :
        self.setWindowTitle("- University -")
        self.resize(1920, 1080)

class InteractiveImage(QLabel) :
    clicked = Signal()

    def __init__(self, image_path, x, y, w, h, parent= None) :
        super().__init__(parent)

        self.normal_geometry = (x, y, w, h)
        self.hover_geometry = (x - 5, y - 5, w + 10, h + 10)

        self.setPixmap(QPixmap(image_path))
        self.setScaledContents(True)
        self.setGeometry(x, y, w, h)
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event) :
        x, y, w, h = self.hover_geometry
        self.setGeometry(x, y, w, h)
        super().enterEvent(event)
    
    def leaveEvent(self, event) :
        x, y, w, h = self.normal_geometry
        self.setGeometry(x, y, w, h)
        super().leaveEvent(event)

    def mousePressEvent(self, event) :
        if event.button() == Qt.LeftButton :
            self.clicked.emit()
        super().mousePressEvent(event)
