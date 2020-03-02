# Python Environments with `pyenv`

If you've ever worked on more than one project at a time, you have probably run into versioning issues. Maybe you're building a web scraper and you're also experimenting with [flask](https://flask.palletsprojects.com/), and both of your projects need the [requests](https://requests.readthedocs.io/) package, but one of them cannot advance beyond version 2.11.1 (`requests<=2.11.1`) and the other must have version 2.21.0 or greater (`requests>=2.21.0`). If you just installed python in your path somewhere, you will probably end up getting very confused in your installation as you add and remove packages, trying to always have the right versions for whichever project you are working on.


## The Fundamental Problem


Unless you only ever work on one Python project, you need a per-project way to install and remove packages that does not interfere with any other project's package space. These environments should be entirely independent from each other in every way.


### The Beginnings of a Solution

The first major breakthrough along these lines was the idea of *virtual environments*. A virtual environment is a standalone build of python and all its related tools in a directory that also holds any installed packages and other external resources.

You would generally create a virtual environment using a tool like [virtualenv](https://virtualenv.pypa.io/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/) or with something like [Conda](https://docs.conda.io/). All of these tools give you command-line access to creating per-project Python environments.


### The New Problem

This shifts the problem from being about package versioning to being about environment management.


#### Environments are everywhere

Each project has a directory (often called `env` or `venv`) that contains the full Python installation for that project (note that sometimes these environments are somewhere else on your computer and not in the project folder, depending on how your project is configured).

Backing up your computer should not require backing up the environments (you have them fully specified with [pipenv](https://pipenv.kennethreitz.org/) or some other specification tool, right?), but creating the right rules to exclude all the actual virtual environments while including other directories with those names is hard.

Some environment managers do allow you to put the virtual environments in a consolidated place, but most of them don't.


#### Switching environments is an extra step

When you change directories from one project to another, you might not remember to also switch your virtual environment. This leaves you running the wrong versions of packages, and perhaps even an incompatible version of Python.

Some environment managers do automate this for you, but most of them don't.


#### Still hard to ensure correct Python version

Most modern package managers (like `brew` or `aptitude`/`apt-get`) give you per-project virtual installations, but they are still derived from only the one or two versions of Python you have installed on your computer (MacOS, for instance, comes with Python 2.7 and with homebrew you can also add Python 3.7). When you create a new virtual environment, it has to derive from one of those two python versions (because of how system-level package managers work). This makes working with any other version challenging.

Some environment managers do give you fine-grained control over which versions of Python are installed locally, but most of them don't.


## The Solution

Luckily there has been a lot of great work in this area over the last couple years. The newest (and nicest in my opinion) contender to make mainstream popularity in the world of environment management is `pyenv`.

`pyenv` is to python environments what `pip` is to python packages: you use it to 

* install and uninstall versions of Python
* create and delete virtual environments
* pick which version of Python is active at any point
* automatically activate a certain version when you change into a given directory (and deactivate when you leave it)
* ... and a whole lot more

### Installing `pyenv`

Use whatever package manager you use on your system to install `pyenv` and `pyenv-virtualenv`. I recommend you follow the official [detailed instructions for all platforms](https://github.com/pyenv/pyenv#installation).

For MacOS users (you might need to install Homebrew first, if you haven't already):

```sh
$ brew install pyenv pyenv-virtualenv
```

You can customize many things about `pyenv` but I recommend you leave evereything as default until you know you have a reason to change something.


### Installing and uninstalling Python versions

First, find the version of python you want:

```sh
$ pyenv install --list | grep 3.8
  3.8.0
  3.8-dev
  3.8.1
  miniconda-3.8.3
  miniconda3-3.8.3
```

... and then install it:

```sh
$ pyenv install 3.8.1
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.8.1.tar.xz...
-> https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz
Installing Python-3.8.1...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.8.1 to /Users/seawolf/dev/pyenv/versions/3.8.1
```

To uninstall:

```sh
$ pyenv uninstall 3.8.1
pyenv: remove /Users/seawolf/dev/pyenv/versions/3.8.1? y
```


### Creating and destroying virtual environments

To create a virtual environment from a particular python version:

```sh
$ pyenv virtualenv 3.8.1 myenv
```

The above command tells pyenv to make a new virtualenv based on 3.8.1 and name it `myenv`.

To delete a virtualenv:

```sh
$ pyenv uninstall myenv
pyenv-virtualenv: remove /Users/seawolf/dev/pyenv/versions/3.8.1/envs/myenv? y
```


### Picking which version of Python is active

Activating a specific virtualenv is easy:

```sh
$ pyenv activate myenv
(myenv) $
```

Deactivating the current environment:

```sh
(myenv) $ pyenv deactivate
$
```


### Setting global and per-directory virtual environments

To set the global virtual environment (to be used when no other has been activated):

```sh
$ pyenv global myenv
(myenv) $
```

To set a virtual environment to be used within a certain directory (and all of its subdirectories):

```sh
$ pyenv local myenv2
(myenv2) $
```

In practice, you'll see something like this:

```sh
$ pyenv install 3.8.1
$ pyenv virtualenv 3.8.1 sys
$ pyenv virtualenv 3.8.1 myproject
$ pyenv global sys
(sys) $ mkdir myproject
(sys) $ cd myproject
(sys) $ pyenv local myproject
(myproject) $ ls -a
.			..
(myproject) $ cd ..
(sys) $ cd myproject
(myproject) $
```

You can see the prompt changing to reflect which virtual environment should be active as you move around on your filesystem.


### Prompt-changing feature deprecation solution

You might notice a message like the following when you try to activate an environment:

```sh
$ pyenv activate myenv
pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.
```

There has been discussion about removing this from `pyenv` for some time, and it looks like it's not going anywhere yet. However, to make this go away in `zsh` on a Mac, add the following to your `.zshrc`:

```
setopt PROMPT_SUBST
_prompt_sub='*/'
PROMPT='(${PYTHON_VIRTUAL_ENV/${~_prompt_sub}/}) <whatever else you want> '
```

This takes the responsibility out of `pyenv` and puts it in your shell. Since `pyenv` updates the `$PYTHON_VIRTUAL_ENV` variable on every change in environment, this will always show the virtual environment you are in. If it ever is completely blank (`()`), it means there is not an active environment at the moment.

Directions for other shells (like `bash`) will be similar but will not be covered here.


## Comparison with Other Environment Managers

In general, `pyenv` can be seen as a better toolset than the environment managers available as python packages (`virtualenv`, `virtualenvwrapper`, etc). It fundamentally changes how virtual environments are created and destroyed to solve problems that limit the others.

**Conda**: `conda` sets out to solve an even bigger problem than `pyenv` does: environment management for multi-language projects. If you are working on a project that incorporates package management for multiple languages simultaneously, you might consider `conda`. It would also be a better choice for teams that are less software-engineering-centric (such as data analysis teams) or teams whose software is difficult to run on multiple operating systems (especially Windows, as configuring tools there tends to confuse a lot of people). If your projects are predominantly Python with some frontend code written in some flavor of JavaScript then `pyenv` will be completely adequate for your needs, even on large projects with multiple active developers.

**Pipenv**: `pipenv` is a tool for managing packages installed within an environment, and works very nicely in conjunction with `pyenv`. Just note that with each new environment you create, you should `pip install pipenv`, and include `pipenv == "*"` in your `Pipfile` so that `pipenv` will always be available in that environment.


## References

* [Pyenv](https://github.com/pyenv/pyenv)
* [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html): this is good for understanding what virtual environments are and why you want them; note that all the steps shown in this are easier with `pyenv`
* [Pipenv](https://pipenv.kennethreitz.org/)
* [Conda](https://docs.conda.io/)