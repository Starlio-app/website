from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import requests
from datetime import datetime
from http import HTTPStatus

router = APIRouter()

template = Jinja2Templates(directory='./src/web/html')


@router.get('/wallpaper/today', response_class=HTMLResponse)
async def today_wallpaper(request: Request):
    date = datetime.today().strftime('%Y-%m-%d')
    res = requests.get(f'https://api.starlio.space/last')

    if not HTTPStatus(res.status_code).is_redirection or \
    not HTTPStatus(res.status_code).is_success:

        return FileResponse('./src/web/html/error/404.html')

    return RedirectResponse(f'/wallpaper/{date}')


@router.get('/wallpaper/{day}', response_class=HTMLResponse)
async def wallpaper(request: Request, day):
    res = requests.get(f'https://api.starlio.space/wallpaper/{day}')

    if not HTTPStatus(res.status_code).is_redirection or \
    not HTTPStatus(res.status_code).is_success:
        return FileResponse('./src/web/html/error/404.html')

    return template.TemplateResponse(
        request,
        '/wallpaper.html',
        {'info': res.json()}
    )
