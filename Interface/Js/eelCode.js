const Startup = () => {
  console.log("Started Jarvis")
  eel.Initialise();
}

function cslPrint(data) {
  console.log(data);
}

eel.expose(cslPrint);

Startup();
// const showNotification = (title, message) => {}

// const showImageInChat = (image) => {}

// const ChangeStatus = (status) => {}

// const ChangeVolume = (volume) => {}

// const disableInput = (toDisable) => {}

// const ChatWithFile = (file) => {}

// const TempEmail = () => {}

// const CodeSupport = (userInput) => {}

// const HomeAutomation = (serial, toTurnOn) => {}


