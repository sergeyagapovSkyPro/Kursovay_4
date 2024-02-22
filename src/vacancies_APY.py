from abc import ABC, abstractmethod


class VacancyAPY(ABC):

    @abstractmethod
    def get_vacancy(self):
        pass
