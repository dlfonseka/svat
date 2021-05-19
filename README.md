# Surgical Video Annotation Tool

The Surgical Video Annotation Tool (SVAT) is a web application designed to facilitate the annotation of medical (or other) videos. The tools was designed using the Django framework by a group of computational engineering students from the University of Texas at Austin.

### Setup

This repository contains a Django application. If you are unfamiliar, consult the [documentation](https://docs.djangoproject.com/en/3.2/).

This application is currently configured to be run in a development environment. This brief document will outline the steps necessary to get this application up and running in this environment, for example on a personal computer. Consult the [deployment](#deployment) section for guidance on deploying this application in a production environment.

#### Setup Steps

1). [Install Django and required dependencies.](https://docs.djangoproject.com/en/3.2/intro/install/)

2). Clone this repository into the desired location in your filesystem. 

3). In your terminal, navigate into the *svat* directory.

4). Type the command: `python manage.py migrate` to create the application's SQLite database.

5). Type the command: `python manage.py createsuperuser` to create the application's administrator profile. Follow the prompts to create the user.

6). Type the command: `python manage.py runserver` to run the development server. Navigate to the address indicated by the response to your command. Make sure you are using a [supported browser](#supported-browsers-and-media).

### Supported Browsers and Media

This application is designed to run on the latest versions of Mozilla Firefox (88.0.1) and Google Chrome (90.0.4430.212). Make sure to check for [browser supported video formats](https://www.encoding.com/html5-video-codec/).

### Deployment





  
