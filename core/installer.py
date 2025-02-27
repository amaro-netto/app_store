import subprocess
import os
import urllib.request
from PyQt5.QtCore import QThread, pyqtSignal


class InstallerThread(QThread):
    progress_signal = pyqtSignal(int)

    def __init__(self, app_name, installer_url):
        super().__init__()
        self.app_name = app_name
        self.installer_url = installer_url

    def run(self):
        # Caminho temporário para salvar o instalador
        download_dir = r"C:\Programas Baixados"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        installer_path = os.path.join(download_dir, f"{self.app_name}_installer.exe")
        
        try:
            # Baixar o instalador
            self.download_installer(installer_path)
            
            # Instalar silenciosamente
            self.install_app_silently(installer_path)
        except Exception as e:
            print(f"Erro ao instalar {self.app_name}: {e}")

    def download_installer(self, installer_path):
        try:
            print(f"Baixando {self.app_name} para {installer_path}...")
            urllib.request.urlretrieve(self.installer_url, installer_path)
            print(f"Instalador baixado para: {installer_path}")
        except Exception as e:
            print(f"Erro ao baixar o instalador para {self.app_name}: {e}")

    def install_app_silently(self, installer_path):
        try:
            print(f"Reiniciando {self.app_name} como administrador para instalação.")
            
            # Usar PowerShell para executar o instalador com privilégios administrativos
            subprocess.run(['powershell', '-Command', f'Start-Process "{installer_path}" -ArgumentList "/quiet" -Verb runAs'], check=True)
            print(f"{self.app_name} instalado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar o instalador para {self.app_name}: {e}")
