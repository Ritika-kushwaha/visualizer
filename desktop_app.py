import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                             QLineEdit, QLabel, QFileDialog, QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DesktopVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.token = None
        self.username = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ChemVisualizer Desktop')
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #f3f4f6;") # Light Gray background

        self.main_layout = QVBoxLayout()
        self.show_login_screen()
        self.setLayout(self.main_layout)

    def show_login_screen(self):
        self.clear_layout()
        
        # Purple Wavy Style Header
        self.header = QLabel("Hello!\nSign in to Desktop")
        self.header.setStyleSheet("font-size: 24px; font-weight: bold; color: #4f46e5; margin: 20px;")
        self.header.setAlignment(Qt.AlignCenter)
        
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Username")
        self.user_input.setStyleSheet("padding: 10px; border-radius: 15px; background: white;")
        
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Password")
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.setStyleSheet("padding: 10px; border-radius: 15px; background: white;")
        
        self.login_btn = QPushButton("SIGN IN")
        self.login_btn.setStyleSheet("background-color: #7c3aed; color: white; padding: 10px; border-radius: 15px; font-weight: bold;")
        self.login_btn.clicked.connect(self.handle_login)

        self.main_layout.addWidget(self.header)
        self.main_layout.addWidget(self.user_input)
        self.main_layout.addWidget(self.pass_input)
        self.main_layout.addWidget(self.login_btn)

    def handle_login(self):
        user = self.user_input.text()
        pw = self.pass_input.text()
        try:
            # Talking to the Django Kitchen
            response = requests.post('http://127.0.0.1:8000/api/login/', data={'username': user, 'password': pw})
            if response.status_code == 200:
                self.token = response.json()['access']
                self.username = user
                self.show_dashboard()
            else:
                self.header.setText("Wrong Credentials!")
        except:
            self.header.setText("Server Offline!")

    def show_dashboard(self):
        self.clear_layout()
        
        # Navbar style
        nav = QHBoxLayout()
        user_lbl = QLabel(f"👤 {self.username}")
        user_lbl.setStyleSheet("font-weight: bold; color: #7c3aed;")
        nav.addWidget(QLabel("ChemVisualizer Dashboard"))
        nav.addStretch()
        nav.addWidget(user_lbl)
        
        # Upload Button
        self.up_btn = QPushButton("Upload CSV")
        self.up_btn.clicked.connect(self.upload_file)
        self.up_btn.setStyleSheet("background-color: #4f46e5; color: white; padding: 10px; border-radius: 10px;")

        # Chart Area
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ax = self.canvas.figure.add_subplot(111)

        self.main_layout.addLayout(nav)
        self.main_layout.addWidget(self.up_btn)
        self.main_layout.addWidget(self.canvas)

    def upload_file(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "CSV files (*.csv)")
        if fname:
            files = {'file': open(fname, 'rb')}
            headers = {'Authorization': f'Bearer {self.token}'}
            res = requests.post('http://127.0.0.1:8000/api/upload/', files=files, headers=headers)
            if res.status_code == 200:
                data = res.json()
                self.update_chart(data['avg_temp'], data['avg_pressure'])

    def update_chart(self, temp, press):
        self.ax.clear()
        self.ax.bar(['Temp', 'Pressure'], [temp, press], color=['orange', 'blue'])
        self.ax.set_title("Chemical Parameters")
        self.canvas.draw()

    def clear_layout(self):
        for i in reversed(range(self.main_layout.count())): 
            self.main_layout.itemAt(i).widget().setParent(None)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DesktopVisualizer()
    ex.show()
    sys.exit(app.exec_())