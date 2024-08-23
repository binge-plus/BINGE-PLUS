import streamlit as st

# Set page configuration
st.set_page_config(page_title="BINGE+", layout="wide")

# Load CSS styles inline
st.markdown(
    """
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f9f9f9;
    }

    .header-container a.header {
        text-decoration: none;
        color: #ff6347;
    }

    .header {
        font-size: 45px;
        font-weight: bold;
        color: #ff6347;
        text-align: left;
        margin-top: 20px;
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
        align-items: center;
    }

    .header-icon img {
        width: 30px;
        height: 30px;
        vertical-align: middle;
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
        flex: 1 1 15%;
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
        .movie-details {
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

    @media screen and (min-width: 1024px) {
        .movie-detail-card {
            flex-direction: row-reverse;
        }
    }

    .movie-detail-image {
        flex-shrink: 0;
        width: 100%;
        border-radius: 10px;
        max-width: px;
    }

    @media screen and (min-width: 1024px) {
        .movie-detail-image {
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
        background-color: #e5533c;
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

    .modal {
        display: block;
        position: fixed;
        z-index: 1;
        padding-top: 100px;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgb(0, 0, 0);
        background-color: rgba(0, 0, 0, 0.4);
    }

    .modal-content {
        background-color: #fefefe;
        margin: auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
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
    """, unsafe_allow_html=True
)

# HTML content
st.markdown(
    """
    <div class="header-container">
        <a href="#" class="header">B.I.N.G.E +</a>
        <div class="header-icons">
            <a class="header-icon" href="#"><img src="https://img.icons8.com/ios-filled/50/home.png" alt="Home"></a>
            <a class="header-icon" href="#"><img src="https://img.icons8.com/ios-filled/50/plus.png" alt="Add Movie"></a>
            <a class="header-icon" href="#"><img src="https://img.icons8.com/ios-filled/50/user.png" alt="Profile"></a>
        </div>
    </div>

    <div class="sub-header">
        <h2>Explore the Latest in Cinema and TV Shows</h2>
    </div>

    <div class="search-bar">
        <input type="text" class="search-input" placeholder="Search for Movies, TV Shows, etc.">
    </div>

    <div class="container">
        <!-- Example movie cards -->
        <a class="movie-card" href="#">
            <img src="https://via.placeholder.com/300x400" alt="Movie Image">
            <div class="movie-title">Movie Title 1</div>
            <div class="movie-details">Release Date | Genre | Director</div>
            <div class="movie-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent non facilisis purus.</div>
            <div class="movie-rating">★ 4.5</div>
        </a>
        <a class="movie-card" href="#">
            <img src="https://via.placeholder.com/300x400" alt="Movie Image">
            <div class="movie-title">Movie Title 2</div>
            <div class="movie-details">Release Date | Genre | Director</div>
            <div class="movie-description">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent non facilisis purus.</div>
            <div class="movie-rating">★ 4.2</div>
        </a>
        <!-- Add more movie cards as needed -->
    </div>

    <!-- Additional sections for movie-details.html can be added similarly -->

    <div class="call-to-action">
        Start Binging Now! Discover Your Next Favorite Movie or TV Show.
    </div>
    """, unsafe_allow_html=True
)


# Movie data
movies = [
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
        "description": "Investigative drama following events in 1990, 2001, 2016. Intertwining storylines blending mysticism, science and mystery across the decades.",
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
]

# Function to display movies
def display_movies(movies_to_display):
    for movie in movies_to_display:
        st.markdown(f"""
        <a href="{movie['link']}" target="_blank" style="text-decoration: none;">
            <div style="border: 1px solid #ddd; border-radius: 15px; padding: 10px; margin: 15px; width: 300px; height: auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); background-color: #f9f9f9; cursor: pointer; color: inherit;">
                <img src="{movie['image']}" alt="{movie['title']}" style="width: 100%; border-radius: 10px;">
                <div style="font-weight: bold; margin-top: 10px;">{movie['title']}</div>
                <div>{movie['details']}</div>
                <div style="margin-top: 5px; color: #555;">{movie['description']}</div>
                <div style="margin-top: 5px; font-weight: bold;">Rating: {movie['rating']}</div>
            </div>
        </a>
        """, unsafe_allow_html=True)

# Function to filter movies based on query
def filter_movies(query):
    query = query.lower()
    filtered_movies = [movie for movie in movies if query in movie['title'].lower()]
    return filtered_movies

# Streamlit app
st.title("Movie Explorer")

# Search bar
search_query = st.text_input("Search for a movie:")

# Display movies based on search query
if search_query:
    filtered_movies = filter_movies(search_query)
    if filtered_movies:
        display_movies(filtered_movies)
    else:
        st.write("No movies found.")
else:
    display_movies(movies)
