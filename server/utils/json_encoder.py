"""
Custom JSON encoder for MongoDB ObjectId.
"""

import json
from bson import ObjectId
from datetime import datetime

class MongoJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder that can handle MongoDB ObjectId and datetime objects.
    """
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
