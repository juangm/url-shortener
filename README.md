# Project: url-shortener

## Description

Small python project for URL shortener

## Requirements

- [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
- [Sqlite](https://www.sqlite.org/index.html)
- Install python packages dependencies `pip3 install -r requirements.txt`

## Specifications

- [ ] Shorten a URL:

  - [x] Input: A regular URL (not from applau.se domain)
  - [x] Output: A shortened URL (use only ten digits, 26 lowercase characters, 26 uppercase characters) of extra length 2 from a given link example: applau.se/5s)
  - [ ] Handle the case that the 2-character length is running out of choices by retiring the shortened URL that has not been called for the longest time

- [x] Retrieve a URL:

  - [x] Input: A shortened URL (from applau.se domain)
  - [x] Output: Retrieve the original URL

- [x] Basic admin:

  - [x] Show all stored shortened URLs (including shortened URL, original URL, call count and latest call time) and sort by call count

## Future improvements

- [ ] Implement login system with password for the admin service
- [ ] Add tests for checking the specs are not being broken when implementing new features
- [ ] Create a CI to run the tests
- [ ] Implement small web application for the user interface
