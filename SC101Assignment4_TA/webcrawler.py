"""
File: webcrawler.py
Name: Jia-Hong GUO (Ryan Kuo)
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        names = soup.find_all('tr')
        count_boy = 0
        count_girl = 0
        for name in names:
            tags = name.find_all('td')
            if len(tags) == 5:
                # get the target figures
                count_boy += int(tags[2].text.replace(',', ''))
                count_girl += int(tags[4].text.replace(',', ''))
        print('---------------------------')
        print(year)
        print(f'Male Number: {count_boy}')
        print(f'Female Number: {count_girl}')


if __name__ == '__main__':
    main()
