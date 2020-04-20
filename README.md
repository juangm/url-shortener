# Project: url-shortener

## Description

Small python project for URL shortener

## Requirements

- [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
- [Sqlite](https://www.sqlite.org/index.html)
- Install python packages dependencies `pip3 install -r requirements.txt`

## Specifications

- Shorten a URL

  - Input: A regular URL (not from applau.se domain)
  - Output: A shortened URL (use only ten digits, 26 lowercase characters, 26 uppercase characters) of extra length 2 from a given link example: applau.se/5s)
  - Handle the case that the 2-character length is running out of choices by retiring the shortened URL that has not been called for the longest time

- Retrieve a URL

  - Input: A shortened URL (from applau.se domain)
  - Output: Retrieve the original URL

- Basic admin
  - Show all stored shortened URLs (including shortened URL, original URL, call count and latest call time) and sort by call count
