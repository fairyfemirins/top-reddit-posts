from flask import Flask, render_template
import praw
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='app/templates')

# Mock data for testing without Reddit API
MOCK_POSTS = [
    {
        'title': 'Why Python is Awesome',
        'url': 'https://reddit.com/r/python/comments/123456/why_python_is_awesome',
        'subreddit': 'python',
        'score': 1234,
        'author': 'femirins',
        'permalink': 'https://reddit.com/r/python/comments/123456/why_python_is_awesome'
    },
    {
        'title': 'The Future of AI in 2026',
        'url': 'https://reddit.com/r/artificial/comments/789012/the_future_of_ai_in_2026',
        'subreddit': 'artificial',
        'score': 5678,
        'author': 'femirins',
        'permalink': 'https://reddit.com/r/artificial/comments/789012/the_future_of_ai_in_2026'
    }
]

# Initialize PRAW (only if credentials are provided)
reddit = None
try:
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT', 'top-reddit-posts/1.0 by Femirins')
    )
except:
    pass

@app.route('/')
def index():
    # Use mock data if Reddit API is not available
    if not reddit or not os.getenv('REDDIT_CLIENT_ID'):
        return render_template('index.html', posts=MOCK_POSTS)
    
    # Fetch top posts from default subreddits
    subreddits = reddit.subreddits.default(limit=10)
    top_posts = []
    for subreddit in subreddits:
        try:
            top_post = subreddit.top(time_filter='month', limit=1)[0]
            top_posts.append({
                'title': top_post.title,
                'url': top_post.url,
                'subreddit': subreddit.display_name,
                'score': top_post.score,
                'author': str(top_post.author),
                'permalink': f"https://reddit.com{top_post.permalink}"
            })
        except Exception as e:
            print(f"Error fetching top post for {subreddit.display_name}: {e}")
    
    return render_template('index.html', posts=top_posts if top_posts else MOCK_POSTS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)