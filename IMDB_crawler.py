from selenium import webdriver
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool, Value


# specify the location of file or variable, You don't have to do anything...
cromdriver_location = './Basic_Data/chromedriver'
tconstfile_location = './Basic_Data/Movie_Genres.tsv'
savefile_location = './IMDB_review_crawling2/'
errorfile_location = './IMDB_review_crawling2/Error.tsv'
multiprocess_count = 24


# 사용 변수
T_const = []
driver = webdriver
Star, User, Title, Content = [], [], [], []
counter = None

class Base:
    def init(self, temp):
        global counter
        counter = temp

    def tconst_list(self):
        T_const_Temp = []

        with open(tconstfile_location) as f:
            for line in f:
                T_const_Temp.append(line[:9])
            for i in range(T_const_Temp.__len__()):
                temp = str(T_const_Temp[i])
                temp = temp.replace('\n', '').replace("\"", '')
                T_const.append(temp)
            return T_const


# Preprocessing 클래스가 인스턴스로 선언 될 때마다 __init__ 이 실행됩니다.
# tidied = [] 변수로 초기화 하는 과정을 거쳐야 trash_remove, trash_remove_Star의 동작이 따로 작동합니다,
# 만약 이 과정을 거치지 않으면 append에 Star,Title,Content 의 정보가 혼재되어 프로그램이 정상작동하지 않습니다.
class Preprocessing:
    def __init__(self):
        self.tidied = []

    def trash_remove(self, inputArray):
        for i in range(inputArray.__len__()):
            temp = str(inputArray[i])
            temp = temp.replace('**SPOILER ALERT**', '').replace('**Spoilers alert**', '').replace('\n', '')
            self.tidied.append(temp)
        return self.tidied

    def trash_remove_star(self, inputArray):
        for i in range(inputArray.__len__()):
            temp = str(inputArray[i])
            temp = temp.replace("/10", '')
            self.tidied.append(temp)
        return self.tidied


class Crawler:
    def click(self):
        while True:
            try:
                time.sleep(5)
                driver.find_element_by_xpath("//*[@id='load-more-trigger']").click()
            except:
                break;

        return driver

    def find_web(self, driver):
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        reviews = soup.find_all('div', class_='review-container')

        for review in reviews:
            rating = review.find('span', class_='rating-other-user-rating')
            if rating:
                rating = ''.join(i.text for i in rating.find_all('span'))
            rating = rating if rating else '0'
            Star.append(rating)
            Title.append(review.find('a', class_='title').text.strip())
            User.append(review.find('span', class_='display-name-link').text)
            Content.append(review.find('div', class_='content').div.text)


def start(i):
    global Star
    global User
    global Title
    global Content
    global driver
    global counter

    # The [While True] is for resolving intermittent Chrome driver errors.
    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument("disable-gpu")
            driver = webdriver.Chrome(executable_path=cromdriver_location, chrome_options=options)
            driver.get('https://www.imdb.com/title/' + str(T_const[i]) + '/reviews?ref_=tt_ov_rt')

            Craw = Crawler()
            Craw.find_web(Craw.click())
            Star = Preprocessing().trash_remove_star(Star)
            Title = Preprocessing().trash_remove(Title)
            Content = Preprocessing().trash_remove(Content)

            write = (savefile_location + str(T_const[i]) + ".tsv")
            with open(write, 'w', encoding='utf-8') as s:
                for row in range(Star.__len__()):
                    s.write(Star[row])
                    s.write("\t")
                    s.write(User[row])
                    s.write("\t")
                    s.write(Title[row])
                    s.write("\t")
                    s.write(Content[row])
                    s.write("\n")

            Star.clear()
            User.clear()
            Title.clear()
            Content.clear()
            driver.quit()

            break

        except:
            print("Error!!" + T_const[i])
            write_error = errorfile_location
            with open(write_error, 'a', encoding='utf-8') as e:
                e.write(T_const[i])
                e.write("\n")

    print(T_const[i] + " | " + str(counter.value) + "/" + str(T_const.__len__()) + " | " + str(
        round(counter.value / T_const.__len__() * 100, 3)) + "%")
    counter.value += 1


base = Base()
T_const = base.tconst_list()

if __name__ == '__main__':
    counter = Value('i', 1)
    pool = Pool(initializer=base.init, initargs=(counter,), processes=multiprocess_count)
    pool.map(start, range(0, T_const.__len__()))
