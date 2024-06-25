#!/usr/bin/env python

import typing
import sqlite3
import strawberry
from pathlib import Path
from decouple import config

base_dir = Path(__file__).resolve().parents[1]
db_dir = base_dir / 'db'
db_file = db_dir / 'cooling_centers.db'
conn = sqlite3.connect(db_file)


def get_cooling_centers(city_county: typing.Optional[str] = None):
    columns = [
        'city_county',
        'location_name',
        'address',
        'phone',
        'hours_of_operation',
        'latitude_longitude'
    ]
    query = f"SELECT {', '.join(columns)} FROM cooling_centers"
    if city_county:
        query += f" WHERE city_county LIKE '%{city_county}%'"
    result = conn.execute(query)
    return [
        CoolingCenter(
            city_county=row[0],
            location_name=row[1],
            address=row[2],
            phone=row[3],
            hours_of_operation=row[4],
            latitude_longitude=row[5],
        )
        for row in result
    ]


@strawberry.type
class CoolingCenter:
    city_county: str
    location_name: str
    address: str
    phone: str
    hours_of_operation: str
    latitude_longitude: str


@strawberry.type
class Query:
    cooling_centers: typing.List[CoolingCenter] = strawberry.field(resolver=get_cooling_centers)


schema = strawberry.Schema(query=Query)
