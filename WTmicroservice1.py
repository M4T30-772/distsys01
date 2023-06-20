from aiohttp import web

async def filter_data(request):
    json_data = await request.json()
    prezime_w = [w['username'] for w in json_data if 'username' in w and w['username'].lower().startswith('w')]
    return web.json_response(prezime_w, status=200)

app = web.Application()
app.router.add_post('/prezimew', filter_data)

if __name__ == '__main__':
    web.run_app(app, port=8082)
#radi