# -*- coding: utf-8 -*-
"""
app.py — Giao diện web chạy trên máy để tách nền + tẩy/khôi phục thủ công.
Chạy:  python app.py      (tự mở trình duyệt tại http://127.0.0.1:8765)
Cần:   pip install pillow numpy scipy
"""
import io
import os
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from PIL import Image

from remove_bg import remove_bg

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = 8765


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        with open(os.path.join(HERE, "index.html"), "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        q = parse_qs(urlparse(self.path).query)
        g = lambda k, d: type(d)(q[k][0]) if k in q else d
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        try:
            img = Image.open(io.BytesIO(body))
            out = remove_bg(
                img, tol=g("tol", 14.0), band=g("band", 3), holes=q.get("holes", ["auto"])[0],
                shadow=q.get("shadow", ["0"])[0] == "1",
            )
            buf = io.BytesIO()
            out.save(buf, "PNG")
            data = buf.getvalue()
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
        except Exception as e:  # noqa
            data = str(e).encode("utf-8")
            self.send_response(500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://127.0.0.1:{PORT}"
    print("Mo", url, "(Ctrl+C de thoat)")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
