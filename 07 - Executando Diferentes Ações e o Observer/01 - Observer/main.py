from invoice import Item, Invoice
from invoice_builder import CreatorOfInvoice
from observers import print, send_by_email, save_in_the_bank


def __main__():
    items = [
        Item(
            description='ITEM A',
            value=100
        ),
        Item(
            description='ITEM B',
            value=200
        )
    ]

    invoice = Invoice(
        social_reason='Limited FHSA',
        cnpj='012345678901234',
        items=items,
        observers=[print, send_by_email, save_in_the_bank]
    )

    """
    items = [
        Item(
            description='ITEM A',
            value=100
        ),
        Item(
            description='ITEM B',
            value=200
        )
    ]

    invoice = (CreatorOfInvoice()
                   .with_social_reason('FHSA Limitada')
                   .with_cnpj('012345678901234')
                   .with_items(items)
                   .build())

    print(invoice.social_reason)
    print(invoice.cnpj)
    print(invoice.details)
    """


if __name__ == "__main__":
    __main__()
