import pandas as pd
from bs4 import BeautifulSoup

df_1 = pd.read_csv('../dump/input.csv')

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
        'bylineInfo': '',
        'rating': '',
        'discount': '',
        'price': '',
        'originalPrice': '',
        'availability': '',
        'brand': '',
        'item_volume': '',
        'item_dims': '',
        'age_range': '',
        'special_feature': '',
        'skin_type': '',
        'number_of_items': '',
        'scent': '',
        'item_form': '',
        'net_quantity': '',
        'about': '',
        'importantInfo': '',
        'productDescription': '',
        'manufacturer': '',
        'country_origin': '',
        'item_model_no': '',
        'product_technical_dims': '',
        'asin': '',
        'prod_details_manufacturer': '',
        'prod_details_packer': '',
        'prod_details_item_dims': '',
        'prod_details_item_weight': '',
        'prod_details_net_quantity': '',
        'prod_details_included_components': '',
        'prod_details_generic_name': '',
        'prod_details_best_sellers_rank': '',
        'reviews': [],
        'delivery_info': '',
        'buybox_info': '',
        'sold_by': '',
        'active': '',
        'ingredients': '',
        'variants': [],
        'offers_1': [],
        'offers_2': [],
        'scrap_date': '2024-08-06'
    }

    try:
        with open(html_file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            if soup is not None:

                breadcrumbEle = soup.select('ul.a-unordered-list.a-horizontal.a-size-small a')
                for i in breadcrumbEle:
                    d1['breadcrumbs'] += '> ' + i.text.strip()

                productTitleEle = soup.select("meta[name='title']")
                productTitleEle2 = soup.select("span#productTitle")
                if len(productTitleEle) > 0:
                    d1['productTitle'] = productTitleEle[0].get('content').strip()
                elif len(productTitleEle2) > 0:
                    d1['productTitle'] = productTitleEle2[0].text.strip()

                images = soup.select("div.imgTagWrapper img")
                for img in images:
                    d1['img_src'].append(img.get('src'))

                images_all = soup.select("div#altImages span.a-list-item img")
                for img in images_all:
                    d1['img_all'].append(img.get('src'))

                bylineInfoEle = soup.select('a#bylineInfo')
                if len(bylineInfoEle) > 0:
                    d1['bylineInfo'] = bylineInfoEle[0].text

                ratingEle = soup.select('span.reviewCountTextLinkedHistogram.noUnderline')
                if len(ratingEle) > 0:
                    d1['rating'] = ratingEle[0].get('title').strip()

                dicountEle = soup.select('span.a-size-large.a-color-price.savingPriceOverride.aok-align-center.reinventPriceSavingsPercentageMargin.savingsPercentage')
                if len(dicountEle) > 0:
                    d1['discount'] = dicountEle[0].text.replace('-','').strip()

                priceEle = soup.select(
                    'span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay span.a-price-whole')
                if len(priceEle) > 0:
                    d1['price'] = priceEle[0].text.replace('₹','').strip()

                originalPriceEle = soup.select(
                    'span[data-a-strike="true"] span.a-offscreen')
                if len(originalPriceEle) > 0:
                    d1['originalPrice'] = originalPriceEle[0].text.replace('₹','').strip()

                availabilityEle = soup.select(
                    'div#availability')
                if len(availabilityEle) > 0:
                    d1['availability'] = availabilityEle[0].text.strip()

                miscEle1 = soup.select('table.a-normal.a-spacing-micro tr')
                for i in range(0, len(miscEle1)):
                    temp = miscEle1[i].text
                    if 'Brand' in temp:
                        d1['brand'] = temp.replace('Brand','').strip()
                    elif 'Item Volume' in temp:
                        d1['item_volume'] = temp.replace('Item Volume','').strip()
                    elif 'Item dimensions L x W x H' in temp:
                        d1['item_dims'] = temp.replace('Item dimensions L x W x H','').strip()
                    elif 'Age Range (Description)' in temp:
                        d1['age_range'] = temp.replace('Age Range (Description)','').strip()
                    elif 'Special Feature' in temp:
                        d1['special_feature'] = temp.replace('Special Feature','').strip()
                    elif 'Skin Type' in temp:
                        d1['skin_type'] = temp.replace('Skin Type','').strip()
                    elif 'Number of Items' in temp:
                        d1['number_of_items'] = temp.replace('Number of Items','').strip()
                    elif 'Scent' in temp:
                        d1['scent'] = temp.replace('Scent','').strip()
                    elif 'Item Form' in temp:
                        d1['item_form'] = temp.replace('Item Form','').strip()
                    elif 'Net Quantity' in temp:
                        d1['net_quantity'] = temp.replace('Net Quantity','').strip()
                    elif 'Active' in temp:
                        d1['active'] = temp.replace('Active','').strip()
                    elif 'Ingredients' in temp:
                        d1['ingredients'] = temp.replace('Ingredients','').strip()

                aboutEle = soup.select(
                    'div#feature-bullets')
                if len(aboutEle) > 0:
                    d1['about'] = aboutEle[0].text.strip()

                importantInfoEle = soup.select('div#important-information')
                if len(importantInfoEle) > 0:
                    d1['importantInfo'] = importantInfoEle[0].text.strip()

                productDescriptionEle = soup.select('div#productDescription')
                if len(productDescriptionEle) > 0:
                    d1['productDescription'] = productDescriptionEle[0].text.strip()

                miscEle2 = soup.select('table#productDetails_techSpec_section_1 tr')
                for i in range(0, len(miscEle2)):
                    temp = miscEle2[i].text
                    if 'Manufacturer' in temp:
                        d1['manufacturer'] = temp.replace('Manufacturer', '').strip()
                    elif 'Country of Origin' in temp:
                        d1['country_origin'] = temp.replace('Country of Origin', '').strip()
                    elif 'Item model number' in temp:
                        d1['item_model_no'] = temp.replace('Item model number', '').strip()
                    elif 'Product Dimensions' in temp:
                        d1['product_technical_dims'] = temp.replace('Product Dimensions', '').strip()
                    elif 'ASIN' in temp:
                        d1['asin'] = temp.replace('ASIN', '').strip()

                miscEle3 = soup.select('table#productDetails_detailBullets_sections1 tr')
                for i in range(0, len(miscEle3)):
                    temp = miscEle3[i].text
                    if 'Manufacturer' in temp:
                        d1['prod_details_manufacturer'] = temp.replace('Manufacturer', '').strip()
                    elif 'Packer' in temp:
                        d1['prod_details_packer'] = temp.replace('Packer', '').strip()
                    elif 'Item Weight' in temp:
                        d1['prod_details_item_weight'] = temp.replace('Item Weight', '').strip()
                    elif 'Item Dimensions LxWxH' in temp:
                        d1['prod_details_item_dims'] = temp.replace('Item Dimensions LxWxH', '').strip()
                    elif 'Net Quantity' in temp:
                        d1['prod_details_net_quantity'] = temp.replace('Net Quantity', '').strip()
                    elif 'Included Components' in temp:
                        d1['prod_details_included_components'] = temp.replace('Included Components', '').strip()
                    elif 'Generic Name' in temp:
                        d1['prod_details_generic_name'] = temp.replace('Generic Name', '').strip()
                    elif 'Best Sellers Rank' in temp:
                        d1['prod_details_best_sellers_rank'] = temp.replace('Best Sellers Rank', '').strip()

                reviewsEle = soup.select('div#cm-cr-dp-review-list div.reviewText')
                for i in range(0, len(reviewsEle)):
                    d1['reviews'].append(reviewsEle[i].text.strip())

                deliveryInfoEle = soup.select('div#mir-layout-DELIVERY_BLOCK')
                if len(deliveryInfoEle) > 0:
                    d1['delivery_info'] = deliveryInfoEle[0].text.strip()

                buyBoxInfoEle = soup.select('div[tabular-attribute-name="Sold by"]')
                if len(buyBoxInfoEle) > 0:
                    d1['sold_by'] = buyBoxInfoEle[-1].text.strip()

                variantsEle = soup.select('li.swatchAvailable')
                for i in range(0, len(variantsEle)):
                    d1['variants'].append(variantsEle[i].get('title').replace('Click to select','').strip())

                offersEle = soup.select('div#soppATF_feature_div div.offersConsistencyEnabled')
                for i in range(0, len(offersEle)):
                    d1['offers_1'].append(offersEle[i].text.strip())

                offersEle2 = soup.select('div#itembox-Partner div.offers-items-content')
                for i in range(0, len(offersEle2)):
                    d1['offers_2'].append(offersEle2[i].text.strip())

                scarped_data.append(d1)

    except Exception as e:
        print(e)
        # raise e

try:
    df = pd.DataFrame(scarped_data)
    df.to_csv('../dump/output.csv', index=False)
except Exception as e:
    raise e