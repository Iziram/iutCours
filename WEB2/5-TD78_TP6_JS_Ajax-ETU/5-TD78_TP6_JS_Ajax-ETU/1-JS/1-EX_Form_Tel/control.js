function control() {
    const mobile = document.getElementById("mobile");
    const tel = document.getElementById("tel");
    const mail = document.getElementById("email");
    const testTel = (tel.value != "" || mobile.value != "");
    if (!testTel)
        alert("Il faut au minimum un téléphone");
    return testTel && /^[a-z0-9._-]+@[a-z0-9.-]{2,}[.][a-z]{2,3}$/.test(mail.value);
}

function control2() {
    const mobile = document.getElementById("mobile2");
    const tel = document.getElementById("tel2");

    if (mobile.value == "") {
        document.getElementsByClassName("libelle telm")[0].classList.add("err");
    } else {
        document.getElementsByClassName("libelle telm")[0].classList.remove("err");
    }

    if (tel.value == "") {
        document.getElementsByClassName("libelle telp")[0].classList.add("err");
    } else {
        document.getElementsByClassName("libelle telp")[0].classList.remove("err");
    }
    const testTel = (tel.value != "" || mobile.value != "");
    const p = document.getElementById("err");
    if (tel.value == "" || mobile.value == "") {
        const p = document.getElementById("err");
        p.innerText = "Erreur";
        p.classList.add("err");
    } else {
        p.innerText = "";
        p.classList.remove("err");
    }

    return false;
}