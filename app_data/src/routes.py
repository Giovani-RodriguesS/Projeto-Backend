from fastapi import APIRouter
from src.database import connect
from src.schema import Person, Account, Card
from src.models import cards, people, accounts

route = APIRouter()
@route.get("/person")
async def get():
    return connect.execute(people.select()).mappings().all()

@route.post("/person")
async def post_person(person: Person):
    connect.execute(people.insert().values(
        name = person.name,
        email = person.email,
        gender = person.gender,
        birth_date = person.birth_date, 
        address = person.address,
        salary = person.salary,
        cpf = person.cpf
    ))
    return connect.execute(people.select()).mappings().all()

@route.post("/account")
async def post_account(account: Account):
    connect.execute(accounts.insert().values(
        status_id = account.status_id,
        due_day = account.due_day,
        person_id = account.person_id,
        balance = account.balance,
        avaliable_balance = account.avaliable_balance
    ))

    return connect.execute(account.select()).mappings().all()

@route.post("/card")
async def post_card(card: Card):
    connect.execute(cards.insert().values(
        card_number = card.card_number,
        account_id = card.account_id,
        status_id  = card.status_id,
        limit = card.limit,
        expiration_date = card.expiration_date
    ))
    return connect.execute(card.select()).mappings().all()

@route.delete("/{id}")
async def delete(id : int):
    connect.execute(people.delete().where(people.c.person_id == id))