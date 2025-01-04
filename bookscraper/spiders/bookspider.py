import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            book_url = book.css("h3 a").attrib["href"]
            yield response.follow(
                book_url,
                callback=self.parse_book_page,
            )

        try:
            next_page = response.css("li.next a").attrib["href"]
        except KeyError:
            next_page = None

        if next_page is not None:
            yield response.follow(
                next_page,
                callback=self.parse,
            )

    def parse_book_page(self, response):
        pass
