import requests


def get_book_data_by_isbn(isbn: str):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    data = response.json()

    print("Raw API response:", data)

    book_info = data.get(f"ISBN:{isbn}")
    if not book_info:
        return None

    print("Book info:", book_info)

    title = book_info.get("title", "Unknown")
    print("Title found:", title)

    authors = book_info.get("authors", [])
    print("Authors data:", authors)
    author_name = authors[0]["name"] if authors else "Unknown"
    print("Author name:", author_name)

    result = {
        "isbn": isbn,
        "title": title,
        "author": author_name,
        "cover": book_info.get("cover", {}).get("large", None),
        "published": int(book_info.get("publish_date", "0")[:4]) if "publish_date" in book_info else None,
        "pages": book_info.get("number_of_pages")
    }

    print("Final processed data:", result)
    return result
