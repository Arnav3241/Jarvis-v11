console.log("script.js loaded");

const Delay = ms => new Promise(res => setTimeout(res, ms));

const showIntro = () => {
  document.getElementById("intro").style.display = "block";
  document.getElementById("main").style.display = "none";
}

const showMain = () => {
  document.getElementById("intro").style.display = "none";
  document.getElementById("main").style.display = "block";
}

showIntro();
Delay(5400).then(() => {
  eel.PrintPyLog("Showing", "Main Div")
  showMain();
})
// showMain();
