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

        self.game_timer = QTimer(self)
        self.game_timer.timeout.connect(self.game_tick)
        self.game_timer.start(500)
    
    def charge_window(self, window_class) :
        new_window = window_class(self, self.player)
        self.setCentralWidget(new_window)

    def game_tick(self):
        self.player.charge_hunger(0.01)
        self.player.charge_thirst(0.01)

        if (
        self.player.hunger >= self.player.max_hunger
        or self.player.thirst >= self.player.max_thirst
        ):
            self.player.charge_health(-0.5)
        else:
            self.player.charge_health(0.5)

        current_window = self.centralWidget()

        if hasattr(current_window, "update_status_hud"):
            current_window.update_status_hud()

        if hasattr(current_window, "health_fill"):
            current_window.update_status_bar(
            current_window.health_fill,
            self.player.health,
            self.player.max_health,
            current_window.health_bar_max_width
        )

        if hasattr(current_window, "thirst_fill"):
            current_window.update_status_bar(
            current_window.thirst_fill,
            self.player.thirst,
            self.player.max_thirst,
            current_window.thirst_bar_max_width
        )

        if hasattr(current_window, "hunger_fill"):
            current_window.update_status_bar(
            current_window.hunger_fill,
            self.player.hunger,
            self.player.max_hunger,
            current_window.hunger_bar_max_width
        )

class Window(QWidget) :
    def __init__(self, main_window, player) :
        super().__init__(main_window)

        self.player = player
        self.main_window = main_window

    def build_hud_progress_bar(self) :
        
        self.health_bar_max_width = 250
        self.thirst_bar_max_width = 250
        self.hunger_bar_max_width = 250
        self.sleep_bar_max_width = 250
        self.health_fill = QLabel(self)
        self.health_fill.setPixmap(QPixmap("assets/MainGameWindow/ProgressStatusBarHealth.png"))
        self.health_fill.setScaledContents(True)
        self.health_fill.setGeometry(0, 2, self.health_bar_max_width, 45)
        self.update_status_bar(
            self.health_fill,
            self.player.health,
            self.player.max_health,
            self.health_bar_max_width
        )
        self.thirst_fill = QLabel(self)
        self.thirst_fill.setPixmap(QPixmap("assets/MainGameWindow/ProgressStatusBar.png"))
        self.thirst_fill.setScaledContents(True)
        self.thirst_fill.setGeometry(0, 45, self.thirst_bar_max_width, 45)
        self.update_status_bar(
            self.thirst_fill,
            self.player.thirst,
            self.player.max_thirst,
            self.thirst_bar_max_width
        )
        self.hunger_fill = QLabel(self)
        self.hunger_fill.setPixmap(QPixmap("assets/MainGameWindow/ProgressStatusBar.png"))
        self.hunger_fill.setScaledContents(True)
        self.hunger_fill.setGeometry(0, 88, self.hunger_bar_max_width, 45)
        self.update_status_bar(
            self.hunger_fill,
            self.player.hunger,
            self.player.max_hunger,
            self.hunger_bar_max_width
        )

    def build_hud_status_player(self) :
        font = QFont()
        font.setPointSize(22)
        self.label_health = QLabel("HEALTH", self)
        self.label_health.setStyleSheet("color: white;")
        self.label_health.setFont(font)
        self.label_health.setGeometry(70, 7, 220, 40)
        self.label_thirst = QLabel("THIRST", self)
        self.label_thirst.setStyleSheet("color: white;")
        self.label_thirst.setFont(font)
        self.label_thirst.setGeometry(70, 49, 220, 40)
        self.label_hunger = QLabel("HUNGER", self) 
        self.label_hunger.setStyleSheet("color: white;")
        self.label_hunger.setFont(font)
        self.label_hunger.setGeometry(60, 92, 220, 40)
        self.label_dev_skill = QLabel("Dev Skill: " + str(self.player.dev_skill), self)
        self.label_dev_skill.setStyleSheet("color: white;")
        self.label_dev_skill.setFont(font)
        self.label_dev_skill.setGeometry(40, 130, 300, 40)
        self.label_money = QLabel("Money: $" + str(self.player.money), self)
        self.label_money.setStyleSheet("color: white;")
        self.label_money.setFont(font)
        self.label_money.setGeometry(40, 160, 350, 40)
        self.label_sleep = QLabel("Hours Left: " + str(self.player.sleep), self)
        self.label_sleep.setStyleSheet("color: white;")
        self.label_sleep.setFont(font)
        self.label_sleep.setGeometry(40, 190, 350, 40)
    
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
        self.label_sleep.setText("Hours Left: " + str(self.player.sleep))

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
        self.base_background = QLabel(self)
        self.base_background.setPixmap(QPixmap("assets/MainGameWindow/BaseBackgroundMain.png"))
        self.base_background.setScaledContents(True)
        self.base_background.setGeometry(0, 0, 1920, 1080)
        self.build_hud_progress_bar()
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/MainGameWindow/BackgroundMainGame.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 1920, 1080)
        self.base_background.lower()
        self.health_fill.raise_()
        self.thirst_fill.raise_()
        self.hunger_fill.raise_()
        self.background.raise_()
        self.blackbase = QLabel(self)
        self.blackbase.setPixmap(QPixmap("assets/MainGameWindow/BlackBase.png"))
        self.blackbase.setScaledContents(True)
        self.blackbase.setGeometry(1460,393,350,400)
        self.bookCase = InteractiveImage(
            "assets/MainGameWindow/BookcaseMainGame.png",
            20, 260, 300, 600,
            self
        )
        self.computer = InteractiveImage(
            "assets/MainGameWindow/ComputerMainGame.png",
            460, 405, 450, 500,
            self
        )
        self.beg = InteractiveImage(
            "assets/MainGameWindow/BegMainGame.png",
            200, 650, 300, 290,
            self
        )
        self.door = InteractiveImage(
            "assets/MainGameWindow/DoorMainGame.png",
            1430, 155, 410, 650,
            self
        )
        self.bed = InteractiveImage(
            "assets/MainGameWindow/BedMainGame.png",
            940, 460, 550, 600,
            self
        )
        self.build_hud_status_player()
        self.bookCase.clicked.connect(lambda : self.main_window.charge_window(StudyWindow))
        self.beg.clicked.connect(lambda : self.main_window.charge_window(FeedingWindow))
        self.computer.clicked.connect(lambda : self.main_window.charge_window(WorkWindow))
        self.bed.clicked.connect(lambda : self.main_window.charge_window(SleepingWindow))
        self.door.clicked.connect(lambda : self.main_window.charge_window(UniversityWindow))

