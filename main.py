from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="DevOps Dashboard")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Pipeline Live</title>
        <style>
            body { font-family: Arial, sans-serif; background: #0f172a; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; width: 350px; border: 1px solid #334155; }
            h1 { color: #38bdf8; font-size: 24px; margin-bottom: 10px; }
            .badge { background: #22c55e; color: black; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 14px; display: inline-block; margin-bottom: 20px; }
            p { color: #94a3b8; font-size: 14px; line-height: 1.6; }
            .btn { display: inline-block; margin-top: 15px; padding: 10px 20px; background: #0284c7; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; }
            .btn:hover { background: #0369a1; }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">🚀 CI/CD Pipeline Active</div>
            <h1>DevOps Automation</h1>
            <p>FastAPI app integrated with <strong>GitHub Actions</strong> & <strong>Render Docker Engine</strong>.</p>
            <a href="/docs" class="btn">View Swagger API Docs</a>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "2.0.0"}