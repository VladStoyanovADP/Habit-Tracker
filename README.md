
# A-bit API

## Project Overview

This repository is a the backend of our team project at Northcoders. It's a RESTful API written in Python and using the Django framework alongside PostgreSQL as a database management system and hosted on Render.

A user is able to interact with the databse with the following methods:

* GET a list of all of the users

* GET a list of all the rewards 
* GET a list of all the habits
* GET a list of all the achievements
* GET/PATCH/POST/DELETE a list of all the rewards of a specific user
* GET/PATCH/POST/DELETE a specific reward of an user
* GET/PATCH/POST/DELETE a specific habit of an user
* GET a specific user's achievement
* GET the currency of a specific user

## Hosted Version

You can see a live version of this API, hosted with `Render`:

https://final-api.onrender.com/

## Setup Instructions

### Installation Requirements

-   **pip**: 20.0.2 or later
-   **PostgreSQL**:  12.12 or later

### Cloning the repository:

Create a directory to clone the repository to. In your terminal:

```
$ mkdir <new directory name>
```

Change directory to the one you just created:

```
$ cd <new directory name>
```

Then clone the repository:

```
$ git clone https://github.com/VladStoyanovADP/Habit-Tracker
```
### Database setup and seeding

Run the build.sh script in the root directory to setup your development, test databases and to install the required dependencies.