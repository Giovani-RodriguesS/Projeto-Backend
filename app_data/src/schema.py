from pydantic import BaseModel

"""
    Person - classe que contem os atributos referentes a tabela person
    Account - classe que contem os atributos referentes a tabela account
    Card - classe que contem os atributos referentes a tabela card
"""

class Person(BaseModel):
    person_id: int
    name: str
    email: str
    gender: str
    birth_date: str
    address: str
    salary: float
    cpf: str

class Account(BaseModel):
    account_id : int
    status_id : int
    due_day : int
    person_id : int
    balance : float
    avaliable_balance: float

class Card(BaseModel):
    card_id: int 	
    card_number: str
    account_id: int 	 
    status_id:	int 	 
    limit: float 	 
    expiration_date: str