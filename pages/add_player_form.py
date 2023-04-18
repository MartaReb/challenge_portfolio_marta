import time

from pages.base_page import BasePage

class AddPlayerForm(BasePage):
    expected_title = "Add player"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title


pass