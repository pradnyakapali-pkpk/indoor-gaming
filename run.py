"""Start the Indoor Gaming Arena server:   python run.py   ->  http://localhost:3000"""
import os

from arena import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    if os.getenv("FLASK_DEBUG") == "1":
        app.run(host="0.0.0.0", port=port, debug=True)
    else:
        from waitress import serve
        print(f"Indoor Gaming Arena running on http://localhost:{port}")
        serve(app, host="0.0.0.0", port=port)
