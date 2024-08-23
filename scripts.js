const movies = [
    {
        "title": "Kill",
        "details": "720p | 1080p",
        "description": "Watch a Action Movie from Bollywood with R-rating, lots of blood and actions on the way with excellent Acting.",
        "rating": "8.5/10",
        "image": "https://images.cnbctv18.com/uploads/2024/07/kill-2024-07-e5d196ca51e467a80627e93b652a6b42-1019x573.jpg",
        "link": "movie_detail.html?title=Kill"
    },
    {
        "title": "Phir Aayi Haseen Dilruba",
        "details": "720p | 1080p",
        "description": "While evading the cops in Agra, Rani and Rishu scheme to run away together. But when their plans go awry, Rani asks a mild-mannered admirer for help.",
        "rating": "8.5/10",
        "image": "https://www.koimoi.com/wp-content/new-galleries/2024/07/all-you-need-to-know-about-phir-aayi-hasseen-dillruba-01.jpg",
        "link": "movie_detail.html?title=Phir Aayi Haseen Dilruba"
    },
    {
        "title": "Gyaarah Gyaarah",
        "details": "720p | 1080p",
        "description": "Investigative drama following events in 1990, 2001, 2016. Intertwining storylines blending mysticism, science and mystery across the decades..",
        "rating": "8.3/10",
        "image": "https://m.media-amazon.com/images/M/MV5BY2JiOTlhYTUtZTk5Zi00MjA1LTkxYmQtOTgyODJmNmJmYmZlXkEyXkFqcGc@._V1_QL75_UX500_CR0,304,500,281_.jpg",
        "link": "movie_detail.html?title=Gyaarah Gyaarah"
    },
    {
        "title": "Life Hill Gayi",
        "details": "720p | 1080p",
        "description": "Siblings turns rivals when they are put on an inheritance race by reviving a down-in-the-dumps hotel in the hills. Who will emerge victorious?",
        "rating": "8.2/10",
        "image": "https://static.tnn.in/thumb/msid-111693274,thumbsize-50298,width-1280,height-720,resizemode-75/111693274.jpg?quality=100",
        "link": "movie_detail.html?title=Life Hill Gayi"
    },
    {
        "title": "kakuda",
        "details": "720p | 1080p",
        "description": "This horror-comedy film follows a town trapped in time by a curse and 3 of its inhabitants face a ghost that makes them question superstition, tradition and love.",
        "rating": "7.0/10",
        "image": "https://img.theweek.in/content/dam/week/week/review/movies/images/2024/7/11/Kakuda.jpg",
        "link": "movie_detail.html?title=kakuda"
    },
    {
        "title": "Deadpool & Wolverine",
        "details": "720p | 1080p",
        "description": "Deadpool is being chased by the TVA and he needs to find a variant of wolverine to save his timeline",
        "rating": "8.0/10",
        "image": "https://images.app.goo.gl/dywboavrPkYGUrHdA",
        "link": "movie_detail.html?title=Deadpool3"
    },
];

function displayMovies(moviesToDisplay) {
    const container = document.getElementById("movies-container");
    container.innerHTML = ""; // Clear previous results

    moviesToDisplay.forEach(movie => {
        const movieCard = document.createElement("a");
        movieCard.href = movie.link;
        movieCard.target = "_blank";
        movieCard.className = "movie-card";
        movieCard.innerHTML = `
            <img src="${movie.image}" alt="${movie.title}">
            <div class="movie-title">${movie.title}</div>
            <div class="movie-details">${movie.details}</div>
            <div class="movie-description">${movie.description}</div>
            <div class="movie-rating">Rating: ${movie.rating}</div>
        `;
        container.appendChild(movieCard);
    });
}

function filterMovies(query) {
    query = query.toLowerCase();
    const filteredMovies = movies.filter(movie => movie.title.toLowerCase().includes(query));
    displayMovies(filteredMovies);
}

document.getElementById("search-input").addEventListener("input", function() {
    filterMovies(this.value);
});

// Display all movies by default
displayMovies(movies);
