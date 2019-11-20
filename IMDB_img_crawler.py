import urllib.request
from multiprocessing import Pool, Value, Lock
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.parse

T_const = []
driver = webdriver

class Base:
    def Tconst_List(self):
        with open('./Basic_Data/Movie_Genres.tsv') as f:
            for line in f:
                T_const.append(line[:9])
            return T_const

    def init(self, temp):
        global counter
        counter = temp

    def counter_plus(self):
        with counter.get_lock():
            counter.value += 1


def crawling(number):
    global counter
    global T_const
    global driver

    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('disable-gpu')
            driver = webdriver.Chrome(executable_path=r'./Basic_Data/chromedriver', chrome_options=options)
            driver.get("https://www.imdb.com/title/" + T_const[number])
            driver.implicitly_wait(2)
            driver.find_element_by_class_name("poster").click()
            url = driver.find_element_by_xpath(
                "// *[ @ id = \"photo-container\"] / div / div[3] / div / div[2] / div[1] / div[2] / div / img[2]").get_attribute(
                "src")
            urllib.request.urlretrieve(url, "./IMDB_img/" + T_const[number] + ".jpg")
            base.counter_plus()
            print(T_const[number] + " | " + str(counter.value) + "/" + str(T_const.__len__()) + " | " +
                  str(round(counter.value / T_const.__len__() * 100, 3)) + "%")
            break

        # 포스터 이미지 자체가 없을때 뜨는 에러 메세지.
        except NoSuchElementException:
            link = urllib.parse.quote("www.imdb.com/title/" + T_const[number])
            print(("-" * 75) + "\n" + T_const[number] +
                  " | NoSuchElementExcpetion, make sure "
                  "Website have a poster image." +
                  "\n" + "https://" + link + "\n" + ("-" * 75))
            base.counter_plus()
            break

        except:
            print(T_const[number])

        finally:
            driver.quit()


base = Base()
counter = Value('i', 0)
base.Tconst_List()

if __name__ == '__main__':
    pool = Pool(initializer=base.init, initargs=(counter,), processes=8)
    pool.map(crawling, range(0, T_const.__len__()))
