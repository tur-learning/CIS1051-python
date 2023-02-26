docker run \
  --name cis1051-lect -it --rm \
  -p 10000:8888 \
  -v "${PWD}:/data" \
  pdonorio/my-py3dataconda:latest