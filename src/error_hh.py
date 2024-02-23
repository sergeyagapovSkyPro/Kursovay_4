from src.user_forms import UserForm


class ErrorHH(UserForm):
    search_query = None
    top_n = None

    def user_input_int(self):
        """
        Метод проверяет значение пользователя, выдает ошибки, выдает не больше 100 вакансий.
        :return: integer
        """
        self.top_n = input("Введите количесво вокансий для вывода в Top-N: ")
        if self.top_n.isalpha():
            raise ValueError("Колличесво не может быть строкой!")

        if self.top_n == "":
            raise AttributeError("Колличество не может быть пустым!")

        if int(self.top_n) > 100:
            self.top_n = 100
        return int(self.top_n)

    def user_input_str(self):
        """
        Метод проверяет значение пользователя, выдает ошибки.
        :return: string
        """
        self.search_query = input("Введите поисковой запрос: ")
        if self.search_query == "":
            raise ValueError("Запрос не может быть пустым!")

        if self.search_query.isdigit():
            raise TypeError("Запрос не может быть числом!")
        return self.search_query


if __name__ == '__main__':
    r = ErrorHH()
    print(r.user_input_str())