let failForm = document.getElementById("failForm");
let rejForm = document.getElementById("rejForm");
let approveConfirmContainer = document.getElementById("approveConfirmContainer");
let blo = document.getElementById("blocker");
let approveText = document.getElementById("approveText");
let chk1 = document.getElementById("chk1");
let chk2 = document.getElementById("chk2");
let approveConfirmBtn = document.getElementById("approveConfirmBtn");

var msg = ["Approving the Volunteer...", "Generating the Certificate...", "Generating the Report...", "Sending an E-Mail...", "Almost done..."];
var currentIndex = 0;

function iterateWithDelay(intervalID) {
    if (currentIndex < msg.length) {
        approveText.innerHTML = '&nbsp; &nbsp;' + msg[currentIndex];
        currentIndex++;
    }
    else {
        clearInterval(intervalID);
        document.getElementById('ApproveForm').submit();
    }
};

function checkboxes(){
    if(chk1.checked && chk2.checked)
        approveConfirmBtn.disabled = false;
    else
        approveConfirmBtn.disabled = true;
};

chk1.addEventListener('change', checkboxes);
chk2.addEventListener('change', checkboxes);

approveConfirmBtn.addEventListener('click', function (event) {

    document.querySelector('.options-container').style.display = 'none';
    document.getElementById('loader').style.display = 'inline-block';
    approveText.style.display = 'inline-block';
    approveConfirmContainer.style.display = "none";
    blo.style.display = "none";
    var intervalID = setInterval(iterateWithDelay, 2100);
    iterateWithDelay(intervalID);
});

document.getElementById('confirmrejectionForm').addEventListener('submit', function (event) {
    event.preventDefault();
    document.getElementById('confirmrejectionBtn').style.display = 'none';
    document.getElementById('rejectText').style.display = 'inline-block';
    document.getElementById('confirmrejectionForm').submit();
});


document.getElementById('confirmfailForm').addEventListener('submit', function (event) {
    event.preventDefault();
    document.getElementById('confirmfailBtn').style.display = 'none';
    document.getElementById('failText').style.display = 'inline-block';
    document.getElementById('confirmfailForm').submit();
});

document.getElementById('approveBtn').addEventListener('click', function() {
    approveConfirmContainer.style.display = "block";
    blo.style.display = "block";
});

document.getElementById('rejectBtn').addEventListener('click', function() {
    rejForm.style.display = "block";
    blo.style.display = "block";
});


document.getElementById('failBtn').addEventListener('click', function() {
    failForm.style.display = "block";
    blo.style.display = "block";
});

document.getElementById('blocker').addEventListener('click', function() {
    rejForm.style.display = "none";
    failForm.style.display = "none";
    approveConfirmContainer.style.display = "none";
    blo.style.display = "none";
});