import time
import pytest
from POM.BasePage import BasePage
from conftest import setup


@pytest.mark.usefixtures("setup")
class Test_Population:
    def test_live_population(self, setup):
        page = BasePage(setup)
        page.open()
        print("Press CTRL + C to stop the Live Population count.")
        try:
            while True:
                live_population = page.get_population()
                print(f"Live World Population: {live_population}")
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopped by user (Ctrl + C).")
