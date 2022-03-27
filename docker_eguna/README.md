# Docker Eguna (10/10/2021)


##  Intro
 
### What is Docker?

- Platform as a service to deliver software in packages called containers. 

- Containers are isolated from one another, and can communicate with each other thorugh well-defined channels.

- All containers share the services of a single operating system kernel, they use fewer resources than VM.

- Initial release in 2013

- Written in Go

- Docker enables an application to run in a variety of locations: on-premises, public cloud, private cloud...

- Docker containers are light. A single server can run several containers simultanously.  

### Containers vs VM

- Both achieve virtualization, but in different levels. VM achieve **hardware virtualization** (it happens at the hardware level). Containers achieve **virtualization at the OS level** ( the OS is calles host-OS).  

- VM achieve **isolation of machines**. Container achieve **process isolation**. Containers share the same kernel and OS. 

- VM have infinite **flexibility** of hardware (number of processors, memory size ...). Containers have infinite **portability** (a few lines of text specify how to build and run the container).  


### Monolith vs Microservices

- Microservices: small deployable services that communicate via API endpoints/HTTP creating one big distributed system.

- Monoliths: A large block of code havign multiple modules (often database, backend and frontend). 

- The trend is (2021) towards developing microservices because scale faster and are easier to maintaing. Docker plays a huge role here. Dedicatign an entire VM instance to deploy a microservice isn't the most efficient option. Docker allows to use **one container for each microservice**. 

### Benefits of Docker

- **Simplify configuration**. Freedom to run an app accross multiple platforms.

- **Developer productivity**. Docker allows DEV to be as close as possible to PROD using few dozen containers running services. This is harder with VMs. 

- **App isolation**.



## Docker under the hood

- Docker containers share the underlying kernel. Assume we have OS-Ubuntu (Linux kernel) with Docker installed. DOcker can run any flavour of OS as long as they have the same Linux kernel (such as CentOS or Fedora). Because they share the same kernel, it is would be impossible to create a Windows based container. However, when you install DOcker on Windows you can create Ubuntu based container because docker creates a Linux VM and builds the containers on top of that under the hood. 

- **A container lives as long as the process inside it is alive**. Once the task is complete the container exits.

- When installing Docker, three components are installed: Docker Deamon, REST API and DOcker CLI (command line interface). The Docker CLI does not necesarilly need to be on the same host, it could be on another system and work with a remote worker engine. THis is achieved using the `-H` tag. For example, `docker -H=10.123.2.1:2375 run nginx`.

- Docker uses **namespaces** to isolate workspaces. 

- The containers within a Docker host share same CPU and memory. By default, there is no restriction as how much of the resources a container could use. Thus, a container may end up utilizing all the resources on the underlyign host. However, there is the option to restrict the amount of cpu and memory and container can use using **cgroups**. The tags `--cpus` and `--memory` limit the resources a container can ocupy. For example, `docker run --cpus=.5 --memory=100m  ubuntu` makes sure the contaienr doesn't ocupy more than 50% of the cpu and 100MB at any given time. 

### Docker components

#### Software

**Dockerd**: The Docker daemon, a persistent process that manages Docker containers and handles objects. 

#### Objects

There are three main classes of Docker objects: images, containers, and services.

- **Container**: Encapsulated environmnet that runs an app. Managed using the Docker API.
- **Image**: Read-only template used to build containers. Multiple containers can be built using one image. Containers are the ones running the images. DockerHub contains common images of widely used producs such as MongoDB, SQLite3... You can also create your own image and push it to DockerHub repository.
- **Service**: Allows containers to be scaled accross multiple Docker daemons. THis is known as swarm, a set of coopering daemons.       


### Docker commands

- `docker run nginx`: Run a container from an image. If the image is not present in the host, it will ceck in DockerHub. 
- `docker ps`: Lists all **running** container and some basic info about them. Add `-a` to show allso stopped containers.  
- `docker stop CONTAINER_ID/CONTAINER_NAME`: Stops the running container. 
- `docker rm CONTAINER_ID/CONTAINER_NAME`: Remove an stopped container permanently.
- `docker images`: List of available iamges and their sizes in the host.
- `docker rmi IMAGE_NAME`: Remove an image. YOu must assure that no container is running usign that image.
- `docker pull IMAGE_NAME`: Downloads an image from DockerHub. 
- `docker run ubuntu sleep 5`: Instrunct DOcker to run a process. 
- `docker exec CONTAINER_NAME COMMAND`: Execute a command on a running container.
- `docker run -d simple-webapp`: Run containers in detached mode.
- `docker run -p 80:5000 simple-webapp`: Maps the local port 80 to the port 5000 of the container. 
- `docker run -v /opt/datadir:/var/lib/mysql mysql`: Map a directory outside the container to persist the data. 
- `docker attach CONTAINER_ID/CONTAINER_NAME`: Attach back to a container. 
- `docker inspect CONTAINER_NAME`: More detailed info about the container in JSON format.
- `docker logs CONTAINER_ID`: Show logs of a container running in the background.
- `docker run -e APP_COLOR=blue simple_app`: Set environment variables in the container.

### Custom Docker images: Dockerfile

Steps to run a python webapp are: 1. OS-Ubuntu 2. Update apt repo 3. Install dependencies using apt 4. Install python dependencies using pip 5. Copy source code to /opt folder 6. Run the web server using a command. To containerize a python webapp these steps must be executed. These steps are specified in the **Dockerfile**. 

