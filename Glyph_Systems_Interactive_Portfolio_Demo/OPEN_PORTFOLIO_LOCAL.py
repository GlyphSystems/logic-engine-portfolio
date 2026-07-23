from __future__ import annotations
import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = 8765

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as server:
    threading.Timer(1.0, lambda: webbrowser.open(f"http://127.0.0.1:{PORT}/index.html")).start()
    print("Glyph Systems portfolio is running.")
    print(f"Open: http://127.0.0.1:{PORT}/index.html")
    print("Keep this window open while viewing. Press Ctrl+C to stop.")
    server.serve_forever()
