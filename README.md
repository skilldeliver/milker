<p align="center">
  <img src="https://i.imgur.com/YwtAJTt.png" width="1024">
</p>

<h1 align="center">
MIhov's popfoLK ExtractoR
</h1>

<div align="center">
	<a>
	    <img src="https://img.shields.io/github/v/tag/skilldeliver/milker" alt="Version">
	</a>
	<a href="https://github.com/ambv/black">
	    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black">
	</a>
	<a href="https://github.com/skilldeliver/milker/blob/master/LICENSE">
	    <img src="https://img.shields.io/github/license/Naereen/StrapDown.js.svg" alt="GitHub license">
	</a>
	<a>
	    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="GitHub license">
	</a>
</div>

<p align="center">
  <a href="#overview">Overview</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#usage">Usage</a>
  •
  <a href="#contributing">Contributing</a>
  •
  <a href="#acknowledgments">Authors</a>
</p>


# Overview
**MILKER** is a Python application that extracts audio information of songs. It does that by collecting names of songs with [YouTube API](https://developers.google.com/youtube) from given playlists, querying them with the [Spotify API](https://developer.spotify.com) and finally extracting the Spotify audio features of the song. **MILKER** was specifically tailored for extracting audio features of [Bulgarian popfolk songs, 2014-2019](https://www.kaggle.com/astronasko/payner).

# Installation
The installation steps are as follows:

1. **Make sure to get git and Python**

This is required to clone the repository and actually run the app.

2. **Clone the repository**

`git clone https://github.com/skilldeliver/milker.git`

3. **Enter the directory**

`cd milker`

4. **Install Pipenv**

`python -m pip install pipenv` (if you don't have it installed)

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

1. **Running the whole process**

 `pipenv run start`

This fetches youtube songs and downloads spotify data

2. **Fetching youtube songs only**

 `pipenv run start yt`

This fetches youtube songs (it's mandatory for running the download of the spotify data)

3. **Downloading spotify data**

 `pipenv run start sp`

This downloads spotify songs data through querieng the youtube fetched songs. 

# Contributing
We are open to contributors. To contribute follow these steps.

1. **Fork and clone the repistory**

This is required to do your own development and then finalize with pull request to us.

2. **Installation**

`pipenv install --dev` 

The installation step is a little bit different because we require linting your code 
and formating it with black. Pipenv this way will install the required development packages.

3. **Development work**

Please write clean and well documented code. Set up the linting with flake8 in your
development enviorement and run black after you are done. 
And write good commit messages! 

4. **Create Pull request**

And wait... :) We will check every pull request and make sure to give detailed remarks
if we are not fully okay with your work.

# Acknowledgments
I wish to thank [@nasko7](https://github.com/nasko7) for having introduced me to the collection of Spotify data and for his subsequent conceptual support.
Thanks to the development team of [Spotipy](https://github.com/plamere/spotipy) for providing easy to use Spotify API wrapper. 
Thanks to [Jagoda Kondratiuk](https://unsplash.com/@jagodakondratiuk) for sharing their work on Unsplash.
