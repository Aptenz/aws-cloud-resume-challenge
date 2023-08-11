// Visitor counter

const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://hermnnqy3apfsjhfrfdlbw23mi0kdfcl.lambda-url.us-east-1.on.aws/");
    let data = await response.json();
    counter.innerHTML = ` Visitors: ${data}`;
}

updateCounter();