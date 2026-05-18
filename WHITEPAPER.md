# Top Reddit Posts - Design Decisions & Rationale

## Problem Statement
Reddit users often want to discover the best content across all subreddits, but browsing the "Top" page only shows posts from a few default subreddits. This project solves that by listing the top post from every default subreddit in one place.

## Design Decisions

### 1. Backend: Flask
- **Why Flask?** Lightweight, easy to set up, and ideal for small-scale web apps.
- **Why PRAW?** The Python Reddit API Wrapper (PRAW) simplifies interactions with Reddit's API.
- **Why Mock Data?** Ensures the app works offline or without Reddit API credentials.

### 2. Frontend: HTML/CSS/JS + Bootstrap
- **Why Bootstrap?** Ensures a responsive, mobile-friendly UI with minimal effort.
- **Why Vanilla JS?** Simplifies deployment and avoids heavy frameworks like React.

### 3. Data Fetching Logic
- **Description**: The app fetches the top post from each of Reddit's default subreddits using PRAW. If the Reddit API is unavailable, it falls back to mock data.
- **Trade-offs**: Using the Reddit API requires credentials, which may not always be available. Mock data ensures the app remains functional in all scenarios.

## Challenges & Solutions

### 1. API Rate Limits
- **Challenge**: Reddit's API has rate limits, which could block frequent requests.
- **Solution**: The app fetches data once per session and caches it in memory. Future work could include persistent caching with SQLite.

### 2. Offline Support
- **Challenge**: Users may not have Reddit API credentials.
- **Solution**: Mock data ensures the app works offline or without credentials.

### 3. Scalability
- **Challenge**: The app currently fetches data for a limited number of subreddits (default: 10).
- **Solution**: Future work could include pagination or lazy loading to support more subreddits.

## Future Work
- **User Customization**: Allow users to select which subreddits to include.
- **Persistent Caching**: Cache API responses in SQLite to reduce redundant requests.
- **Real-Time Updates**: Use WebSocket or polling to update the page dynamically.
- **Social Sharing**: Add buttons to share posts on social media.

## License
MIT