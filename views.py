# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from element.papago import translate

import json
import sqlite3
from datetime import *
from dateutil.relativedelta import *

# GET ~/keyboard/ 요청에 반응
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['알리미 시작하기', '파파고(NMT 번역)']
    })

# csrf 토큰 에러 방지, POST 요청에 message response
@csrf_exempt
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    identify = received_json_data['content']
    cert = received_json_data['content']
    responder = received_json_data['content']
    schoolhome = 'http://gsh.hs.kr/m/main.jsp?SCODE=S0000000718&mnu=M001006001'

    daystring = ["월", "화", "수", "목", "금", "토", "일"]
    nextdaystring = ["화", "수", "목", "금", "토", "일", "월"]

    today = date.today().weekday()
    today_date = date.today()
    tomorrow_date = today_date+relativedelta(days=+1)

    if responder in daystring:
        if today == 6:
            days = today_date + relativedelta(weekday=daystring.index(responder))
        else:
            days = today_date + relativedelta(days=-today, weekday=daystring.index(responder))

## 로그인 화면 설정
    if identify == '알리미 시작하기':
        return JsonResponse({
            'message': {
                'text': '서비스 이용을 위해 학년을 선택해 주세요'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['1학년 사용자', '2학년 사용자', '3학년 사용자']
            }
        })
    elif identify == '파파고(NMT 번역)':
        return JsonResponse({
            'message': {
                'text': '파파고 인공신경망 번역 기능입니다.\n번역하려면 입력해 주세요(한영, 영한 가능)'
            },
            'keyboard': {
                'type': 'text'
            }
        })

## 학년별 인터페이스 구성
    if identify == '1학년 사용자':
        return JsonResponse({
            'message': {
                'text': '1학년의 경우 반별 데이터가 제공되지 않으니 양해바랍니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표', '학사일정', '파파고(NMT 번역)', '오늘의 날씨', '홈페이지 공지사항']
            }
        })
    elif identify == '2학년 사용자':
        return JsonResponse({
            'message': {
                'text': '경상고 2학년 선택되었습니다. 학반을 선택해 주세요.\n반별로 제공되는 서비스의 종류가 다소 차이가 있을 수 있습니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-1', '2-2', '2-3', '2-4', '2-5', '2-6', '2-7', '2-8']
            }
        })
    elif identify == '2-1' or identify == '2-2' or identify == '2-3' or identify == '2-4':
        return JsonResponse({
            'message': {
                'text': '2학년 문과의 경우 반별 데이터가 제공되지 않으니 양해바랍니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표', '학사일정', '파파고(NMT 번역)', '오늘의 날씨', '홈페이지 공지사항']
            }
        })
    elif identify == '2-5' or identify == '2-6' or identify == '2-7' or identify == '2-8':
        return JsonResponse({
            'message': {
                'text': '서비스에 오신것을 환영합니다. 많은 이용 부탁드립니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 서비스', '학생증 바코드', '2학년 시간표', '우리학교 학사일정 ', '파파고(NMT 번역)', '오늘의 날씨는?', '우리학교 공지사항']
            }
        })
    elif identify == '3학년 사용자':
        return JsonResponse({
            'message': {
                'text': '경상고 3학년 선택되었습니다. 학반을 선택해 주세요.\n반별로 제공되는 서비스의 종류가 다소 차이가 있을 수 있습니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-1', '3-2', '3-3', '3-4', '3-5', '3-6', '3-7', '3-8']
            }
        })
    elif identify == '3-1' or identify == '3-2' or identify == '3-3' or identify == '3-4':
        return JsonResponse({
            'message': {
                'text': '3학년 문과의 경우 반별 데이터가 제공되지 않으니 양해바랍니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표', '학사일정', '파파고(NMT 번역)', '오늘의 날씨', '홈페이지 공지사항']
            }
        })
    elif identify == '3-5' or identify == '3-6' or identify == '3-7' or identify == '3-8':
        return JsonResponse({
            'message': {
                'text': '서비스에 오신것을 환영합니다. 많은 이용 부탁드립니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 열람하기', '학생증 바코드', '3학년 시간표 보기', '학사일정 열람하기', '파파고(NMT 번역)', '오늘의 날씨 검색하기', '홈페이지 공지사항 불러오기']
            }
        })

