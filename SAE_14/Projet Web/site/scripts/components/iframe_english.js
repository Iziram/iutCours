function iframe(id = "body"){
    let element = undefined;
    if(id === "body"){
        element = document.getElementsByTagName('body')[0]
    }else{
        element = document.getElementById(id)
    }
    element.appendChild(
        new DOMParser()
        .parseFromString(`
        <iframe src="https://iut.iziram.fr" style="border:0px #ffffff none;" name="english_blog" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="720px" width="1280px" allowfullscreen></iframe>
        `, "text/html").firstChild)
}

{/* <div id="iframeEnglish" class="container">
    <script>
        iframe("iframeEnglish")
    </script>
</div> */}