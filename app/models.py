from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class UserDB(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
    primary_key=True, index=True
    )
    borrower_name: Mapped[str] = mapped_column(
    String(50), nullable=False
    )
    purpose: Mapped[str] = mapped_column(
    String(255), unique=True, index=True,
    nullable=False
    )
    loan_days: Mapped[int] = mapped_column(Integer)
    equipment_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    status: Mapped[str] = mapped_column(
        String(50), nullable=False
    )