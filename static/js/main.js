function checkPassword() {
    if (document.getElementById('pwd').value == 'Password') {
        alert('Correct Password!');
        newDoc();
    } else {
        alert('Wrong Password!');
        return false;
    }
}

function newDoc() {
    window.location.assign("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    alert("redirecting")
}