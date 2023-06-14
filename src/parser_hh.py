import json
import os

import requests

# from src.abs import SaveVac, ParsingErorr

from fake_user_agent import user_agent


class SaveHH:
    """
    Получает данные о работодателях и их вакансий с сайта hh.ru
    """

    def __init__(self, key_word: str):
        self.key_word = key_word  # ключевое слово для поиска
        self.page_number = 0
        self.url = 'https://api.hh.ru/employers?'
        self.min_payment = 0

    def get_vacancies(self):
        """ Создание файлов с работодателями """
        hh_employers = []
        params = {'text': self.key_word,
                  'only_with_vacancies': True,
                  'page': self.page_number,
                  'per_page': 20}
        headers = {'User-Agent': user_agent('chrome')}
        # headers = {'User-Agent': 'K_ParserApp/1.0'}
        response = requests.get(self.url, params=params, headers=headers)
        count_data = response.json()['pages']
        for i in range(count_data):
            param_cycle = {'text': self.key_word,
                           'only_with_vacancies': True,
                           'page': i}
            response_cycle = requests.get(self.url, params=param_cycle, headers=headers)
            #     # if response.status_code != 200:
            #     #     raise ParsingErorr
            print(f'Запрос № {str(i)} к сайту HeadHunter')
            result = response_cycle.json()
            hh_employers.extend(result['items'])
            path = os.path.join('src', 'references', f'{self.key_word}.json')
            f = open(path, mode='w', encoding='utf8')
            f.write(json.dumps(hh_employers, ensure_ascii=False))
            f.close()

    def __str__(self):
        return self

