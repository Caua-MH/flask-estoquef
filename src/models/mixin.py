from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import  DateTime

class DataModelMixin:
    dta_cadastro: Mapped[DateTime] = mapped_column(DateTime,
                                                   nullable=False,
                                                   server_default=sa.func.now())
    dta_atualizado: Mapped[Optional[DateTime]] = mapped_column(DateTime,
                                                               nullable=True,
                                                               server_default=sa.func.now(),
                                                               onupdate=sa.func.now())