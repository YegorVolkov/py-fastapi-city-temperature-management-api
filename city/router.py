from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from engine import session_manager

from city import schemas, crud

router = APIRouter()


@router.get(path="/cities/",
            response_model=list[schemas.CityBase],
            tags=["Cities"])
async def read_all_cities(
        session: AsyncSession = Depends(session_manager),
        skip: int = 0,
        limit: int = 10):
    check_first_city = await crud.get_city_by_id(session=session,
                                                 city_id=1)

    if check_first_city is None:
        raise HTTPException(status_code=404,
                            detail="the Database is Empty")

    return await crud.get_all_cities(session=session,
                                     skip=skip,
                                     limit=limit)


@router.get(path="/cities/{city_id}",
            response_model=schemas.CityBase,
            tags=["Cities"])
async def read_specific_city(
        city_id: int,
        session: AsyncSession = Depends(session_manager)):
    check_city_id = await crud.get_city_by_id(session=session,
                                              city_id=city_id)

    if check_city_id is None:
        raise HTTPException(status_code=404,
                            detail="No Such city in the Database")

    return check_city_id


@router.post(path="/cities/",
             response_model=schemas.City,
             tags=["Cities"])
async def create_city(
        city: schemas.CityBase,
        session: AsyncSession = Depends(session_manager)):
    check_city_name = await crud.get_city_by_name(session=session,
                                                  city_name=city.name)

    if check_city_name:
        raise HTTPException(
            status_code=400,
            detail="City with such name is present in the Database")

    return await crud.create_new_city(
        session=session,
        city=city)


@router.put(path="/cities/{city_id}",
            response_model=schemas.CityBase,
            tags=["Cities"])
async def rewrite_city_info(
        city_id: int,
        city: schemas.CityUpdate,
        session: AsyncSession = Depends(session_manager)):
    check_city_id = await crud.get_city_by_id(session=session,
                                              city_id=city_id)

    if check_city_id is None:
        raise HTTPException(status_code=404,
                            detail="No Such city in the Database")

    return await crud.update_city_info(
        session=session,
        city=city,
        city_id=city_id)


@router.delete(path="/cities/{city_id}",
               tags=["Cities"])
async def delete_city(
        city_id: int,
        session: AsyncSession = Depends(session_manager)):
    check_city_by_id = await crud.get_city_by_id(session=session,
                                                 city_id=city_id)

    if check_city_by_id is None:
        raise HTTPException(status_code=404,
                            detail="No such city in the Database")

    return await crud.delete_city(
        session=session,
        city_id=city_id)
