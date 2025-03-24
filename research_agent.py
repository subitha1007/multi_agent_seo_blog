import requests
from bs4 import BeautifulSoup

class ResearchAgent:
    def __init__(self):
        self.sources = [
            "https://www.shrm.org/resourcesandtools/hr-topics/pages/default.aspx",
            "https://www.forbes.com/work/"
        ]

    def get_trending_topics(self):
        topics = []
        for url in self.sources:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                headlines = soup.find_all("h2")  # Adjust selector as needed
                for h in headlines:
                    topics.append(h.text.strip())
        return topics[:5]  # Return top 5 trending topics

if __name__ == "__main__":
    agent = ResearchAgent()
    trending_topics = agent.get_trending_topics()
    print("Trending HR Topics:")
    for idx, topic in enumerate(trending_topics, 1):
        print(f"{idx}. {topic}")
