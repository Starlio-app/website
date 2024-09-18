from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

router = APIRouter()


@router.get('/')
async def main():
    return FileResponse('./src/web/html/index.html')
