# telegram-select-random-pv-chat
A telegram client app, using telethon to randomly select a pv to chat. You may use it when you need someone to send messages to but don't know who.

## About Telethon and Telegram client API
You may know about telegram bots API and how you can programmize them, there's also an API for telegram clients. 
Which you can use by registering an app in telegram developers page and then make calls to telegram servers, 
with client level access (list of all contacts, send messages to anyone, ...) with the `api_id` and `api_hash` telegram gives you.


## Usage
- first of all register a telegram client app following instruction in [this page](https://core.telegram.org/api/obtaining_api_id)
  - enter `api_id` and `api_hash` of the app you created, along with your `phone_number` in `.env` file, or enter them directly at the top of the code
  - it's better if you don't share these two keys with anyone
- you may create and enter a virtualenv
- now you can either
  - use `make all` for the first time and `make run` for the future runs
  - or enter the command in the `Makefile` manualy (it's nothing complicated)
