import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont

from ui.main_window.main_window import MainWindow
from ui.styles.theme import apply_theme

def main():
    app = QApplication(sys.argv)
    
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI",15))

    window = MainWindow()
    apply_theme(window, "dark")       # DARK = DEFAULT
    window.showMaximized()           # START MAXIMIZED

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
