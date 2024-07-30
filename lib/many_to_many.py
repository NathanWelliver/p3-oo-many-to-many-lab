class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        contracts = self.contracts()
        books = [contract.book for contract in contracts]
        return books
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(author=self, book=book, date=date, royalties=royalties)
        return contract

    def total_royalties(self):
        contracts = self.contracts()
        royalties = sum([contract.royalties for contract in contracts])
        return royalties

class Book:

    all =[]

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        contracts = self.contracts()
        authors = [contract.author for contract in contracts]
        return authors


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception
        if not isinstance(book, Book):
            raise Exception
        self.author = author
        self.book = book
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception
        Contract.all.append(self)

    @classmethod    
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]