from datetime import datetime
import feedparser
import newspaper
import webbrowser
import os
import concurrent.futures  # for parallel execution

# Ask for the keyword to search for
keyword_search = input("What would you like to search for? ")

now = datetime.now()
feed_urls = [
    'https://feeds.skynews.com/feeds/rss/home.xml',
    'https://feeds.bbci.co.uk/news/rss.xml',
    'https://feeds.bbci.co.uk/news/politics/rss.xml',
    'https://feeds.bbci.co.uk/news/business/rss.xml',
    'https://feeds.skynews.com/feeds/rss/us.xml',
    'https://feeds.bbci.co.uk/news/technology/rss.xml',
    'https://www.gbnews.com/feeds/news.rss'
]


# Function to scrape an article
def scrape_article(entry):
    article = newspaper.Article(entry.link)
    try:
        # Download and parse the article
        article.download()
        article.parse()
        # Return relevant data
        return {
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text,
            'url': entry.link  # Add the article URL
        }
    except Exception as e:
        print(f"Failed to download or parse article from {entry.link}: {e}")
        return None


# Function to scrape all articles from a feed URL
def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    # Use concurrent futures for parallel processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Map the scrape_article function to each feed entry in parallel
        results = executor.map(scrape_article, feed.entries)
        for result in results:
            if result:  # Filter out any None results (failed articles)
                articles.append(result)
    return articles


# Aggregate articles from all feeds using concurrent futures
all_articles = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Map the scrape_news_from_feed function to each feed URL in parallel
    results = executor.map(scrape_news_from_feed, feed_urls)
    for result in results:
        all_articles.extend(result)

# Prepare the .html file to save results, named with the current date and time
filename = now.strftime("news_results_%Y_%m_%d_%H_%M_%S.html")
with open(filename, 'w', encoding='utf-8') as f:
    # Write the beginning of the HTML file
    f.write("<html>\n<head>\n<title>News Results</title>\n</head>\n<body>\n")
    f.write(f"<h1>Today's News Results for '{keyword_search}'</h1>\n")
    f.write(f"<p>Date: {now.strftime('%Y-%m-%d %H:%M:%S')}</p>\n")
    f.write("<hr>\n")

    # Write only articles containing the keyword in the title or content
    for article in all_articles:
        if keyword_search.lower() in article['title'].lower() or keyword_search.lower() in article['content'].lower():
            # Write article details in HTML format
            f.write(f"<h2>{article['title']}</h2>\n")
            f.write(f"<p><strong>URL:</strong> <a href='{article['url']}'>{article['url']}</a></p>\n")
            f.write(
                f"<p><strong>Author(s):</strong> {', '.join(article['author']) if article['author'] else 'N/A'}</p>\n")
            f.write(f"<p><strong>Publish Date:</strong> {article['publish_date']}</p>\n")
            f.write(
                f"<p><strong>Content:</strong> {article['content'][:500]}...</p>\n")  # Write a snippet of the content
            f.write("<hr>\n")

    # Write the end of the HTML file
    f.write("</body>\n</html>")

print(f"Results saved to {filename}")

# Open the HTML file in Chrome automatically
filepath = os.path.abspath(filename)

# Register Chrome with its full path (make sure to adjust the path if necessary)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Change this path if Chrome is elsewhere
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open the file in Chrome
webbrowser.get('chrome').open_new_tab(f"file://{filepath}")
