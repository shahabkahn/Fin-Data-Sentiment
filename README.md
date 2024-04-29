# Financial-Data-Sentiment-Analyzer
### This repository contains files for building a RESTful API using FastAPI to perform sentiment analysis on finanical data using a pre-trained Hugging Face Transformer model.

## Table of Contents
* Introduction
* Requirements
* Code Overview
* Installation
* Docker Container
* API Usage
* API Testing
* Model

## Introduction
#### The main purpose of this project is to develop an API for sentiment analysis tasks using FastAPI, Docker, and Hugging Face Transformers. It passes input through the model to classify the sentiment as positive, negative, or neutral.

## Requirements
#### This project has the following dependencies.
* FastAPI: A framework for building APIs.
* Transformers: The Hugging Face library for (NLP) tasks.
* Pyngrok: A Python wrapper for ngrok, which exposes local servers over public URLs.
* Nest_asyncio: A library for running asyncio nested in other asyncio loops.
* Pydantic: A data validation library

## Code Overview
#### The main files of the code are:
* main.py: This file contains the FastAPI application, including the definition of endpoints, and model integration.
* test_.py: This file contains 3 tests for the API endpoints using FastAPI's TestClient.
* Dockerfile: The Dockerfile has all instructions for building the Docker image for the API.
* requirements.txt: This file has all the dependencies required by the project.

## Installation
#### To use the API locally, follow these steps:
* Clone this repository to your local machine.
* Have Docker installed.
* Build the Docker container using the Dockerfile.
* Run the Docker container.

## Docker Container
#### To use the Docker container, follow these steps:
* Open the project directory in your terminal.
* Build a Docker image using the following command
   'docker build -t api_image .'
* Creating a Docker container from the built image
   'docker run -p 8000:8000 api_image'
* The API will be available at http://localhost:8000
* The API documentaion will be avaialable at http://localhost:8000/docs or http://localhost:8000/redoc

## API Usage


## API Testing


## Model
