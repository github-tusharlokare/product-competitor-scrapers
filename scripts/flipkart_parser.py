import pandas as pd
from bs4 import BeautifulSoup

df_1 = pd.read_csv('../dump/flipkart_products_input.csv')

htmls = '../htmls/'

scarped_data = []

k = 0
for row in df_1.iterrows():
    k += 1
    print(f'processing>> {str(k)}')
    id = row[-1]['id']
    href = row[-1]['href']
    print(id, href)

    html_file_path = f"{htmls}{id}.html"
    d1 = dict()
    d1 = {
        'id': id,
        'href': href,
        'breadcrumbs': '',
        'productTitle': '',
        'img_src': [],
        'img_all': [],
        'rating': '',
        'rating_count': '',
        'review_count': '',
        'discount': '',
        'price': '',
        'originalPrice': '',
        'availability': '',
        'about': '',
        'productDescription': '',
        'reviews': [],
        'delivery_info': '',
        'sold_by': '',
        'variants': [],
        'offers_1': [],
        'highlights': [],
        'sales_package':'',
        'number_of_contents_sales_package':'',
        'brand':'',
        'type':'',
        'ideal_for':'',
        'character':'',
        'fragrance':'',
        'container_type':'',
        'maximum_shelf_life':'',
        'certification':'',
        'alcohol_free':'',
        'model_name':'',
        'model_id':'',
        'net_quantity':'',
        'scrap_date': '2024-09-01'
    }

    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            if soup is not None:

                breadcrumbEle = soup.select('div._7dPnhA div.r2CdBx a')
                for i in breadcrumbEle:
                    d1['breadcrumbs'] += '> ' + i.text.strip()

                productTitleEle = soup.select("meta[name='og_title']")
                productTitleEle2 = soup.select("h1._6EBuvT span.VU-ZEz")
                if len(productTitleEle) > 0:
                    d1['productTitle'] = productTitleEle[0].get('content').strip()
                elif len(productTitleEle2) > 0:
                    d1['productTitle'] = productTitleEle2[0].text.strip()

                images = soup.select("div._4WELSP._6lpKCl img")
                for img in images:
                    d1['img_src'].append(img.get('src'))

                images_all = soup.select("img._0DkuPH")
                for img in images_all:
                    d1['img_all'].append(img.get('src'))

                ratingEle = soup.select('span#productRating_LSTWIPFJYYWEBTJEWJHLFMWHN_WIPFJYYWEBTJEWJH_ div.XQDdHH')
                if len(ratingEle) > 0:
                    d1['rating'] = ratingEle[0].text.strip()

                ratingReviewsEle = soup.select('div._5OesEi.HDvrBb  span.Wphh3N')
                if len(ratingReviewsEle) > 0:
                    d1['rating_count'] = ratingReviewsEle[0].text.split('&')[0].strip()
                    d1['review_count'] = ratingReviewsEle[0].text.split('&')[-1].strip()

                dicountEle = soup.select('div.UkUFwK.WW8yVX span')
                if len(dicountEle) > 0:
                    d1['discount'] = dicountEle[0].text.replace('-','').strip()

                priceEle = soup.select(
                    'div.Nx9bqj.CxhGGd')
                if len(priceEle) > 0:
                    d1['price'] = priceEle[0].text.replace('₹','').strip()

                originalPriceEle = soup.select(
                    'div.yRaY8j')
                if len(originalPriceEle) > 0:
                    d1['originalPrice'] = originalPriceEle[0].text.replace('₹','').strip()

                availabilityEle = soup.select(
                    'button.QqFHMw')
                if len(availabilityEle) > 0:
                    d1['availability'] = availabilityEle[0].text.strip()

                aboutEle = soup.select(
                    'div.GNDEQ-')
                if len(aboutEle) > 0:

                    for i in range(0, len(aboutEle)):
                        temp = aboutEle[i].text
                        if 'Additional Features' in temp:
                            d1['about'] = temp.replace('Additional Features','').strip()
                            break

                productDescriptionEle = soup.select('div.Xbd0Sd')
                if len(productDescriptionEle) > 0:
                    d1['productDescription'] = productDescriptionEle[0].text.replace('Description','').strip()

                reviewsEle = soup.select('div.col.EPCmJX div.ZmyHeo div div')
                for i in range(0, len(reviewsEle)):
                    d1['reviews'].append(reviewsEle[i].text.strip())

                deliveryInfoEle = soup.select('div.nRBH83')
                if len(deliveryInfoEle) > 0:
                    d1['delivery_info'] = deliveryInfoEle[0].text.strip()

                buyBoxInfoEle = soup.select('div#sellerName span span')
                if len(buyBoxInfoEle) > 0:
                    d1['sold_by'] = buyBoxInfoEle[-1].text.strip()

                variantsEle = soup.select('ul.hSEbzK li a')
                for i in range(0, len(variantsEle)):
                    d1['variants'].append(variantsEle[i].text.strip())

                offersEle = soup.select('div.NYb6Oz li')
                for i in range(0, len(offersEle)):
                    d1['offers_1'].append(offersEle[i].text.strip())

                # div.xFVion ul li
                highlightsEle = soup.select('div.xFVion ul li')
                for i in range(0, len(highlightsEle)):
                    d1['highlights'].append(highlightsEle[i].text.strip())

                miscEle1 = soup.select('table._0ZhAN9 tr')
                for i in range(0, len(miscEle1)):
                    temp = miscEle1[i].text
                    if 'Sales Package' in temp and 'Number of Contents in Sales Package' not in temp:
                        d1['sales_package'] = temp.replace('Sales Package','').strip()
                    elif 'Number of Contents in Sales Package' in temp:
                        d1['number_of_contents_sales_package'] = temp.replace('Number of Contents in Sales Package','').strip()
                    elif 'Brand' in temp:
                        d1['brand'] = temp.replace('Brand','').strip()
                    elif 'Type' in temp:
                        d1['type'] = temp.replace('Type','').strip()
                    elif 'Ideal For' in temp:
                        d1['ideal_for'] = temp.replace('Ideal For','').strip()
                    elif 'Character' in temp:
                        d1['character'] = temp.replace('Character','').strip()
                    elif 'Fragrance' in temp:
                        d1['fragrance'] = temp.replace('Fragrance','').strip()
                    elif 'Container Type' in temp:
                        d1['container_type'] = temp.replace('Container Type','').strip()
                    elif 'Maximum Shelf Life' in temp:
                        d1['maximum_shelf_life'] = temp.replace('Maximum Shelf Life','').strip()
                    elif 'Certification' in temp:
                        d1['certification'] = temp.replace('Certification','').strip()
                    elif 'Alcohol Free' in temp:
                        d1['alcohol_free'] = temp.replace('Alcohol Free','').strip()
                    elif 'Model Name' in temp:
                        d1['model_name'] = temp.replace('Model Name','').strip()
                    elif 'Model ID' in temp:
                        d1['model_id'] = temp.replace('Model ID','').strip()
                    elif 'Net Quantity' in temp:
                        d1['net_quantity'] = temp.replace('Net Quantity','').strip()

                scarped_data.append(d1)

    except Exception as e:
        print(e)

try:
    df = pd.DataFrame(scarped_data)
    df.to_csv('../dump/flipkart_products_output.csv', index=False)
except Exception as e:
    raise e