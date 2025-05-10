"""
MongoDB connection and operations module.
"""
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from app.core.config import MONGODB_URI, DATABASE_NAME


class MongoDB:
    """MongoDB connection manager."""

    _instance = None
    _client: MongoClient = None
    _db: Database = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDB, cls).__new__(cls)
            cls._client = MongoClient(MONGODB_URI)
            cls._db = cls._client[DATABASE_NAME]
        return cls._instance

    def get_collection(self, collection_name: str) -> Collection:
        """Get a MongoDB collection.

        Args:
            collection_name: Name of the collection

        Returns:
            Collection object
        """
        return self._db[collection_name]

    def close_connection(self):
        """Close the MongoDB connection."""
        if self._client:
            self._client.close()
            self._client = None
            self._db = None
            MongoDB._instance = None
