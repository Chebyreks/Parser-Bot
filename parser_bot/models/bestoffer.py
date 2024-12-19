from sqlalchemy import String, BigInteger, Date
from sqlalchemy.orm import Mapped, mapped_column
from parser_bot.core.db import Base

class BestOffer(Base):
    __tablename__ = "bestoffer"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key = True, autoincrement=True, nullable=False)
    date: Mapped[Date] = mapped_column(Date(), nullable=False)
    offer: Mapped[str] = mapped_column(String(), nullable=False)
    url: Mapped[str] =  mapped_column(String(), nullable=False)
    price: Mapped[int] = mapped_column(BigInteger(), nullable=False)
