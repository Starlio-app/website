from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi import FastAPI

from src.routes import index
from src.routes import wallpaper

app = FastAPI()

app.include_router(index.router)
app.include_router(wallpaper.router)

app.mount('/static/', StaticFiles(directory='./src/web/static/'))
app.mount('/.well-known/', StaticFiles(directory='./.well-known/'))


@app.route('/app-ads.txt')
async def app_ads(req):
    return FileResponse('./app-ads.txt')


@app.route('/robots.txt')
async def robots_txt(req):
    return FileResponse('./robots.txt')


@app.exception_handler(404)
async def not_found(req, __):
    return FileResponse('./src/web/html/error/404.html')
