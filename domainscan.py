import argparse
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import urllib.parse
import pyfiglet
from termcolor import colored

def print_harmoni():
    ascii_banner = pyfiglet.figlet_format("KeyCrawler", font="slant")
    colored_banner = colored(ascii_banner, 'blue')
    print(colored_banner)
    print("projectharmoni keycrawlerv1.0")
    print("-----------------------------------------------------------------------------")

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def crawl_url(session, url, keywords):
    try:
        content = await fetch(session, url)
        soup = BeautifulSoup(content, 'html.parser')
        page_text = soup.get_text()
        if any(keyword.lower() in page_text.lower() for keyword in keywords):
            return url
    except Exception as e:
        print(f"Error crawling {url}: {e}")
    return None

async def main_crawler(domain, keywords):
    matched_urls = set()
    async with aiohttp.ClientSession() as session:
        try:
            content = await fetch(session, domain)
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find_all('a', href=True)

            tasks = []
            for link in links:
                href = link['href']
                if href.startswith("http"):
                    parsed_href = urllib.parse.urljoin(domain, href)
                    tasks.append(crawl_url(session, parsed_href, keywords))

            results = await asyncio.gather(*tasks)
            matched_urls = {result for result in results if result}
        except Exception as e:
            print("Error:", e)

    return matched_urls

def main():
    print_harmoni()
    parser = argparse.ArgumentParser(description="Crawl URLs containing specific keywords from a domain")
    parser.add_argument("-d", "--domain", required=True, help="Domain or subdomain to crawl")
    parser.add_argument("-k", "--keywords", nargs="+", required=True, help="Keywords to search for")
    args = parser.parse_args()

    domain = args.domain
    keywords = args.keywords

    print("\nCrawling URLs for keywords...")

    matched_urls = asyncio.run(main_crawler(domain, keywords))

    print("\nURLs containing specified keywords:")
    for url in matched_urls:
        print(url)

if __name__ == "__main__":
    main()
