from datetime import datetime


class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.author == self]

    
    def books(self):
        return list(set(contract.book for contract in self._contracts))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book parameter must be an instance of the Book class.")
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        book._contracts.append(new_contract)  
        return new_contract

    def total_royalties(self):
        total = 0
        for contract in self._contracts:
            if contract.author == self and isinstance(contract.royalties, int) and contract.royalties >= 0:
                total += contract.royalties
        print("Total royalties calculated:", total)
        return total

class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.members.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return list(set(contract.book for contract in self._contracts))


class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author parameter must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The book parameter must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The date parameter must be a string.")
        if not isinstance(royalties, int):
            raise Exception("The royalties parameter must be an integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.members if contract.date == date]
