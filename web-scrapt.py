from bs4 import BeautifulSoup
import requests

username = ""
password = ""
login_data = {
    'username': username,
    'password': password
}


def main():
    with requests.Session() as session:
        session.post("https://tinchi.qnu.edu.vn/Login/index", login_data)
        year_study = session.get("https://tinchi.qnu.edu.vn/ThoiKhoaBieu")
        soup_year_study = BeautifulSoup(year_study.text, 'lxml')

        years_in_soup = soup_year_study.find('select', id="YearStudy")
        years = []

        for option in years_in_soup:
            if "\n" not in option.string:
                years.append(option.string)
        print(years)
        for year in years:
            for HK in {"HK01", "HK02"}:
                payload = {
                    "YearStudy": year,
                    "TermID": HK}

                tkb = session.get(
                    "https://tinchi.qnu.edu.vn/ThoiKhoaBieu/HienthiTKBTheoMon", params=payload)
                if 'td' in tkb.text:
                    with open('index.html', 'a', encoding="utf-8") as file:
                        file.write(tkb.text)

if __name__ == "__main__":
    main()
