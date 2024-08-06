import uvicorn
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(
        'api:app',
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=False,
    )