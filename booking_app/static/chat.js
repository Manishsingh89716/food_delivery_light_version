// Get the booking ID from the current URL
const bookingId = window.location.pathname.split("/").filter(Boolean).pop();

// Connect WebSocket for real-time communication
const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/chat/" + bookingId + "/"
);

// When a message is received, display it
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const chatBox = document.querySelector("#chat-box");
    chatBox.value += "👤 " + data.message + "\n"; // append new message
};

// Handle socket closing
chatSocket.onclose = function(e) {
    console.error("Chat socket closed unexpectedly");
};

// Send message to backend when user clicks Send
document.querySelector("#send-button").onclick = function(e) {
    const inputElem = document.querySelector("#chat-message-input");
    const message = inputElem.value.trim();
    if (message !== "") {
        chatSocket.send(JSON.stringify({ message: message }));
        inputElem.value = ""; // clear input
    }
};