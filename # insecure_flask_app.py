# insecure_flask_app.py
#
# Intentionally INSECURE Flask configuration for demo purposes ONLY.
# Do NOT use this in real life.

from flask import Flask, request

app = Flask(__name__)

# ❌ Insecure configuration:
app.config["DEBUG"] = True                     # Debug mode enabled
app.config["SECRET_KEY"] = "super-weak-secret" # Hardcoded weak secret
app.config["SESSION_COOKIE_SECURE"] = False    # Cookies not marked as secure
app.config["SESSION_COOKIE_HTTPONLY"] = False  # Cookies accessible to JS


@app.route("/echo", methods=["GET"])
def echo():
    # Not the main point of the demo, just a simple endpoint
    msg = request.args.get("msg", "hello")
    return f"You said: {msg}"


if __name__ == "__main__":
    # ❌ More insecure config: debug + 0.0.0.0 (open on all interfaces)
    app.run(host="0.0.0.0", port=5000, debug=True)
