function closeWindow() {
    window.close();
}

function notClosed()
{
    document.getElementById('countdownText').style.display = 'none';
    document.getElementById('not-closed').style.display = 'block';
};

function updateCountdown()
{
    const countdownElement = document.getElementById('countdown');
    let countdownValue = parseInt(countdownElement.textContent);
    if (countdownValue <= 1)
    {
        setTimeout(closeWindow, 1);
        setTimeout(notClosed, 1);
    }
    else
    {
        countdownValue--;
        countdownElement.textContent = countdownValue;
        setTimeout(updateCountdown, 1000);
    }
}
window.onload = function () {
    updateCountdown();
};