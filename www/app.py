#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type="text/html")
    # ", content_type="text/html"" 这段网上找，没有下载而非打开

@asyncio.coroutine
def init(loop):
    app = web.Application() # loop=loop删掉，3.7写法
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app._make_handler(), '127.0.0.1', 9000) # make_handler前面加_，3.7写法
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()