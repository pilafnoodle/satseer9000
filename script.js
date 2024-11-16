fetch('http://api.open-notify.org/iss-now.json')
            .then(response => response.json())  // Convert the response to JSON
            .then(data => {
                // Access and log the timestamp and latitude values
                console.log('Timestamp:', data.timestamp);
                console.log('Latitude:', data.iss_position.latitude);
                console.log('Longitude:', data.iss_position.longitude);
                document.getElementById('sublong').textContent = data.iss_position.longitude;
                document.getElementById('sublat').textContent = data.iss_position.latitude;
                
            })
            .catch(error => {
                // Handle any errors that occur during the fetch
                console.error('Error fetching data:', error);
            });