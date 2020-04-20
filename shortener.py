from helpers.sqlite import Sqlite3Helper
from helpers.url import UrlHelper
from cmd import Cmd


class UrlShortenerInteractive(Cmd):
    sql_helper = Sqlite3Helper()
    url_helper = UrlHelper()
    user = None
    prompt = "URL shortener => "

    def preloop(self):
        print("== Welcome to url-shortener ==")
        print("Select the type of user [admin, normal]")
        self.user = input("user => ")

    def do_exit(self, inp):
        """ Exits the program """
        print("Thanks for using our URL shortened!!")
        return True

    def do_url(self, inp):
        """ Introduce an URL for shorting or unshorting """
        input_url = input("Introduce the url to short or unshort => ")
        operation = self.url_helper.check_domain(input_url)
        if operation == 'to_short':
            # Check if URL doesn't exist in DB
            url = self.sql_helper.search_url(input_url)
            if url != []:
                print("URL is already in DB!!")
                print("short url associated => {}".format(url[2]))
                return False
            index = self.sql_helper.count_urls_stored()
            if index == self.url_helper.max_combinations:
                # Update last visit url
                url = self.sql_helper.update_latest_visit(input_url)
                print("The short URL is => {}".format(url[2]))
            else:
                short = self.url_helper.generate_short_url(index)
                self.sql_helper.input_new_url(input_url, short[1])
                print("The short URL is => {}/{}".format(short[0], short[1]))
        elif operation == 'to_unshort':
            original_url = self.sql_helper.search_short_path(input_url[-2:])
            if original_url == []:
                print("Short URL not found in DB!!")
                return False
            self.sql_helper.update_short_url(input_url[-2:])
            print("Original URL => {}".format(original_url[2]))

    def do_setup_db(self, inp):
        """ Create table in DB and erase all data if table exists
            Only for Admin users! """
        if self.user == 'admin':
            print("Creating table in DB")
            self.sql_helper.setup_db()
        else:
            print('Sorry this option is only for Admins')

    def do_show_db(self, inp):
        """ Display all the values in DB order by count
            Only for Admin users! """
        if self.user == 'admin':
            self.sql_helper.admin_get_all_urls()
        else:
            print('Sorry this option is only for Admins')


if __name__ == "__main__":
    sql_helper = Sqlite3Helper()

    count = sql_helper.count_urls_stored()
    print(count)

    url_interact = UrlShortenerInteractive()
    url_interact.cmdloop()

    print("after")
