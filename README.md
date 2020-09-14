## About
This project is a fullstack dockerized version of my previous project https://github.com/MichaelNZ404/podcast-react-redux, a simple netflix style podcast player 

Built in Django, React, and Ant Design

![homepage](readme.png "Homepage")

## Install/Run
- Install docker compose https://docs.docker.com/compose/install/)
- Run `docker-compose up`
- Visit http://0.0.0.0:3000/ to interact with the React frontend
- Backend django API runs at http://0.0.0.0:8000/

### Working with code locally
- To have live frontend changes, make sure you have run `npm i` locally, and mounted the frontend directory inside of docker-compose.yml (commented out by    default)

## Troubleshooting:
- Rebuild the images with `docker-compose up --build`
- To fix ESLint typescript errors with flow in VSCode add `"javascript.validate.enable": false` to settings
- To run the initial migrations `docker-compose exec web python manage.py migrate --noinput`

### Shelling in to containers:
`docker ps` to get id of running container followed by `docker exec -it <containerID> /bin/bash` to launch bash inside container. 
OR
`docker-compose exec <name> sh` eg `docker-compose exec web sh`

### Remove all docker containers/volumes:
`docker-compose down` 
`docker rm -f $(docker ps -a -q)`
`docker volume rm $(docker volume ls -q)`