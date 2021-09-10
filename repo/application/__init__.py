import os
from .server import app


def run_app(host="0.0.0.0", port=5000, debug=False):
    app.run(host=host, port=port, debug=debug, use_reloader=True)
