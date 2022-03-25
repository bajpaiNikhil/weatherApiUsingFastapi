import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    return {
        "about": "hi iamStupid"
    }


if __name__ == '__main__':
    uvicorn.run(api)
