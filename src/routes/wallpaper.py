from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

import requests

router = APIRouter()

template = Jinja2Templates(directory='./src/web/html')


@router.get('/wallpaper/{day}', response_class=HTMLResponse)
async def wallpaper(request: Request, day):
    res = requests.get('https://api.nasa.gov/planetary/apod', params={
        'api_key': '1gI9G84ZafKDEnrbydviGknReOGiVK9jqrQBE3et',
        'date': day,
    })

    if res.status_code != 200:
        return FileResponse('./src/web/html/error/404.html')

    return template.TemplateResponse(
        request,
        '/wallpaper.html',
        {'info': res.json()}
    )
