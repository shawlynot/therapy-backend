from sqlmodel import Session
from therapy_backend.model import AccountBase


def create_account(session: Session, account: AccountBase) -> AccountBase:
    session.add(account)
    session.commit()
    session.refresh(account)
    return account
