# Top Reddit Posts

> A static webpage that lists the top post from all default subreddits, updated monthly.

![Demo](https://via.placeholder.com/468x240?text=Top+Reddit+Posts+Demo)

## Features
- **Top Posts**: Fetches the top post from each of Reddit's default subreddits.
- **Mock Data**: Uses mock data for local testing if Reddit API credentials are not provided.
- **Responsive Design**: Built with Bootstrap for mobile and desktop compatibility.

## Installation
```bash
# Clone the repository
 git clone https://github.com/fairyfemirins/top-reddit-posts.git
 cd top-reddit-posts

# Set up a virtual environment (optional but recommended)
 python3 -m venv venv
 source venv/bin/activate  # Linux/Mac
 # OR
 venv\Scripts\activate  # Windows

# Install dependencies
 pip install -r requirements.txt
```

## Usage
```bash
# Run the application
 python app.py
```

Open your browser and navigate to `http://localhost:5000` to view the top posts.

## Technical Architecture
- **Backend**: Python + Flask
- **Frontend**: HTML/CSS/JS + Bootstrap 5
- **API**: PRAW (Python Reddit API Wrapper)
- **Mock Data**: Built-in mock data for local testing

## License
MIT