from playwright.sync_api import sync_playwright
import os

Login = "Jarmil"
Heslo ="Admin123" 
# U: Proměnné píšeme malými písmeny



def main():

     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page= browser.New_page # U: dodržujte správné názvy funkcí! new_page()
        page.goto("https://js-trebesin.github.io/playwright-exam/")

        page.fill("INPUT[id='Login']"Login) # U: chybí čárky mezi argumenty! Proč je input capslockem?
        page.fill("INPUT[id='Heslo']"Heslo) # U: chybí čárky mezi argumenty!
        page.click("botton[type = 'submit']")

        # !!!
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!


        browser.close()
    

if __name__ == "__main__":
    main()
