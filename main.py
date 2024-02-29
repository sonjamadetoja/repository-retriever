from uvicorn import run
from app import app as fastapi_app


def main():

    def start_fastapi_app():
        run(fastapi_app, host="127.0.0.1", port=8000)

    start_fastapi_app()

if __name__ == "__main__":
    main()
