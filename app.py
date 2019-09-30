import os
import sys
import logging
from time import time
from sanic.response import text
from app.config import app

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

DEBUG = os.environ.get('DEBUG')


@app.middleware('request')
async def add_start_time(request):
    request['start_time'] = time()


@app.middleware('response')
async def add_spent_time(request, response):
    spend_time = round((time() - request['start_time']) * 1000)
    if request.method == 'POST':
        logger.info(
            '%s %s %s %s %s %s',
            response.status, request.method,
            request.path, request.query_string,
            request.json, spend_time
        )


@app.route('/', methods=['GET', 'OPTIONS'])
async def index(request):
    if request.method == 'OPTIONS':
        return text('', 204)
    return text('Hello World!', 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)
