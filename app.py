import streamlit as st
from pymongo import MongoClient
import json
import os

# Set the page configuration
st.set_page_config(
    page_title="Binge+ Add Movies",  # Title to be displayed in the browser tab
    page_icon=":movie_camera:",  # Optional: an emoji or an icon to be displayed in the browser tab
)

# MongoDB Connection
client = MongoClient('mongodb+srv://bingemovies:CWuhFDboOssypOfD@binge.qvrdf.mongodb.net/')
db = client['BINGE']
collection = db['movies']

# Define File Paths
json_file_path = 'movie_template.json'
checksum_file_path = 'previous_checksum.txt'
details_default = "720p | 1080p"  # Default value for the Details field

# Function to Calculate a Simple Checksum of the JSON Content
def calculate_checksum(data):
    return hash(json.dumps(data, sort_keys=True))

# Streamlit UI
st.title("Movie Data Submission")

# Form to Capture Movie Details
with st.form(key='movie_form'):
    title = st.text_input("Title", placeholder="Enter the movie title")
    
    # Details is read-only
    st.text_input("Details", value=details_default, disabled=True)
    
    description = st.text_area("Description", placeholder="Enter movie description")
    rating = st.text_input("Rating", placeholder="Enter movie rating (e.g., 8.5/10)")
    image = st.text_input("Image URL", placeholder="Enter the URL of the movie poster image")
    visit_movie = st.text_input("Visit Movie", placeholder="Enter the URL to visit the movie e.g., Google Drive link")
    trailer = st.text_input("Trailer", placeholder="Enter the URL of the movie trailer")
    release_date = st.text_input("Release Date", placeholder="Enter release date (e.g., 25-08-2024)")
    genre = st.text_input("Genre", placeholder="Enter the genre of the movie")
    director = st.text_input("Director", placeholder="Enter the director's name")
    cast = st.text_area("Cast (comma separated)", placeholder="Enter the cast members separated by commas")

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Convert cast input to list
        cast_list = [member.strip() for member in cast.split(',') if member.strip()]
        if len(cast_list) < 3:
            st.error("Please provide at least three cast members.")
        else:
            # Load the JSON Template
            if os.path.exists(json_file_path):
                with open(json_file_path, 'r') as file:
                    movie_data = json.load(file)
            else:
                st.error("JSON file not found.")
                st.stop()

            # Automatically update 'Link' based on 'Title'
            if title:
                movie_data['Link'] = f"movie_detail.html?title={title}"

            # Load the Previous Checksum (if exists)
            previous_checksum = None
            if os.path.exists(checksum_file_path):
                with open(checksum_file_path, 'r') as file:
                    previous_checksum = file.read()

            # Prepare Movie Data
            movie_data.update({
                "Title": title,
                "Details": details_default,  # Preserve the default value
                "Description": description,
                "Rating": rating,
                "Image": image,
                "Link": movie_data['Link'],
                "Visit_Movie": visit_movie,
                "Trailer": trailer,
                "ReleaseDate": release_date,
                "Genre": genre,
                "Director": director,
                "Cast": cast_list
            })

            # Calculate Current Checksum
            current_checksum = str(calculate_checksum(movie_data))

            # Check if JSON Data Has Been Updated
            if current_checksum == previous_checksum:
                st.info("JSON file has not been updated. No changes were made.")
            else:
                # Validate and Insert Data into MongoDB
                required_fields = ["Title", "Details", "Description", "Rating", "Image", "Link", "Visit_Movie", "Trailer", "ReleaseDate", "Genre", "Director", "Cast"]
                if all(field in movie_data and movie_data[field] for field in required_fields):
                    try:
                        collection.insert_one(movie_data)
                        st.success(f"Movie '{title}' has been added to the collection.")

                        # Save the Current Checksum
                        with open(checksum_file_path, 'w') as file:
                            file.write(current_checksum)

                        # Clear the JSON File (Except 'Link' and 'Details' Fields) with Specific Formatting
                        new_data = {
                            "Title": "",
                            "Details": details_default,  # Ensure Details is preserved with default value
                            "Description": "",
                            "Rating": "",
                            "Image": "",
                            "Link": "movie_detail.html?title=",
                            "Visit_Movie": "",
                            "Trailer": "",
                            "ReleaseDate": "",
                            "Genre": "",
                            "Director": "",
                            "Cast": []
                        }

                        # Manually write the JSON data with each key-value on a new line
                        with open(json_file_path, 'w') as file:
                            json.dump(new_data, file, indent=2)
                        
                        st.info("JSON file has been cleared (except 'Link' and 'Details' fields) with specific formatting after successful insertion.")
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                else:
                    st.error("The template is not fully filled out. Please complete all fields.")
