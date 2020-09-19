# About
This project is a fullstack dockerized version of my previous project https://github.com/MichaelNZ404/podcast-react-redux, a simple netflix style podcast player 

Built in Django, React, and Ant Design

![homepage](readme.png "Homepage")

# How To Install & Run Locally
- Install docker compose https://docs.docker.com/compose/install/
- Run `docker-compose up`
- Visit http://0.0.0.0:3000/ to interact with the React frontend
- Backend django API runs at http://0.0.0.0:8000/

#### Backend Notes
- `backend/entrypoint.sh` is responsible for ensuring psql is ready before django attempts to run. It also flushes, migrates and loads the fixtures. For manual control of database data, remove those lines. 
- Superuser provided within fixture `users.json` is user `admin` with matching password, so you can log into the django backend http://0.0.0.0:8000/admin without needing to createsuperuser
- Local virtual environment setup: `sudo apt install python3-virtualenv; virtualenv -p python3 backend/venv; source backend/venv/bin/activate; pip install -r requirements.txt`, remember to freeze into requirements.txt and rebuild the backend image when installing new packages.
- Run tests manually with `docker-compose exec web pytest` while local environment is running

#### Frontend Notes
- By default, the hosts node_modules is not mounted inside the container with the rest of the frontend application. If you install an npm module while developing locally you must either rebuild the frontend container or comment out the annonymous node_modules volume in `docker-compose.yml`
- Check for flow type errors with `npm run flow`
- Check for vulnerabilities with npm audit `npm audit`
- Run tests manually with `docker-compose exec frontend npm run test` while local environment is running
- Using jest-environment-jsdom-sixteen for testing due to react-scripts currently being out of date https://github.com/testing-library/dom-testing-library/issues/477 causing `MutationObserver is not a constructor` error.

#### Troubleshooting / Help:
- Rebuild the images with `docker-compose up --build`
- To fix ESLint typescript errors with flow in VSCode add `"javascript.validate.enable": false` to settings
- To manually run the initial migrations `docker-compose exec web python manage.py migrate --noinput`
- For pylint in vscode, make sure you have set up a local python virtual environment and point vscodes python interpreter at this (bottom left in vscode)

- Shelling in to containers:
    - `docker ps` to get id of running container followed by `docker exec -it <containerID> /bin/bash` to launch bash inside container. 
    - `docker-compose exec <name> sh` eg `docker-compose exec web sh`

- Remove all docker containers/volumes:
    - `docker-compose down` 
    - `docker rm -f $(docker ps -a -q); docker volume rm $(docker volume ls -q)`

## Production Deploy
- Configure a psql database for django to use.
- Provide the environment variables indicated in `.env.example` when building dockerfile (`backend/dockerfile.prod`)
- If doing a clean install, shell into a running backend container, and run the migrations with `python manage.py migrate`
- Build `frontend/dockerfile.prod` and verify site is functional when pointing DNS at port 3000. 
