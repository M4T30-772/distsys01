import json
import asyncio
import aiofiles
import aiohttp
import aiosqlite
from aiohttp import web

routes = web.RouteTableDef()

async def json_data(request):
    async with aiofiles.open('main.json', mode='r') as file:
        print("Opening JSON")
        read = [json.loads(line) async for line in file]
        data = [
            {
                'username': item['repo_name'].rsplit('/', 1)[0],
                'ghlink': f"https://github.com/{item['repo_name']}",
                'filename': item['path'].rsplit('/', 1)[-1]
            }
            for item in read
        ]
        async with aiosqlite.connect('mydb.db') as db:
            print("Connected.")
            await db.execute('CREATE TABLE IF NOT EXISTS mydb2 ('
                             'username TEXT, ghlink TEXT, filename TEXT)')
            print("Created.")
            await db.executemany('INSERT INTO mydb2 (username, ghlink, filename) '
                                 'VALUES (:username, :ghlink, :filename)', data)
            print("Data inserted into the table.")
            async with db.execute('SELECT * FROM mydb2 LIMIT 100') as cur:
                columns = [column[0] for column in cur.description]
                rows = await cur.fetchall()
                result = [dict(zip(columns, row)) for row in rows]
                print("Data fetched from the table:", result)

        async with aiohttp.ClientSession() as session:
            async with session.post('http://127.0.0.1:8080', json=result) as resp:
                assert resp.status == 200

        return web.json_response(result)

app = web.Application()
app.router.add_routes([web.get('/Json', json_data)])
web.run_app(app, port=8080)
#radi