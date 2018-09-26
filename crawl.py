import urllib.request
import sqlite3

from bs4 import BeautifulSoup

# original git = https://github.com/SerenityS/kakaobot_hyoammeal

# 이용할 학교 정보 설정
regioncode = 'gne.go.kr'
schulcode = 'S100000492'

# Tuple
day = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat']
meal = ['', '', '', '', '', '', '일요일은 학교를 안갑니다.']

# Crawling Code
sccode = 1
while sccode < 4:
    # NEIS에서 주간 급식 파싱
    url = ('http://stu.' + regioncode + '/sts_sci_md01_001.do?schulCode=' + schulcode + '&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=' + str(sccode))
    try:
        source = urllib.request.urlopen(url, timeout=3)
    except Exception as e:
        print(e)
        menu = ('서버에 문제가 발생하였습니다.\n빠른 시일 내에 수정하겠습니다.')
    else:
        # beautifulsoup4를 이용해 utf-8, lxml으로 파싱
        soup = BeautifulSoup(source, "lxml", from_encoding='utf-8')

        # div_id="contents"안의 table을 모두 검색 후 td태그만 추출
        table_div = soup.find(id="contents")
        tables = table_div.find_all("table")
        menu_table = tables[0]
        td = menu_table.find_all('td')

        today = 0
        while today < 6:
            # 월요일 ~ 토요일 = td[8] ~ td[13]
            menu = td[today + 8]

            # 파싱 후 불필요한 태그 잔여물 제거 -- 각 학교별로 다른 종류의 태그들이 붙어있을 겁니다. 그것을 파악하시고 ".replace('제거할 태그;', '')" 안에 수정하셔서 아래 줄의 맨 뒤에 붙여주세요.
            menu = str(menu).replace('*', '').replace('amp;', '').replace('<td', "").replace('<br/></td>', "").replace('</td>', '').replace('class="textC last">', '').replace('class="textC">','').replace('<br/>', '\nㆍ').replace('1.', '').replace('2.', '').replace('3.', '').replace('4.', '').replace('5.', '').replace('6.','').replace('7.', '').replace('8.', '').replace('9.', '').replace('10.', '').replace('11.', '').replace('12.', '').replace('13.', '').replace('14.', '').replace('15.', '').replace('1', '').replace(' ', '')

            if menu == '':
                menu = '급식 데이터를 쿼리하지 못했습니다.\n급식을 실시하지 않는 시간대인 것 같습니다.'

            if today != 6:
                if sccode == 2:
                    meal[today] = "#점심메뉴는?\nㆍ" + menu
                elif sccode == 3:
                    meal[today] = meal[today] + "\n\n#저녁메뉴는?\nㆍ" + menu
            today = today + 1
#        # 일부학교에서의 토요일 주간식단 나이스 정보 없음으로 인한 대체문구 표시
#        if today == 5:
#            if sccode == 2:
#                meal[today] = "토요 주간식단은 이 서비스에서 제공되지 않습니다."

    sccode = sccode + 1

# SQL Save
con = sqlite3.connect("database/responder.db")
cur = con.cursor()

check = ("SELECT * FROM meal")
cur.execute(check)
data = cur.fetchone()

if data is None:
    insert = ("INSERT into meal('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun') VALUES (?, ?, ?, ?, ?, ?, ?)")
    cur.execute(insert, meal)
else:
    for i in day:
        update = ("UPDATE meal SET " + i + " = '" + meal[(day.index(i))] + "' WHERE no = 1")
        cur.execute(update)
con.commit()
con.close()
