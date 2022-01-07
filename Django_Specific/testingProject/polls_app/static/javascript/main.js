console.log("Hello");
choice = document.getElementById("choice");
submitchoice = document.querySelector(".submitchoice");
choicelist = document.getElementById("choicelist");

submitchoice.addEventListener("click", (e) => {
    console.log(choice.value)
    let value = choice.value
    e.preventDefault();
    choice.value = null;

    for (let i = 0; i < +value; i++) {
        let node = document.createElement("INPUT");
        node.setAttribute("type", "text");
        choicelist.appendChild(node)
    }
})