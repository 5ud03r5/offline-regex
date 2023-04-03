# Offline regex test

Offline Regex Test is a simple web app that allows you to test regular expressions against sample text. It's a great tool for developers, analysts and engineers who need to quickly validate regular expressions without having to connect to a server or write complex code.

It also have posibility to save regex into your own repository, tag this regex, and search repository so you can easily access it.

## Installation

Offline regex tool requires you to have docker installed on your workstation. First clone git repository, then run following command from root project directory:

    docker compose up 

It will run docker containers (backend and frontend) and migrate database

# How to use

To run your first regex go to Tester page and create one:

![image](https://user-images.githubusercontent.com/94323029/229560919-d39ac79a-7561-493a-a4c2-eff0c1e11653.png)

Click Save button to save. You can tag your regex while saving it.
After creation you can navigate to Registry page to easily find your regex either by clicking on a tag or typing in search:

![image](https://user-images.githubusercontent.com/94323029/229377210-05ad2bf4-057d-46cc-9130-a1f87fa0b11c.png)

You can also click on Try it button to go back to Tester page with prefilled fields for typed regex.

There is a way to export capturing groups to JSON/CSV/Text. To do it you need to click export groups button in Match information block and choose option which you wanna use. Next you can copy to clipboard in preffered format:

![image](https://user-images.githubusercontent.com/94323029/229561381-6812f5a4-0ac1-44cc-9bca-f5182d949a1f.png)