class StudyWindow(Window) :
    def __init__(self, main_window, player) :
        super().__init__(main_window, player)
    
        self.build_it()
    
    def build_it(self) :
        self.setWindowTitle("- Study -")
        self.resize(1920, 1080)
        self.base_background = QLabel(self)
        self.base_background.setPixmap(QPixmap("assets/MainGameWindow/BaseBackgroundMain.png"))
        self.base_background.setScaledContents(True)
        self.base_background.setGeometry(0, 0, 1920, 1080)
        self.build_hud_progress_bar()
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/StudyWindow/BackgroundStudy.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 1920, 1080)
        self.build_hud_status_player()
        self.book_study = InteractiveImage(
            "assets/StudyWindow/BookStudy.png",
            480, 120, 1000, 700,
            self
        )
        font = QFont()
        font.setPointSize(22)
        self.label_study = QLabel("Click on the book to study.", self)
        self.label_study.setStyleSheet("color: white;")
        self.label_study.setFont(font)
        self.label_study.setGeometry(800, 800, 450, 40)
        font2 = QFont()
        font2.setPointSize(18)
        self.label_study2 = QLabel("Each click equals +1 dev skill", self)
        self.label_study2.setStyleSheet("color: white;")
        self.label_study2.setFont(font2)
        self.label_study2.setGeometry(815, 840, 450, 40)

        self.book_study.clicked.connect(self.study_action)

        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(1700,985,200,50)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("""
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
        self.back_button.clicked.connect(lambda : self.main_window.charge_window(MainGameWindow))

    def study_action(self):
        if self.player.sleep >= 3:
            self.player.charge_dev_skill(1)
            self.player.charge_sleep(-3)

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
