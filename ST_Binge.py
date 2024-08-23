import streamlit as st
import streamlit.components.v1 as components
import json



movie = [
    {
        "title": "Kill",
        "details": "720p | 1080p",
        "description": "Watch a Action Movie from Bollywood with R-rating, lots of blood and actions on the way with excellent Acting.",
        "rating": "8.5/10",
        "image": "https://images.cnbctv18.com/uploads/2024/07/kill-2024-07-e5d196ca51e467a80627e93b652a6b42-1019x573.jpg",
        "link": "movie_detail.html?title=Kill",
        "trailer": "https://www.youtube.com/watch?v=y2HZqeVeBNc&pp=ygUEa2lsbA%3D%3D",
        "releaseDate": "2024-07-10",
        "genre": "Horror-Comedy",
        "director": "Aditya Sarpotdar",
        "cast": [
            "Kunal Khemu",
            "Shweta Tripathi",
            "Vikrant Massey",
            "Pooja Gor"
        ]
    },
    {
        "title": "Phir Aayi Haseen Dilruba",
        "details": "720p | 1080p",
        "description": "While evading the cops in Agra, Rani and Rishu scheme to run away together. But when their plans go awry, Rani asks a mild-mannered admirer for help.",
        "rating": "8.5/10",
        "image": "https://www.koimoi.com/wp-content/new-galleries/2024/07/all-you-need-to-know-about-phir-aayi-hasseen-dillruba-01.jpg",
        "link": "movie_detail.html?title=Phir Aayi Haseen Dilruba",
        "trailer": "https://www.youtube.com/watch?v=ATGQdcN4UBs&pp=ygUhcGhpciBhYXlpIGhhc2VlbiBkaWxscnViYSB0cmFpbGVy",
        "releaseDate": "2024-07-10",
        "genre": "Horror-Comedy",
        "director": "Aditya Sarpotdar",
        "cast": [
            "Kunal Khemu",
            "Shweta Tripathi",
            "Vikrant Massey",
            "Pooja Gor"
        ]
    },
    {
        "title": "Gyaarah Gyaarah",
        "details": "720p | 1080p",
        "description": "Investigative drama following events in 1990, 2001, 2016. Intertwining storylines blending mysticism, science and mystery across the decades.",
        "rating": "8.3/10",
        "image": "https://m.media-amazon.com/images/M/MV5BY2JiOTlhYTUtZTk5Zi00MjA1LTkxYmQtOTgyODJmNmJmYmZlXkEyXkFqcGc@._V1_QL75_UX500_CR0,304,500,281_.jpg",
        "link": "movie_detail.html?title=Gyaarah Gyaarah",
        "trailer": "https://youtu.be/qssOLOr5i4c",
        "releaseDate": "2024-07-10",
        "genre": "Horror-Comedy",
        "director": "Aditya Sarpotdar",
        "cast": [
            "Kunal Khemu",
            "Shweta Tripathi",
            "Vikrant Massey",
            "Pooja Gor"
        ]
    },
    {
        "title": "Life Hill Gayi",
        "details": "720p | 1080p",
        "description": "Siblings turns rivals when they are put on an inheritance race by reviving a down-in-the-dumps hotel in the hills. Who will emerge victorious?",
        "rating": "8.2/10",
        "image": "https://static.tnn.in/thumb/msid-111693274,thumbsize-50298,width-1280,height-720,resizemode-75/111693274.jpg?quality=100",
        "link": "movie_detail.html?title=Life Hill Gayi",
        "trailer": "https://www.youtube.com/watch?v=7V77GFLdKpE&pp=ygUPbGlmZSBoaWxsIEdheWkg",
        "releaseDate": "2024-07-10",
        "genre": "Horror-Comedy",
        "director": "Aditya Sarpotdar",
        "cast": [
            "Kunal Khemu",
            "Shweta Tripathi",
            "Vikrant Massey",
            "Pooja Gor"
        ]
    },
    {
        "title": "kakuda",
        "details": "720p | 1080p",
        "description": "This horror-comedy film follows a town trapped in time by a curse and 3 of its inhabitants face a ghost that makes them question superstition, tradition and love.",
        "rating": "7.0/10",
        "image" : "https://img.theweek.in/content/dam/week/week/review/movies/images/2024/7/11/Kakuda.jpg",
        "link": "movie_detail.html?title=kakuda",
        "trailer": "https://www.youtube.com/watch?v=5V8Z3h9oVMc&pp=ygUGa2FrdWRh",
        "releaseDate": "2024-07-10",
        "genre": "Horror-Comedy",
        "director": "Aditya Sarpotdar",
        "cast": [
            "Kunal Khemu",
            "Shweta Tripathi",
            "Vikrant Massey",
            "Pooja Gor"
        ]
    },
    {
        "title": "Deadpool & Wolverine",
        "details": "720p | 1080p",
        "description": "Deadpool is being chased by the TVA and he needs to find a variant of wolverine to save his timeline",
        "rating": "7.0/10",
        "image": "https://www.google.com/imgres?q=deadpool%203%20poster&imgurl=http%3A%2F%2Fwww.impawards.com%2F2024%2Fposters%2Fdeadpool_and_wolverine_ver11_xlg.jpg&imgrefurl=http%3A%2F%2Fwww.impawards.com%2F2024%2Fdeadpool_and_wolverine_ver11_xlg.html&docid=Tih6zig6bZRwSM&tbnid=FoVN8s-yFP2BOM&vet=12ahUKEwivjvaQpYqIAxUgUGcHHdRrOfcQM3oFCIEBEAA..i&w=1080&h=1080&hcb=2&ved=2ahUKEwivjvaQpYqIAxUgUGcHHdRrOfcQM3oFCIEBEAA",
        "link": "movie_detail.html?title=Deadpool3",
        "trailer": "https://www.youtube.com/watch?v=73_1biulkYk",
        "releaseDate": "2024-07-26",
        "genre": "Sci-fi , Comedy",
        "director": "Shawn Levy",
        "cast": [
            "Ryan Reynolds",
            "Hugh Jackman",
            "Emma Corin",
            "Matthew Macfadyen"
        ]
    }
]


