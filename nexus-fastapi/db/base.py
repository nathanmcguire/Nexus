from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    __name__: str

    # Automatically generate table names if not explicitly defined
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()