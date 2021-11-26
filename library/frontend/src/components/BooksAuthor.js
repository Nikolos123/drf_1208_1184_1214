import {useParams} from "react-router-dom";
import React from "react";


const BookItem = ({book,authors}) => {
    return (
        <tr>
            <td>{book.id}</td>
            <td>{book.name}</td>
            <td>

                {book.author.map((authorID) =>{return authors.find((author) => author.id == authorID).first_name})}

            </td>
        </tr>
    )
}

const BookListAuthor=({books,authors}) =>{

    let {id} = useParams();
    console.log(id)
    let filtered_items = books.filter((book => book.author.includes(parseInt(id))))


     return (
        <table>
            <th>Id</th>
            <th>Name</th>
            <th>Author</th>
            {filtered_items.map((book) => < BookItem book={book} authors={authors}/> )}
        </table>
    )


}


export default BookListAuthor