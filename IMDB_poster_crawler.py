import urllib.request
from multiprocessing import Pool, Value, Lock
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.parse

# specify the location of file or variable, You don't have to do anything...
cromdriver_location = './Basic_Data/chromedriver'
tconstfile_location = './Basic_Data/Movie_Genres.tsv'
savefile_location = './IMDB_img/'
errorfile_location = './IMDB_img/error.tsv'


# 이곳에서 할당을 안 하기에 T_const global 을 선언 해 주지 않아도 오류가 나지 않는다. 만약 할당을 해 준다면 오류가 발생할 것이다.
class Base:
    def Tconst_List(self):
        global T_const
        with open(tconstfile_location) as f:
            for line in f:
                T_const.append(line[:9])
            return T_const

    def init(self, temp):
        global counter
        counter = temp

    def counter_plus(self, number, classify):
        global counter
        global T_const

        link = urllib.parse.quote("www.imdb.com/title/" + T_const[number])

        with counter.get_lock():
            counter.value += 1
            output = (T_const[number] + " | " + str(counter.value) + "/" + str(T_const.__len__()) + " | " +
                      str(round(counter.value / T_const.__len__() * 100, 3)) + "%") \
                if classify == 0 else (("-" * 75) + "\n" + T_const[number] + " | NoSuchElementException, make sure "
                    "Website have a poster image." + "\n" + "https://" + link + "\n" + ("-" * 75))
            print(output)


def crawling(number):
    global counter
    global T_const
    global driver

    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('disable-gpu')
            driver = webdriver.Chrome(executable_path=cromdriver_location, chrome_options=options)
            driver.get("https://www.imdb.com/title/" + T_const[number])
            driver.implicitly_wait(2)
            driver.find_element_by_class_name("poster").click()
            url = driver.find_element_by_xpath(
                "// *[ @ id = \"photo-container\"] / div / div[3] / div / div[2] / div[1] / div[2] / div / img[2]").get_attribute(
                "src")
            urllib.request.urlretrieve(url, savefile_location + T_const[number] + ".jpg")
            base.counter_plus(number, 0)
            break

        # 포스터 이미지 자체가 없을때 뜨는 에러 메세지.
        except NoSuchElementException:
            write_error = errorfile_location
            link = urllib.parse.quote("www.imdb.com/title/" + T_const[number])

            with open(write_error, 'a', encoding='utf-8') as e:
                e.write((("-" * 75) + "\n" + T_const[number] +
                         " | NoSuchElementException, make sure "
                         "Website have a poster image." +
                         "\n" + "https://" + link + "\n" + ("-" * 75)))
                e.write("\n")

            base.counter_plus(number, 1)
            break

        except:
            print("Retry!!" + T_const[number])
            write_error = errorfile_location
            with open(write_error, 'a', encoding='utf-8') as e:
                e.write("Retry : " + T_const[number])
                e.write("\n")

        finally:
            driver.quit()


T_const = []

driver = webdriver
counter = Value('i', 0)

base = Base()
base.Tconst_List()

if __name__ == '__main__':
    pool = Pool(initializer=base.init, initargs=(counter,), processes=8)
    pool.map(crawling, range(0, T_const.__len__()))
