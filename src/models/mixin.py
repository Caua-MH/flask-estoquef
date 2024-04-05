from typing import Optional

import sqlalchemy as sa
from sqlalchemy import Mapped, mapped_column
from sqlalchemy.types import  DateTime

class DataModelMixin:
    dta_cadastro: Mapped[Datetime] = mapped_column(DateTime,
                                                   nullable=False,
                                                   server_default=func.now())
    dta_atualizado: Mapped[Optional[datetime]] = mapped_column(DateTime,
                                                               nullable=True,
                                                               server_default=func.now(),
                                                               onupdate=func.now())