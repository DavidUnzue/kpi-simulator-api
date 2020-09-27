# KPI simulation API

## Installation

Due to issues with the installation of Geopandas' dependecies, it's adviced to install and use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for the package management instead of alternatives like `pip`. Also, make sure you have [geos](https://trac.osgeo.org/geos) installed in your system:

```bash
# for macOS with homebrew
brew install geos
```

Create a new virtual environmnet and install all project dependencies from the `requirements.txt` file:

```bash
conda create --name venv --file requirements.txt
```

Or if you don't have the needed conda channels, add the `conda-forge` channel first:

```bash
conda create -n venv
conda activate venv
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install --file requirements.txt
```

## Start the server

The project uses [Uvicorn](https://www.uvicorn.org/) as a ASGI server to run a [FastAPI](https://fastapi.tiangolo.com) app.

From the root directory, start the server like this:

```bash
uvicorn app.main:app
```

## Tests

To run the unit tests:

```bash
pytest
```
