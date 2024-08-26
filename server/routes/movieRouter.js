import express from "express";
import Movie from "../models.js";

const router = express.Router();


router.get('/movies/find', async (req, res) => {
    console.log("HEy");
    
    try {

        const movies = await Movie.find();
        res.status(200).json({  movies });
    } catch (err) {
        res.status(500).json({ error: 'Failed to fetch movies' });
    }
});

router.get('/movies/find/:id', async (req, res) => {
    
    try {
        const id  = req.params.id;
        console.log(id);
        if (id) {
            // If a title query is present, find the movie with that title
            const movie = await Movie.findOne({ Title : id });
            if (!movie) {
                return res.status(404).json({ error: 'Movie not found' });
            }
            return res.json(movie);
        } else {
            // If no title query, return all movies
            const movies = await Movie.find();
            res.json({ movies });
        }
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
} )


export default router;