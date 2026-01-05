from odmantic import AIOEngine, Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    # Collection Name 지정.
    model_config = {"collection": "books"}


# MongoDB: db -> collection -> document
# MySQL: db -> table -> row
