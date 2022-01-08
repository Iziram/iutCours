function age(){
    var dob = new Date("01/20/2003"); // ma date de naissance mm/jj/yyyy
    var month_diff = Date.now() - dob.getTime(); // On fait la différence entre maintenant et le jour de naissance
    
    var age_dt = new Date(month_diff);  // On en créer une nouvelle date
    
    //extract year from date    
    var year = age_dt.getUTCFullYear(); // et récuppère l'année
    
    //now calculate the age of the user
    var age_i = Math.abs(year - 1970); // on fait l'année - 1970 pour avoir l'age

    return age_i
}


pointers  = document.getElementsByClassName("responsive py-2 px-1 pointer")






function assignCanva(){
    const icons = [
        {
            title: "info",
            informations: "bite"
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "",
            informations: ""
        },
        {
            title: "bite",
            informations: "info"
        }
    ]
    for(var i = 0; i< pointers.length; i++){
        const icon = pointers[i]
        const obj = icons[i]
        icon.addEventListener("click", ()=>{
            var myOffcanvas = document.getElementById('myCanvas')
            const label = document.getElementById("offcanvasRightLabel")
                label.innerText = obj.title
            const body = document.getElementById("canvasBody")
                body.innerHTML = obj.informations
            
            var bsOffcanvas = new bootstrap.Offcanvas(myOffcanvas)
            bsOffcanvas.show()
        })
    }
}

assignCanva()

anchorsId = -1
nextScroll()

function nextScroll(){
    anchors = [
        "title",
        "informations",
        "compétences",
        "formations",
        "experiences",
        "interets"
    ]

    anchorsId++

    if (anchorsId >= anchors.length){
        anchorsId = 0;
    }

    document.location.href = "#"+anchors[anchorsId]
    return false;
}

window.addEventListener('wheel', nextScroll);