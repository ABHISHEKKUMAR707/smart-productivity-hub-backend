"""
TODO:
- Create FastAPI app instance
- Add app metadata (title, version, description)
- Add health check endpoint
- Later: include routers
"""
from fastapi import FastAPI

app= FastAPI(
    title = "smart-productivity-hub",
      version= "0.128.0",
        description = "backend-api-forTask"
        )

@app.get("/health")
def health():
    return {"health" : "healthy"} 

@app.get("/")
def devRoot():
    return {"status": "ok", "message":"fastapi is running"}
 
