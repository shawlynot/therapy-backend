from sqlmodel import Session
from therapy_backend.model import Account


def create_account(session: Session, account: Account) -> Account:
    session.add(account)
    session.commit()
    session.refresh(account)
    return account
