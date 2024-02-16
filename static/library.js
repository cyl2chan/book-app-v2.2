//books - main div holding all the books
const books = document.querySelector(".books");
const addBook = document.querySelector('.add-book');
const modal = document.querySelector('#modal');
const closeModal = document.querySelector('.close');

window.addEventListener('click', (e) => {
    if (e.target == modal) {
        modal.style.display = 'none';
    }
})

closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
})

addBook.addEventListener('click', () => {
    modal.style.display = 'block';
    //document.querySelector('.form-title').textContent = 'Add Book';
    //document.querySelector('.form-add-button').textContent = 'Add';
})

function Book(title, author, pages, read) {
    this.title = title;
    this.author = author;
    this.pages = pages;
    this.read = read;
    this.id = Math.floor(Math.random() * 10000000000);
}


function addBookToLibrary(title, author, pages, read) {
    myLibrary.push(new Book(title, author, pages, read));
    saveAndDisplayBooks();
}


const addBookForm = document.querySelector('.add-book-form');
addBookForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const data = new FormData(e.target);
    let newBook = {}; //temporary empty object
    for (let [name, value] of data) {
        if (name === 'book-read') {
            newBook['book-read'] = true;
        } else {
            newBook[name] = value || "";
        }
    }

    if (!newBook['book-read']) {
        newBook['book-read'] = false;
    }

    if (document.querySelector('.form-title').textContent === 'Edit Book') {
        let id = e.target.id;
        let editBook = myLibrary.filter(book => book.id == id)[0];
        editBook.title = newBook["book-title"];
        editBook.author = newBook['book-author'];
        editBook.pages = newBook['book-pages'];
        editBook.read = newBook['book-read'];
        saveAndDisplayBooks();
    } else {
        addBookToLibrary(newBook['book-title'], 
        newBook['book-author'], 
        newBook['book-pages'], 
        newBook['book-read']);
    };

    addBookForm.reset();
    modal.style.display = 'none';
});



//array of books 
let myLibrary = [
    
    {
    title: 'Can\'t Hurt Me',
    author: 'David Goggins',
    pages: 326,
    read: true,
    id: 8726347298,
},{
    title: 'Extreme Ownership',
    author: 'Jocko Willink',
    pages: 332,
    read: false,
    id: 89072983723,
}
    
];


/*
“localStorage.getItem('library') === null”  will be true if user has never ever saved any book in the localStorage  before,
that means when he opens the website for the first time. That’s why the 'library' item will be null. 
But once books are saved and user deletes them by pressing the delete icon. Then even if there is no book in the localStorage , 
the above condition doesn’t hold. This is because localStorage will have an empty array “[]” stored in this condition and not null.

That’s where the second statement  “localStorage.getItem('library') === '[]'” comes into play and checks for an empty array in localStorage.
*/
function addLocalStorage() {
    if (localStorage.getItem('library') === null || localStorage.getItem('library') === '[]') {
        saveAndDisplayBooks(); //if no books saved in LS, show default 2 books
    } else {
        //if books are saved in LS, show all of them
        myLibrary = JSON.parse(localStorage.getItem('library'));
        saveAndDisplayBooks();
    }
}


//helper function to create html elements with text content and classes
function createBookElement(el, content, className) {
    const element = document.createElement(el);
    element.textContent = content;
    element.setAttribute('class', className);
    return element;
}

//helper function to create an input checkbox for if a book is read with event listener
function createReadElement(bookItem, book) {
    let read = document.createElement('div');
    read.setAttribute('class', 'book-read');
    read.appendChild(createBookElement('h1', 'Read?', 'book-read-title'));
    let input = document.createElement('input');
    input.type = 'checkbox';
    input.addEventListener('click', (e) => {
        if (e.target.checked) {
            bookItem.setAttribute('class', 'card book read-checked');
            book.read = true;
            saveAndDisplayBooks();
        } else {
            bookItem.setAttribute('class', 'card book read-unchecked');
            book.read = false;
            saveAndDisplayBooks();
        }
    });
    if (book.read) {
        input.checked = true;
        bookItem.setAttribute('class', 'card book read-checked');
    }
    read.appendChild(input);
    return read;
}

function fillOutEditForm(book) {
    modal.style.display = 'block';
    document.querySelector('.form-title').textContent = 'Edit Book';
    document.querySelector('.form-add-button').textContent = 'Edit';
    document.querySelector('.add-book-form').setAttribute('id', book.id);
    document.querySelector('#book-title').value = book.title || '';
    document.querySelector('#book-author').value = book.author || '';
    document.querySelector('#book-pages').value = book.pages || '';
    document.querySelector('#book-read').checked = book.read;
}


//create the edit icon w/ event listener
function createEditIcon(book) {
    const editIcon = document.createElement('img');
    editIcon.src = '../static/icons/pencil.svg';
    editIcon.setAttribute('class', 'edit-icon');
    editIcon.addEventListener('click', () => {
        fillOutEditForm(book);
    });
    return editIcon;
}

//create three icons at the bottom of each card (they don't do anything yet)
function createIcons() {
    const div = createBookElement('div', null, 'cardIcons');
    const icon1 = document.createElement('img');
    icon1.src = '../static/icons/star-plus-outline.svg';
    const icon2 = document.createElement('img');
    icon2.src = '../static/icons/eye-plus-outline.svg';
    const icon3 = document.createElement('img');
    icon3.src = '../static/icons/share-variant-outline.svg';

    div.appendChild(icon1);
    div.appendChild(icon2);
    div.appendChild(icon3);
    return div;
}

function deleteBook(index) {
    myLibrary.splice(index,1);
    saveAndDisplayBooks();
}


//function to create all book content on the card
function createBookItem(book, index) {
    const bookItem = document.createElement('div');
    bookItem.setAttribute('id', index);
    bookItem.setAttribute('key', index);
    bookItem.setAttribute('class', 'card book');
    bookItem.appendChild(
        createBookElement('h1', `${book.title}`, 'book-title')
    );
    bookItem.appendChild(
        createBookElement('h1', `Author: ${book.author}`, 'book-author')
    );
    bookItem.appendChild(
        createBookElement('h1', `Pages: ${book.pages}`, 'book-pages')
    );
    bookItem.appendChild(createReadElement(bookItem, book));
    bookItem.appendChild(createBookElement('button', 'X', 'delete'));
    bookItem.appendChild(createIcons());
    bookItem.appendChild(createEditIcon(book));

    bookItem.querySelector('.delete').addEventListener('click', () => {
        deleteBook(index);
    })

    books.insertAdjacentElement('afterbegin', bookItem);
}

//function to display all the books
function displayBooks() {
    books.textContent = '';
    myLibrary.map((book, index) => {
        createBookItem(book, index)
    });
}

function saveAndDisplayBooks() {
    localStorage.setItem('library', JSON.stringify(myLibrary));
    displayBooks();
}

//display on 
addLocalStorage();


//function of show hide icons
/*
$(document).ready(function(){
    $("#hideBtn").click(function(){
        $(".hide-show-right").hide();
        $("#hideBtn").hide();
        $("#showBtn").show();
    });

    $("#showBtn").click(function(){
        $(".hide-show-right").show();
        $("#showBtn").hide();
        $("#hideBtn").show();
    });
})
*/