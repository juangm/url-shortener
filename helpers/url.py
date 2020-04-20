from urllib.parse import urlparse
import validators


class UrlHelper:

    def __init__(self):
        # Load the possible combinations
        self.base_domain = 'https://www.applau.se/'
        self.combinations = []

    def get_domain(self, input_url):
        """Method to get the domain of the url"""
        # Check the input is a valid URL
        if validators.url(input_url):
            return urlparse(input_url).netloc
        else:
            print("x Invalid URL please introduce a valid URL")
            print("(for example: https://www.example.com/path")
            return False

    def generate_short_url(self, position):
        """Generate shorten url based in index"""
        return self.base_domain + self.combinations[position]
