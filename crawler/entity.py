from dataclasses import dataclass

@dataclass
class Entity: # 프로퍼티는 url, parser, path, api, apikey 전부 str 타입
    
    url: str = 'https://comic.naver.com/webtoon/weekday.nhn'
    parser: str = 'html.parser'
    path: str = ''
    api: str = ''
    apikey: str =  ''    

 
