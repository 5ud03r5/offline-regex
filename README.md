# Offline regex test

Offline Regex Test is a simple web app that allows you to test regular expressions against sample text. It's a great tool for developers, analysts and engineers who need to quickly validate regular expressions without having to connect to a server or write complex code.

It also have posibility to save regex into your own repository, tag this regex, and search repository so you can easily access it.

## Installation

Offline regex tool requires you to have docker installed on your workstation. First clone git repository, then run following command from root project directory:

    docker compose up 

It will run docker containers (backend and frontend) and migrate database

# How to use

To run your first regex go to Tester page and create one:

![image](https://user-images.githubusercontent.com/94323029/229377065-94b89b0d-be8f-4c0e-a0ae-98207e79106c.png)

Click Save button to save. You can tag your regex while saving it.
After creation you can navigate to Registry page to easily find your regex either by clicking on a tag or typing in search:

![image](https://user-images.githubusercontent.com/94323029/229377210-05ad2bf4-057d-46cc-9130-a1f87fa0b11c.png)

You can also click on Try it button to go back to Tester page with prefilled fields for typed regex

