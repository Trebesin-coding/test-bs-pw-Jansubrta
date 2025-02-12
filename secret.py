from playwright.sync_api import sync_playwright
import os

Login = "Jarmil"
Heslo ="Admin123"



def main():

     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page= browser.New_page
        page.goto("https://js-trebesin.github.io/playwright-exam/")

        page.fill("INPUT[id='Login']"Login)
        page.fill("INPUT[id='Heslo']"Heslo)
        page.click("botton[type = 'submit']")

        # !!!
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!


        browser.close()
    

if __name__ == "__main__":
    main()
