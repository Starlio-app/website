from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import requests

router = APIRouter()

template = Jinja2Templates(directory='./src/web/html')

@router.get('/wallpaper/{day}', response_class=HTMLResponse)
async def wallpaper(request: Request, day):
    token = '1gI9G84ZafKDEnrbydviGknReOGiVK9jqrQBE3et'
    res = requests.get('https://api.nasa.gov/planetary/apod', params={
        'api_key': '1gI9G84ZafKDEnrbydviGknReOGiVK9jqrQBE3et',
        'date': day,
    })

    return template.TemplateResponse(
        request,
        '/wallpaper.html',
        {'info': res.json()}
    )