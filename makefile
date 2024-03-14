-include .creds

BASEIMAGE := xycarto/nz-lidar
IMAGE := $(BASEIMAGE):2024-03-14

RUN ?= docker run -it --rm --net=host --user=$$(id -u):$$(id -g) \
	-e DISPLAY=$$DISPLAY \
	-e HOME=/work \
	--env-file .creds \
	-e RUN= -v$$(pwd):/work \
	--privileged \
	-w /work $(IMAGE)

.PHONY: 

##### CATCHMENTS #####
get-data:
	$(RUN) python3 src/index/get-data.py $(region) $(workunit)

get-regions:
	$(RUN) python3 src/index/get-regions.py

list-region:
	$(RUN) python3 src/index/list-region.py $(region)

index-region:
	$(RUN) bash builds/index-region.sh $(region)

merge-region:
	$(RUN) bash src/index/merge-region.sh $(region)

all-regions:
	$(RUN) bash builds/index-all-region.sh

single-index:
	$(RUN) bash builds/single-index.sh


##### DOCKER #####
test-local: docker/Dockerfile
	docker run -it --rm  \
	--user=$$(id -u):$$(id -g) \
	-e DISPLAY=$$DISPLAY \
	--env-file .creds \
	-e RUN= -v$$(pwd):/work \
	-w /work $(IMAGE)
	bash
	
docker-local: docker/Dockerfile
	docker build --tag $(BASEIMAGE) - < docker/Dockerfile  && \
	docker tag $(BASEIMAGE) $(IMAGE)

docker-push: docker/Dockerfile
	docker build --tag $(BASEIMAGE) - < docker/Dockerfile  && \
	docker tag $(BASEIMAGE) $(IMAGE) && \
	docker push $(IMAGE)

docker-pull:
	docker pull $(IMAGE)