movies_json = json.dumps(movie)

# Movie data
movies = [
    {
        "title": "Kill",
        "details": "720p | 1080p",
        "description": "Watch an action movie from Bollywood with R-rating, lots of blood and actions on the way with excellent Acting.",
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
        "description": "Investigative drama following events in 1990, 2001, 2016. Intertwining storylines blending mysticism, science, and mystery across the decades.",
        "rating": "8.3/10",
        "image": "https://m.media-amazon.com/images/M/MV5BY2JiOTlhYTUtZTk5Zi00MjA1LTkxYmQtOTgyODJmNmJmYmZlXkEyXkFqcGc@._V1_QL75_UX500_CR0,304,500,281_.jpg",
        "link": "movie_detail.html?title=Gyaarah Gyaarah"
    },
    {
        "title": "Life Hill Gayi",
        "details": "720p | 1080p",
        "description": "Siblings turn rivals when they are put on an inheritance race by reviving a down-in-the-dumps hotel in the hills. Who will emerge victorious?",
        "rating": "8.2/10",
        "image": "https://static.tnn.in/thumb/msid-111693274,thumbsize-50298,width-1280,height-720,resizemode-75/111693274.jpg?quality=100",
        "link": "movie_detail.html?title=Life Hill Gayi"
    },
    {
        "title": "kakuda",
        "details": "720p | 1080p",
        "description": "This horror-comedy film follows a town trapped in time by a curse and 3 of its inhabitants face a ghost that makes them question superstition, tradition, and love.",
        "rating": "7.0/10",
        "image": "https://img.theweek.in/content/dam/week/week/review/movies/images/2024/7/11/Kakuda.jpg",
        "link": "movie_detail.html?title=kakuda"
    },
    {
        "title": "Deadpool & Wolverine",
        "details": "720p | 1080p",
        "description": "Deadpool is being chased by the TVA and he needs to find a variant of Wolverine to save his timeline.",
        "rating": "8.0/10",
        "image": "https://images.app.goo.gl/dywboavrPkYGUrHdA",
        "link": "movie_detail.html?title=Deadpool3"
    },
]

