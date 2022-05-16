function cacherBtnOK() {
    const btn = Array.from(document.getElementsByTagName('input')).filter((el) => {
        return el.type == "button"
    });
    btn.forEach(el => {
        el.remove();
    });
}