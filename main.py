import uvicorn
from v1.endpoints.endpoints import *


if __name__ == "__main__":
    uvicorn.run(
        'core:app', 
        host="localhost", 
        port=5000, 
        log_level="info", 
        reload=True
    )