from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
    <body style="background:#0f172a;color:white;text-align:center;font-family:sans-serif;padding:20px;">
    <h1>Hello, I'm a Developer from Khanpur! 🚀</h1>
    <p>Meri pehli LIVE Website!</p>
    <div style="background:white;color:black;padding:20px;border-radius:15px;max-width:320px;margin:20px auto;">
    <h3>Contact Me</h3>
    <button onclick="alert('Khanpur LIVE! ✅')" style="background:#3b82f6;color:white;border:none;padding:10px 20px;border-radius:8px;">Click Karo</button>
    </div></body></html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
  
