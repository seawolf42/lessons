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
PIPENV ?= ${BIN_DIR}/pipenv


#
# requirements
#

.PHONY: init
init: reqs

.PHONY: reqs
reqs:
	${PIPENV} install


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
