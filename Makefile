# -------------------------------------
# MAKEFILE
# -------------------------------------

#
# project settings
#

ENV_DIR = ${PWD}/env
BIN_DIR = ${ENV_DIR}/bin
JUPYTER ?= ${BIN_DIR}/jupyter
PYTHON ?= ${BIN_DIR}/python
PIPENV ?= pipenv

DEV_ENV = ./.devcontainer

#
# requirements
#

.PHONY: init
init: reqs

.PHONY: reqs
reqs:
	${PIPENV} lock -r --dev > ${DEV_ENV}/requirements.txt


#
# shell
#

.PHONY: shell
shell:
	${PYTHON}


#
# serve
#

.PHONY: serve
serve:
	${JUPYTER} notebook .
