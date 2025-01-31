const instructionsContainer = document.getElementById("instructionsContainer");
const proceedBtn = document.getElementById("proceedBtn");
const proceedMessage = document.getElementById("proceedMessage");
var currentIndex = 0;
var proceedStatus = ["Establishing secure connection with our servers...", "Initialising Plagarism Detection Software...", "Encrpyting your data...", "Allocating back-end resource...", "Almost done...", "Proceeding to Report Filling page..."];

function uncheckAllCheckboxes()
{
    const ckboxes = document.querySelectorAll('input[type="checkbox"]')
    ckboxes.forEach(function (checkbox) {
        checkbox.checked = false;
    });
    proceedBtn.disabled = true;
}

function iterateWithDelay(intervalID) {
    if (currentIndex < proceedStatus.length) {
        proceedMessage.innerHTML = proceedStatus[currentIndex]
        currentIndex++;
    }
    else {
        clearInterval(intervalID);
        uncheckAllCheckboxes();
        window.location.href = '/v/report-filling';
    }
};

proceedBtn.addEventListener('click', function () {
    proceedBtn.style.display = 'none';
    proceedMessage.style.display = 'block';
    document.getElementById("loader").style.display = 'block';
    var intervalID = setInterval(iterateWithDelay, 3000);
    iterateWithDelay(intervalID);
});


function checkCheckboxes() {
    const ckboxes = document.querySelectorAll('input[type="checkbox"]')
    var state = true;
    ckboxes.forEach(function (checkbox) {
        if (!checkbox.checked) {
            state = false;
        }
    });
    return state;
}
const checkboxes = document.querySelectorAll('input[type="checkbox"]')

checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
        var state = checkCheckboxes();
        if (state) {
            proceedBtn.disabled = false;
        }
        else {
            proceedBtn.disabled = true;
        }
    })
})