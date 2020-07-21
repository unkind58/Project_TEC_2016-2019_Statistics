from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def komandos_rungtynes():
    team_games = driver.find_element_by_link_text('Komandos rungtynės')
    return team_games.click()

def rungtyniu_skaicius():
    games_quantity = len(driver.find_elements_by_xpath('//*[@id="rungtynes"]/table/tbody/tr'))
    return games_quantity

def rungtynes():
    part_one = '//*[@id="rungtynes"]/table/tbody/tr['
    part_two = ']/td[6]/a'
    counter_games = 1

    for r in range(2, rungtyniu_skaicius() + 1):
        try:
            game = driver.find_element_by_xpath(part_one + str(r) + part_two)
            game.click()
            game_squad = driver.find_element_by_link_text('Komandų sudėtys')
            game_squad.click()
        except NoSuchElementException:
            pass

        row_count = len(driver.find_elements_by_xpath('//*[@id="sudetys"]/div/div[2]/div'))
        first_part = '//*[@id="sudetys"]/div/div[2]/div['
        second_part = ']'
        counter_squad = 0
        for i in range(2, row_count + 1):
            final_path = first_part + str(i) + second_part
            table_data = driver.find_element_by_xpath(final_path).text
            with open('Scrapping_text.txt', "a+", encoding="utf-8") as f:
                if counter_squad < 12:
                    counter_squad += 1
                    f.write(table_data + ' [startas]' + '\n')
                else:
                    f.write(table_data + '\n')
        with open('Scrapping_text.txt', "a+", encoding="utf-8") as f:
            f.write('# ' + str(counter_games) + ' #' + '\n')
        counter_games += 1
        driver.back()
        driver.refresh()
        komandos_rungtynes()

    return print('Viso sužaista ' + str(rungtyniu_skaicius() - 1) + ' rungtynių(-ės)')


if __name__ == "__main__":
    chrome_driver = r"D:\Python\Scraping\chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)
    driver.get(r'http://www.vilniausfutbolas.lt/komanda/FK-TEC/62/1/22')
    komandos_rungtynes()
    rungtynes()
