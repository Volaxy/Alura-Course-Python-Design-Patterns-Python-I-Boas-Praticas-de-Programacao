from invoice import Invoice


class CreatorOfInvoice:
    def __init__(self):
        self.__social_reason = None
        self.__cnpj = None
        self.__issue_date = None
        self.__details = ''
        self.__items = None

    def with_social_reason(self, social_reason):
        self.__social_reason = social_reason
        return self

    def with_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def with_issue_date(self, issue_date):
        self.__issue_date = issue_date
        return self

    def with_items(self, items):
        self.__items = items
        return self

    def build(self):
        if self.__social_reason is None:
            raise Exception("Company name must be filled")
        if self.__cnpj is None:
            raise Exception("CNPJ must be filled")
        if self.__items is None:
            raise Exception("Items must be filled")

        return Invoice(
            social_reason=self.__social_reason,
            cnpj=self.__cnpj,
            items=self.__items,
            issue_date=self.__issue_date,
            details=self.__details
        )
