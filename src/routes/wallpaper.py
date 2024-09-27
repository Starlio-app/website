from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import requests
from datetime import datetime

router = APIRouter()

template = Jinja2Templates(directory='./src/web/html')

def get_wallpaper(date: str):
    return requests.get('https://api.nasa.gov/planetary/apod', params={
        'api_key': '1gI9G84ZafKDEnrbydviGknReOGiVK9jqrQBE3et',
        'date': date,
    })

@router.get('/wallpaper/today', response_class=HTMLResponse)
async def today_wallpaper(requests: Request):
    date = datetime.today().strftime('%Y-%m-%d')
    res = get_wallpaper(date)

    if res.status_code != 200:
        return FileResponse('./src/web/html/error/404.html')

    return RedirectResponse(f'/wallpaper/{date}')


@router.get('/wallpaper/{day}', response_class=HTMLResponse)
async def wallpaper(request: Request, day):
    res = get_wallpaper(day)

    if res.status_code != 200:
        return FileResponse('./src/web/html/error/404.html')

    return template.TemplateResponse(
        request,
        '/wallpaper.html',
        {'info': res.json()}
    )