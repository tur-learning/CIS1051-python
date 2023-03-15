---
title: Quickstart Setup
layout: default
filename: 03_setup
--- 

<h1>{{ page.title }}</h1>

### TL;DR

- [Docker setup](#docker-setup)
- [GitHub Codespace setup](#github-codespace-setup)

To install the compiler, or the interpreter (with Python for example) and anything you need to work with, in your dev environment (i.e. dependencies, plugins, frameworks, servers), usually means being familiar with the operating system (OS), particularly the command-line interface (CLI), in other words: system administration.

The concept of running Python programs on a browser-based dev environment (e.g. GUI, IDE, CLI) may seem like a distant dream, but fortunately, with the current technology stack available, this is already a viable solution!

To run simple Python scripts, there are couple options out there:

- [PythonAnywhere](https://www.pythonanywhere.com/) a fully-fledged Python environment, ready to go, for students and teachers (host, run, and code Python in the cloud).
- [Google Colab](https://colab.research.google.com/) notebooks to combine executable code and rich text in a single document (along with images, HTML, LaTeX and more).

However, if we need something more advanced &ndash; as well as more control over the dev enviroment itself &ndash; go on to the next sections to find out how to fire up a powerful Linux host and anything you need, with just a couple commands!

## Docker setup

This is the most effective solution to get a fully fledged dev environment (locally): with minimal installation requirements (just Docker) and full controll over the available resources, as well as over the whole environment!

## GitHub Codespace setup 

This is the quickest way to spin up a lightweight dev environment (in the cloud): without the need of installing anything at all on your personal computer, althougth sacrifying to some extent the available resources and control, over the environment itself.

Once logged-in on GitHub, go to the repo ( i.e. [tur-learning/CIS1051-python](https://github.com/tur-learning/CIS1051-python/tree/master) ) and click on the `Use this template > Open in a codespace` button 

![Open Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/open_codespace.png)

This will open a browser-based IDE (essentially vscode) in a new tab.

![IDE Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/ide_codespace.png)

From inside the integrated CLI, change to the parent `/workspaces` directory with 

    cd ..

![CLI Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/cli_codespace.png)

so we can start installing all the necessary dependecies we need, starting from the most important one, the `pygame` module!

    pip install pygame

the next one is necessary to render `pygame` graphics on a browser-based GUI, in a new tab, installing a custom version of the `pygbag` module:

    git clone https://github.com/andreagalle/pygbag.git
    cd pygbag
    git checkout gh-codespaces
    pip install -e $PWD

![pygbag Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/pygbag_codespace.png)

At this point, go back to the repo root and navigate to the example you want to run, for instance:

    cd ..
    cd CIS1051-python/lab-sessions/snake/challenge/lab_4/level_10/

![challenge Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/challenge_codespace.png)

fom there you can run it with the following command

    pygbag --gh_codespace ${CODESPACE_NAME} main.py

![port Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/port_codespace.png)

thanks to the `pygbag` module, you can access the game (webapp) on the default port `8000` under the (randomly choosed) Codespace Domain name

![URL Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/url_codespace.png)

Then click on the `Ready to start !` button and that's it!

![Ready Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/ready_codespace.png)

**N.B.** always remember to turn off the codespace we just instantiated, not to waste useful resources (i.e. core hours used). Thus click on the GitHub `Codespace` tab at the Top Navigation Bar of the repo

![Bar Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/bar_codespace.png)

then, search for the previous (randomly choosed) name of the codespace running and stop it.

![Stop Codespace](https://raw.githubusercontent.com/tur-learning/CIS1051-python/gh-pages/lectures/notebooks/img/stop_codespace.png)

