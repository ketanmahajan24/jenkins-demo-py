 
from datetime import datetime
import socket
import os

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Deployment Success</title>
    <style>
        body {{
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #4f46e5, #9333ea);
        }}
        .card {{
            background: white;
            padding: 40px;
            width: 420px;
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.25);
            text-align: center;
        }}
        h1 {{
            margin-top: 0;
            color: #111827;
        }}
        .status {{
            margin: 20px 0;
            padding: 12px;
            background: #dcfce7;
            color: #166534;
            border-radius: 999px;
            font-weight: bold;
        }}
        .info {{
            text-align: left;
            margin-top: 20px;
            font-size: 14px;
        }}
        .info div {{
            margin-bottom: 8px;
        }}
        footer {{
            margin-top: 30px;
            font-size: 12px;
            color: #6b7280;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Deployment Successful</h1>
        <div class="status">Application Deployed</div>

        <div class="info">
            <div><strong>Host:</strong> {socket.gethostname()}</div>
            <div><strong>Time:</strong> {datetime.now()}</div>
            <div><strong>Status:</strong> OK</div>
        </div>

        <footer>
            GitHub • Jenkins • Python
        </footer>
    </div>
</body>
</html>
"""

with open("deploy.html", "w") as f:
    f.write(html)

print("Deployment successful!")
print("Generated deploy.html")
print("Open the file in a browser to view the GUI.")
