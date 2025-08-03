import requests

def search_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=5"
    response = requests.get(url)

    if response.status_code == 200:
        books = response.json().get('items', [])
        if not books:
            print("❌ No books found.")
            return

        print(f"\n Top 5 books for '{query}':\n")
        for i, book in enumerate(books, 1):
            volume_info = book.get('volumeInfo', {})
            title = volume_info.get('title', 'No Title')
            authors = volume_info.get('authors', ['Unknown Author'])
            print(f"{i}. {title} by {', '.join(authors)}")
    else:
        print("❌ Failed to fetch books. Check your internet connection.")

def book_chatbot():
    print(" Hello! I'm BookBot - I find books for you from the web!")
    while True:
        query = input("\nWhat kind of books are you looking for? (e.g., mystery, love, fantasy): ").strip()
        search_books(query)

        again = input("\n Want to search again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\n Thank you for using BookBot! Happy reading!")
            break

book_chatbot()
