from datetime import datetime
import feedparser
import newspaper

keyword_search = input("What would you like to search for?  ")

now = datetime.now()
feed_url = 'https://feeds.bbci.co.uk/news/technology/rss.xml'

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        # create a newspaper article object
        article = newspaper.Article(entry.link)
        # download and parse the article
        article.download()
        article.parse()
        # extract relevant information
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })
    return articles  # Move this outside the loop

articles = scrape_news_from_feed(feed_url)


# print the extracted articles
for article in articles:
    if keyword_search in article['title']:
        print(article['title'])
        # print('Author:', article['author'])
        # print('Publish Date:', article['publish_date'])
        # print('Content:', article['content'])
        print()


