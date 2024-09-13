function getMovieTitleFromURL() {
    const params = new URLSearchParams(window.location.search);
    const title = params.get("title");
    console.log("Raw title from URL:", title);
    if (!title) {
        console.error("No title found in URL");
        return null;
    }
    const decodedTitle = decodeURIComponent(title.replace(/%(?![0-9A-Fa-f]{2})/g, '%25'));
    console.log("Decoded title:", decodedTitle);
    return decodedTitle;
}
async function fetchMovieDetails() {
    const title = getMovieTitleFromURL();
    if (!title) {
        console.error("No title provided in URL");
        return null;
    }
    try {
        console.log('Fetching movie:', title);
        const encodedTitle = encodeURIComponent(title);
        const url = `http://34.45.6.128:1111/movies/find/${encodedTitle}`;
        console.log('Fetch URL:', url);
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const movie = await response.json();
        console.log('Fetched movie data:', movie);
        return movie;
    } catch (error) {
        console.error("Failed to fetch movie details:", error);
        return null;
    }
}

// Function to display the movie details
async function displayMovieDetails() {
    const movie = await fetchMovieDetails();
    if (!movie) {
        document.getElementById('movie-details-container').innerHTML = '<p>Failed to load movie details. Please try again later.</p>';
        return;
    }

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

    document.getElementById('movie-details-container').innerHTML = movieDetailCard;
}

document.addEventListener('DOMContentLoaded', displayMovieDetails);