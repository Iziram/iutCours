// Fonction vérifiant la question 1 : la réponse est 1995
function verifierQ1() {
    const reponses = document.getElementsByName("annee");
    let choix;
    for (var i = 0; i < reponses.length; i++) {
        if (reponses[i].checked) {
            choix = reponses[i].value;
        }
    }
    if (choix === "1995") {
        afficherQuestion(2);
    } else {
        const p = document.getElementById('msg1');
        p.classList.add("rouge");
        p.textContent = "Ce n'est pas la bonne réponse";
    }
    // Vérifier si la case cochée est correcte, si oui, afficher la question 2
    // sinon afficher un message. Le message doit être stylé.

}

// Fonction vérifiant la bonne réponse à la question 2 : la réponse est 10
let tentative = 0;

function verifierQ2() {

    const saisie = document.getElementById('nbJours').value;
    // On stocke dans une variable 'saisie' la saisie du nombre de jours

    // On incrémente le nombre de tentatives
    tentative++;

    if (tentative > 10 || saisie == "10") {
        const p = document.getElementById('msg2');
        p.classList.add("bleu");
        p.textContent = "Bien joué.";
        afficherQuestion(3);
    } else {
        if (Number.parseInt(saisie) > 10) {
            const p = document.getElementById('msg2');
            p.classList.add("rouge");
            p.textContent = `tentative : ${tentative} saisie : ${saisie} | Dommage c'est Moins`;
        } else {
            const p = document.getElementById('msg2');
            p.classList.add("rouge");
            p.textContent = `tentative : ${tentative} saisie : ${saisie} | Dommage c'est Plus`;
        }
    }

    // Si le nombre de tentatives est supérieure à 10 ou que la réponse est correcte
    // on affiche un message et on passe à la question 3


    // sinon on affiche en message le numéro de la tentative, le nombre saisi
    // ainsi que l'indication "C'est plus" ou "C'est moins"



}


// Fonction vérifiant la question 3 : la réponse est vrai
// Inspirez vous de la fonction verifierQ1()
function verifierQ3() {
    const radios = document.getElementsByName('vraifaux');
    let rep;
    for (let i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            rep = radios[i].value;
        }
    }
    if (rep.toLowerCase() == "vrai") {
        const p = document.getElementById('msg3');
        p.classList.add("bleu");
        p.textContent = "Bien Joué";
        document.getElementById('msgFinal').classList.remove('estCache');
        cacherBtnOK();
    } else {
        const p = document.getElementById('msg3');
        p.classList.add("rouge");
        p.textContent = "Ce n'est pas la bonne réponse";
    }
}

// Fonction cachant les 3 questions ainsi que le message final
function cacherQuestions() {
    const toHide = Array.from(document.getElementsByTagName('div'));
    toHide.push(document.getElementById('msgFinal'));

    toHide.forEach(element => {
        element.classList.add('estCache');
    });
}

// Fonction affichant la question dont le numéro sera passé en paramètre
function afficherQuestion(num) {
    document.getElementById(`question${num}`).classList.remove('estCache');
}