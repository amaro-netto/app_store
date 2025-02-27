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

APP_DOWNLOAD_URLS = {
    "Adobe Acrobat Reader": "https://get.adobe.com/br/reader/",
    "Google Chrome": "https://www.google.com/chrome/",
    "Firefox": "https://www.mozilla.org/firefox/",
    "Opera": "https://net.geo.opera.com/opera/stable/windows?utm_source=PWNgames&utm_medium=pa&utm_campaign=PWN_BR_HVR_9571_WEB_2676&edition=std-2&utm_id=9ba0c822f9b84965b58b885406d693db&http_referrer=https%3A%2F%2Fwww.opera.com%2Fget%2Fopera-gx%3Futm_medium%3Dpa%26utm_campaign%3DPWN_BR_HVR_9571_WEB_2676%26utm_id%3D9ba0c822f9b84965b58b885406d693db%26utm_source%3DPWNgames%26edition%3Dstd-2&utm_site=opera_com&utm_lastpage=opera.com%2F&dl_token=33309433",
    "Safari": "https://www.apple.com/safari/",
    "WinRAR": "https://www.rarlab.com/download.htm",
    "Photoshop": "https://www.adobe.com/products/photoshop.html",
    "Illustrator": "https://www.adobe.com/products/illustrator.html",
    "Visual Studio Code": "https://code.visualstudio.com/",
    "WhatsApp": "https://www.whatsapp.com/download",
    "UltraViewer": "https://www.ultraviewer.net/",
    "AnyDesk": "https://anydesk.com/download",
    "Microsoft Office": "https://www.microsoft.com/pt-br/microsoft-365/get-started-with-office-2021",
    "PJE Office": "https://www.pje.jus.br/portalpje/download",
    "Java": "https://www.java.com/pt-BR/download/"
}
