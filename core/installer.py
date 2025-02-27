# core/installer.py - Simulação de instalação, remoção e versões
from PyQt5.QtWidgets import QMessageBox

def get_installed_version(app_name):
    """Simula a obtenção da versão instalada de um aplicativo"""
    installed_versions = {
        "Google Chrome": "120.0.0",
        "Firefox": "115.2.1",
        "Visual Studio Code": "1.85.0",
        "Java": "8.0.321"
    }
    return installed_versions.get(app_name, "Não instalado")

def get_available_version(app_name):
    """Simula a obtenção da versão mais recente disponível"""
    available_versions = {
        "Google Chrome": "121.0.0",
        "Firefox": "116.3.2",
        "Visual Studio Code": "1.86.0",
        "Java": "8.0.350"
    }
    return available_versions.get(app_name, "Desconhecido")

def install_app(app_name, progress_bar, callback):
    """Simula a instalação do aplicativo com barra de progresso"""
    import time
    for i in range(0, 101, 20):
        time.sleep(0.5)  # Simula o tempo de instalação
        progress_bar.setValue(i)
    callback(app_name, "instalação")  # Chama o callback para exibir o popup

def remove_app(app_name, progress_bar, callback):
    """Simula a remoção do aplicativo com barra de progresso"""
    import time
    for i in range(100, -1, -20):
        time.sleep(0.5)  # Simula o tempo de remoção
        progress_bar.setValue(i)
    callback(app_name, "remoção")  # Chama o callback para exibir o popup

def update_app(app_name, progress_bar, callback):
    """Simula a atualização do aplicativo com barra de progresso"""
    import time
    for i in range(0, 101, 20):
        time.sleep(0.5)  # Simula o tempo de atualização
        progress_bar.setValue(i)
    callback(app_name, "atualização")  # Chama o callback para exibir o popup
