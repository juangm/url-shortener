# Project: url-shortener

## Description

Small python project for URL shortener

## :warning: Security Warning

- This program was created for education purposes.
- This program is not protected against :syringe: `sql injection`
  - If the script is added to a web service, the service will filter the inputs to avoid this issue

## Requirements

- [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
- [Sqlite](https://www.sqlite.org/index.html)
- Install python packages dependencies `pip3 install -r requirements.txt`

## Specifications

- [x] Shorten a URL:

  - [x] Input: A regular URL (not from applau.se domain)
  - [x] Output: A shortened URL (use only ten digits, 26 lowercase characters, 26 uppercase characters) of extra length 2 from a given link example: applau.se/5s)
  - [x] Handle the case that the 2-character length is running out of choices by retiring the shortened URL that has not been called for the longest time.

- [x] Retrieve a URL:

  - [x] Input: A shortened URL (from applau.se domain)
  - [x] Output: Retrieve the original URL.

- [x] Basic admin:

  - [x] Show all stored shortened URLs (including shortened URL, original URL, call count and latest call time) and sort by call count.

## Run

To run the url-shortener locally, you just need to install the requirements and execute:

```sh
python3 shortener.py
```

The program has the following options implemented:

- url: provide a url to short or unshort.
- setup_db: create table in DB and erase previous data if table existed before (only admin)
- show_db: show all the data in the urls table (only admin)
- help: help menu.
- exit: exit the program.

## Future improvements

- [ ] Implement login system with password for the admin service.
- [ ] Add tests for checking the specs are not being broken when implementing new features.
- [ ] Create a CI to run the tests.
- [ ] Implement small web application for the user interface.