# Add CSS styling
st.markdown("""
<style>

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: white;
}

/* Style for header link */
.header-container a.header {
    text-decoration: none; /* Remove underline */
    color: #ff6347; /* Tomato color for consistency */
}

.header {
    font-size: 45px;
    font-weight: bold;
    color: #ff6347; /* Tomato color for header */
    text-align: left;
    margin-top: 20px;
}

@media screen and (max-width: 480px) {
    .header{
        font-size: 30px;
    }
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
    margin-bottom: 20px;
    padding: 0 20px;
}

.header-icons {
    display: flex;
    gap: 32px;
    align-items: right;
}

.header-icon img {
    width: 30px;
    height: 30px;
    vertical-align: right;
}

.sub-header {
    font-size: 20.28px;
    color: #ff6347;
    text-align: left;
}

.search-bar {
    text-align: right;
    margin-top: 20px;
    padding: 0 20px;
}

.search-input {
    width: 401px;
    padding: 10px;
    font-size: 16px;
    border-radius: 5px;
    border: 1px solid #ddd;
}

.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 0 20px;
}

.movie-card {
    flex: 1 1 15%; /* Adjust percentage to fit 5 cards per row */
    border: 1px solid #ddd;
    border-radius: 15px;
    padding: 10px;
    margin: 15px;
    width: 300px;
    height: auto;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s, box-shadow 0.3s;
    background-color: #f9f9f9;
    cursor: pointer;
    text-decoration: none;
    color: inherit;
}

.movie-card:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.movie-card img {
    max-width: 100%;
    border-radius: px;
}

.movie-title {
    font-size: 22px;
    font-weight: bold;
    margin-top: 10px;
    color: #333;
}

.movie-details {
    font-size: 14px;
    color: #888;
    margin-top: 5px;
}

@media screen and (min-width: 375px) {
    .movie-details{
        font-size: 7px;
    }
}

.movie-description {
    font-size: 14px;
    color: #666;
    margin-top: 10px;
    line-height: 1.5;
}

.movie-rating {
    font-size: 16px;
    color: #ff9800;
    margin-top: 10px;
    font-weight: bold;
}

.movie-detail-card {
    display: flex;
    flex-direction: column;
    align-items: left;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 15px;
    padding: 20px;
    margin: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

@media screen and (min-width: 768px) {
    .movie-card {
        flex: 1 1 calc(33.333% - 30px); /* 3 cards per row with margin adjustment */
    }
}

@media screen and (max-width: 768px) {
    .movie-card {
        flex: 1 1 calc(50% - 30px); /* 2 cards per row for tablets */
    }
}

@media screen and (max-width: 480px) {
    .movie-card {
        flex: 1 1 100%; /* 1 card per row for mobile */
    }
}

.movie-detail-image {
    flex-shrink: 0;
    width: 100%;
    border-radius: 10px;
    max-width: px; /* Adjust as needed */
}

@media screen and (min-width: 1024px) {
    .movie-detail-image{
        width: 50%;
    }
}

.movie-detail-info {
    text-align: left;
    margin-top: 1px;
}

.movie-detail-title {
    font-size: 28px;
    font-weight: bold;
    color: #333;
}

.movie-detail-details {
    font-size: 16px;
    color: #888;
    margin-top: 10px;
    line-height: 1;
}

.movie-detail-description {
    font-size: 16px;
    color: #666;
    font-weight: bold;
    margin-top: 15px;
    line-height: 1;
}

.movie-detail-rating {
    font-size: 17px;
    color: #ff9800;
    margin-top: 15px;
    font-weight: bold;
    line-height: 1;
}

/* Additional styles for new details */
.movie-detail-release-date {
    font-size: 0.969em;
    color: #666;
    font-weight: bold;
    margin-top: 15px;
}

.movie-detail-genre {
    font-size: 0.969em;
    color: #666;
    font-weight: bold;
    margin-top: 15px;
    line-height: 1;
}

.movie-detail-director {
    font-size: 0.969em;
    color: #666;
    font-weight: bold;
    margin-top: 15px;
    line-height: 1;
}

.movie-detail-cast {
    font-size: 0.969em;
    color: #666;
    font-weight: bold;
    margin-top: 15px;
    line-height: 1;
}

.movie-detail-release-date {
    font-size: 0.969em;
    font-weight: bold;
    color: #666;
    margin-bottom: 10px;
    margin-top: 25px;
}

.movie-detail-genre {
    color: #666;
    font-style: italic;
    margin-bottom: 10px;
}

.movie-detail-director {
    font-style: italic;
    margin-bottom: 10px;
}

.movie-detail-link {
    display: inline-block;
    margin-top: 25px;
    padding: 15px 20px;
    font-size: 18px;
    color: #ffffff;
    background-color: #ff6347;
    border-radius: 20px;
    text-decoration: none;
    transition: background-color 0.3s, box-shadow 0.3s;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
    margin-right: 20px;
}

.movie-detail-link:hover {
    background-color: #e5533c; /* Darker tomato color */
    box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3);
}

.call-to-action {
    text-align: center;
    margin-top: 30px;
    font-size: 16px;
    font-weight: bold;
    color: #080001;
    padding: 0 20px;
}

/* Modal Styles */
.modal {
    display: none; /* Hidden by default */
    position: fixed;
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto; /* 15% from the top and centered */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Could be more or less, depending on screen size */
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)


# Footer
st.markdown("""
<div class="call-to-action">
    <p>Check out the latest movies on Binge+!</p>
</div>
""", unsafe_allow_html=True)


# Header Section
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background-color: #282c34;">
    <div>
        <a href="index.html" style="color: #61dafb; font-size: 2rem; text-decoration: none;">B.I.N.G.E +</a>
    </div>
    <div style="display: flex; gap: 15px;">
        <a href="https://t.me/rdpchintukchii" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Telegram" width="30"></a>
        <a href="https://github.com/ankushjha-aj" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" width="30"></a>
        <a href="https://www.linkedin.com/in/jhaankush/" target="_blank"><img src="https://www.logo.wine/a/logo/LinkedIn/LinkedIn-Icon-Logo.wine.svg" alt="LinkedIn" width="30"></a>
    </div>
</div>
""", unsafe_allow_html=True)