## 공통 응답 설정
    if responder == '처음으로':
        return JsonResponse({
            'message': {
                'text': '항목을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표', '학사일정', '파파고(NMT 번역)', '오늘의 날씨', '홈페이지 공지사항']
            }
        })
    elif responder == '식단표':
        return JsonResponse({
            'message': {
                'text': '식단표를 열람하기 위해 항목을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '이번주의 다른 요일 식단표', '처음으로']
            }
        })
    elif responder == '오늘 식단표':
        return JsonResponse({
            'message': {
                'text': '@' + responder + '\n' + today_date.strftime("%m월 %d일 ") + daystring[today] + '요일 식단표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '이번주의 다른 요일 식단표', '처음으로']
            }
        })
    elif responder == '내일 식단표':
        return JsonResponse({
            'message': {
                'text': '@' + responder + '\n' + tomorrow_date.strftime("%m월 %d일 ") + nextdaystring[today] + '요일 식단표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '이번주의 다른 요일 식단표', '처음으로']
            }
        })
    elif responder == '이번주의 다른 요일 식단표':
        return JsonResponse({
            'message': {
                'text': '식단 정보가 필요한 요일을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['월', '화', '수', '목', '금', '처음으로']
            }
        })
    elif responder in daystring and responder != "일":
        return JsonResponse({
            'message': {
                'text': '@' + responder + '\n' + days.strftime("%m월 %d일 ") + responder + '요일 식단표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표', '내일 식단표', '이번주의 다른 요일 식단표', '처음으로']
            }
        })
    elif responder == '학사일정':
        return JsonResponse({
            'message': {
                'text': '학교 금년 학사일정을 열람합니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정', '1학기 학사일정', '2학기 학사일정', '처음으로']
            }
        })
    elif responder == '전체 학사일정':
        return JsonResponse({
            'message': {
                'text': data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정', '1학기 학사일정', '2학기 학사일정', '처음으로']
            }
        })
    elif responder == '1학기 학사일정':
        return JsonResponse({
            'message': {
                'text': data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정', '1학기 학사일정', '2학기 학사일정', '처음으로']
            }
        })
    elif responder == '2학기 학사일정':
        return JsonResponse({
            'message': {
                'text': data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정', '1학기 학사일정', '2학기 학사일정', '처음으로']
            }
        })
    elif responder == '오늘의 날씨':
        return JsonResponse({
            'message': {
                'text': '@오늘은 날씨가 어떨까요?',
                'photo': {
                    'url': 'https://is1-ssl.mzstatic.com/image/thumb/Purple115/v4/b5/40/73/b5407382-3409-9318-f3a2-bbc51fe8af4f/AppIcon-1x_U007emarketing-85-220-8.png/246x0w.jpg',
                    'width': 500,
                    'height': 500
                },
                'message_button': {
                    'label': '확인해 보기',
                    'url': 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
				}
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표', '학사일정', '파파고(NMT 번역)', '오늘의 날씨', '홈페이지 공지사항']
            }
        })
    elif responder == '홈페이지 공지사항':
        return JsonResponse({
            'message': {
                'text': '@홈페이지 공지사항을 알아봅니다.',
                'photo': {
                    'url': 'http://www.airmajor.co.kr/kr/images/icon04.png',
                    'width': 500,
                    'height': 500
                },
                'message_button': {
                    'label': '확인해 보기',
                    'url': schoolhome
				}
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표', '학사일정', '파파고(NMT 번역)', '오늘의 날씨', '홈페이지 공지사항']
            }
        })
		
