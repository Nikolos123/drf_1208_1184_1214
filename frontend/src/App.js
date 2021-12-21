import logo from './logo.svg';
import './App.css';
import React from 'react'
import axios from 'axios'
import Cookies from "universal-cookie/lib";
import AuthorList from "./components/Author";
import {HashRouter, BrowserRouter, Route, Link, Switch, Redirect} from "react-router-dom";
import BookList from "./components/Book";
import NotFound404 from "./components/NotFound404";
import BookListAuthor from "./components/BooksAuthor";
import LoginForm from "./components/LoginForm";
import BookForm from "./components/BookForm";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'token': '',
        }
    }


     createBook(name,author){
        const headers = this.get_headers()
        const data = {name:name,author:author}
        axios.post(`http://127.0.0.1:8000/api/book/`,data,{headers}).then(
            response => {

                // let new_book = response.data
                // const  author = this.state.authors.filter((item) => item.id === new_book.author)[0]
                // new_book.author = author
                // this.setState({books: [...this.setState.books,new_book]})
                //

                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({books:[]})
        })


    }




    deleteBook(id){

        const headers = this.get_headers()
        console.log(headers)
        console.log(id)
        axios.delete(`http://127.0.0.1:8000/api/book/${id}`,{headers}).then(
            response => {
                // this.setState(
                //     {
                //         'books': this.state.books.filter((item) => item.id !==id)
                //     }
                // )
                this.load_data()
            }
        ).catch(error => {
            console.log(error)
            this.setState({books:[]})
        })


    }

    set_token(token) {
        // console.log(token)
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token},()=>this.load_data())
    }

    is_auth() {
        return !!this.state.token
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token},()=>this.load_data())
    }


    get_token(username, password) {
        const data = {username: username, password: password}
        console.log(data)
        axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(
            response => {
                this.set_token(response.data['token'])
            }
        ).catch(error => alert('Неверный логин или пароль'))

    }

    load_data() {
        const headers = this.get_headers()
        console.log(headers)
        axios.get('http://127.0.0.1:8000/api/authors/',{headers}).then(
            response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({authors:[]})
        })


        axios.get('http://127.0.0.1:8000/api/book/',{headers}).then(
            response => {
                const books = response.data
                this.setState(
                    {
                        'books': books
                    }
                )
            }
        ).catch(error => {
            console.log(error)
            this.setState({books:[]})
        })

    }


    get_headers() {
        let headers = {
            'Content-Type': 'application/json',

        }

        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    componentDidMount() {
        this.get_token_from_storage()
    }


    render() {
        return (
            <div>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'> Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'> Books</Link>
                            </li>
                            <li>
                                {this.is_auth() ? <button onClick={() => this.logout()}> Logout
                                </button> : <Link to='/login'> Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}
                                                                              deleteBook={(id) => this.deleteBook(id)}/>}/>
                         <Route exact path='/books/create' component={() =>
                             <BookForm authors={this.state.authors} createBook={(name,author) => this.createBook(name,author)}/>}/>

                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route path='/author/:id'>
                            <BookListAuthor books={this.state.books} authors={this.state.authors}/>
                        </Route>
                        <Redirect from='/authors' to='/'/>

                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>
        );
    }


}

export default App;
