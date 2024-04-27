import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.python.org/")
        time.sleep(1)

    def test_case_01_meta_info(self):
        self.assertEqual("Welcome to Python.org", self.driver.title)

        meta_keywords = self.driver.find_element(By.XPATH, "//meta[@name='keywords']")
        keywords_content = meta_keywords.get_attribute("content")
        expected_content = "Python programming language object oriented web free open source software license documentation download community"
        self.assertEqual(expected_content, keywords_content)

    def test_02_menu1(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "#top > nav > ul > li")
        self.assertGreater(len(menu_items), 0)

    def test_03_menu1_links(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "#top > nav > ul > li")
        self.assertIn("Python", menu_items[0].text)
        self.assertIn("PSF", menu_items[1].text)
        self.assertIn("Docs", menu_items[2].text)
        self.assertIn("PyPI", menu_items[3].text)
        self.assertIn("Jobs", menu_items[4].text)
        self.assertIn("Community", menu_items[5].text)

    def test_04_menu2(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "#mainnav > ul > li")
        self.assertGreater(len(menu_items), 0)

    def test_05_menu2_links(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "#mainnav > ul > li")
        self.assertIn("About", menu_items[0].text)
        self.assertIn("Downloads", menu_items[1].text)
        self.assertIn("Documentation", menu_items[2].text)
        self.assertIn("Community", menu_items[3].text)
        self.assertIn("Success Stories", menu_items[4].text)
        self.assertIn("News", menu_items[5].text)
        self.assertIn("Events", menu_items[6].text)

    def test_case_06_footer(self):
        footer_menu = self.driver.find_elements(By.CSS_SELECTOR, "#site-map > div.main-footer-links > div.container > ul > li")
        self.assertGreater(len(footer_menu), 0)

    def test_case_07_footer_links(self):
        footer_menu = self.driver.find_elements(By.CSS_SELECTOR, "#site-map > div.main-footer-links > div.container > ul > li")
        self.assertIn("About", footer_menu[0].text)
        self.assertIn("Downloads", footer_menu[1].text)
        self.assertIn("Documentation", footer_menu[2].text)
        self.assertIn("Community", footer_menu[3].text)
        self.assertIn("Success Stories", footer_menu[4].text)
        self.assertIn("News", footer_menu[5].text)

    def test_case_08_search_found(self):
        search_field = self.driver.find_element(By.ID, "id-search-field")
        self.assertTrue(search_field)
        search_field.send_keys("Python")
        search_field.send_keys(Keys.RETURN)
        time.sleep(3)
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "ul.list-recent-events.menu > li")
        self.assertGreater(len(search_results), 0)

    def test_case_09_search_not_found(self):
        search_field = self.driver.find_element(By.ID, "id-search-field")
        self.assertTrue(search_field)
        search_field.send_keys("Weirdtextthatwontbefound")
        search_field.send_keys(Keys.RETURN)
        time.sleep(3)
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "ul.list-recent-events.menu > li")
        self.assertEqual(len(search_results), 0)

    def test_10_shell_button(self):
        time.sleep(1)
        start_shell_button = self.driver.find_element(By.ID, "start-shell")
        self.assertIsNotNone(start_shell_button)
        self.assertEqual(start_shell_button.text, ">_")
        start_shell_button.click()
        time.sleep(5)
        console = self.driver.find_element(By.ID, "dive-into-python")
        self.assertTrue(console is not None)

    def test_11_slider(self):
        slider_items = self.driver.find_elements(By.CSS_SELECTOR, ".flex-slideshow.slideshow .slides.menu li")

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slide-copy h1")))
        self.assertEqual(slider_items[0].find_element(By.CSS_SELECTOR, ".slide-copy h1").text, "Functions Defined")

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slides.menu li:nth-child(2) .slide-copy h1")))
        self.assertEqual(slider_items[1].find_element(By.CSS_SELECTOR, ".slide-copy h1").text, "Compound Data Types")

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slides.menu li:nth-child(3) .slide-copy h1")))
        self.assertEqual(slider_items[2].find_element(By.CSS_SELECTOR, ".slide-copy h1").text, "Intuitive Interpretation")

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slides.menu li:nth-child(4) .slide-copy h1")))
        self.assertEqual(slider_items[3].find_element(By.CSS_SELECTOR, ".slide-copy h1").text, "All the Flow You’d Expect")

        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slides.menu li:nth-child(5) .slide-copy h1")))
        self.assertEqual(slider_items[4].find_element(By.CSS_SELECTOR, ".slide-copy h1").text, "Quick & Easy to Learn")


    def test_12_highlighted_menu(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "#top > nav > ul > li")
        is_highlighted = "active" in menu_items[0].get_attribute("class")
        if is_highlighted:
            self.assertEqual("Python", menu_items[0].text)

    def test_13_menu1_navigation(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "#top > nav > ul > li")
        menu_items[1].click()
        time.sleep(2)
        current_url_after_click = self.driver.current_url
        expected_url = "https://www.python.org/psf-landing/"
        self.assertEqual(current_url_after_click, expected_url)

    def test_14_menu2_display(self):
        about_menu = self.driver.find_element(By.ID, "about")
        sub_menu = self.driver.find_element(By.CSS_SELECTOR, "#about ul.subnav")
        self.assertFalse(sub_menu.is_displayed())

        action = ActionChains(self.driver)
        action.move_to_element(about_menu).perform()
        time.sleep(2)

        self.assertTrue(sub_menu.is_displayed())

    def test_15_donate_button(self):
        donate_button = self.driver.find_element(By.LINK_TEXT, "Donate")
        donate_button.click()
        time.sleep(2)
        current_url_after_click = self.driver.current_url
        expected_url = "https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2"
        self.assertEqual(current_url_after_click, expected_url)

    def test_16_socialize_menu(self):
        socialize_menu = self.driver.find_element(By.LINK_TEXT, "Socialize")
        actions = ActionChains(self.driver)
        actions.move_to_element(socialize_menu)
        actions.perform()

        linkedin_option = self.driver.find_element(By.LINK_TEXT, "LinkedIn")
        mastodon_option = self.driver.find_element(By.LINK_TEXT, "Mastodon")
        irc_option = self.driver.find_element(By.LINK_TEXT, "Chat on IRC")
        twitter_option = self.driver.find_element(By.LINK_TEXT, "Twitter")
        self.assertTrue(linkedin_option.is_displayed())
        self.assertTrue(mastodon_option.is_displayed())
        self.assertTrue(irc_option.is_displayed())
        self.assertTrue(twitter_option.is_displayed())

    def test_17_hover_color_change(self):
        applications_link = self.driver.find_element(By.XPATH, "//footer[@id='site-map']//a[text()='Applications']")
        self.driver.execute_script("arguments[0].scrollIntoView();", applications_link)
        original_background_color = applications_link.value_of_css_property("background-color")
        actions = ActionChains(self.driver)
        actions.move_to_element(applications_link)
        actions.perform()
        hovered_background_color = applications_link.value_of_css_property("background-color")
        self.assertNotEqual(original_background_color, hovered_background_color)

    def test_18_highlighted_menu_hover(self):
        menu_items = self.driver.find_elements(By.CSS_SELECTOR, "#top > nav > ul > li > a")
        original_background_color = menu_items[1].value_of_css_property("background-color")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu_items[1])
        actions.perform()
        hovered_background_color = menu_items[1].value_of_css_property("background-color")
        self.assertNotEqual(original_background_color, hovered_background_color)

    def test_19_hover_about_applications_color_change(self):
        about_option = self.driver.find_element(By.XPATH, "//nav[@id='mainnav']//a[text()='About']")
        actions = ActionChains(self.driver)
        actions.move_to_element(about_option)
        actions.perform()
        applications_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[@id='about']//ul[@class='subnav menu']//a[text()='Applications']")))
        original_background_color = applications_option.value_of_css_property("background-color")
        actions.move_to_element(applications_option)
        actions.perform()
        applications_option = self.driver.find_element(By.XPATH,"//li[@id='about']//ul[@class='subnav menu']//a[text()='Applications']")
        hovered_background_color = applications_option.value_of_css_property("background-color")
        self.assertNotEqual(original_background_color, hovered_background_color)

    def test_20_django_button(self):
        django_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='tag-wrapper']//a[text()='Django']")))
        self.assertTrue(django_button)
        django_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("djangoproject"))
        self.assertIn("djangoproject", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()