import requests
from django.core.management.base import BaseCommand
from news.models import News

class Command(BaseCommand):
    help = "Fetch news articles from an external API for a specific category"

    def add_arguments(self, parser):
        parser.add_argument('category', type=str, help="Category of news to fetch (e.g., sports, politics, entertainment, share_market)")

    def handle(self, *args, **kwargs):
        category = kwargs['category']
        API_KEY = "3b3fec87a7a5454f8dc7a48e5a0e8eff"
        URL = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}"

        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            for article in articles:
                title = article.get("title", "No Title")
                description = article.get("description", "No description available.")
                image_url = article.get("urlToImage", "")
                category = category  
                
                News.objects.get_or_create(
                    title=title,
                    defaults={
                        "description": description,
                        "image": image_url,
                        "category": category,
                    },
                )
            self.stdout.write(self.style.SUCCESS(f"News articles for category '{category}' fetched and saved successfully."))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch news articles for category '{category}'."))