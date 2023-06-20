from aiohttp import web
import requests

routes = web.RouteTableDef()

@routes.post("/test")
async def filter_data(request):
    json_data = await request.json()
    dic = []
    for item in json_data:
        dic.append(item)
        
    result = dic
    print("result", result)
    
    url1 = 'http://127.0.0.1:8082/'  #d
    url2 = 'http://127.0.0.1:8083/'  #w
    requests.post(url1, json=result)
    requests.post(url2, json=result)
    
    return web.json_response(result, status=200)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8086)
#radi