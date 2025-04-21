// 1. Create element
const box = document.createElement("div");
box.id = "box";
box.innerText = "Hello, I'm a Box!";
box.style.width = "200px";
box.style.height = "100px";
box.style.backgroundColor = "lightblue";
box.style.color = "black";
box.style.textAlign = "center";
box.style.lineHeight = "100px";
box.style.margin = "20px";
box.style.fontSize = "20px";

// 2. Add it to the page
document.body.appendChild(box);

// 3. Create buttons and their functions
function createButton(text, onClick) {
  const btn = document.createElement("button");
  btn.innerText = text;
  btn.onclick = onClick;
  btn.style.margin = "5px";
  document.body.appendChild(btn);
}

// 4. Change content
function changeText() {
  box.innerText = "Text Changed!";
}

// 5. Change styles
function changeColor() {
  box.style.backgroundColor = "salmon";
  box.style.color = "white";
}

// 6. Event handling - hide/show
function hideBox() {
  box.style.display = "none";
}

function showBox() {
  box.style.display = "block";
}

// Add buttons to page
createButton("Change Text", changeText);
createButton("Change Color", changeColor);
createButton("Hide Box", hideBox);
createButton("Show Box", showBox);
