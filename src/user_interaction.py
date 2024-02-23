from src.error_hh import ErrorHH
from src.error_user_json import ErrorUserJson
from src.sorted_vacancies import SortedVacancies
from src.connection_hh import HeadHunter


class UserInteractionHeadHunter(ErrorHH):
    def hh_user_search(self):
        """
        Метод для поиска вакансий на сайте
        """
        search_query = self.user_input_str()
        top_n = self.user_input_int()
        result_search = HeadHunter(search_query, top_n)
        result_search.get_json()


class UserInteractionJson(ErrorUserJson):
    def json_user_search(self):
        """
        Метод сортировки вакансиий
        """
        vacancies_list = []
        json_file = SortedVacancies()
        json_vacancies = json_file.sorted_vacancies
        payment = self.user_input_int()
        city = self.user_input_str()
        for vacancies in json_vacancies:
            if payment > vacancies["payment_from"]:
                continue

            if city == vacancies["city"]:
                vacancies_list.append(vacancies)

            if city == "":
                vacancies_list.append(vacancies)

        for result in vacancies_list:
            print(f"Город: {result['city']}\nДата публикации: {result['data']}\n"
                  f"Должность: {result['name']}\nТребование: {result['skill_1']}\n"
                  f"Ответственность: {result['skill_2']}\nЗарплата от {result['payment_from']}\n")
        if len(vacancies_list) == 0:
            print(f'Результатов 0')


if __name__ == '__main__':
    r = UserInteractionJson()
    r.json_user_search()
