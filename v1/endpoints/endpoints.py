from . import app

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}