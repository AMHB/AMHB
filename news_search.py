import requests
from newsapi import NewsApiClient
from tabulate import tabulate
import subprocess

# Set up News API client
newsapi = NewsApiClient(api_key='cedeab2c21e94e32b28ef61bc2b0939d')
def get_news(keyword):
    # Fetch news articles
    response = newsapi.get_everything(q=keyword, language='en', sort_by='publishedAt', page_size=10)

    articles = response['articles']
    news_data = []

    # Extract relevant data from each article
    for article in articles:
        title = article['title']
        source = article['source']['name']
        published_at = article['publishedAt']
        description = article['description']
        news_data.append([title, source, published_at, description])

    return news_data

def display_news_table(news_data):
    # Define table headers
    headers = ['Title', 'Source', 'Published At', 'Description']

    # Display news articles in a table
    table = tabulate(news_data, headers, tablefmt='grid')

    # Split table into chunks of 10 rows
    table_rows = table.split('\n')
    chunks = [table_rows[i:i + 10] for i in range(0, len(table_rows), 10)]

    # Create a text file and save the table contents
    with open('news_output.txt', 'w') as file:
        for chunk in chunks:
            file.write('\n'.join(chunk))
            file.write('\n' + '-' * len(chunk[0]) + '\n')

    # Open the text file with gedit (Linux)
    subprocess.call(['gedit', 'news_output.txt'])

def main():
    keyword = input("Enter a keyword or sentence: ")
    news_data = get_news(keyword)
    display_news_table(news_data)

if __name__ == '__main__':
    main()