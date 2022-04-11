from ..routes import *
from core import app, settings as APPSETTING
from starlette.responses import RedirectResponse

@app.get(API_ROOT)
async def root_redirect_to_docs():
    return RedirectResponse(url=app.docs_url)

