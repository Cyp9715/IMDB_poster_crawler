# Python-IMDB-WebCrawler
IMDB reviews web crawler with Python

If you don't use Korean, use Google Translator.

It's not hard, Personally, I do not feel much value in translating.(Only this repo)

# 1. 권장 사양

#### 1) 멀티프로세싱을 이용해 해당 소스를 구동하는데 있어 다음과 같은 사양을 권장합니다.

  1. 충분한 인터넷 속도 (Half Giga, Giga LAN)
  2. CPU (4 Core / 8 Thread)
  3. RAM (16GB / Vitual 40GB)
  4. 여유 저장 공간

#### 2) 멀티프로세싱을 사용하지 않는다면 다음과 같은 최소 사양이 권장됩니다.

  1. 인터넷 속도 (100Mb)
  2. CPU (2 core / 2 Thread)
  3. RAM (4GB)
  4. 여유 저장 공간
  
#### 3) Linux, Windows 10 에서 모두 사용 가능 합니다.

  1. 해당 코드는 Python 3.7 (Anaconda Interpreter) 버전에서 검증 하였습니다.
  2. Windows 10 의 경우 Chrome 버전과, Chrome 드라이버의 버전을 같이 맞춰 주세요.
  3. Linux 의 경우 Chromium 버전과, Chrome 드라이버의 버전을 같이 맞춰 주세요.


# 2. 필요한 재료

해당 소스를 구동하기 위해 다음과 같은 것이 필요합니다.

  1. Chrome Driver
  2. IMDB Movie code number
  
IMDB 코드 번호의 경우, Enter(\n) 으로 구분되거나, .tsv 파일 형식, .csv 파일 형식 모두 상관 없습니다.

하지만 최종적으로 각 IMDB 영화 코드 번호가 (\n) 으로 구분되어 있어야 합니다.


# 3. 출력 값

#### 1) IDE 에서의 출력 값입니다.

![pycharm output](https://user-images.githubusercontent.com/16573620/68953770-f1095200-0805-11ea-9a51-14da2e94328b.png)

Pycharm 내에서 다음과 같이 출력됩니다.

[crawling 성공한 IMDB Code Number | 현재까지 진행된 크롤링 리뷰 / 총 크롤링 할 리뷰 수 | 진행률]

#### 2) File 저장 방식

파일에는 다음과 같은 정보들이 Tsv 형식으로 저장 됩니다.

  1. 리뷰별 평점
  2. 리뷰별 유저 ID
  3. 리뷰별 리뷰 제목
  4. 리뷰별 리뷰 내용

즉 다음과 같이 저장됩니다.

![save](https://user-images.githubusercontent.com/16573620/68954724-f23b7e80-0807-11ea-84d3-7a40fa7cbee9.png)

# 4. 알아둬야 할 사안.

#### 1) IMDB 내 보이는 총 영화 리뷰 수는 정확하지 않습니다.

  영화 [Bad Boys](https://www.imdb.com/title/tt0085210/reviews?ref_=tt_ov_rt) 의 총 리뷰 수는 57개 라고 표기되어 있지만, 

  실제로 세어 보거나, 옵션을 활용해 숫자를 해아려 보면 56개로 하나 부족한것을 알 수 있습니다

  때문에 실제 저장되는 크롤링 리뷰 수는 **[56개로, 이는 정상]** 입니다.

  2019-11-16

#### 2) 평점 0점은 해당 리뷰의 평점이 존재하지 않는다는 것을 의미합니다.

  IMDB의 리뷰 점수는 1~10점 까지 존재합니다.

  그런데, 간혹 리뷰중 평점이 존재하지 않는 리뷰가 존재합니다.

  그런 리뷰들의 빈 공간을 채우기 위해 0점으로 표기 하였습니다.

  즉 0점 = 낮은평점이 아닌, [**0점 = Null 값 입니다.**]

#### 3) 권장 사양을 표기한 이유

  인터넷 속도가 부족하다면 중간에 페이지 [Read-More] 버튼을 인식하는 과정에서 크롤링이 끊어져, 

  일부 데이터만 가져오게 될 수 있습니다.

  때문에 인터넷 페이지 다운로드 속도를 감안하여 멀티프로세싱 숫자를 결정 하는것을 권장 드립니다.

  이에대한 소스코드의 개선을 허용합니다. [Cypher9715@naver.com]

#### 4) 중간에 프로그램을 강제로 종료하게 되면 크롬 드라이버가 메모리에 잔재하게 됩니다.

  추후 작업에서 이 쓸모없는 크롬 드라이버들이 메모리와, CPU 자원을 소모하게 되므로,

  이를 제거하는것을 권장 드립니다.

  추후 이를 간편히 제거할 수 있는 .bat 파일을 배포 하겠습니다.

