from .simulator import Simulator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import config

app = FastAPI()

origins = [
    'https://davidunzue.com',
    config['client_url'],
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/kpis')
def run_simulation(number_of_requests: int = 10):
    # boundaries of Berlin
    bounding_box = (13.34014892578125, 52.52791908000258,
                    13.506317138671875, 52.562995039558004)
    result = Simulator(bounding_box).simulate(number_of_requests)

    return result
