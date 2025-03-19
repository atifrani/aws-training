from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

app = FastAPI()

# Database configuration
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_HOST = "your-db-instance.rds.amazonaws.com"
DB_NAME = "your_db_name"
DB_PORT = "5432"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define models
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, nullable=False)
    available = Column(Boolean, default=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class BookCreate(BaseModel):
    title: str
    author: str

class UserCreate(BaseModel):
    name: str

# Add a book
@app.post("/books/")
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"message": f"Livre '{book.title}' ajouté !"}

# Search for a book
@app.get("/books/", response_model=List[BookCreate])
def search_book(title: str = "", db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
    return books

# Borrow a book
@app.post("/borrow/")
def borrow_book(title: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.title == title, Book.available == True).first()
    if book:
        book.available = False
        db.commit()
        return {"message": f"Livre '{title}' emprunté avec succès !"}
    raise HTTPException(status_code=404, detail="Livre non disponible ou introuvable.")

# Add a user
@app.post("/users/")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return {"message": f"Utilisateur '{user.name}' ajouté !"}
    except:
        db.rollback()
        raise HTTPException(status_code=400, detail="Utilisateur existe déjà.")

# Delete a user
@app.delete("/users/")
def delete_user(name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == name).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": f"Utilisateur '{name}' supprimé !"}
    raise HTTPException(status_code=404, detail="Utilisateur non trouvé.")

# Run API with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
