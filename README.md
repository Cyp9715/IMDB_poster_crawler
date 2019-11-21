# Python-IMDB_Poster_crawler

if you don't use korean, just use Google translator.

this content not hard. personally, I feel not worth translate (only this repo)

# 1. 권장 사양.

#### 1) 멀티 프로세싱의 수를 임의적으로 늘리지 마십시오. 

IMDB 내에서 Get Flooding Attack 으로 오인, IP가 차단될 수 있습니다.

8개의 프로세스를 운영하는 것이 적당한 속도와 안전범위내 동작을 보장합니다.

#### 2) Linux, Windows 10 에서 모두 사용 가능 합니다.

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

#### 1) IDE 에서의 정상 출력 값입니다.

![pycharm output](https://user-images.githubusercontent.com/16573620/68953770-f1095200-0805-11ea-9a51-14da2e94328b.png)

Pycharm 내에서 다음과 같이 출력됩니다.

[crawling 성공한 IMDB Code Number | 현재까지 진행된 크롤링 리뷰 / 총 크롤링 할 리뷰 수 | 진행률]

#### 2) IDE, Error.tsv 파일에서의 에러 출력 값입니다.

![NosuchElement](https://user-images.githubusercontent.com/16573620/69302131-fd553b00-0c5b-11ea-9418-c60ae0906647.png)

해당 에러 출력값은, 포스터가 존재하지 않는 영화에 한해 출력됩니다.

드라마 [General Hospital](https://www.imdb.com/title/tt1032414/) 를 살펴보시면 포스터가 없는 모습을 볼 수 있습니다.

