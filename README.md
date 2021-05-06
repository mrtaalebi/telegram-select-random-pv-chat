# telegram-select-random-pv-chat
A telegram client app, using telethon to randomly select a pv to chat. You may use it when you need someone to send messages to but don't know who.


## About Telethon and Telegram client API
You may know about telegram bots API and how you can programmize them, there's also an API for telegram clients. 
Which you can use by registering an app in telegram developers page and then make calls to telegram servers. 
These APIs allow the code to do everything you can normally do with telegram apps and more (list of all contacts, send messages to anyone, ...).

Telethon is just a library in python that makes calling those APIs much easier


## Usage
- first of all register a telegram client app following instruction in [this page](https://core.telegram.org/api/obtaining_api_id)
  - copy `.env.sample` file to `.env` file
  - enter `api_id` and `api_hash` of the app you created, along with your `phone_number` in `.env` file, or enter them directly at the top of the code
  - it's better if you don't share these two keys with anyone
- you may create and enter a virtualenv
- now you can either
  - use `make all` for the first time and `make run` for the future runs
  - or enter the commands listed in the `Makefile` manualy (it's nothing complicated or long)


## Further usage
This code is just an example and you can use telegram client api (with telethon if your choice of language is python) to do a lot of crazy things!
