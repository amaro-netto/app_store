# ui/main_window.py - Interface principal
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from core.config import APPS, APP_ICONS, APP_DETAILS
from core.installer import install_app, get_installed_version, get_available_version, remove_app, update_app
import os
import random

class AppStore(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loja de Aplicativos")
        self.setGeometry(100, 100, 900, 600)
        self.initUI()
    
    def initUI(self):
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        
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
        
        # Lista de cores de fundo para os cards
        colors = ["#f0f0f0", "#e1f5fe", "#e8f5e9", "#fff3e0", "#fce4ec"]
        
        for app in APPS:
            if search_text and search_text not in app.lower():
                continue
            
            icon = self.get_icon_from_file(APP_ICONS.get(app, "assets/icons/default.png"))
            details = APP_DETAILS.get(app, {"description": "", "size": "", "category": ""})
            installed_version = get_installed_version(app)
            available_version = get_available_version(app)
            
            # Criando o card do aplicativo com largura ajustada para 300px
            app_widget = QtWidgets.QWidget()
            app_widget.setStyleSheet(f"""
                background-color: {random.choice(colors)}; 
                border-radius: 10px; padding: 10px; margin: 10px; border: 1px solid #ddd;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  # Sombra suave no card
            """)
            app_widget.setFixedWidth(300)  # Largura ajustada para 300px
            v_layout = QtWidgets.QVBoxLayout()
            
            # Ícone sem borda
            app_icon = QtWidgets.QLabel()
            app_icon.setPixmap(icon.scaled(100, 100, QtCore.Qt.KeepAspectRatio))
            app_icon.setAlignment(QtCore.Qt.AlignCenter)
            app_icon.setStyleSheet("border: none;")  # Removendo a borda do ícone
            v_layout.addWidget(app_icon)
            
            # Nome do app em negrito e caixa alta sem borda
            app_name = QtWidgets.QLabel(f"{app}")
            app_name.setAlignment(QtCore.Qt.AlignCenter)
            app_name.setStyleSheet("font-weight: bold; text-transform: uppercase; font-size: 16px; border: none;")
            v_layout.addWidget(app_name)
            
            # Versão do app em colunas separadas, uma em cima da outra
            version_layout = QtWidgets.QVBoxLayout()  # Layout vertical para as versões
            
            version_info_installed = QtWidgets.QLabel(f"Instalada: {installed_version}")
            version_info_installed.setAlignment(QtCore.Qt.AlignCenter)
            version_layout.addWidget(version_info_installed)
            
            version_info_available = QtWidgets.QLabel(f"Disponível: {available_version}")
            version_info_available.setAlignment(QtCore.Qt.AlignCenter)
            version_layout.addWidget(version_info_available)
            
            v_layout.addLayout(version_layout)  # Adiciona o layout de versões no card
            
            app_info = QtWidgets.QLabel(f"{details['category']} - {details['size']}\n{details['description']}")
            app_info.setAlignment(QtCore.Qt.AlignCenter)
            app_info.setWordWrap(True)  # Permite quebra de linha na descrição
            app_info.setStyleSheet("border: none;")  # Removendo a borda da descrição
            v_layout.addWidget(app_info)
            
            # Botões de instalação, atualização ou remoção
            button = QtWidgets.QPushButton()
            
            # Lógica para exibir o botão correto
            if not installed_version:
                button.setText("Instalar")
                button.setStyleSheet("""
                    background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px 20px;
                    border: none; min-width: 200px;  # Largura do botão ajustada para 200px
                """)
                button.clicked.connect(lambda _, a=app: self.install_selected_app(a))
            elif installed_version and available_version and installed_version < available_version:
                button.setText("Atualizar")
                button.setStyleSheet("""
                    background-color: #2196F3; color: white; border-radius: 5px; padding: 10px 20px;
                    border: none; min-width: 200px;  # Largura do botão ajustada para 200px
                """)
                button.clicked.connect(lambda _, a=app: self.update_selected_app(a))
            else:
                button.setText("Remover")
                button.setStyleSheet("""
                    background-color: #f44336; color: white; border-radius: 5px; padding: 10px 20px;
                    border: none; min-width: 200px;  # Largura do botão ajustada para 200px
                """)
                button.clicked.connect(lambda _, a=app: self.remove_selected_app(a))
            
            # Efeito hover: ao passar o mouse, o botão clareia
            button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50; color: white; border-radius: 5px; padding: 10px 20px; border: none; min-width: 200px;
                }
                QPushButton:hover {
                    background-color: #45a049;  # Clareia o botão quando o mouse passa por cima
                }
            """)
            v_layout.addWidget(button)
            
            app_widget.setLayout(v_layout)
            
            # Adicionando o widget do aplicativo à grid
            self.grid_layout.addWidget(app_widget, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1
    
    def get_icon_from_file(self, path):
        return QtGui.QPixmap(path) if os.path.exists(path) else QtGui.QPixmap("assets/icons/default.png")
    
    def install_selected_app(self, app_name):
        self.progress_bar.setValue(0)
        QtCore.QTimer.singleShot(100, lambda: install_app(app_name, self.progress_bar, self.show_popup))
    
    def remove_selected_app(self, app_name):
        self.progress_bar.setValue(0)
        QtCore.QTimer.singleShot(100, lambda: remove_app(app_name, self.progress_bar, self.show_popup))
    
    def update_selected_app(self, app_name):
        self.progress_bar.setValue(0)
        QtCore.QTimer.singleShot(100, lambda: update_app(app_name, self.progress_bar, self.show_popup))
    
    def show_popup(self, app_name, action_type):
        """Exibe um popup informando o sucesso da instalação, remoção ou atualização"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"{app_name} foi {action_type} com sucesso!")
        msg.setWindowTitle(f"{action_type.capitalize()} Concluída")
        msg.exec_()
