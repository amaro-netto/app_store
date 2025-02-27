# core/config.py - Configuração
APPS = [
    "Adobe Acrobat Reader", "Google Chrome", "Firefox", "Opera", "Safari", 
    "WinRAR", "Photoshop", "Illustrator", "Visual Studio Code", "WhatsApp", 
    "UltraViewer", "AnyDesk", "Microsoft Office", "PJE Office", "Java"
]

APP_ICONS = {
    "Adobe Acrobat Reader": "assets/icons/acrobat.png",
    "Google Chrome": "assets/icons/chrome.png",
    "Firefox": "assets/icons/firefox.png",
    "Opera": "assets/icons/opera.png",
    "Safari": "assets/icons/safari.png",
    "WinRAR": "assets/icons/winrar.png",
    "Photoshop": "assets/icons/photoshop.png",
    "Illustrator": "assets/icons/illustrator.png",
    "Visual Studio Code": "assets/icons/vscode.png",
    "WhatsApp": "assets/icons/whatsapp.png",
    "UltraViewer": "assets/icons/ultraviewer.png",
    "AnyDesk": "assets/icons/anydesk.png",
    "Microsoft Office": "assets/icons/office.png",
    "PJE Office": "assets/icons/pjeoffice.png",
    "Java": "assets/icons/java.png"
}

APP_DETAILS = {
    "Adobe Acrobat Reader": {"description": "Leitor de arquivos PDF", "size": "250MB", "category": "Produtividade"},
    "Google Chrome": {"description": "Navegador rápido e seguro", "size": "100MB", "category": "Navegador"},
    "Firefox": {"description": "Navegador da Mozilla", "size": "120MB", "category": "Navegador"},
    "Opera": {"description": "Navegador com VPN integrada", "size": "110MB", "category": "Navegador"},
    "Safari": {"description": "Navegador da Apple", "size": "90MB", "category": "Navegador"},
    "WinRAR": {"description": "Compactador de arquivos", "size": "5MB", "category": "Utilitário"},
    "Photoshop": {"description": "Edição de imagens avançada", "size": "1.5GB", "category": "Design"},
    "Illustrator": {"description": "Design vetorial profissional", "size": "2GB", "category": "Design"},
    "Visual Studio Code": {"description": "Editor de código leve", "size": "200MB", "category": "Desenvolvimento"},
    "WhatsApp": {"description": "Mensageiro instantâneo", "size": "80MB", "category": "Comunicação"},
    "UltraViewer": {"description": "Acesso remoto fácil", "size": "50MB", "category": "Utilitário"},
    "AnyDesk": {"description": "Acesso remoto rápido", "size": "60MB", "category": "Utilitário"},
    "Microsoft Office": {"description": "Pacote de produtividade", "size": "4GB", "category": "Produtividade"},
    "PJE Office": {"description": "Software para acesso ao PJe", "size": "200MB", "category": "Utilitário"},
    "Java": {"description": "Ambiente de execução para aplicativos", "size": "150MB", "category": "Desenvolvimento"}
}
