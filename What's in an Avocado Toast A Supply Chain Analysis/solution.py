import pandas as pd

subset_columns = [
    'code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands',
    'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins',
    'origins_tags'
]


def get_top_origin(ingredient_filename, ingredient_category_file_name):
    ingredient = pd.read_csv(ingredient_filename, sep='\t')
    ingredient = ingredient[subset_columns]
    # Read categories and convert it to list
    ingredient_relevant_categories = pd.read_csv(ingredient_category_file_name, names=['category']).category.values.tolist()

    # Split categories tag to list and select only those available in relevant category
    ingredient['categories_list'] = ingredient['categories_tags'].str.split(',')
    ingredient = ingredient.dropna(subset='categories_list')
    ingredient = ingredient[ingredient['categories_list'].apply(lambda x: any([i for i in x if i in ingredient_relevant_categories]))]

    ingredient_uk = ingredient[(ingredient['countries'] == 'United Kingdom')]
    origin = ingredient_uk['origins_tags'].value_counts().index[0]
    return origin.replace('en:', '').replace('-', ' ')


top_avocado_origin = get_top_origin('data/avocado/avocado.csv', 'data/avocado/relevant_avocado_categories.txt')
top_olive_oil_origin = get_top_origin('data/avocado/olive_oil.csv', 'data/avocado/relevant_olive_oil_categories.txt')
top_olive_oil_origin = get_top_origin('data/avocado/sourdough.csv', 'data/avocado/relevant_sourdough_categories.txt')
