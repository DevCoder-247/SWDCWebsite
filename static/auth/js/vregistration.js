const emailField = document.getElementById("email");
const emailContainer = document.getElementById("emailContainer");
const emailLabel = document.getElementById("emailLabel");
const emailCheckbox = document.getElementById("emailCheckbox");

const prnField = document.getElementById("prn");
const PRNContainer = document.getElementById("PRNContainer");
const PRNLabel = document.getElementById("PRNLabel");
const PRNCheckbox = document.getElementById("PRNCheckbox");

const phoneField = document.getElementById("phone");
const phnoContainer = document.getElementById("phnoContainer");
const phnoLabel = document.getElementById("phnoLabel");
const phnoCheckbox = document.getElementById("phnoCheckbox");

const divField = document.getElementById("div");
const divContainer = document.getElementById("divContainer");
const divLabel = document.getElementById("divLabel");
const divCheckbox = document.getElementById("divCheckbox");

emailField.addEventListener('input', showEmailCheckbox);
prnField.addEventListener('input', showPRNCheckbox);
phoneField.addEventListener('input', showPhNoCheckbox);
divField.addEventListener('change', showDivCheckbox);


function showEmailCheckbox() {
    const text = 'My Email ID is ' + emailField.value;
    if (emailField.value.length === 0) {
        emailContainer.style.display = 'none';
        emailCheckbox.checked = false;
        checkCheckboxes();
    }
    else {
        emailContainer.style.display = 'block';
        emailLabel.textContent = text;
    }
};

function showPRNCheckbox() {
    const text = 'My PRN is ' + prnField.value;
    if (prnField.value.length === 0) {
        PRNContainer.style.display = 'none';
        PRNCheckbox.checked = false;
        checkCheckboxes();
    }
    else {
        PRNContainer.style.display = 'block';
        PRNLabel.textContent = text;
    }
};

function showPhNoCheckbox() {
    const text = 'My Phone Number is ' + phoneField.value;
    if (phoneField.value.length === 0) {
        phnoContainer.style.display = 'none';
        phnoCheckbox.checked = false;
        checkCheckboxes();
    }
    else {
        phnoContainer.style.display = 'block';
        phnoLabel.textContent = text;
    }
};

function showDivCheckbox() {
    const text = 'My Division is ' + divField.value;
    if (divField.value.length === 0) {
        divContainer.style.display = 'none';
        divCheckbox.checked = false;
        checkCheckboxes();
    }
    else {
        divContainer.style.display = 'block';
        divLabel.textContent = text;
    }
};

document.getElementById('myForm').addEventListener('submit', function (event) {
    document.getElementById('btnRegister').style.display = 'none';
    document.getElementById('loader').style.display = 'inline-block';
    document.getElementById('registeringText').style.display = 'inline-block';
});
const el = document.getElementById('activity');
const box1 = document.getElementById('tandc');
const box2 = document.getElementById('check');
const checkbox = document.getElementById('chkAgree');
const btnRegister = document.getElementById('btnRegister');
const ul_list = document.getElementById('ul_list');
const tcText = document.getElementById('tcText');
box1.style.display = "none";
box2.style.display = "none";
el.addEventListener('change', function handleChange(event) {
box2.style.display = 'block';
if (event.target.value === 'Choose') {
    box1.style.display = "none";
    box2.style.display = "none";
    checkbox.checked = false;
    checkCheckboxes()
}
else {
    box1.style.display = "none";
    box2.style.display = 'none';
    var content = "Terms and Conditions for " + event.target.value;
    tcText.textContent = content;
    tcText.style.fontSize = "20px";
    tcText.style.textAlign = "center";
    tcText.style.fontWeight = "bold";
    box1.style.display = "none";
    box2.style.display = "none";
    checkbox.checked = false;
    checkCheckboxes()
    while (ul_list.firstChild) {
        ul_list.removeChild(ul_list.firstChild);
    }
    const t_and_c = document.getElementById(event.target.value).value.split('$');
    for (let i = 0; i < t_and_c.length; i++) {
        const item = document.createElement('li');
        item.textContent = t_and_c[i];
        ul_list.appendChild(item)
    };
    box1.style.display = "block";
    box2.style.display = 'block';
    }
});


function checkCheckboxes() {
    if (checkbox.checked && PRNCheckbox.checked && phnoCheckbox.checked && divCheckbox.checked && emailCheckbox.checked) {
        btnRegister.removeAttribute('disabled');
        btnRegister.style.backgroundColor = 'green';
    } else {
        btnRegister.setAttribute('disabled', 'disabled');
        btnRegister.style.backgroundColor = 'lightgray';
    }
}
checkbox.addEventListener('change', checkCheckboxes);
PRNCheckbox.addEventListener('change', checkCheckboxes);
phnoCheckbox.addEventListener('change', checkCheckboxes);
divCheckbox.addEventListener('change', checkCheckboxes);
emailCheckbox.addEventListener('change', checkCheckboxes);