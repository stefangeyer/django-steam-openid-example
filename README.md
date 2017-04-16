# Steam OpenId authentication with python-social-auth

This application shows how to create a django app with steam openid
authentication using the steam backend in the package python-social-auth.

**This example uses Steam authentication ONLY and does not rely
on the django model auth backend**

The contains the necessary configuration for the backend and uses a
custom user model in order to process all the
[extra data](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0002.29)
retrieved from the Web-API.

## Pipeline

The pipeline was updated to make sure the steam backend works best.
All changes to the pipeline can be viewed in the file `social_auth/pipeline.py`

- **user_exists**
  This function checks if a user with the retrieved uid already exists
  and passes the user object down the pipeline if true.
- **user_details**
  This function replaces the related function provided by the library
  and updates the user with the user data retrieved from the steam
  Web-API

## Models

WIP

## Settings

WIP