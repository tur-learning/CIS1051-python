# Docker setup

To run this jupyter notebooks on Docker, type the following command on the CLI:

```
docker run -it --rm -p 10000:8888 -v ${PWD}:/data pdonorio/my-py3dataconda:latest
```

To run a jupyter-lab notebook, to get the .html and .pdf slideshow, type the following:

```
docker run -it --rm -p 10001:8888 -v ${PWD}:/home/jovyan/work jupyter/minimal-notebook:latest
```
