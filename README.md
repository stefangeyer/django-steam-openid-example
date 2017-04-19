# Steam OpenId authentication with python-social-auth

This application shows how to create a django app with steam openid
authentication using the steam backend in the package python-social-auth.

**This repository aims to authenticate users ONLY via steam.**

The contains the necessary configuration for the backend and uses a
custom user model in order to process all the
[extra data](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0002.29)
retrieved from the Web-API.

## Pipeline

This application extends the social auth pipeline to make sure the steam
backend works best. All changes to the pipeline can be viewed in the
file `authentication/pipeline.py`.

- **associate_existing_user**
  Checks if a user with the retrieved uid already exists
  and passes the user object down the pipeline if true.
- **get_username**
  Since we also associate existing accounts, slugification of the
  retrieved steamid is not necessary. Username is always the steamid
- **user_details**
  Replaces the corresponding function provided by the library
  and updates the user with the user data retrieved from the steam
  Web-API.

## Models

In order to properly store the received information, a custom
auth user model was created which identifies users by their Steam id
and also stores additional information like the display name on the
player's profile and the links referring to the player's profile picture.

## Settings

The settings for python-social-auth are collected at the bottom of
`steam_openid/settings.py`.