from datetime import datetime
import feedparser
import newspaper
import webbrowser
import os
import concurrent.futures
import openai

# Set up OpenAI API key (replace "your-api-key" with your actual key)
openai.api_key = "your-api-key"

# Ask for the keyword to search for
keyword_search = input("What would you like to search for? ")

now = datetime.now()

# Define the feed URLs with names
feed_urls = {
    'Sky News': 'https://feeds.skynews.com/feeds/rss/home.xml',
    'BBC News': 'https://feeds.bbci.co.uk/news/rss.xml',
    'BBC Business': 'https://feeds.bbci.co.uk/news/business/rss.xml',
    'Sky News US': 'https://feeds.skynews.com/feeds/rss/us.xml',
    'GB News': 'https://www.gbnews.com/feeds/news.rss'
}

# Function to generate a combined summary of all articles
def generate_combined_summary(all_texts):
    try:
        combined_text = "\n\n".join(all_texts)
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Using gpt-4-turbo for combined summaries as well
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Provide a brief summary of the following events:\n\n{combined_text}"}
            ],
            max_tokens=150
        )
        combined_summary = response.choices[0].message['content'].strip()
        return combined_summary
    except Exception as e:
        print(f"Failed to generate combined summary: {e}")
        return "Combined summary unavailable."

# Function to scrape an article
def scrape_article(entry):
    article = newspaper.Article(entry.link)
    try:
        article.download()
        article.parse()
        if not article.title or not article.text:
            print(f"Skipping article with no title or content: {entry.link}")
            return None

        return {
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text,
            'url': entry.link
        }
    except Exception as e:
        print(f"Failed to download or parse article from {entry.link}: {e}")
        return None

# Function to scrape all articles from a feed URL
def scrape_news_from_feed(feed_url, feed_name):
    articles = []
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        print(f"No entries found in feed: {feed_url}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(scrape_article, feed.entries)
        for result in results:
            if result:
                articles.append(result)
    return articles

# Aggregate articles from all feeds
all_articles = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(lambda url_name: scrape_news_from_feed(url_name[1], url_name[0]), feed_urls.items())
    for result in results:
        all_articles.extend(result)

print(f"Found {len(all_articles)} articles")

# Collect content of articles that match the keyword
matching_texts = []
for article in all_articles:
    if keyword_search.lower() in article['title'].lower() or keyword_search.lower() in article['content'].lower():
        matching_texts.append(article['content'])

# Generate a combined summary from matching articles
combined_summary = generate_combined_summary(matching_texts)

# Prepare the .html file to save results, named with the current date and time
filename = now.strftime("news_results_%Y_%m_%d_%H_%M_%S.html")
with open(filename, 'w', encoding='utf-8') as f:
    f.write("<html>\n<head>\n<title>News Results</title>\n</head>\n<body>\n")
    f.write(f"<h1>News Search Results for '{keyword_search}'</h1>\n")
    f.write(f"<p>Date: {now.strftime('%Y-%m-%d %H:%M:%S')}</p>\n")
    f.write("<hr>\n")

    # Write the combined summary at the start of the HTML file
    f.write("<h2>Combined Summary of News Articles</h2>\n")
    f.write(f"<p>{combined_summary}</p>\n")
    f.write("<hr>\n")

    # Write full article details without individual summaries
    found_articles = 0
    for article in all_articles:
        if keyword_search.lower() in article['title'].lower() or keyword_search.lower() in article['content'].lower():
            found_articles += 1
            f.write(f"<h2>{article['title']}</h2>\n")
            f.write(f"<p><strong>URL:</strong> <a href='{article['url']}'>{article['url']}</a></p>\n")
            f.write(f"<p><strong>Author(s):</strong> {', '.join(article['author']) if article['author'] else 'N/A'}</p>\n")
            f.write(f"<p><strong>Publish Date:</strong> {article['publish_date']}</p>\n")
            f.write(f"<p><strong>Content:</strong> {article['content'][:500]}...</p>\n")  # Limit content preview
            f.write("<hr>\n")

    if found_articles == 0:
        print("No articles found with the specified keyword.")

    f.write("</body>\n</html>")

print(f"Results saved to {filename}")

# Open the HTML file in Chrome automatically
filepath = os.path.abspath(filename)
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(f"file://{filepath}")
