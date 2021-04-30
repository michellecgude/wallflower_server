![Wallflower banner image](https://i.ibb.co/Q9tPWYY/wallflower-github-banner.png)

![language used: python](https://img.shields.io/badge/language-python-yellow) ![framework used: django](https://img.shields.io/badge/framework-django-brightgreen) ![deployed via: heroku](https://img.shields.io/badge/deployed%20via-heroku-blueviolet)

---

**The server-side repository for Wallflower. A mental health application built around making self-care simpler, more accessible, and personalized to those struggling with letting go of the trauma from the COVID-19 pandemic.**

If curious, you can view the deployed django app [here](https://wallflower-api.herokuapp.com/) although you will only be directed to the homepage as this is a private API.

## Understanding the Wallflower-Server API

The Wallflower API is organized around [REST](https://restfulapi.net/) principles. The API has simple, data-oriented URLs, uses standard HTTP responses, as well as JWT Tokens and Djoser Authentication to provide security and an ability to authenticate users. However, to view your data via the Django REST website, you'll need to be authenticated. If you'd like to be, please visit the application and make an account.

`BASE URL: https://wallflower-api.herokuapp.com`

Here is an example endpoint for the journals:

**GET `/data/journals/`**

**Response**

```
{
    "user": foo,
    "title": "bar",
    "body": "mental health is important!"
}
```

## Tech Stack

> - `Python`
> - `Django`
> - `Postgres/PSQL`
> - `curl` _(for testing endpoints)_

## Django Management Frameworks

> - `JWT | JSON Web Tokens`
> - `Djoser`

## Changes/Developments

This API has undergone major changes since its beginnings. If there's one major aspect I've learned throughout refactoring the code is learning how to be "efficient" and when to recognize where and when its happening. If it's not? Fix them quickly.

At the beginning, I was planning on supporting my [Wallflower](https://github.com/michellecgude/wallflower_client) application solely through the data I'd manually add within the Django admin. Because of this, I initially began with creating detailed models, serializers, etc for the meditations, habits, journal entries, uplifting news. After taking some space from the project and revisiting it weeks later, I decided to work on the [wireframes]() and completely revamp, simplify, and make the application more meaningful in its build and interactions. This meant shaving off a lot of initial data (such as removing the habits and only having the CRUD functionality with the journal entries, removing the individualized meditations and uplifting news from the models themselves because the users weren't going to save, update, or delete the information anyways) within the Django/PSQL database & learning to be comfortable with third party APIs.

## Author

I'm an artist turned software developer. Several years ago I was painting on canvases, now I'm painting with code. This is the first ever Django/Python API I've built with no prior knowledge. Although the end code may seem minimal, the commit history gives a more detailed view of the history behind the API. Thanks so much for checking out my code!
