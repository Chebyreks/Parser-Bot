from sqlalchemy import insert, update, select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from parser_bot.models.bestoffer import BestOffer
from parser_bot.schemas.bestoffer import BestOfferBase


async def create_offer(new_offer: BestOfferBase, session: AsyncSession) -> BestOffer:
    created_offer_data = new_offer.model_dump(exclude_none=True, exclude_unset=True)
    created_offer = await session.execute(
        insert(BestOffer).values(**created_offer_data).returning(BestOffer)
    )
    created_offer = created_offer.scalars().first()
    await session.commit()
    await session.refresh(created_offer)
    return created_offer

async def get_all_offers(session: AsyncSession):
    offers = await session.execute(select(BestOffer))
    offers = offers.scalars().all()
    return offers

async def get_offer_by_date(date: date, session: AsyncSession) -> BestOffer:
    offer_by_date = await session.execute(select(BestOffer).where(BestOffer.date == date))
    offer_by_date = offer_by_date.scalars().first()
    return offer_by_date

async def delete_offer_by_date(date: date, session: AsyncSession):
    await session.execute(delete(BestOffer).where(BestOffer.date == date))