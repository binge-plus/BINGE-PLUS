
// Fetch movies from the backend
async function fetchMovies() {
    try {
        const response = await fetch('http://34.45.6.128:1111/movies/find', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        console.log(response);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data, response);
        return data.movies; // Assuming the response has a property 'movies'
    } catch (error) {
        console.error('Failed to fetch movies:', error);
        return []; // Return an empty array if the fetch fails
    }
}

// Display movies on the page
async function displayMovies(movies) {
    const container = document.getElementById("movies-container");
    container.innerHTML = "";
    console.log(movies);

    movies.forEach(movie => {
        const movieCard = document.createElement("a");
        movieCard.href = movie.Link;
        movieCard.className = "movie-card";
        movieCard.innerHTML = `
            <img src="${movie.Image}" alt="${movie.Title}">
            <div class="movie-title">${movie.Title}</div>
            <div class="movie-details">${movie.Details}</div>
            <div class="movie-description">${movie.Description}</div>
            <div class="movie-rating">Rating: ${movie.Rating}</div>
        `;
        container.appendChild(movieCard);
    });
}

// Initialize and handle search input
async function init() {
    const movies = await fetchMovies(); // Fetch movies once
    displayMovies(movies); // Display all movies initially

    // Handle search input
    document.getElementById("search-input").addEventListener("input", function() {
        const query = this.value.toLowerCase();
        const filteredMovies = movies.filter(movie => movie.Title.toLowerCase().includes(query));
        displayMovies(filteredMovies); // Display filtered movies
    });
}

// Initial load
init();
