## 🎵 Making my own Spotify

A full-stack, cloud-native music player inspired by Spotify. This project demonstrates end-to-end data engineering and web application development: from ingesting audio files and metadata into the cloud, to exposing data via an API, and rendering a sleek, web-based frontend.

## 🚀 Features

### Music Library Management

 - Upload songs as a bundle of MP3, album cover (JPG), and JSON metadata.
 - Store and manage song details (title, artist, album, genre, year).

### Cloud Data Pipeline
  - Files uploaded to Amazon S3 trigger a Lambda function.
  - Metadata is parsed and inserted into a relational database (MySQL).

### Backend API
  - Built with FastAPI, containerized with Docker, deployed on AWS EC2.
  - REST endpoints to retrieve songs and genres as JSON.

### Frontend Player
  - Static web interface hosted on S3.
  - Dynamically loads song data from the API for playback.

## 🛠️ Tech Stack
  - Cloud Infrastructure: AWS S3, Lambda, RDS (MySQL), EC2, CloudFormation
  - Backend: FastAPI (Python), Docker, MySQL Connector
  - Frontend: HTML/CSS/JavaScript (customized UI for playback)
  - Other Tools: Chalice (serverless framework), boto3, SQL

## 🔄 Data Flow Overview
  1. A song bundle (MP3 + JPG + JSON metadata) is uploaded to S3.
  2. Lambda is triggered by the JSON upload and parses metadata.
  3. Metadata + file URIs are inserted into the songs table in MySQL.
  4. FastAPI serves /songs and /genres endpoints from the database.
  5. The frontend player fetches songs via the API and renders them for playback.


## 📊 Example API Endpoints

Songs → GET /songs

[
  {
    "title": "Starting Over",
    "album": "Starting Over",
    "artist": "Chris Stapleton",
    "genre": "Country",
    "year": 2020,
    "file": "https://<bucket>.s3.amazonaws.com/9e4d555f.mp3",
    "image": "https://<bucket>.s3.amazonaws.com/9e4d555f.jpg"
  }
]

Genres → GET /genres
[
  { "genreid": 1, "genre": "Rock" },
  { "genreid": 2, "genre": "Indie" },
  { "genreid": 3, "genre": "Pop" }
]

## 📈 What I Learned
  - Building a full cloud-native data ingestion pipeline.
  - Integrating serverless functions (Lambda + Chalice) with relational databases.
  - Deploying FastAPI with Docker on EC2.
  - Designing REST APIs and connecting them to a web frontend.
