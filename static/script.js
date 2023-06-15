document.getElementById('message').addEventListener('keydown', function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    chat()
  }
});

function chat() {
    var message = document.getElementById('message').value;
    var resultContainer = document.getElementById('result');
    return fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'text': message
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Произошла ошибка. Статус: ' + response.status);
        }
        return response.json();
    })
    .then(data => {
        var response = data["message"];
        // Вставка HTML-кода таблиц в контейнер
        resultContainer.innerHTML = response;
    })
}