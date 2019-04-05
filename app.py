# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import json


app = Sanic()


@app.route('/')
async def test(request):
	payload = {
		'hello': 'Lamborghini',
		'philip': 'kevin'
	}
	return json(payload)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

