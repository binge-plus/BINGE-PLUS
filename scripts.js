async function fetchMovies() {
    try {
        const response = await fetch('http:/34.45.6.128:4444/movies/find', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data.movies;
    } catch (error) {
        console.error('Failed to fetch movies:', error);
        return [];
    }
}

async function displayMovies(movies) {
    const container = document.getElementById("movies-container");
    container.innerHTML = "";

    movies.forEach(movie => {
        const movieCard = document.createElement("a");
        const encodedTitle = encodeURIComponent(movie.Title);
        movieCard.href = `movie_detail.html?title=${encodedTitle}`;
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

async function init() {
    const movies = await fetchMovies();
    displayMovies(movies);

    document.getElementById("search-input").addEventListener("input", function() {
        const query = this.value.toLowerCase();
        const filteredMovies = movies.filter(movie => movie.Title.toLowerCase().includes(query));
        displayMovies(filteredMovies);
    });
}

document.addEventListener('DOMContentLoaded', init);