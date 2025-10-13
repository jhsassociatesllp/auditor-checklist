from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class AuditForm(BaseModel):
    audit_date: str
    delivery_centre: str
    time_in: str
    time_out: str
    warehouse_address: str
    warehouse_name: str
    auditor_name: str
    warehouse_manager_name: str
    previous_audit_date: str
    previous_auditor_name: str
    previous_auditor_type: str
    agency_name: str | None = None  # Optional if not External
    warehouse_capacity: float
    capacity_utilization: float