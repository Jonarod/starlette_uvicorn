from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import uvicorn

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'])

@app.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})

@app.route('/test', methods=['POST'])
async def post_test(request):
    b = await request.body()
    print(b)
    return JSONResponse({'status': 'ok'})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
