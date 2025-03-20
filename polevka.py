from bs4 import BeautifulSoup
import requests
import json


def main():
    URL = "https://js-trebesin.github.io/bsoup-exam/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    all_p = soup.find_all("p")
    # U: v dokumentu jsou nějaké <p> ?
    list_p = []
    print(list_p)
    # response = requests.get(url)

    # BeautifulSoup(response.content, "html.parser") <--- Úkol: popiš krátce, co tohle dělá zkontroluje jestli jsme připojeni na stranku
    # toto nekontroluje připojení na stránku, ale umožňuje zpracovat její obsah
    for p in all_p:
        list_p.append(p.text)
        print(list_p)
    # U: chybí filtrování správných ingrediencí

    with open("data.json", mode="w") as file:
        json.dump(list_p, file, indent=4)


if __name__ == "__main__":
    main()
