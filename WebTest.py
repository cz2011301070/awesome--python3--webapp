'''
# main.py
from aiohttp import web


async def index(request):
    return web.json_response(text='hello')


app = web.Application()
app.add_routes([web.get('/', index)])
web.run_app(app)
'''

import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):# web content
	return web.json_response(text='hello')#, headers = {"content-type": "text/html"}


async def init(loop):
	app = web.Application()
	app.add_routes([web.get("/", index)])
	srv = await loop.create_server(web.AppRunner(app), "127.0.0.1", 9090)
	logging.info("the server started at http://127.0.0.1:9090....")
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
