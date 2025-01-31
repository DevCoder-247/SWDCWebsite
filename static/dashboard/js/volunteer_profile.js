const prn = document.getElementById('prn');
const submitBtn = document.getElementById('submitBtn');
const contact_num = document.getElementById('contact_num');
const parent_num = document.getElementById('parent_num');
const profileForm = document.getElementById('profileForm');
const vname = document.getElementById('name');
const gender = document.getElementById('gender');
const blood_group = document.getElementById('blood_group');
const div = document.getElementById('div');
const current_add = document.getElementById('current_add');
const profileCheckbox1 = document.getElementById('profileCheckbox1');
const profileCheckbox2 = document.getElementById('profileCheckbox2');
const profileCheckbox3 = document.getElementById('profileCheckbox3');


prn.addEventListener('keyup', function () {
    if (prn.value.length != 8) {
        document.getElementById('prnerror').style.display = 'block';
    }
    else {
        document.getElementById('prnerror').style.display = 'none';

    }
});
contact_num.addEventListener('keyup', function () {
    if (contact_num.value.length != 10) {
        document.getElementById('contact_num_error').style.display = 'block';
    }
    else {
        document.getElementById('contact_num_error').style.display = 'none';

    }
});

parent_num.addEventListener('keyup', function () {
    if (parent_num.value.length != 10) {
        document.getElementById('parent_num_error').style.display = 'block';
    }
    else {
        document.getElementById('parent_num_error').style.display = 'none';

    }
});


submitBtn.addEventListener('click', function () {
    var result = confirm('Please check your details once again: \n\nName - ' + vname.value + '\nPRN - ' + prn.value + '\nMy Number - ' + contact_num.value + '\nParent\'s Number - ' + parent_num.value + '\nGender - ' + gender.value + '\nBlood Group - ' + blood_group.value + '\nDivision - ' + div.value + '\nAddress - ' + current_add.value + '\n\nClick "Ok" to submit.\nClick "Cancel" to make changes again.');
    if (result) {
        profileForm.submit();
    }
});

function checkCheckboxes(){
    if(profileCheckbox1.checked && profileCheckbox2.checked && profileCheckbox3.checked){
        submitBtn.disabled = false;
    } else {
        submitBtn.disabled = true;
    }
}

profileCheckbox1.addEventListener('change', function () {
    checkCheckboxes();
});

profileCheckbox2.addEventListener('change', function () {
    checkCheckboxes();
});


profileCheckbox3.addEventListener('change', function () {
    checkCheckboxes();
});