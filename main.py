import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate, Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient
from datetime import date

class AgeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Magical Age Calculator")
        self.setFixedSize(600, 700)
        
        # Set gradient background
        gradient = QLinearGradient(0, 0, 0, 700)
        gradient.setColorAt(0.0, QColor(142, 68, 173))
        gradient.setColorAt(1.0, QColor(52, 152, 219))
        
        palette = self.palette()
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        
        # Title label with animation
        self.title = QLabel("✨ Magical Age Calculator ✨")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont('Arial', 24, QFont.Bold))
        self.title.setStyleSheet("color: white; padding: 20px;")
        layout.addWidget(self.title)
        
        # Instructions label
        instructions = QLabel("Select your birthdate:")
        instructions.setFont(QFont('Arial', 14))
        instructions.setStyleSheet("color: white;")
        instructions.setAlignment(Qt.AlignCenter)
        layout.addWidget(instructions)
        
        # Calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setStyleSheet("""
            QCalendarWidget QWidget {
                background-color: white;
                color: #333;
            }
            QCalendarWidget QToolButton {
                color: white;
                background-color: #8e44ad;
                border: none;
                border-radius: 5px;
            }
            QCalendarWidget QMenu {
                background-color: white;
            }
            QCalendarWidget QSpinBox {
                background-color: white;
                color: #333;
            }
        """)
        self.calendar.clicked.connect(self.calculate_age)
        layout.addWidget(self.calendar)
        
        # Result label
        self.result = QLabel("")
        self.result.setFont(QFont('Arial', 16))
        self.result.setStyleSheet("color: white; padding: 20px;")
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setWordWrap(True)
        layout.addWidget(self.result)
        
        # Setup animation
        self.animation = QPropertyAnimation(self.result, b"geometry")
        self.animation.setDuration(1000)
        
    def calculate_age(self):
        birth_date = self.calendar.selectedDate().toPyDate()
        today = date.today()
        
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day
        
        if days < 0:
            months -= 1
            days += 30
        
        if months < 0:
            years -= 1
            months += 12
            
        # Animate result
        self.result.setText(f"🎉 Your age is:\n{years} years, {months} months, and {days} days!")
        
        # Create bounce animation
        current_geometry = self.result.geometry()
        self.animation.setStartValue(QRect(current_geometry.x(), current_geometry.y() + 50,
                                         current_geometry.width(), current_geometry.height()))
        self.animation.setEndValue(current_geometry)
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = AgeCalculator()
    calculator.show()
    sys.exit(app.exec_())