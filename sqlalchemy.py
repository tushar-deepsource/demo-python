import sqlalchemy
from sqlalchemy import select

user = sqlalchemy.Table(
    "user",
    sqlalchemy.MetaData(),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("org", sqlalchemy.String),
)

select([user.id, user.name]).where((user.org == "DeepSource") and (user.active == True))