# Sub-header Section
st.markdown("""
<div style="text-align: center; margin-top: 10px;">
    <h2 style="color: #444;">Your Ultimate Destination for Streaming and Downloading Movies from Google Photos Application</h2>
</div>
""", unsafe_allow_html=True)

# Search bar
search_query = st.text_input("Search Movies Title...", placeholder="Search Movies Title...")

# Modal Popup for Notice
if "modal_shown" not in st.session_state:
    st.session_state.modal_shown = False

if not st.session_state.modal_shown:
    st.session_state.modal_shown = True
    with st.expander("Important Notice!"):
        st.markdown("""
        Welcome to Binge+! Please be aware that our site does not support or provide access to pirated movies or series. The content available on Binge+ is solely for demonstration purposes. This project is designed to showcase our DevOps tools and practices.
        - **Cloud Technologies**
        - **Docker**
        - **CI/CD Pipelines**
        - **GitHub Actions**

        We use HTML, CSS, and JavaScript for development, and we plan to enhance our site in the future by using Streamlit.
        """)

# Display movies
def display_movies(movies_to_display):
    cols = st.columns(3)
    for idx, movie in enumerate(movies_to_display):
        with cols[idx % 3]:
            st.markdown(f"""
            <a href="{movie['link']}" target="_blank" style="text-decoration: none;">
                <div style="border: 1px solid #ddd; border-radius: 15px; padding: 10px; margin: 15px 0; width: 100%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); background-color: #f9f9f9; cursor: pointer; color: inherit;">
                    <img src="{movie['image']}" alt="{movie['title']}" style="width: 100%; border-radius: 10px;">
                    <div style="font-weight: bold; margin-top: 10px; text-align: center;">{movie['title']}</div>
                    <div style="text-align: center;">{movie['details']}</div>
                    <div style="margin-top: 5px; color: #555; text-align: center;">{movie['description']}</div>
                    <div style="margin-top: 5px; font-weight: bold; text-align: center;">Rating: {movie['rating']}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

# Filter movies based on query
def filter_movies(query):
    query = query.lower()
    filtered_movies = [movie for movie in movies if query in movie['title'].lower()]
    return filtered_movies

# Display filtered or all movies
if search_query:
    filtered_movies = filter_movies(search_query)
    if filtered_movies:
        display_movies(filtered_movies)
    else:
        st.write("No movies found.")
else:
    display_movies(movies)

# Footer Section
st.markdown("""
<div style="text-align: center; padding: 10px; background-color: #282c34; color: #61dafb;">
    <p>&copy; 2024 Binge+. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        .movie-detail-card {{
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
        }}
        .movie-detail-image {{
            width: 100%;
            height: auto;
        }}
        .movie-detail-info {{
            padding: 10px;
        }}
        .movie-detail-link {{
            display: block;
            margin-top: 10px;
            color: blue;
            text-decoration: underline;
        }}
        .movie-detail-cast {{
            margin-top: 10px;
        }}
        .movie-detail-header {{
            font-size: 24px;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div id="movie-details-container"></div>
    <script>
        const movies = {movies_json};

        function getMovieByTitle(title) {{
            return movies.find(movie => movie.title === title);
        }}

        function displayMovieDetails(movie) {{
            const container = document.getElementById("movie-details-container");
            let linkHtml = '';
            if (movie.link) {{
                linkHtml = `<a href="${{movie.link}}" class="movie-detail-link">Visit Movie Site</a>`;
            }}
            let trailerHtml = '';
            if (movie.trailer) {{
                trailerHtml = `<a href="${{movie.trailer}}" class="movie-detail-link" target="_blank">Watch Trailer</a>`;
            }}
            let castHtml = '';
            if (movie.cast) {{
                castHtml = `<div class="movie-detail-cast"><strong>Cast:</strong> ${{movie.cast.join(', ')}}</div>`;
            }}
            container.innerHTML = `
                <div class="movie-detail-card">
                    <img src="${{movie.image}}" alt="${{movie.title}}" class="movie-detail-image">
                    <div class="movie-detail-info">
                        <h1 class="movie-detail-title">${{movie.title}}</h1>
                        <div class="movie-detail-details">${{movie.details}}</div>
                        <div class="movie-detail-description">${{movie.description}}</div>
                        <div class="movie-detail-rating">Rating: ${{movie.rating}}</div>
                        <div class ="movie-release-date">Release Date: ${{movie.releaseDate}}</div>
                        <div class="movie-detail-cast"> ${movie.cast}</div>
                        <div class="movie-detail-genre">Genre: ${{movie.genre}}</div>
                        <div class="movie-detail-director">Director: ${movie.director}</div>
                        ${linkHtml}
                        ${trailerHtml}
                    </div>
                </div>
            `;
        }}

        function getQueryParam(param) {{
            const urlParams = new URLSearchParams(window.location.search);
            return urlParams.get(param);
        }}

        document.addEventListener("DOMContentLoaded", function() {{
            const title = getQueryParam("title");
            const movie = getMovieByTitle(title);
            if (movie) {{
                displayMovieDetails(movie);
            }} else {{
                document.getElementById("movie-details-container").innerHTML = "<p>Movie not found.</p>";
            }}
        }});
    </script>
</body>
</html>
"""

# Render HTML in Streamlit
components.html(html_code, height=800)
