import logo from './logo.svg';
import './App.css';
import React from 'react'
import axios from 'axios'
import AuthorList from "./components/Author";
import {HashRouter, BrowserRouter, Route, Link, Switch,Redirect} from "react-router-dom";
import BookList from "./components/Book";
import NotFound404 from "./components/NotFound404";
import BookListAuthor from "./components/BooksAuthor";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/').then(
            response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }
        ).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/book/').then(
            response => {
                const books = response.data
                this.setState(
                    {
                        'books': books
                    }
                )
            }
        ).catch(error => console.log(error))
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
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList books={this.state.books}/>}/>
                        <Route path='/author/:id'>
                            <BookListAuthor books={this.state.books} authors={this.state.authors}/>
                        </Route>
                        <Redirect from='/authors' to='/' />

                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>
        );
    }


}

export default App;
