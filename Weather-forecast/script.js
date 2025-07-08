// Replace with your actual OpenWeatherMap API key
const API_KEY = "002e51ae87c100670d163acd904be155";  // Replace with your real API key

// Listen for click on the "Get Forecast" button
document.getElementById("forecastBtn").addEventListener("click", function() {
    const location = document.getElementById("location").value;  // Get the location entered by the user

    // If no location is provided, alert the user
    if (!location) {
        alert("Please enter a location.");
        return;
    }

    // Fetch weather forecast from OpenWeatherMap API
    fetch(`https://api.openweathermap.org/data/2.5/forecast?q=${location}&appid=${API_KEY}&units=metric`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok " + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Log the full response data for debugging
            console.log(data);

            // If the API responds with an error, alert the user
            if (data.cod !== "200") {
                alert("Error: " + data.message);
                return;
            }

            // Display the weather data
            displayWeather(data);
        })
        .catch(err => {
            console.error("Error fetching data:", err);  // Log any errors that occur
            alert("Failed to fetch data. Please try again later.");
        });
});

// Function to display the weather forecast
function displayWeather(data) {
    const forecast = data.list.slice(0, 3);  // Get the forecast for the next 3 time periods (3 hourly forecasts)
    let output = '';  // Initialize the output string

    // Loop through the forecast data and create HTML for each period (hourly forecast)
    forecast.forEach(item => {
        output += `
            <h3>${new Date(item.dt * 1000).toLocaleString()}</h3>
            <p>Condition: ${item.weather[0].description}</p>
            <p>Temperature: ${item.main.temp}°C</p>
            <p>Humidity: ${item.main.humidity}%</p>
        `;
    });

    // Insert the weather data into the #forecast div
    document.getElementById('forecast').innerHTML = output;
}