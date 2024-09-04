import mongoose from "mongoose";
mongoose.connect("mongodb+srv://bingemovies:CWuhFDboOssypOfD@binge.qvrdf.mongodb.net/BINGE")
    .then(() => console.log("Connected to MongoDB"))
    .catch(error => console.error("Failed to connect to MongoDB", error));

const movieSchema = new mongoose.Schema({
    
    title: String,
    details: String,
    description: String,
    rating: Number,
    image: String,
    link: String,
    releaseDate: String,
    cast: [String],
    genre: String,
    director: String,
    visitMovie: String,
    trailer: String

});

const Movie = mongoose.model("Movie", movieSchema);

export default Movie;