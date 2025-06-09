# Arma 3 Server (Antistasi mod)

## Prerequisite

- Ensure you have Docker installed
- Ensure you have downloaded all the mods you plan to use for the server

# Installation


## Step 0 (installation) : run docker compose build for the first time

This will initialize the folder structure and create a `mods` folder for step 1

`docker compose build`

`docker compose up`

The stack will be created and you can close it when it start failing due to incorrect user credentials

## Step 1 (installation) : Prepare folder structure

- Copy each mod folder and place them in the newly created `mods` folder


run the python script with `python rename_mods.py` in order to rename each folder with lowercase.


## Step 2 (installation) : Modify env variable

You need to setup Steam credentials.
Put username (without "") and password in the correct places inside the `.env` file

## Step 3 (installation) : Port forwarding

If you want to play online ensure your Ports `2302` and `2303` are forwarded

## Step 4 (installation) : Relaunch the server

`docker compose up`

## Step 5 (installation) : Run and enjoy
