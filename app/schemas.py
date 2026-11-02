from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints

borrowerStr = Annotated [str, StringConstraints(min_length=2, max_length=60)]
purposeStr = Annotated [str, StringConstraints(min_length=5, max_length=100)]
UniqueIdStr = Annotated [str, StringConstraints(pattern= r"^S\d{7}$")]
class UserCreate(BaseModel):
    borrower_name:borrowerStr
    email:EmailStr
    loan_days : int = Field(gt=1, lt=14)
    id:UniqueIdStr
    purpose: purposeStr
    equipment_id: UniqueIdStr

