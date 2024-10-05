from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app import Base


class Task(Base):
    __bind_key__ = "Task"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('Customer.id'), nullable=True)
    task_text: Mapped[str] = mapped_column(String(240), nullable=False)
    load_type: Mapped[str] = mapped_column(String(240), nullable=True)
    date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now(), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    completion_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=func.now(), nullable=True)
    __tablename__ = "Task"
    
    def __init__(self, id: int, customer_id: int, task_text: str, load_type: str, date: datetime, completed: bool, completion_date: datetime):
        self.id: int = id
        self.customer_id: int = customer_id
        self.task_text: str = task_text
        self.load_type: str = load_type
        self.date: datetime = date
        self.completed: bool = completed
        self.completion_date: datetime = completion_date
        
    def __repr__(self) -> str:
        return f""


class TaskLocation(Base):
    __bind_key__ = "TaskLocation"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey('Task.id'), nullable=False)
    task_city: Mapped[str] = mapped_column(String(24), nullable=True)
    task_postal_code: Mapped[str] = mapped_column(String(6), nullable=True)
    task_street: Mapped[str] = mapped_column(String(12), nullable=True)
    task_house: Mapped[int] = mapped_column(Integer, nullable=True)
    __tablename__ = "TaskLocation"

    def __init__(self, id: int, task_id: int, task_city: str, task_postal_code: str, task_street: str, task_house: int):
        self.id: int = id
        self.task_id: int = task_id
        self.task_postal_code: str = task_postal_code
        self.task_city: str = task_city
        self.task_street: str = task_street
        self.task_house: int = task_house
    
    def __repr__(self) -> str:
        return f""


class TaskIncome(Base):
    __bind_key__ = "TaskIncome"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey('Task.id'), nullable=False)
    task_income: Mapped[float] = mapped_column(Float, nullable=True)
    __tablename__ = "TaskIncome"

    def __init__(self, id: int, task_id: int, task_income: float):
        self.id: int = id
        self.task_id: int = task_id
        self.task_income: float = task_income

    def __repr__(self) -> str:
        return f""


class Customer(Base):
    __bind_key__ = "Customer"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    customer_name: Mapped[str] = mapped_column(String(12), nullable=False)
    customer_surname: Mapped[str] = mapped_column(String(12), nullable=False)
    customer_street: Mapped[str] = mapped_column(String(12), nullable=True)
    customer_house: Mapped[int] = mapped_column(Integer, nullable=True)
    customer_city: Mapped[str] = mapped_column(String(24), nullable=True)
    customer_postal_code: Mapped[str] = mapped_column(String(6), nullable=True)
    __tablename__ = "Customer"
    
    def __init__(self, id: int, customer_name: str, customer_surname: str, customer_street: str, customer_house: int, customer_city: str, customer_postal_code: str):
        self.id: int = id
        self.customer_name: str = customer_name
        self.customer_surname: str = customer_surname
        self.customer_street: str = customer_street
        self.customer_house: int = customer_house
        self.customer_city: str = customer_city
        self.customer_postal_code: str = customer_postal_code

    def __repr__(self) -> str:
        return f"{self.id} {self.customer_name} {self.customer_surname}"


class User(Base):
    __bind_key__ = "User"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    nickname: Mapped[str] = mapped_column(String(24), nullable=False)
    password: Mapped[str] = mapped_column(String(48), nullable=False)
    email: Mapped[str] = mapped_column(String(48), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    __bind_key__ = "User"
    
    def __init__(self, id: int, nickname: str, password: str, email: str, is_superuser: bool):
        self.id: int = id
        self.nickname: str = nickname
        self.password: str = password
        self.email: str = email
        self.is_superuser: bool = is_superuser
    
    def __repr__(self) -> str:
        return f""
    