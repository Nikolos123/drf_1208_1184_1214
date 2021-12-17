import React from "react";
import App from "../App";


const BookItem = ({book,deleteBook}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>{book.author}</td>
            <td>
                <button onClick={() => deleteBook(book.id)} type='button'>
                    Delete
                </button>
            </td>
        </tr>
    )
}

const BookList = ({books,deleteBook}) => {

    return (
        <table>
            <tr>
                <th>Id</th>
                <th>Name</th>
                <th>Author</th>
                <th>
                </th>
            </tr>
            {books.map((book) => < BookItem book={book} deleteBook={deleteBook}/>)}
        </table>
    )
}

export default BookList;