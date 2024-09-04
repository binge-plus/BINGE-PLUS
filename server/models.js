import mongoose from "mongoose";

mongoose.connect("mongodb+srv://bingemovies:CWuhFDboOssypOfD@binge.qvrdf.mongodb.net/BINGE-SERIES")
    .then(() => console.log("Connected to MongoDB"))
    .catch(error => console.error("Failed to connect to MongoDB", error));

const movieSchema = new mongoose.Schema({
    Title: String,
    Image: String,
    Details: String,
    Description: String,
    Rating: String,
    ReleaseDate: String,
    Cast: [String],
    Genre: String,
    Director: String,
    Trailer: String,
    Episodes: [
      {
        EpisodeNumber: Number,
        EpisodeTitle: String,
        EpisodeLink: String
      }
    ]
});

const Movie = mongoose.model("Movie", movieSchema);

export default Movie;