from helpers.url import UrlHelper

import pytest


class TestUrlHelper:

    @pytest.fixture
    def url_helper(self):
        return UrlHelper()

    @pytest.mark.parametrize("not_urls", [("www.asdf.asdf.com/asdf"), (""), ("www.google.com")])
    def test_check_not_valid_url(self, url_helper, not_urls, capsys):
        assert url_helper.check_domain(not_urls) == False
        captured = capsys.readouterr()
        assert captured.out == """x Invalid URL please introduce a valid URL\n--- for example: https://www.example.com/path\n"""

    @pytest.mark.parametrize("not_short_urls", [("https://www.applau.se/gfa"), ("https://www.applau.se/a"), ("https://www.applau.se/f@")])
    def test_check_not_valid_short_url(self, url_helper, not_short_urls, capsys):
        assert url_helper.check_domain(not_short_urls) == False
        captured = capsys.readouterr()
        assert captured.out == """x Invalid URL to get original URL\n--- for example: https://www.applau.se/gf\n"""

    def test_valid_url(self, url_helper):
        assert url_helper.check_domain(
            "http://www.google.com/asdfoweira") == "to_short"

    @pytest.mark.parametrize("valid_short", [("https://www.applau.se/gF"), ("https://www.applau.se/a2"), ("https://www.applau.se/Fd"), ("https://www.applau.se/34")])
    def test_valid_short_url(self, url_helper, valid_short):
        assert url_helper.check_domain(valid_short)

    def test_short_url_generation(self, url_helper):
        assert url_helper.generate_short_url(
            5) == ['https://www.applau.se', 'af']

    def test_short_url_generation_invalid_input(self, url_helper):
        assert url_helper.generate_short_url('asdf') == False
