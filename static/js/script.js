function copyToClipboard() {
    /* Get the text field */
    var copyText = document.getElementById("url");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/

    /* Copy the text inside the text field */
    document.execCommand("copy");

    alert("Successfully copied Image link!");
}



function showRatings() {
    document.getElementById("ratings").style.display = " block"; 
    document.getElementById("reviews").style.display = "none"; 


}

function showReviews() {
    document.getElementById("reviews").style.display = " block";
    document.getElementById("ratings").style.display = "none";


}
