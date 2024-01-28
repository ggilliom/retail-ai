import scrapy

class RetailSpider(scrapy.Spider):
    name = 'retail'
    start_urls = ['https://bananarepublic.gap.com/browse/product.do?pid=817562012&cid=1183416&vid=1#pdp-page-content']

    def parse(self, response):

        print("AAAAAAAAA\n\n\n\n")

        head = response.css('head')

        title = head.css('title::text').get()

        meta = response.css('meta').getall()
        print(meta)

        print("\n\n\n\nBBBBBBBBB")

        product_title = response.css('h1::text').get().strip()
        product_price = response.css('div.amount-price::text').get()
        product_description = response.css('p::text').getall()

        yield {
            'product_title': product_title,
            'title': title,
            'price': product_price,
            'description': ' '.join(product_description).strip(),
            'meta' : meta
        }
