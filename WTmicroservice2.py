from aiohttp import web

async def filter_data(request):
    json_data = await request.json()
    prezime_d = [d['username'] for d in json_data if 'username' in d and d['username'].lower().startswith('d')]
    return web.json_response(prezime_d, status=200)

app = web.Application()
app.router.add_post('/prezimed', filter_data)

if __name__ == '__main__':
    web.run_app(app, port=8083)
#radi