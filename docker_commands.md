# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume


### Create the volume

```bash
docker volume create fastapi-db
```

### Seed the volume (via Docker Desktop)

```bash
docker run --rm -v fastapi-db:/data -v ${PWD}:/backup alpine tar -xvf /backup/seed_data.tar -C /data
```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run -d --name refael -v fastapi-db:/app/db -p 8080:8000 2bf8c7ac47c1 
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run -d --name refael -v fastapi-db:/app/db -p 8070:8000 shopping-server2:v1
```



 
 