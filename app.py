# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import json
from sanic.exceptions import ServerError

from datetime import datetime, timedelta
import jwt
import config

app = Sanic(__name__)
app.config.from_object(config)

@app.route('/')
async def test(request):
	payload = {
		'hello': 'Lamborghini',
		'philip': 'kevin',
		'config': app.config
	}
	return json(payload)


@app.route('/auth/jwt')
async def auth_jwt(request):
	payload = {
		'auth': 'jwt'
	}
	return json(payload)


@app.route('/auth/register', methods=['POST'])
async def auth_register(request):
	if 'id' not in request.json or len(request.json['id']) == 0:
		raise ServerError('Bad request', status_code=400)
	if 'password' not in request.json or len(request.json['password']) == 0:
    		raise ServerError('Bad request', status_code=400)
	payload = {
		'data': request.json
	}
	return json(payload)


@app.route('/auth/login', methods=['PUT'])
async def auth_login(request):
	if 'id' not in request.json or len(request.json['id']) == 0:
		raise ServerError('Bad request', status_code=400)
	if 'password' not in request.json or len(request.json['password']) == 0:
    		raise ServerError('Bad request', status_code=400)
	now = datetime.utcnow()
	payload = dict(
		exp=now+timedelta(days=7),
		iat=now,
		id=request.json['id'],
		password=request.json['password']
	)
	access_token = jwt.encode(payload, app.config.AUTH_TOKEN).decode('utf-8')
	return json({
		'data': {
			'access_token': access_token
		}
	})


if __name__ == '__main__':
	app.run(host=app.config.APP_HOSTNAME, port=app.config.APP_PORT, debug=app.config.DEBUG, auto_reload=app.config.AUTO_RELOAD)
