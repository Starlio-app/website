from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import requests
from datetime import datetime

router = APIRouter()

template = Jinja2Templates(directory='./src/web/html')


@router.get('/wallpaper/today', response_class=HTMLResponse)
async def today_wallpaper(request: Request):
    date = datetime.today().strftime('%Y-%m-%d')
    res = requests.get(f'https://api.starlio.space/last')

    if res.status_code != 200:
        return FileResponse('./src/web/html/error/404.html')

    return RedirectResponse(f'/wallpaper/{date}')


@router.get('/wallpaper/{day}', response_class=HTMLResponse)
async def wallpaper(request: Request, day):
    res = requests.get(f'https://api.starlio.space/wallpaper/{day}')

    if res.status_code != 200:
        return FileResponse('./src/web/html/error/404.html')

    return template.TemplateResponse(
        request,
        '/wallpaper.html',
        {'info': res.json()}
    )
