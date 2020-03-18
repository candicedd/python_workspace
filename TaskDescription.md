# Task Description

## Architecture

C/S, Client/Server

## Server Function

The server once started, generates a random number in a fixed range periodically. For example, between 1 and 1000 for every 2 second.

The range and interval is configurable when starting the server.

## Client Function

The client monitors the server, and tells the current number generated on server side.

The client keeps a history of the number for a fixed time, e.g., keeps all number for 10 minutes.
