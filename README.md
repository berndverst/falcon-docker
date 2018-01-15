# falcon-docker
Minimal Docker image for Falcon Framework Python3 app on Alpine Linux

Run with:
`docker run -it -p8080:80 berndverst/falcon`


## How to use this image

We assume your application code is in the directory `./app` and your *Falcon* entrypoint is the `app` object in `./app/main.py`.

```bash
.
├── Dockerfile
└── app
    └── main.py
```

Create a Dockerfile as follows:

```Dockerfile
FROM berndverst/falcon
COPY ./app /app
```

Make sure to map a local port to container port `80`.

Example:
```bash
docker build -t myfalcon .`
docker run -it -p8080:80 myfalcon
```

Docker Hub: https://hub.docker.com/r/berndverst/falcon
