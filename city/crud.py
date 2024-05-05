from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from city import schemas, models


async def create_new_city(session: AsyncSession, city: schemas.CityBase):
    query = insert(models.DBCity).values(
        name=city.name,
        additional_info=city.additional_info
    )
    result = await session.execute(query)
    await session.commit()
    response = {**city.model_dump(), "id": result.lastrowid}
    return response


async def get_all_cities(session: AsyncSession,
                         skip: int = 0,
                         limit: int = 10):
    query = select(models.DBCity).offset(skip).limit(limit)
    city_list = await session.execute(query)
    return [city[0] for city in city_list.all()]


async def get_city_by_id(session: AsyncSession, city_id: int):
    query = select(models.DBCity).where(models.DBCity.id == city_id)
    city_result = await session.execute(query)
    return city_result.scalar()


async def get_city_by_name(session: AsyncSession, city_name: str):
    query = select(models.DBCity).where(models.DBCity.name == city_name)
    city_result = await session.execute(query)
    return city_result.scalar()


async def update_city_info(session: AsyncSession,
                           city: schemas.CityUpdate,
                           city_id: int):
    query = update(models.DBCity).where(
        models.DBCity.id == city_id).values(
        additional_info=city.additional_info)
    await session.execute(query)
    await session.commit()

    return await get_city_by_id(session=session,
                                city_id=city_id)


async def delete_city(session: AsyncSession,
                      city_id: int):
    delete_query = delete(models.DBCity).where(models.DBCity.id == city_id)

    await session.execute(delete_query)
    await session.commit()

    return {"message": f"city with id \"{city_id}\" was deleted from the Database"}


# async def first_city_temperature(session: AsyncSession,
#                                  temperature: schemas.):
#     query = insert(models.DBTemperature).values(
#         city_id=,
#         date_time=,
#         temperature=
#     )
#     result = await session.execute(query)
#     await session.commit()
#     response = {**temperature.model_dump(), "id": result.lastrowid}
#     return response