from flask import Flask, jsonify, request

app = Flask(__name__)

# Creating list with values of type dictionary for example

books = [
    {
        "id": 1,
        "title": "O senhor dos aneis - a sociedade do anel",
        "author": "J.R.R Tolkien",
    },
    {
        "id": 2,
        "title": "Harry potter e a pedra filosofal",
        "author": "J.K Howling",
    },
    {
        "id": 3,
        "title": "James clear",
        "author": "hábitos atômicos",
    },
]

"""
Next step for action: read(all)
                      read(id)
                      edit
                      delete 
"""


# Need create function for each endpoint
@app.route("/books", methods=["GET"])
def get_book():
    return jsonify(books)


# Now create function for return data about book based in ID
@app.route("/books/<int:id>", methods=["GET"])
def get_book_id(id):
    for book in books:
        if (
            book.get("id") == id
        ):  # The value of id after signal equals this is reference a value parameter
            return jsonify(book)


# Creating endpoint of update data of books
@app.route("/books/<int:id>", methods=["PUT"])
def update_book_id(id):
    book_updated = (
        request.get_json()
    )  # Variable book_updated for storing data of request
    for index, book in enumerate(books):
        if book.get("id") == id:
            books[index].update(book_updated)
            return jsonify(books[index])


# Creating function for inserting book
@app.route("/books/", methods=["POST"])
def create_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)


# And delete book with value ID
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get("id") == id:
            del books[index]

    return jsonify(books)


# Action for run application
app.run(port=5000, host="localhost", debug=True)
