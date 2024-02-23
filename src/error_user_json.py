from src.user_forms import UserForm


class ErrorUserJson(UserForm):
    payment_from = None
    city = None

    def user_input_int(self):
        """
        Метод проверяет значение пользователя,
        :return: intenger
        """
        self.payment_from = input("Введите минимальную заработную плату: ")
        if self.payment_from.isalpha():
            raise ValueError("Заработная плата должна быть числом!")

        if self.payment_from == "":
            self.payment_from = 0
        return int(self.payment_from)

    def user_input_str(self):
        """
        Метод проверяет значение пользователя,
        :return: string

        """
        self.city = input("Введите город или нажмите 'Enter' что бы увидить все города: ").title()

        if self.city.isdigit():
            raise TypeError("Город не может быть числом!")
        return self.city


if __name__ == '__main__':
    r = ErrorUserJson()
    print(r.user_input_int())