```
FROM Ubuntu   #base OS 

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flas-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```

The command `docker build Dockerfile -t my-custom-app` builds the Docker image localy. To make it available in the DockerHub registry run `docker push my-custom-app`.   
 
Docker builds images in a **layered architecture**. Each line on the Dockerfile creates a new layer with just the changes from the previous layer. This history can be shown running `docker history IMAGE_NAME` command. All layers are cached by Docker, so if one step fails we don't neet to start all over again. 
 
  

### Docker Networking

By default, Docker has installed 3 networs: Bridge, none and host. The network can be specified when running the container as `docker run ubuntu --network=host`. The **none** type run in an isolated network and cannot interact with the outside worlds. The **bridge** network (by default) each container receives an internal IP and they can access each other using it (access within same host OS). In bridge mode, to access the container from the outside world the ports of the Docker host and the containers must be mapped. In **host** mode the network isolation between the Docker host and the Docket container is taken out and the port of the container is automatically associated to the same port of the host (port mapping is not required).   
All the containes within a Docker host can refer to each other using the name of the container. 


### Docker storage

- Docker stores all its data at `/var/lib/docker`. All files related to containers and images are stored in `./containers` and `./images` respectively. emember the layered architecture of docker images.

- When building a container, Docker creates a new writeable layer called **container layer** on top of the image layer. This layer is used to store data created by the container. However, this layer is deleted when the container stops. All the files withing the image layers are read only, but the container layer is writeable. If a file in the iamge layer is modified, Docker automatically creates a copy of it in the container layer and that one is the one modified (copy-on-write mechanism).

- To persist the data we need a **persistent volume**. Run `docker volume create data_volume` creates `/var/lib/docker/volumes/data_volume`. Then this volume is mounter when running the container with `docker run -v data_volume:/var/lib/mysql mysql`. All the data written by the database is in fact stored in the volume created on the Docker host. Even if the container is destroyed the data is active. This is called **volume mounting**.   

- To load data from `/data/mysql` in the Docker host to the container we run `docker run -v /data/mysql:/var/lib/mysql mysql`. This is called **bind mounting**.

- `-v` is the old way to do it. It is prefered to use `--mount``option. For example `docker run --mount type=bind, source=/data/mysql, target?/var/lib/mysql mysql`.

- Remark that the **Storage drivers** are the ones that take care of all this work of creatign the layers and mounting, which depend on the underlying OS (host OS).   


### Docker compose

- When dealing with multiple containers within a Docker host, **links** can be stablished between each other. This is one using the `--link` option when running docker containers. For example `docker run --link redis:redis voting-app` links the container name with the name of the host. However, this can be too simple when dealing with complex applications.

- Docker compose is used to run a complex application with multiple containers (and avoid running them one by one). Docker compose is a YAML format configuration file. 

```
#docker-compose.yml

redis:
	image: redis
db:
	image: postgres:9.4
vote:
	image: voting-app
	ports:
		- 5000:80
	links:
		-redis
result:
	image: result-app
	ports:
		-5001:80
	links:
		-db   #db:db = db
worker:
	image: worker
	links:
		-redis
		db = db

```

Then we simply run `docker-compose up` to build up the entire application stack. This is happening all within one same Docker host. If the image does not exist and we want to build it, we can specify it by adding `build: ./vote` where the directory contains the respective Dockerfile. 

- There are different versions for the docker-compose file. It supports a lot of options. **Version 2** of the previous docker-comose.yml file is the following: 

```
#docker-compose.yml
version: 2
services:
	redis:
		image: redis
	db:
		image: postgres:9.4
	vote:
		image: voting-app
		ports:
			- 5000:80
	result:
		image: result-app
		ports:
			-5001:80
	worker:
		image: worker
		depends_on:
			-redis
```

Note that for every version besides version 1, the version must be specified in the beginning of the file. Version 1 attaches all the containers to the default bridge network, and then uses links to enable communication. Version 2 allows not to use links by allowing contaienrs to communicate with each other by their service names. Version 2 also allows to specify a startup order using the `depends` field. Then comes **Version 3**. Similar to version 2, but comes with support for Docker Swarm and other specific details. 


- By default all the containers are deployed on the bridge network. Assume we want to modify the architecture a little bit by splitting the traffic from diferent sources, such as front-end (user generated traffic) and back-end (app itnernal traffic). We then create a front-end network and a back-end network. We are going to connect the voting-app and result-app to both networks, an the rest jsut to the back-end network. Docker compose allows to configure this architecture easily. 

```
#docker-compose.yml
version: 2
services:
	redis:
		image: redis
		networks:
			- back-end
	db:
		image: postgres:9.4
		networks:
			- back-end
	vote:
		image: voting-app
		ports:
			- 5000:80
		networks:
			- back-end
			- front-end
	result:
		image: result-app
		ports:
			-5001:80
		networks:
			- back-end
			- front-end
	worker:
		image: worker
		depends_on:
			-redis
		networks:
			- back-end
networks:
	front-end:
	back-end:
```


## Example

In `/2deg-root-calculator` a toy example thats put into practice Docker concepts can be found.
## Resources 

- https://en.wikipedia.org/wiki/Docker_(software)
- https://www.youtube.com/watch?v=zJ6WbK9zFpIi
- https://www.youtube.com/watch?v=cjXI-yxqGTI




