from cli.pages import define_page, navigate
from cli.view_all_restaurants import display_restaurants
import click

def view_all_restaurants():
    page_number = 1
    while True:
        display_restaurants(page_number)
        choice = click.prompt("\nEnter your choice (p: Previous Page, n: Next Page, x: Back to Restaurants Menu)")
        if choice == 'p' and page_number > 1:
            page_number -= 1
        elif choice == 'n':
            page_number += 1
        elif choice == 'x':
            navigate("restaurants")
            break
        else:
            click.echo("Invalid choice. Please try again.")

def filter_by_cuisine():
    click.echo("Restaurants filtered by cuisine.")

def filter_by_location():
    click.echo("Restaurants filtered by location.")

restaurants_page = define_page("restaurants", "Restaurants")
restaurants_page.add_option("View All Restaurants", view_all_restaurants)
restaurants_page.add_option("Filter by Cuisine", filter_by_cuisine)
restaurants_page.add_option("Filter by Location", filter_by_location)
restaurants_page.add_option("Back", lambda: navigate("home"))