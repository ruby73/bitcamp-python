from entity import Entity
import sys
sys.path.insert(0, '/Users/KAREN/SbaProjects/')
import numpy as np
import pandas as pd
import os, shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Service:
    def __init__(self):
        self.entity = Entity()
    
    def bugs_music(self):
        pass

    def naver_movie(self):
        pass
    
    @staticmethod
    def naver_cartoon(url) -> object:
        myparser = 'html.parser' # html.parser : 간단한 HTML과 XHTML 구문 분석기. 표준 라이브러리
        response = urlopen(url)
        soup = BeautifulSoup(response, myparser)
        return soup

    # 요일별 폴더 생성
    @staticmethod
    def create_folder_weekend(this) -> object:
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}

        mydict = this.dict
        myfolder = 'd:\\imsi\\' # 유닉스 기반은 '/'이 구분자

        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)
        return myfolder      

    # 각 이미지를 저장해주는 함수
    @staticmethod
    def saveFile(myfolder, mysrc, myweekday, mytitle, this):

        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
        # print(mysrc)
        # print(filename)

        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) # 바이트 형태로 저장
        myfile.close()

    