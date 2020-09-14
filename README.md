# About
This project is a fullstack dockerized version of my previous project https://github.com/MichaelNZ404/podcast-react-redux, a simple netflix style podcast player 

Built in Django, React, and Ant Design

![homepage](readme.png "Homepage")

# How To Install & Run Locally
- Install docker compose https://docs.docker.com/compose/install/)
- Run `docker-compose up`
- Visit http://0.0.0.0:3000/ to interact with the React frontend
- Backend django API runs at http://0.0.0.0:8000/

## Backend Notes
- `backend/entrypoint.sh` is responsible for ensuring psql is ready before django attempts to run. It also flushes, migrates and loads the fixtures. For manual control of database data, remove those lines. 
- Superuser provided within fixture `users.json` is user `admin` with matching password, so you can log into the django backend http://0.0.0.0:8000/admin without needing to createsuperuser

## Frontend Notes
- By default, the hosts node_modules is not mounted inside the container with the rest of the frontend application. If you install an npm module while developing locally you must either rebuild the frontend container or comment out the annonymous node_modules volume in `docker-compose.yml`

## Troubleshooting/Help:
- Rebuild the images with `docker-compose up --build`
- To fix ESLint typescript errors with flow in VSCode add `"javascript.validate.enable": false` to settings
- To manually run the initial migrations `docker-compose exec web python manage.py migrate --noinput`

### Shelling in to containers:
`docker ps` to get id of running container followed by `docker exec -it <containerID> /bin/bash` to launch bash inside container. 
OR
`docker-compose exec <name> sh` eg `docker-compose exec web sh`

### Remove all docker containers/volumes:
`docker-compose down` 
`docker rm -f $(docker ps -a -q)`
`docker volume rm $(docker volume ls -q)`

## Production Deploy
- Configure a psql database for django to use.
- Provide the environment variables indicated in `.env.example` when building dockerfile (`backend/dockerfile.prod`)
- If doing a clean install, shell into a running backend container, and run the migrations with `python manage.py migrate`
- Build `frontend/dockerfile.prod` and verify site is functional when pointing DNS at port 3000. 
