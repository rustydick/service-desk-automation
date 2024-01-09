"""Database module."""

from motor.motor_asyncio import AsyncIOMotorClient

from ..utils.config import config

client = AsyncIOMotorClient(config["mongodb_url"], uuidRepresentation="standard")
db = client[config["mongodb_db_name"]]
