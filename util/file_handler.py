from dataclasses import dataclass
'''
context: /Users/KAREN/SbaProjects
fname: /titanic/data/
'''
@dataclass
class FileReader:

    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''
 