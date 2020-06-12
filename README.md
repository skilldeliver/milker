
# Overview
TODO

# Installation
The installation and running steps are as follows:

1. **Make sure to get git and Python**

This is required to clone the repository and actually run the app.

2. **Clone the repository**

`https://github.com/skilldeliver/payner.git`

3. **Enter the directory**

`cd discord-bot`

4. **Install Pipenv**

`python -m pip install pipenv`

5. **Install dependencies**

`pipenv install`

6. **Set up Youtube Data API credentials**
You will need to set up your project at YouTube to get the credentials necessary to make authorized calls.

https://developers.google.com/youtube/v3/quickstart/python#step_1_set_up_your_project_and_credentials

Name your `client_secret_CLIENTID.json` -> `client_yt_secret.json` and paste it in the app directory 

7. **Set up Spotify API credentials**
You will need to register your app at Spotify to get the credentials necessary to make authorized calls (a client id and client secret).

https://developer.spotify.com/dashboard/applications

```json
{
	"client_id": "your_client_id",
	"client_secret": "your_client_secret",
	"redirect_uri": "http://localhost/"
}
```

Save this file as `client_sp_secret.json` it in the app directory 


# Usage
There are three options for running the applications.

1. **Running the whole process** `pipenv run start`
This fetches youtube songs and downloads spotify data

2. **Fetching youtube songs only** `pipenv run start yt`
This fetches youtube songs (it's mandatory for running the downloading of the spotify data)

3. **Downloading spotify data** `pipenv run start sp`
This downloads spotify songs data through querieng the youtube fetched songs. 

# Roadmap
TODO

# Contributing
TODO

# Authors and acknowledgment
TODO

# License
TODO