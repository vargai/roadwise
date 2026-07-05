from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class CacheFriendlyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    port = 4174
    server = ThreadingHTTPServer(("127.0.0.1", port), CacheFriendlyHandler)
    try:
        print(f"Serving {root} at http://127.0.0.1:{port}/", flush=True)
    except RuntimeError:
        pass
    server.serve_forever()
