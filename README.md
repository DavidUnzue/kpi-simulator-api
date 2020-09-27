# KPI simulation API

## TL;DR

Try the deployed API on Heroku:

[https://kpi-simulator-api.herokuapp.com/kpis](https://kpi-simulator-api.herokuapp.com/kpis)

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

The app will run now under `http://localhost:8000`.

## API Endpoints

See the Swagger docs under: `http://localhost:8000/docs`.

**/kpis**

Returns simulation results.

Try it:

```bash
curl --request GET 'http://localhost:8000/kpis'
```

Response:

```json
{
  "booking_distance_bins": {
    "From 0->1km": 2,
    "From 1->2km": 1,
    "From 2->3km": 3,
    "From 3->4km": 4
  },
  "most_popular_dropoff_points": "{\"type\": \"FeatureCollection\", \"features\": [{\"id\": \"101\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dbjhg4dr9\", \"name\": \"S+U Wedding (Berlin)\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.366015515190512, 52.54264161998003]}}, {\"id\": \"1916\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33e12v2pv06\", \"name\": \"Berlin, Arnold-Zweig-Str.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.42184948812617, 52.56274084126975]}}, {\"id\": \"1973\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33db6fstvb2\", \"name\": \"Berlin, Scharnhorststr./Habersaathstr.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.374041962292988, 52.53055799826455]}}, {\"id\": \"1909\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33e421qg0t8\", \"name\": \"Berlin, Pasedagplatz\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.460104850571536, 52.55975518681808]}}, {\"id\": \"1353\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dbh34kgww\", \"name\": \"Berlin, Fennbrücke\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.360961120331002, 52.53840042725972]}}, {\"id\": \"416\", \"type\": \"Feature\", \"properties\": {\"id\": \"u337pbeumh4v\", \"name\": \"Berlin, Holländerstr./Aroser Allee\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.353756980025569, 52.56209224523224]}}, {\"id\": \"2495\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dfw7dx86v\", \"name\": \"Berlin, Hansastr.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.474370533714957, 52.54941220429778]}}, {\"id\": \"1153\", \"type\": \"Feature\", \"properties\": {\"id\": \"u336zg1xcb0s\", \"name\": \"Berlin, Stendaler Str.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.35052452341235, 52.53245909611511]}}, {\"id\": \"1218\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dbtwcj5h1\", \"name\": \"Berlin, Rügener Str.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.390837564937527, 52.54504885335276]}}, {\"id\": \"1950\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dcxnfu7ke\", \"name\": \"Berlin, Gustav-Adolf-Str./Langhansstr.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.434751268686853, 52.553590654306404]}}]}",
  "most_popular_pickup_points": "{\"type\": \"FeatureCollection\", \"features\": [{\"id\": \"194\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dcu9x68k0\", \"name\": \"S Greifswalder Str. (Berlin)\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.438452014140616, 52.540613713487126]}}, {\"id\": \"2821\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33e18xj0v6d\", \"name\": \"Berlin, Tino-Schwierzina-Str.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.434941621620494, 52.56222729605458]}}, {\"id\": \"1815\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dc6rve1gn\", \"name\": \"Berlin, Am Friedrichshain\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.425082483917585, 52.527962700033164]}}, {\"id\": \"1693\", \"type\": \"Feature\", \"properties\": {\"id\": \"u336zgz02mxc\", \"name\": \"Berlin, Perleberger Brücke\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.358022878858023, 52.53532049503019]}}, {\"id\": \"2052\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dfqyhyy98\", \"name\": \"Berlin, Berliner Allee/Indira-Gandhi-Str. [Bus Wegenerstr.]\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.466783709395516, 52.55257766369599]}}, {\"id\": \"2184\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dgq1zey0c\", \"name\": \"Berlin, Hauptstr./Rhinstr.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.504762480757808, 52.54892727357319]}}, {\"id\": \"1702\", \"type\": \"Feature\", \"properties\": {\"id\": \"u336zy0m8b7d\", \"name\": \"Berlin, Antwerpener Str.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.348768935200779, 52.5485533473965]}}, {\"id\": \"929\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dbrc7zw30\", \"name\": \"U Osloer  Str. (Berlin)\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.372401453106258, 52.557897749987305]}}, {\"id\": \"2570\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33dgjmxmvse\", \"name\": \"Berlin, Bahnhofstr.\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.499016904602733, 52.544762127440336]}}, {\"id\": \"1961\", \"type\": \"Feature\", \"properties\": {\"id\": \"u33df5kpkj2p\", \"name\": \"Berlin, Storkower Str./Einkaufszentrum\"}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [13.452930470889527, 52.53377519734386]}}]}"
}
```

## Tests

To run the unit tests:

```bash
pytest
```
