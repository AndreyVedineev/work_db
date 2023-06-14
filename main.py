from src.parser_hh import SaveHH


def user_interaction():
    """ """
    employers_top = ['Сбер', 'Яндекс', 'Альфа-банк', 'VK', 'Газпром-нефть', 'ВТБ', 'Сибур', 'Tele2', 'МТС',
                     'Газпромбанк']
    for i in employers_top:
        hh = SaveHH(i)  # 53 - Краснодар. 2444 - Мостовской. 1438 - Краснодарский край 70 - Оренбург
        hh.get_vacancies()


if __name__ == "__main__":
    user_interaction()
