// Author - Arnav Singh ()

const output = document.getElementById('output');
let recognition;

const Recognition = () => {
  recognition = new webkitSpeechRecognition() || new SpeechRecognition();
  recognition.lang = 'en-IN';
  recognition.continuous = true;
  recognition.onresult = function(event) {
    const transcript = event.results[event.results.length - 1][0].transcript;
    output.textContent += transcript;
  };
  recognition.onend = function() {
    recognition.start();
  };
  recognition.start();
}

const Clear = () => {
  recognition.stop();
  output.innerHTML = ""
}

