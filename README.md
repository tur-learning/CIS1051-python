## Docker setup

This is the most effective solution to get a fully fledged dev environment (locally): with minimal installation requirements (just Docker) and full controll over the available resources, as well as over the whole environment!

Once installed [Docker](https://www.docker.com/) on you personal computer (check out the right installation package given the OS)

After the [alnoda/python-workspace](https://hub.docker.com/r/alnoda/python-workspace) Docker image has been pulled open a terminal and run the following command

    docker run --name tur23-python -d -p 8020-8040:8020-8040 alnoda/python-workspace

this will run a Docker container, in detached mode, with the promised dev environment accessible from the browser.

Go to [localhost:8020](http://localhost:8020/)

From there open the `Terminal` webapp (CLI) and clone the repo [tur-learning/CIS1051-python](https://github.com/tur-learning/CIS1051-python)

    git clone https://github.com/tur-learning/CIS1051-python.git

Let's start installing all the necessary dependecies (pygame and pygbag)

    cd CIS1051-python/lab-sessions
    git checkout lab-sessions
    source .env
    setup
    
Now you are ready to start. To run a pygame script use the `deploy` command in the script directory and go to localhost:8030 in your browser.