## 2학년 이과 응답 설정
    if responder == '기본메뉴로':
        return JsonResponse({
            'message': {
                'text': '항목을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 서비스', '학생증 바코드', '2학년 시간표', '우리학교 학사일정', '파파고(NMT 번역)', '오늘의 날씨는?', '우리학교 공지사항']
            }
        })
    elif responder == '식단표 서비스':
        return JsonResponse({
            'message': {
                'text': '식단표를 열람하기 위해 항목을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표 서비스', '내일 식단표 서비스', '이번주의 다른 요일 식단표 서비스', '기본메뉴로']
            }
        })
    elif responder == '오늘 식단표 서비스':
        return JsonResponse({
            'message': {
                'text': '@' + responder + '\n' + today_date.strftime("%m월 %d일 ") + daystring[today] + '요일 식단표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표 서비스', '내일 식단표 서비스', '이번주의 다른 요일 식단표 서비스', '기본메뉴로']
            }
        })
    elif responder == '내일 식단표 서비스':
        return JsonResponse({
            'message': {
                'text': '@' + responder + '\n' + tomorrow_date.strftime("%m월 %d일 ") + nextdaystring[today] + '요일 식단표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표 서비스', '내일 식단표 서비스', '이번주의 다른 요일 식단표 서비스', '기본메뉴로']
            }
        })
    elif responder == '이번주의 다른 요일 식단표 서비스':
        return JsonResponse({
            'message': {
                'text': '식단 정보가 필요한 요일을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['월', '화', '수', '목', '금', '기본메뉴로']
            }
        })
    elif responder == '2학년 시간표':
        return JsonResponse({
            'message': {
                'text': '시간표를 확인할 학반을 선택해 주세요.\n이과반만 조회가 가능합니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['기본메뉴로', '2-5반 시간표', '2-6반 시간표', '2-7반 시간표', '2-8반 시간표']
            }
        })
    elif responder == '2-5반 시간표':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-5 오늘 시간표', '2-5 내일 시간표', '2-5 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-5 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("2-5반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-5 오늘 시간표', '2-5 내일 시간표', '2-5 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-5 내일 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("2-5반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-5 오늘 시간표', '2-5 내일 시간표', '2-5 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-5 전체 시간표':
        return JsonResponse({
            'message': {
                'text': '@2-5반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-5 오늘 시간표', '2-5 내일 시간표', '2-5 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-6반 시간표':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-6 오늘 시간표', '2-6 내일 시간표', '2-6 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-6 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("2-6반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-6 오늘 시간표', '2-6 내일 시간표', '2-6 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-6 내일 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("2-6반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-6 오늘 시간표', '2-6 내일 시간표', '2-6 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-6 전체 시간표':
        return JsonResponse({
            'message': {
                'text': '@2-6반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-6 오늘 시간표', '2-6 내일 시간표', '2-6 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-7반 시간표':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-7 오늘 시간표', '2-7 내일 시간표', '2-7 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-7 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("2-7반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-7 오늘 시간표', '2-7 내일 시간표', '2-7 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-7 내일 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("2-7반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-7 오늘 시간표', '2-7 내일 시간표', '2-7 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-7 전체 시간표':
        return JsonResponse({
            'message': {
                'text': '@2-7반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-7 오늘 시간표', '2-7 내일 시간표', '2-7 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-8반 시간표':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-8 오늘 시간표', '2-8 내일 시간표', '2-8 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-8 오늘 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("2-8반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-8 오늘 시간표', '2-8 내일 시간표', '2-8 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-8 내일 시간표':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("2-8반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-8 오늘 시간표', '2-8 내일 시간표', '2-8 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '2-8 전체 시간표':
        return JsonResponse({
            'message': {
                'text': '@2-8반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['2-8 오늘 시간표', '2-8 내일 시간표', '2-8 전체 시간표', '기본메뉴로']
            }
        })
    elif responder == '우리학교 학사일정':
        return JsonResponse({
            'message': {
                'text': '학교 금년 학사일정을 열람합니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['우리학교 전체 학사일정', '우리학교 1학기 학사일정', '우리학교 2학기 학사일정', '기본메뉴로']
            }
        })
    elif responder == '우리학교 전체 학사일정':
        return JsonResponse({
            'message': {
                'text': '@' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['우리학교 전체 학사일정', '우리학교 1학기 학사일정', '우리학교 2학기 학사일정', '기본메뉴로']
            }
        })
    elif responder == '우리학교 1학기 학사일정':
        return JsonResponse({
            'message': {
                'text': '@' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['우리학교 전체 학사일정', '우리학교 1학기 학사일정', '우리학교 2학기 학사일정', '기본메뉴로']
            }
        })
    elif responder == '우리학교 2학기 학사일정':
        return JsonResponse({
            'message': {
                'text': '@' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['우리학교 전체 학사일정', '우리학교 1학기 학사일정', '우리학교 2학기 학사일정', '기본메뉴로']
            }
        })
    elif responder == '오늘의 날씨는?':
        return JsonResponse({
            'message': {
                'text': '@오늘은 날씨가 어떨까요?',
                'photo': {
                    'url': 'https://is1-ssl.mzstatic.com/image/thumb/Purple115/v4/b5/40/73/b5407382-3409-9318-f3a2-bbc51fe8af4f/AppIcon-1x_U007emarketing-85-220-8.png/246x0w.jpg',
                    'width': 500,
                    'height': 500
                },
                'message_button': {
                    'label': '확인해 보기',
				    'url': 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
				}
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 서비스', '학생증 바코드', '2학년 시간표', '우리학교 학사일정', '파파고(NMT 번역)', '오늘의 날씨는?', '우리학교 공지사항']
            }
        })
    elif responder == '우리학교 공지사항':
        return JsonResponse({
            'message': {
                'text': '@홈페이지 공지사항을 알아봅니다.',
                'photo': {
                    'url': 'http://www.airmajor.co.kr/kr/images/icon04.png',
                    'width': 500,
                    'height': 500
                },
                'message_button': {
                    'label': '확인해 보기',
                    'url': schoolhome
				}
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 서비스', '학생증 바코드', '2학년 시간표', '우리학교 학사일정', '파파고(NMT 번역)', '오늘의 날씨는?', '우리학교 공지사항']
            }
        })

## 3학년 이과 응답 설정
    if responder == '초기화면으로 가기':
        return JsonResponse({
            'message': {
                'text': '항목을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 열람하기', '학생증 바코드', '3학년 시간표 보기', '학사일정 열람하기', '파파고(NMT 번역)', '오늘의 날씨 검색하기', '홈페이지 공지사항 불러오기']
            }
        })
    elif responder == '식단표 열람하기':
        return JsonResponse({
            'message': {
                'text': '식단표를 열람하기 위해 항목을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표 열람하기', '내일 식단표 열람하기', '이번주의 다른 요일 식단표 열람하기', '초기화면으로 가기']
            }
        })
    elif responder == '오늘 식단표 열람하기':
        return JsonResponse({
            'message': {
                'text': '@' + responder + '\n' + today_date.strftime("%m월 %d일 ") + daystring[today] + '요일 식단표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표 열람하기', '내일 식단표 열람하기', '이번주의 다른 요일 식단표 열람하기', '초기화면으로 가기']
            }
        })
    elif responder == '내일 식단표 열람하기':
        return JsonResponse({
            'message': {
                'text': '@' + responder + '\n' + tomorrow_date.strftime("%m월 %d일 ") + nextdaystring[today] + '요일 식단표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘 식단표 열람하기', '내일 식단표 열람하기', '이번주의 다른 요일 식단표 열람하기', '초기화면으로 가기']
            }
        })
    elif responder == '이번주의 다른 요일 식단표 열람하기':
        return JsonResponse({
            'message': {
                'text': '식단 정보가 필요한 요일을 선택해 주세요.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['월', '화', '수', '목', '금', '토', '초기화면으로 가기']
            }
        })
    elif responder == '3학년 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '시간표를 확인할 학반을 선택해 주세요.\n이과반만 조회가 가능합니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['초기화면으로 가기', '3-5반 시간표 보기', '3-6반 시간표 보기', '3-7반 시간표 보기', '3-8반 시간표 보기']
            }
        })
    elif responder == '3-5반 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-5 오늘 시간표 보기', '3-5 내일 시간표 보기', '3-5 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-5 오늘 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("3-5반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-5 오늘 시간표 보기', '3-5 내일 시간표 보기', '3-5 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-5 내일 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("3-5반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-5 오늘 시간표 보기', '3-5 내일 시간표 보기', '3-5 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-5 전체 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@3-5반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-5 오늘 시간표 보기', '3-5 내일 시간표 보기', '3-5 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-6반 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-6 오늘 시간표 보기', '3-6 내일 시간표 보기', '3-6 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-6 오늘 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("3-6반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-6 오늘 시간표 보기', '3-6 내일 시간표 보기', '3-6 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-6 내일 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("3-6반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-6 오늘 시간표 보기', '3-6 내일 시간표 보기', '3-6 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-6 전체 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@3-6반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-6 오늘 시간표 보기', '3-6 내일 시간표 보기', '3-6 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-7반 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-7 오늘 시간표 보기', '3-7 내일 시간표 보기', '3-7 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-7 오늘 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("3-7반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-7 오늘 시간표 보기', '3-7 내일 시간표 보기', '3-7 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-7 내일 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("3-7반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-7 오늘 시간표 보기', '3-7 내일 시간표 보기', '3-7 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-7 전체 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@3-7반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-7 오늘 시간표 보기', '3-7 내일 시간표 보기', '3-7 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-8반 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '열람할 항목을 선택해 주세요..'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-8 오늘 시간표 보기', '3-8 내일 시간표 보기', '3-8 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-8 오늘 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + today_date.strftime("3-8반의 %m월 %d일 ") + daystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-8 오늘 시간표 보기', '3-8 내일 시간표 보기', '3-8 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-8 내일 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@' + tomorrow_date.strftime("3-8반의 %m월 %d일 ") + nextdaystring[today] + '요일 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-8 오늘 시간표 보기', '3-8 내일 시간표 보기', '3-8 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '3-8 전체 시간표 보기':
        return JsonResponse({
            'message': {
                'text': '@3-8반의 전체 시간표입니다. \n \n' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['3-8 오늘 시간표 보기', '3-8 내일 시간표 보기', '3-8 전체 시간표 보기', '초기화면으로 가기']
            }
        })
    elif responder == '학사일정 열람하기':
        return JsonResponse({
            'message': {
                'text': '학교 금년 학사일정을 열람합니다.'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정 열람하기', '1학기 학사일정 열람하기', '2학기 학사일정 열람하기', '초기화면으로 가기']
            }
        })
    elif responder == '전체 학사일정 열람하기':
        return JsonResponse({
            'message': {
                'text': '@' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정 열람하기', '1학기 학사일정 열람하기', '2학기 학사일정 열람하기', '초기화면으로 가기']
            }
        })
    elif responder == '1학기 학사일정 열람하기':
        return JsonResponse({
            'message': {
                'text': '@' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정 열람하기', '1학기 학사일정 열람하기', '2학기 학사일정 열람하기', '초기화면으로 가기']
            }
        })
    elif responder == '2학기 학사일정 열람하기':
        return JsonResponse({
            'message': {
                'text': '@' + data_from_db(responder, today, daystring)
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['전체 학사일정 열람하기', '1학기 학사일정 열람하기', '2학기 학사일정 열람하기', '초기화면으로 가기']
            }
        })
    elif responder == '오늘의 날씨 검색하기':
        return JsonResponse({
            'message': {
                'text': '@오늘은 날씨가 어떨까요?',
                'photo': {
                    'url': 'https://is1-ssl.mzstatic.com/image/thumb/Purple115/v4/b5/40/73/b5407382-3409-9318-f3a2-bbc51fe8af4f/AppIcon-1x_U007emarketing-85-220-8.png/246x0w.jpg',
                    'width': 500,
                    'height': 500
                },
                'message_button': {
                    'label': '확인해 보기',
				    'url': 'https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8'
				}
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 열람하기', '학생증 바코드', '3학년 시간표 보기', '학사일정 열람하기', '파파고(NMT 번역)', '오늘의 날씨 검색하기', '홈페이지 공지사항 불러오기']
            }
        })
    elif responder == '홈페이지 공지사항 불러오기':
        return JsonResponse({
            'message': {
                'text': '@홈페이지 공지사항을 알아봅니다.',
                'photo': {
                    'url': 'http://www.airmajor.co.kr/kr/images/icon04.png',
                    'width': 500,
                    'height': 500
                },
                'message_button': {
                    'label': '확인해 보기',
                    'url': schoolhome
				}
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 열람하기', '학생증 바코드', '3학년 시간표 보기', '학사일정 열람하기', '파파고(NMT 번역)', '오늘의 날씨 검색하기', '홈페이지 공지사항 불러오기']
            }
        })
    elif responder == '학생증 바코드':
        return JsonResponse({
            'message': {
                'text': '2학년 이과 학생들과 3학년 신청자에게만 제공되는 학생별 맞춤형 서비스 입니다.\n간단한 인증 절차를 통해 학생증 바코드를 생성합니다.\n자신의 학생증 하단에 있는 코드와 이름를 입력해 주세요.\n\nWARNING!! 경고!!\n타인의 신분을 도용하여 사용하는 것은 잘못된 행위입니다. 관련법에 의해 처벌될 수 있으므로 주의하시기 바랍니다.\n\n초기화면으로 이동되는 경우 등록되지 않은 사용자 이거나 학생 코드 또는 이름이 잘못 입력된 것이니 오류를 정정하여 다시 시도하세요. 영어 알파벳의 경우 대문자만 인식합니다.\n\n입력 예시 : S2013001 김땡땡'
            },
            'keyboard': {
                'type': 'text'
            }
        })

### 인증 성공시 학생증 바코드 출력
    if cert == 'S2016206 최재성':
        return JsonResponse({
            'message': {
                'text': 'Certification Result; Success\nUser 최재성(3-7) was in.\nS2016206 최재성 학생증 입니다.\n오류 발생의 여지가 있으므로 자신의 코드가 맞는지 확인 후 사용하시기 바랍니다.\n바코드가 인식이 잘 안되는 경우 화면 밝기를 올려주세요.',
                'photo': {
                    'url': 'https://www.barcodesinc.com/generator/image.php?code=S2016206&style=452&type=C128A&width=386&height=200&xres=3&font=4',
                    'width': 840,
                    'height': 480
                },
                'message_button': {
                    'label': '크게 보기',
                    'url': 'https://www.barcodesinc.com/generator/image.php?code=S2016206&style=452&type=C128A&width=386&height=200&xres=3&font=4'
                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['식단표 열람하기', '학생증 바코드', '3학년 시간표 보기', '학사일정 열람하기', '파파고(NMT 번역)', '오늘의 날씨 검색하기', '홈페이지 공지사항 불러오기']
            }
        })

    else:
        translated = translate(received_json_data['content'])
        return JsonResponse({
            'message': {
               'text': translated
            },
            'keyboard': {
               'type': 'buttons',
               'buttons': ['알리미 시작하기', '파파고(NMT 번역)']
            }
        })
#    else:
#        return JsonResponse({
#            'message': {
#                'text': '등록되지 않은 사용자 이거나 학생 코드 또는 이름이 잘못 입력되었습니다. 확인후 오류를 정정하여 다시 시도하세요.\n입력됨 : ' + '[' + cert + ']'
#            },
#            'keyboard': {
#                'type': 'text'
#            }
#        })


# DB에 저장된 자료 내보내기(급식, 시간표, 학사일정 등)
def data_from_db(responder, today, daystring):
    day_eng = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

    con = sqlite3.connect("element/database/responder.db")
    cur = con.cursor()

	## 식단표 서비스
    if responder == '오늘 식단표' or responder == '오늘 식단표 서비스' or responder == '오늘 식단표 열람하기':
        query = ("SELECT " + (day_eng[today]) + " FROM meal")
    if responder == '내일 식단표' or responder == '내일 식단표 서비스' or responder == '내일 식단표 열람하기':
        if today == 6:
            query = ("SELECT mon FROM meal")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM meal")
    if responder in daystring:
        query = ("SELECT " + (day_eng[daystring.index(responder)]) + " FROM meal")
	## 2학년 시간표 서비스
    if responder == '2-5 오늘 시간표':
        query = ("SELECT " + (day_eng[today]) + " FROM afive")
    if responder == '2-5 내일 시간표':
        if today == 6:
            query = ("SELECT mon FROM afive")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM afive")
    if responder == '2-5 전체 시간표':
        query = ("SELECT ald FROM afive")
    if responder == '2-6 오늘 시간표':
        query = ("SELECT " + (day_eng[today]) + " FROM bsix")
    if responder == '2-6 내일 시간표':
        if today == 6:
            query = ("SELECT mon FROM bsix")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM bsix")
    if responder == '2-6 전체 시간표':
        query = ("SELECT ald FROM bsix")
    if responder == '2-7 오늘 시간표':
        query = ("SELECT " + (day_eng[today]) + " FROM csev")
    if responder == '2-7 내일 시간표':
        if today == 6:
            query = ("SELECT mon FROM csev")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM csev")
    if responder == '2-7 전체 시간표':
        query = ("SELECT ald FROM csev")
    if responder == '2-8 오늘 시간표':
        query = ("SELECT " + (day_eng[today]) + " FROM deigh")
    if responder == '2-8 내일 시간표':
        if today == 6:
            query = ("SELECT mon FROM deigh")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM deigh")
    if responder == '2-8 전체 시간표':
        query = ("SELECT ald FROM deigh")
	## 3학년 시간표 서비스
    if responder == '3-5 오늘 시간표 보기':
        query = ("SELECT " + (day_eng[today]) + " FROM alpha")
    if responder == '3-5 내일 시간표 보기':
        if today == 6:
            query = ("SELECT mon FROM alpha")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM alpha")
    if responder == '3-5 전체 시간표 보기':
        query = ("SELECT ald FROM alpha")
    if responder == '3-6 오늘 시간표 보기':
        query = ("SELECT " + (day_eng[today]) + " FROM beta")
    if responder == '3-6 내일 시간표 보기':
        if today == 6:
            query = ("SELECT mon FROM beta")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM beta")
    if responder == '3-6 전체 시간표 보기':
        query = ("SELECT ald FROM beta")
    if responder == '3-7 오늘 시간표 보기':
        query = ("SELECT " + (day_eng[today]) + " FROM cinnamon")
    if responder == '3-7 내일 시간표 보기':
        if today == 6:
            query = ("SELECT mon FROM cinnamon")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM cinnamon")
    if responder == '3-7 전체 시간표 보기':
        query = ("SELECT ald FROM cinnamon")
    if responder == '3-8 오늘 시간표 보기':
        query = ("SELECT " + (day_eng[today]) + " FROM donut")
    if responder == '3-8 내일 시간표 보기':
        if today == 6:
            query = ("SELECT mon FROM donut")
        else:
            query = ("SELECT " + (day_eng[today + 1]) + " FROM donut")
    if responder == '3-8 전체 시간표 보기':
        query = ("SELECT ald FROM donut")
	## 학사일정 서비스
    if responder == '전체 학사일정' or responder == '우리학교 전체 학사일정' or responder == '전체 학사일정 열람하기':
        query = ("SELECT whole FROM schedule")
    if responder == '1학기 학사일정' or responder == '우리학교 1학기 학사일정' or responder == '1학기 학사일정 열람하기':
        query = ("SELECT par FROM schedule")
    if responder == '2학기 학사일정' or responder == '우리학교 2학기 학사일정' or responder == '2학기 학사일정 열람하기':
        query = ("SELECT part FROM schedule")

    cur.execute(query)
    data = cur.fetchone()

    return data[0]
	