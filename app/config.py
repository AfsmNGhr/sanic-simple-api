from sanic import Sanic
from sanic_cors import CORS

app = Sanic(__name__)
CORS(app)