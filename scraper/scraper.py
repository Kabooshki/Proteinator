def Scrape():
    products = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    search_url = "https://www.tesco.com/groceries/en-GB/search?query=protein"
