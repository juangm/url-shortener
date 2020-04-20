from urllib.parse import urlparse

import json
import validators


class UrlHelper:

    def __init__(self):
        self.base_domain = 'www.applau.se'
        self.combinations = None
        # Load the possible combinations
        with open('combinations/encoding.json') as f:
            self.combinations = json.load(f)
        self.max_combinations = len(self.combinations)

    def check_domain(self, input_url):
        """Method to detect if url needs to be shorted or return original"""
        # Check the input is a valid URL
        if validators.url(input_url):
            url_parsed = urlparse(input_url)
            if self.base_domain in url_parsed.netloc:
                # Check path doesn't contains more than 2 characters
                if len(url_parsed.path) != 3:
                    print("x Invalid URL to get original URL")
                    print("--- for example: https://www.applau.se/gf")
                else:
                    return 'to_unshort'
            else:
                return 'to_short'
        else:
            print("x Invalid URL please introduce a valid URL")
            print("--- for example: https://www.example.com/path")
            return False

    def generate_short_url(self, position):
        """Generate shorten url path based in index"""
        return ['https://{}'.format(self.base_domain), ''.join(self.combinations[position])]
