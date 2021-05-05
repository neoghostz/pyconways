# Makefile for building publishing container
PROJECT = conways
VERSION = edge
PWD = $(shell pwd)
GITSHORTHASH = $(shell git rev-parse HEAD | cut -c 1-7)
GITSHORTHASH_AWS = $(shell echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
APP_IMAGE = $(PROJECT):$(GITSHORTHASH)
APP_IMAGE_AWS = $(PROJECT):$(GITSHORTHASH_AWS)
CONTAINER_TAG = latest

genReqs:
	pipenv lock -r > requirements.txt
.PHONY: genReqs

genTestReqs:
	pipenv lock -r --dev > requirements.txt
.PHONY: genTestReqs

buildLocal: genReqs
	docker build -t $(APP_IMAGE) -f Dockerfile.alpine .
.PHONY: build

build: genReqs
	docker build -t $(APP_IMAGE_AWS) -f Dockerfile.ubuntu .
.PHONY: build

test: genTestReqs
	docker build -f Dockerfile.test -t $(PROJECT)-test .
.PHONY: test

buildRequirements:
	pipenv lock -r > requirements.txt
.PHONY: buildRequirements

unittest:
	PYTHONPATH=$(shell pwd)/src/ pytest --cov=src --cov-branch --cov-report term-missing ./tests
.PHONY: unittest

lint:
	flake8 --max-line-length 120
.PHONY: lint
