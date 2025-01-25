async function fetchMovies() {
    try {
        const response = await fetch('http://34.55.187.199:4444/movies/find', {
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
            <img src="${movie.Image}" alt="${movie.Title}" class = "movie-img">
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

const body = document.querySelector('body');
const attr = body.getAttribute('theme');
const button = document.querySelector('#theme-toggle');
let flag = 0;
button.addEventListener('click', function () {
    if (flag == 0) {
        body.setAttribute('theme', 'dark');
        button.innerHTML = '🔅';
        flag = 1;
    }
    else {
        body.setAttribute('theme', 'light');
        button.innerHTML = '🌙'
        flag = 0;
    }
});

document.addEventListener('DOMContentLoaded', init);
