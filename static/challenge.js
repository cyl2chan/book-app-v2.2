const goalNumber= document.querySelector('#goal');
const updateBtn = document.querySelector('#update-btn');
const goalDiv = document.querySelector('#goal-div');
const progressDiv = document.querySelector('#progress-div');
const progressBar = document.querySelector('#progressbar');
const progressLabel = document.querySelector('#progress-label');
const progressPercent = document.querySelector('#progressPercent');

//Local Storage: create output of "You have read X of X books" (Progress div)
var myGoal = localStorage.getItem('goal');
var myLibrary = JSON.parse(localStorage.getItem('library'));
var bookReadNum = 0;


//progress in the progress bar
var booksRead;
if (libraryEmpty()) { //Setting booksread to 0 if there're no books in the library
    booksRead = 0;
} else {
    booksRead = myLibrary.filter(function(book) {
        if (book.read === true) {
            return true
        } else {
            return false
        }
    }).length;
}

//when Library is empty
function libraryEmpty() {
    return (myLibrary === null || myLibrary.length === 0)
}


//showing progress page if goal is already set
showProgressPage();
function showProgressPage() {
    /*
    show Progress page if goal is already saved in localStorage.
    if there's no goal saved, user will be shpown the goal page by default
    */
    if (myGoal !== null && myGoal !== '0'){
        
        //setting up saved progress
        let progressPercentNum = Math.round(booksRead / myGoal *100);
        progressLabel.style.width =  `${progressPercentNum}%`;   
        progressPercent.textContent = `${progressPercentNum}%`;

        document.querySelector('#progressLine').textContent = `You have read ${booksRead} of ${myGoal} books`;

        //showing the page
        goalDiv.style.display = 'none';
        progressDiv.style.display = 'flex';
    }
    

}


/*
function outputProgLine() {
    var myGoal = localStorage.getItem('goal');
    document.querySelector('#progressLine').textContent = `You have read ${booksRead} of ${myGoal} books`;
}
*/
//add EventListener to 'Update' button (Goal div)
updateBtn.addEventListener('click', (e) => {  //'submit' is only for forms
    e.preventDefault();

    //add Event Listener to goal input??

    //if input box has a number, save number; if not, no reponse, or console.log said "Please enter a number"
    /*
    If user doesn't write anything in goal input, value of goal input will be "".
    So condition "goalNumber.value !== null" will still be true
    */
    if (goalNumber.value !== "" && goalNumber.value !== '0') {
        //myGoal === goalNumber.value; //solve bug!!!
        //saveGoal();
        localStorage.setItem('goal', goalNumber.value);
        goalDiv.style.display = 'none';
        progressDiv.style.display = 'flex'; //already 'block' in CSS, so just 'flex' here

        var myGoal = localStorage.getItem('goal');
        document.querySelector('#progressLine').textContent = `You have read ${booksRead} of ${myGoal} books`;
        progressBar1();

    } else if (goalNumber.value == "" || goalNumber.value == '0') { //
        console.log('Please enter a number!');   //even when no number in goal input, 'Please enter a number!' still doesn't show up
    }

})



//progress bar and %

function progressBar1() {
    var myGoal = localStorage.getItem('goal');
    let progressPercentNum = Math.round(booksRead / myGoal *100);

    //var entireBarWidth = progressBar.offsetWidth;
    //var progressLabelWidth = progressPercentNum/100 * entireBarWidth;

    progressLabel.style.width =  `${progressPercentNum}%`;   
    progressPercent.textContent = `${progressPercentNum}%`;
}


//add EventListener to 'Cancel' button (Goal div)
const cancelBtn = document.querySelector('#cancel-btn');

cancelBtn.addEventListener('click', (e) => {
    //when cancled btn is clicked, progress page is only shown when goal is set and LIbrary isn't empty
    if (localStorage.getItem("goal") !== null && !libraryEmpty()) {
        goalDiv.style.display = 'none';
        progressDiv.style.display = 'flex';
    }
})



//create 'Edit' button (Progress div)
function createProgressEdit() {
    const editProgIcon = document.createElement('img');
    editProgIcon.src = '../static/icons/pencil.svg';
    editProgIcon.setAttribute('class', 'edit-prog-icon');

    progressDiv.insertBefore(editProgIcon, progressDiv.children[1]); //insert icon b4 Progress Line

    editProgIcon.addEventListener('click', () => {
        goalDiv.style.display = 'flex';
        progressDiv.style.display = 'none';
    });
    return editProgIcon;
}

createProgressEdit();









