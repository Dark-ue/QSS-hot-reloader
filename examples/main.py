import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.hot_reload import reload_qss

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS Hot Reloader Example")
        self.setGeometry(100, 100, 400, 300)

        label = QLabel("Hello, QSS Hot Reloader!", self)
        label.setGeometry(50, 50, 300, 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Path to the QSS file(s) to monitor
    qss_files = [r"c:/Users/preet/Desktop/Website/python/QSS-hot-reloader/examples/main.qss"]

    # Enable QSS hot reloading
    reload_qss(window, qss_files)

    # Start the application event loop
    sys.exit(app.exec())