from fastapi.responses import RedirectResponse
from api import app

@app.get('/')
async def root_redirect_to_docs():
    return RedirectResponse(url=app.docs_url)
