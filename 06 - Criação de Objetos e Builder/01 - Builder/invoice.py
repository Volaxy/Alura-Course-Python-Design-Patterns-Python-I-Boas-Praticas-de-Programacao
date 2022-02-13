from datetime import date


class Item:
    def __init__(self, description, value):
        self.__description = description
        self.__value = value

    @property
    def description(self):
        return self.__description

    @property
    def value(self):
        return self.__value


class Invoice:
    def __init__(self, social_reason, cnpj, items, issue_date=date.today(), details=""):
        self.__social_reason = social_reason
        self.__cnpj = cnpj
        self.__issue_date = issue_date

        if len(details) > 20:
            raise Exception("Note details cannot be longer than 20 characters")

        self.__details = details
        self.__items = items

    @property
    def social_reason(self):
        return self.__social_reason

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def details(self):
        return self.__details
