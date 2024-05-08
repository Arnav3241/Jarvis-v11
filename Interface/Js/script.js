console.log("🚀 eelCode.js loaded");

const Delay = ms => new Promise(res => setTimeout(res, ms));

function JSPrint(text) { console.log("Python " + text); }

eel.expose(JSPrint);

function ShowPreRender() { eel.PrintPyLog("Showing", "PreRender"); document.getElementById("preRender").style.display = "block"; document.getElementById("main").style.display = "none"; document.getElementById("intro").style.display = "none"; }
function ShowIntro() { eel.PrintPyLog("Showing", "Intro"); document.getElementById("intro").style.display = "block"; document.getElementById("main").style.display = "none"; document.getElementById("preRender").style.display = "none"; }
function ShowMain() { eel.PrintPyLog("Showing", "Main"); document.getElementById("intro").style.display = "none"; document.getElementById("main").style.display = "block"; document.getElementById("preRender").style.display = "none"; }

eel.expose(ShowPreRender);
eel.expose(ShowIntro);
eel.expose(ShowMain);

function showMainWindow() { eel.PrintPyLog("Showing", "Main Window"); document.getElementById("wake_window").style.display = "none"; }
function showWakeWindow() { eel.PrintPyLog("Showing", "Wake Window"); document.getElementById("wake_window").style.display = "block"; }

eel.expose(showMainWindow);
eel.expose(showWakeWindow);

const RecognitionOutput = document.getElementById('RecOutput');
let recognition;

function Recognition() {
  RecognitionOutput.innerHTML = "Listning...";
  recognition = new webkitSpeechRecognition() || new SpeechRecognition();
  recognition.lang = 'en-IN';
  recognition.continuous = true;

  recognition.onresult = function(event) {
    eel.PrintPyLog("Transcript", transcript);
    const transcript = event.results[event.results.length - 1][0].transcript;
    RecognitionOutput.textContent += transcript;
  };
  recognition.onend = function() {
    recognition.start();
  };
  recognition.start();
}

eel.expose(Recognition);

//? Main Programme Running:
window.addEventListener("DOMContentLoaded", () => {
  console.log("🚀: DOM Loaded")
  ShowPreRender(); showMainWindow();
  eel.Jarvis()
})




// const showNotification = (title, message) => {}

// const showImageInChat = (image) => {}

// const ChangeStatus = (status) => {}

// const ChangeVolume = (volume) => {}

// const disableInput = (toDisable) => {}

// const ChatWithFile = (file) => {}

// const TempEmail = () => {}

// const CodeSupport = (userInput) => {}

// const HomeAutomation = (serial, toTurnOn) => {}


