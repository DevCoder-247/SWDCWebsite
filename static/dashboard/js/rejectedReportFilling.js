const myForm = document.getElementById("myForm");
const submitBtn = document.getElementById("submitBtn");
const errorMessage = document.getElementById("errorMessage");
const userName = document.getElementById("userName");
const ans1 = document.getElementById("ans1");
const ans2 = document.getElementById("ans2");
const ans3 = document.getElementById("ans3");
const ans4 = document.getElementById("ans4");
const ans5 = document.getElementById("ans5");
const ans6 = document.getElementById("ans6");
const ans1_Hidden = document.getElementById("ans1_Hidden");
const ans2_Hidden = document.getElementById("ans2_Hidden");
const ans3_Hidden = document.getElementById("ans3_Hidden");
const ans4_Hidden = document.getElementById("ans4_Hidden");
const ans5_Hidden = document.getElementById("ans5_Hidden");
const ans6_Hidden = document.getElementById("ans6_Hidden");
const url = document.getElementById("url");
const urlError = document.getElementById("urlError");
var countMessage1 = document.getElementById("countMessage1");
var countMessage2 = document.getElementById("countMessage2");
var countMessage3 = document.getElementById("countMessage3");
var countMessage4 = document.getElementById("countMessage4");
var countMessage5 = document.getElementById("countMessage5");
var countMessage6 = document.getElementById("countMessage6");
const guardian_faculty = document.getElementById('guardian_faculty');
const guardianFacultyNotChosen = document.getElementById('guardianFacultyNotChosen');

var dictionary = {}
dictionary.ans1 = '1';
dictionary.ans2 = '2';
dictionary.ans3 = '3';
dictionary.ans4 = '4';
dictionary.ans5 = '5';
dictionary.ans6 = '6';


function checkUrl() {
    var urlVal = url.value;
    urlVal = urlVal.trim();
    if (urlVal === "http://" || urlVal === "https://") {
        urlError.innerHTML = "Your URL should be a valid URL. It has only http:// or https:// ";
        return false;
    }
    if (!(urlVal.includes("https://") || urlVal.includes("http://"))) {
        urlError.innerHTML = "Your URL must contain a http:// or https://";
        return false;

    }
    if (urlVal.includes(" ") || urlVal.includes(",")) {
        urlError.innerHTML = "Your URL cannot have a blank space or a comma.";
        return false;
    }
    return true;
};


submitBtn.addEventListener('click', function () {
    var c1 = (ans1.value.match(/[a-zA-Z]/g) || []).length;
    var c2 = (ans2.value.match(/[a-zA-Z]/g) || []).length;
    var c3 = (ans3.value.match(/[a-zA-Z]/g) || []).length;
    var c4 = (ans4.value.match(/[a-zA-Z]/g) || []).length;
    var c5 = (ans5.value.match(/[a-zA-Z]/g) || []).length;
    var c6 = (ans6.value.match(/[a-zA-Z]/g) || []).length;

    if(c1<=700)
        countMessage1.innerHTML = (700-c1).toString() + ' more characters needed.';
    else
        countMessage1.innerHTML = '';

    if(c2<=700)
        countMessage2.innerHTML = (700-c2).toString() + ' more characters needed.';
    else
        countMessage2.innerHTML = '';

    if(c3<=700)
        countMessage3.innerHTML = (700-c3).toString() + ' more characters needed.';
    else
        countMessage3.innerHTML = '';

    if(c4<=700)
        countMessage4.innerHTML = (700-c4).toString() + ' more characters needed.';
    else
        countMessage4.innerHTML = '';

    if(c5<=700)
        countMessage5.innerHTML = (700-c5).toString() + ' more characters needed.';
    else
        countMessage5.innerHTML = '';

    if(c6<=700)
        countMessage6.innerHTML = (700-c6).toString() + ' more characters needed.';
    else
        countMessage6.innerHTML = '';




    if (c1 >= 700 && c2 >= 700 && c3 >= 700 && c4 >= 700 && c5 >= 700 && c6 >= 700) {
        if (checkUrl())
        {
            if(guardian_faculty.value === 'Choose')
            {
                guardianFacultyNotChosen.style.display = 'block';
            }
            else
            {
                myForm.submit();
            }
        }
    }
    else
    {
        errorMessage.style.display = 'block';
    }
});


var textareas = document.querySelectorAll('textarea');
textareas.forEach(function (textarea) {
    textarea.addEventListener('paste', function (e) {
        e.preventDefault();
        alert('Please type the answers in your own words instead of copy-pasting.');
    });
});


textareas.forEach(function (textarea) {
    textarea.addEventListener('input', function () {
        var hiddenID = this.id.toString() + '_Hidden'
        const previousVal = document.getElementById(hiddenID);
        var diff = this.value.length - previousVal.value.length;
        if (diff > 15) {
            this.value = previousVal.value
            alert('You can enter at max 15 characters at once.');
        }
        else
            previousVal.value = this.value
    })
});




const logged_in_hours = document.getElementById('hours');
const logged_in_minutes = document.getElementById('minutes');
const time_left = document.getElementById('time_left');
function updateTimeLeft() {
    var currentDate = new Date();
    var timeLeft = 250 - (currentDate.getHours() * 60 + currentDate.getMinutes() - 330 - logged_in_hours.value * 60 - logged_in_minutes.value);
    time_left.innerHTML = timeLeft;
}

setInterval(updateTimeLeft, 60000);
updateTimeLeft();


guardian_faculty.addEventListener('change', function(){
    alert('ALERT:\n\nYou have chosen your Guardian Faculty as ' + guardian_faculty.value + '.\n\nNote that "Guardian Faculty" may not necessarily be your class teacher.\n\nGuardian Faculty is one who is allotted to you by the DESH Department.');
});