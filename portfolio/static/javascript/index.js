function selection(){
    var x = document.getElementById("First");
    if (window.getComputedStyle(x).display === "none") {
        console.log("not")
    }else{
    console.log("success")
    }
}