from fastapi import FastAPI, Header, HTTPException, Request

from api.books.models import Book
from auth import verify_signature
from openlibrary import get_book_info_by_isbn

app = FastAPI()


@app.post("/books")
async def create_book(request: Request, Key: str = Header(...), Sign: str = Header(...)):
    body = await request.json()
    isbn = body.get("isbn")
    if not isbn:
        raise HTTPException(status_code=400, detail="ISBN is required.")

    if not verify_signature(Key, Sign, isbn):
        raise HTTPException(status_code=401, detail="Invalid signature.")

    book_data = get_book_info_by_isbn(isbn)
    if not book_data:
        raise HTTPException(status_code=404, detail="Book not found.")

    book = Book(book_data)
    return {"data": {"book": book.dict()}}
