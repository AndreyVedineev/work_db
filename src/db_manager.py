import json

import psycopg2

insert_emp = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)"
class DBManager:
    """Класс DBManager использует библиотеку
     для работы с БД.
    Менеджер БД"""
    def __init__(self, insert):
        self.insert = insert
        self.path = path = os.path.join('src', 'references', f'{self.key_word}.json')

        conn = psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password='11122'
            )
        try:
            with open(self.path, encoding='UTF-8', newline='') as file:
                reader = json.load(file)
                for i in reader:
                    with conn:
                        with conn.cursor() as cur:
                            cur.execute(self.insert, i)

        finally:
            conn.close()

    def get_companies_and_vacancies_count():
        """Получает список всех компаний и количество вакансий у каждой компании"""

    pass

    def get_all_vacancies():
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию"""
        pass

    def get_avg_salary():
        """Получает среднюю зарплату по вакансиям"""
        pass

    def get_vacancies_with_higher_salary():
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        pass

    def get_vacancies_with_keyword():
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например 'python'."""
        pass
