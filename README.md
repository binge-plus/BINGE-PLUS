## NOTE :  
- Please Make Sure to check out this `https://github.com/binge-plus/BINGE-PLUS/tree/terraform-gcp` before proceeding further.

# BINGE MOVIES
Binge Movies is a modern web application that allows users to browse, search, and discover movies through an engaging and user-friendly interface. The application offers both frontend and backend components, making it a full-stack project with features for users to explore movie details, provide feedback, and even contact the platform. It's fully containerized for easy deployment using Docker, and the CI/CD pipeline ensures smooth integration and delivery.

# Project Structure
- |-- .github/workflows/      # CI/CD workflow files for automated builds and deployments
- |-- .vscode/                # Configuration files for Visual Studio Code (e.g., extensions, settings)
- |-- logo/                   # Project logo assets and icons
- |-- server/                 # Main application backend (Node.js, Express.js)
-    |-- routes/             # Express routes for different endpoints (movies, feedback, etc.)
-    |-- controllers/        # Logic for handling requests and data processing
-    |-- models/             # Mongoose models for MongoDB collections (Movies, Feedback)
-    |-- config/             # Configuration files for the database, environment variables, etc.
- |-- public/                 # Static frontend assets (HTML, CSS, JavaScript)
-    |-- images/             # Movie poster images, backgrounds, etc.
-    |-- scripts/            # Frontend JavaScript files (scripts.js, movie_detail.js)
-    |-- styles/             # CSS files for styling (styles.css, project.css)
- |-- Dockerfile              # Docker configuration for containerizing the app
- |-- package.json            # Node.js project configuration and dependencies
- |-- notify.py               # Script for sending notifications (e.g., Telegram alerts)
- |-- last_message_timestamp.txt # Utility file for storing timestamps for rate-limiting messages


# Features
- Movie List: A homepage displaying a grid of movies, including their titles, posters, and a brief description. Users can browse and select movies to view more detailed information.
- Movie Details: Clicking on a movie will take users to a dedicated movie details page where they can view the full description, cast, director, release date, and other metadata about the movie.
- Search Functionality: A search bar at the top allows users to find movies by their title, genre, or other attributes, providing a fast and dynamic search experience.
- Feedback Form: Users can submit feedback through a form, which is sent to the backend for storage in MongoDB. This allows the developers to gather insights into the app's performance and user experience.
- Contact Page: A contact form where users can enter their name, email, and a message, which will be processed on the backend and sent to the support team via email.

# Technologies Used
## Frontend:
- HTML: Used for structuring the web pages, forms, and movie display sections.- CSS: Used for styling the components and making the site responsive. Additional files like project.css are used for advanced styling.
- JavaScript: Powers the interactive elements, such as the search functionality and dynamic movie detail loading.

## Backend:
- Node.js: A powerful JavaScript runtime used to build the server-side of the application.
- Express.js: A minimalist Node.js framework used to handle routing, requests, and serve the frontend.
- MongoDB Atlas: A cloud-based NoSQL database service used for storing movies, feedback, and contact data.

## Containerization and Deployment:
- Docker: The application is fully containerized, making it easy to run and deploy across different environments.
- GitHub Actions: Used for setting up continuous integration and continuous deployment (CI/CD) pipelines.
- Apache: The workflow configures and installs the Apache web server for hosting the application in production.

## Notifications (using chat id and bot token)
Integrated with a custom Python script (notify.py) that sends notifications to the BINGE-PLUS Channel whenever key events occur, such as successful builds or deployments.

# Required Secrets in GitHub
To ensure your workflows run smoothly, you'll need to store sensitive information in GitHub Secrets. Follow the steps below to configure them:

- GITHUB_TOKEN: Automatically provided by GitHub for authenticating actions. It's used for tasks like SonarCloud analysis or accessing GitHub resources.
No manual setup is needed for this.

- SONAR_TOKEN: A token from your SonarCloud account to authenticate the analysis process.
- DOCKERHUB_USERNAME & DOCKERHUB_PASSWORD: Used for authenticating Docker builds and pushes.
- GCP_VM_HOST: The public IP or hostname of your GCP Virtual Machine.
- GCP_VM_USERNAME: The SSH username for connecting to your GCP VM.
- GCP_VM_PRIVATE_KEY: The private key used for SSH authentication to your GCP VM.

# Setup and Installation
1. Clone the repository using `git clone https://github.com/username/binge-movies.git
2. Install dependencies using `npm install`
3. Start the application using `npm start`
4. Access the application at `http://localhost:1111` (or change port in scripts.js, movie_details.js and server/index.js like `http://localhost:1111` )
5. For Docker, build the image using `docker build -t binge-movies .` and run the container using `docker run -p 1111:111 binge-movies`

# Deployment
## CI/CD Workflow:
The project utilizes GitHub Actions for continuous integration and deployment. The main actions performed by the workflow include:

- Building the Project: Automatically builds the Docker image for the application.
- Pushing Docker Images: Pushes the Docker image to Docker Hub for storage.
- Installing Dependencies: Installs required Node.js packages, configures Apache, and sets up the application.
- Notifications: Sends deployment status and notifications via Telegram to the BINGE-PLUS Channel for visibility into each step of the pipeline.

## GitHub Actions Workflow Breakdown:
- Build and Test: Ensures the application builds successfully and passes tests.
- Docker Push: Pushes the Docker image to Docker Hub.
- Notify via Telegram: The notify.py script triggers alerts for each successful deployment, providing visibility for the team.
