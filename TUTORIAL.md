# Top Reddit Posts - Reproducible Setup Guide

## Prerequisites
- Python 3.8+
- pip
- A modern web browser (Chrome, Firefox, Edge)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/fairyfemirins/top-reddit-posts.git
cd top-reddit-posts
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Set Up Reddit API Keys
1. Sign up for a Reddit API key at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
2. Create a `.env` file in the project directory:
   ```bash
   echo "REDDIT_CLIENT_ID=your_client_id_here" > .env
   echo "REDDIT_CLIENT_SECRET=your_client_secret_here" >> .env
   echo "REDDIT_USER_AGENT=top-reddit-posts/1.0 by Femirins" >> .env
   ```

### 5. Run the Server
```bash
python app.py
```

### 6. Access the App
Open your browser and navigate to:
```
http://localhost:5000
```

## Usage
- The app will display the top post from each of Reddit's default subreddits.
- If Reddit API credentials are not provided, the app will use mock data for demonstration.

## Troubleshooting

### 1. Port Already in Use
If port `5000` is already in use, change the port in `app.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

### 2. Reddit API Not Working
- Ensure your Reddit API credentials are correct in `.env`.
- Check Reddit's API rate limits.
- Use mock data for offline testing.

### 3. Frontend Not Loading
- Ensure the server is running (`python app.py`).
- Check the browser console for errors.

## License
MIT