import click
from classes.Restaurant import Restaurant

def display_restaurants_by_cuisine(cuisine, page_number):
    restaurants_per_page = 10
    offset = (page_number - 1) * restaurants_per_page
    restaurants = Restaurant.get_restaurants_by_cuisine(cuisine, limit=restaurants_per_page, offset=offset)
    
    total_restaurants = Restaurant.get_count_by_cuisine(cuisine)
    total_pages = (total_restaurants + restaurants_per_page - 1) // restaurants_per_page

    click.clear()
    click.echo(f"Restaurants in {cuisine}")
    click.echo("=" * 20)

    if not restaurants:
        print("No restaurants found.")
    else:
        print(f"Displaying restaurants {offset + 1} - {offset + len(restaurants)} of {total_restaurants}")
        for restaurant in restaurants:
            print(f"Name: {restaurant.name}")
            print("---")

    print(f"\nPage {page_number} of {total_pages}")