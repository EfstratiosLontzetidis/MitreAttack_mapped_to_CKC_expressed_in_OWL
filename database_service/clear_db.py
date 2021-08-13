from database_service.database import ClientDB


def clear_db():
    collections = ["default",
                   "test"]

    for collection in collections:
        col = ClientDB.db[collection]
        col.drop()
