import sys
from PySide6.QtWidgets import QApplication
import gui
import game

def main() :
    app = QApplication(sys.argv)
    player = game.Player()
    main_window = gui.MainWindow(player)
    main_window.show()
    app.exec()

if __name__ == "__main__" :
    main()