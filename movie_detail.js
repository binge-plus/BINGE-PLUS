function getMovieTitleFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get("title");
}
async function fetchMovieDetails() {
    const title = getMovieTitleFromURL();
    const response = await fetch(`http://localhost:8080/movies/find/${title}`);
    const movie = await response.json();

    // Assuming `movie` contains the movie object from MongoDB/
    return movie;
}


// Function to display the movie details
async function displayMovieDetails() {
    const movie = await fetchMovieDetails();
    console.log(movie);
    

    const movieDetailCard = `
        <div class="movie-detail-card">
            <img src="${movie.Image}" alt="${movie.Title}" class="movie-detail-image">
            <div class="movie-detail-info">
                <h1 class="movie-detail-title">${movie.Title}</h1>
                <div class="movie-detail-details">${movie.Details}</div>
                <div class="movie-detail-description">${movie.Description}</div>
                <div class="movie-detail-rating">Rating: ${movie.Rating}</div>
                <div class="movie-release-date">Release Date: ${movie.ReleaseDate}</div>
                <div class="movie-detail-cast">Cast: ${movie.Cast.join(', ')}</div>
                <div class="movie-detail-genre">Genre: ${movie.Genre}</div>
                <div class="movie-detail-director">Director: ${movie.Director}</div>
                <a href="${movie.Visit_Movie}" class="movie-detail-link">Visit Movie</a>
                <a href="${movie.Trailer}" class="movie-detail-trailer">Watch Trailer</a>
            </div>
        </div>
    `;

    console.log(movieDetailCard);
    

    document.querySelector('#movie-details-container').innerHTML = movieDetailCard;
}

// Call this function with the movie title you want to display
displayMovieDetails();