import click
from classes.Restaurant import Restaurant
from classes.Visit import Visit
from classes.User import User
from rich import print

def display_restaurants(restaurants, page_number, total_restaurants, total_pages):
    click.clear()
    print("[bold #FF7EF5]Restaurants[/bold #FF7EF5]")
    print("=" * 20)

    if not restaurants:
        print("No restaurants found.")
    else:
        print(f"Displaying restaurants {(page_number - 1) * 10 + 1} - {min(page_number * 10, total_restaurants)} of {total_restaurants}")
        for restaurant in restaurants:
            print(f"[#FF7EF5]{restaurant.id}. [purple]{restaurant.name}[/purple] || [blue]Location: {restaurant.ward}[/blue] || [yellow]Cuisine: {restaurant.cuisine}[/yellow]")
            print("---")

    print(f"\nPage {page_number} of {total_pages}")

def select_restaurant(restaurant_id):
    restaurant = Restaurant.get_by_id(restaurant_id)
    if restaurant:
        display_restaurant_details(restaurant)
    else:
        click.echo("Invalid restaurant number. Please try again.")

def display_restaurant_details(restaurant):
    click.clear()
    print('[white]=[/white]' * 20)
    print(f'\n[#FF7EF5]{restaurant.name}[/#FF7EF5]\n')
    print(f'\n[white]{restaurant.description}[/white]\n')
    print(f'\n[#FF7EF5]Location:[/#FF7EF5] {restaurant.address}\n')
    print(f'[#FF7EF5]Cuisine:[/#FF7EF5] [blue]{restaurant.cuisine}[/blue]\n')
    print(f'[#FF7EF5]Price:[/#FF7EF5] [blue]{restaurant.price}[/blue]\n')
    print(f'[#FF7EF5]Award:[/#FF7EF5] [blue]{restaurant.award}[/blue]\n')
    print('[white]=[/white]' * 20)
    print('\n')
    print("\nOptions:")
    print("[#FF7EF5]1.[/#FF7EF5] View Visits")
    print("[#FF7EF5]2.[/#FF7EF5] Add Visit")
    print("[#FF7EF5]x.[/#FF7EF5] Return to Restaurant List")
    choice = click.prompt("Enter your choice")
    if choice == "1":
        display_visits(restaurant.id)
    elif choice == "2":
        add_visit(restaurant.id)
    elif choice.lower() == "x":
        pass
    else:
        click.echo("Invalid choice. Please try again.")
        display_restaurant_details(restaurant)

def display_visits(restaurant_id):
    rest_obj = Restaurant.get_by_id(restaurant_id)
    visits = rest_obj.visits()
    
    click.clear()
    print("[bold #FF7EF5]Visits[/bold #FF7EF5]")
    print("=" * 20)

    if visits:
        for visit in visits:
            user_object = User.get_user_by_id(visit.user_id)
            visit_name = user_object.name
            print(f"User: {visit_name}")
            print(f"Description: {visit.description}")
            print(f"Rating: {visit.rating}/10")
            print(f"Date: {visit.date}")
            print("---")
    else:
        print("No visits found.")
    print("\nPress any key to return to the restaurant details.")
    click.getchar()

def add_visit(restaurant_id):
    click.clear()
    print("[bold #FF7EF5]Add Visit[/bold #FF7EF5]")
    print("=" * 20)

    while True:
        try:
            rating = int(click.prompt("Enter your rating (1-10)"))
            if rating < 1 or rating > 10:
                raise ValueError
            break
        except ValueError:
            click.echo("Please enter a valid rating between 1 and 10.")

    description = click.prompt("Enter your description")
    #!Add Date Validation?
    date = click.prompt("Enter the visit date (MM-DD-YYYY)")
    user_id = User.current_user.id

    try:
        visit = Visit.create(rating, description, date, user_id, restaurant_id)
        print("\n[green]Visit added successfully![/green]\n")
        click.pause()
    except Exception as e:
        print(f"\n[red]An error occurred while adding the visit: {str(e)}[/red]\n")
        click.pause()

