from PyQt5 import QtWidgets, QtGui, QtCore
from core.config import APPS, APP_ICONS, APP_DETAILS
from core.installer import install_app, get_installed_version, get_available_version, remove_app
import os

class AppStore(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loja de Aplicativos")
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QtGui.QIcon("assets/icon.png"))  # Ícone do programa
        self.initUI()
    
    def initUI(self):
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        
        # Logo no cabeçalho
        self.logo_label = QtWidgets.QLabel()
        self.logo_label.setPixmap(QtGui.QPixmap("assets/logo_header.png").scaled(150, 150, QtCore.Qt.KeepAspectRatio))
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.logo_label)
        
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setPlaceholderText("Buscar aplicativo...")
        self.search_bar.textChanged.connect(self.load_apps)
        layout.addWidget(self.search_bar)
        
        self.grid_layout = QtWidgets.QGridLayout()
        scroll_area = QtWidgets.QScrollArea()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setLayout(self.grid_layout)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.scroll_widget)
        layout.addWidget(scroll_area)
        
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        self.footer = QtWidgets.QLabel("\u00a9 2025 Minha Empresa - Todos os direitos reservados", self)
        self.footer.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.footer)
        
        self.load_apps()
    
    def load_apps(self):
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)
        
        search_text = self.search_bar.text().lower()
        row, col = 0, 0
        
        for app in APPS:
            if search_text and search_text not in app.lower():
                continue
            
            icon = self.get_icon_from_file(APP_ICONS.get(app, "assets/icons/default.png"))
            details = APP_DETAILS.get(app, {"description": "", "size": "", "category": ""})
            installed_version = get_installed_version(app)
            available_version = get_available_version(app)
            
            app_widget = QtWidgets.QWidget()
            app_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
            v_layout = QtWidgets.QVBoxLayout()
            
            app_icon = QtWidgets.QLabel()
            app_icon.setPixmap(icon.scaled(80, 80, QtCore.Qt.KeepAspectRatio))
            app_icon.setAlignment(QtCore.Qt.AlignCenter)
            v_layout.addWidget(app_icon)
            
            app_name = QtWidgets.QLabel(f"<b>{app.upper()}</b>")
            app_name.setAlignment(QtCore.Qt.AlignCenter)
            v_layout.addWidget(app_name)
            
            version_info = QtWidgets.QLabel(f"Instalada: {installed_version}\nDisponível: {available_version}")
            version_info.setAlignment(QtCore.Qt.AlignCenter)
            v_layout.addWidget(version_info)
            
            app_info = QtWidgets.QLabel(f"{details['category']} - {details['size']}\n{details['description']}")
            app_info.setAlignment(QtCore.Qt.AlignCenter)
            v_layout.addWidget(app_info)
            
            button = QtWidgets.QPushButton()
            button.setFixedWidth(200)
            if not installed_version:
                button.setText("Instalar")
                button.clicked.connect(lambda _, a=app: self.install_selected_app(a))
            elif installed_version and available_version and installed_version < available_version:
                button.setText("Atualizar")
                button.clicked.connect(lambda _, a=app: self.install_selected_app(a))
            else:
                button.setText("Remover")
                button.clicked.connect(lambda _, a=app: self.remove_selected_app(a))
            
            button.setStyleSheet(""
                "QPushButton { background-color: #0078D7; color: white; border-radius: 5px; padding: 5px; }"
                "QPushButton:hover { background-color: #005A9E; }"
            "")
            v_layout.addWidget(button, alignment=QtCore.Qt.AlignCenter)
            
            app_widget.setLayout(v_layout)
            self.grid_layout.addWidget(app_widget, row, col)
            
            col += 1
            if col > 2:
                col = 0
                row += 1
    
    def get_icon_from_file(self, path):
        return QtGui.QPixmap(path) if os.path.exists(path) else QtGui.QPixmap("assets/icons/default.png")
    
    def install_selected_app(self, app_name):
        self.progress_bar.setValue(0)
        QtCore.QTimer.singleShot(100, lambda: install_app(app_name, self.progress_bar))
    
    def remove_selected_app(self, app_name):
        self.progress_bar.setValue(0)
        QtCore.QTimer.singleShot(100, lambda: remove_app(app_name, self.progress_bar))
