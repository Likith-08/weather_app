function getWeather() {
    const city = document.getElementById("city").value;

    fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ city: city })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("result").innerHTML = data.error;
        } else {
            document.getElementById("result").innerHTML = `
                <h3>${data.city}</h3>
                <p>🌡 Temp: ${data.temp} °C</p>
                <p>💧 Humidity: ${data.humidity}%</p>
                <p>💨 Wind: ${data.wind} m/s</p>
                <p>☁ Condition: ${data.condition}</p>
            `;
        }
    });
}
