import sys
sys.path.insert(0, '/Karen/SbaProjects')
from service import Service
from entity import Entity

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
        print('hello')

if __name__ == '__main__':
    api = Controller()
    service = Service()
    service.naver_cartoon('https://comic.naver.com/webtoon/weekday.nhn')
    