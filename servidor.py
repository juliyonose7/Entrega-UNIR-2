"""
Servidor HTTP local con soporte CORS y apertura automática del navegador.
Laboratorio: Tecnologías JavaScript y AJAX
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PUERTO = 8000
DIRECTORIO = os.path.dirname(os.path.abspath(__file__))

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORIO, **kwargs)

    def end_headers(self):
        # Habilitar CORS para permitir peticiones AJAX locales
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "OK")
        self.end_headers()

def iniciar():
    os.chdir(DIRECTORIO)
    handler = CORSHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PUERTO), handler) as httpd:
        url = f"http://localhost:{PUERTO}/index.html"
        print("=" * 65)
        print(" LABORATORIO: TECNOLOGÍAS JAVASCRIPT Y AJAX (REACT + CSS)")
        print("=" * 65)
        print(f" Servidor iniciado en: {url}")
        print(f" Directorio raíz:     {DIRECTORIO}")
        print(" Presiona CTRL+C para detener el servidor.")
        print("=" * 65)
        
        try:
            webbrowser.open(url)
        except Exception:
            pass

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido por el usuario.")
            httpd.server_close()

if __name__ == "__main__":
    iniciar()

