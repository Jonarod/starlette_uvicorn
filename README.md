# Starlette + Uvicorn = :heart:

Just clone this repo:

`git clone git@github.com:Jonarod/starlette_uvicorn.git`

Change your API logic in `server.py`, and add python packages in `dependencies.txt`.

Then launch the server environment using docker:

```docker run -it -p 8000:8000 -v `pwd`:/home jonarod/starlette_uvicorn```

There you have it ! A brand new API server listening to all requests at http://localhost:8000.


# Need to scale ?! No problem ! 
Just leverage the power of docker containers and copy/paste your server accross multiple machines. Then use a load balancer like `nginx` to distribute requests across all machines :)


# Documentation

Check the docs at [starlette.io](https://starlette.io) to create your next big thing faster.
