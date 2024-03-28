import click
from rich import print
from rich.prompt import Prompt
from cli.pages import navigate
from classes.User import User
from classes.Visit import Visit
from classes.Restaurant import Restaurant
from cli.pages import go_back

def view_visit(visit_id):
    exit = False
    visit = Visit.get_visit_by_id(visit_id)
    restaurant_obj = Restaurant.get_by_id(visit.restaurant_id)

    print('\n')
    print('[white]=[/white]' * 20)
    print(f'\nDate: {visit.date}')
    print(f'\nRestaurant: [purple]{restaurant_obj.name}[/purple] in [blue]{restaurant_obj.ward}[/blue]')
    print(f'\nDescription: [yellow]{visit.description}[/yellow]')
    print(f'\nRating: [red]{visit.rating}/10[/red]\n')
    print('[white]=[/white]' * 20)
    print('\n')

    while not exit:

        choice = click.prompt(f'Edit or Delete visit? (d/e/x)').lower()
        if choice == 'd':
            confirmation = click.prompt('\nAre you sure you want to delete this visit? (y/n)').lower()
            if confirmation == 'y':
                visit.delete()
                print('\n[red]Visit has been deleted[/red]\n')
                display_my_visits()
                click.pause()
                exit = True
            elif confirmation == 'n':
                print('\n[red]Aborting Delete...[/red]\n')
                click.pause()
                exit = True
            else:
                print('\n[red]Please use a valid input[/red]\n')
                click.pause()
                print('\n')
        elif choice == 'e':

            edit_choice = click.prompt('\nWhat would you like to change? (1. Rating, 2. Date, 3. Description)')

            if edit_choice == '1':
                try:
                    rating = int(Prompt.ask(f'\nChange rating from [#FF7EF5]{visit.rating}[/#FF7EF5] to'))
                    visit.rating = rating
                    visit.update()
                    print('\n[green]Updated Rating[green]\n')
                    click.pause()
                    display_my_visits()
                    exit = True
                except ValueError:
                    print('\n[red]Please enter a valid rating between 1 and 10[/red]\n')
                    click.pause()
                    print('\n')

            elif edit_choice == '2':
                try:
                    date = Prompt.ask(f'\nChange date from [#FF7EF5]{visit.date}[/#FF7EF5] to')
                    visit.date = date
                    visit.update()
                    print('\n[green]Updated Date[green]\n')
                    click.pause()
                    display_my_visits()
                    exit = True
                except ValueError:
                    print('\n[red]Please enter a valid date with the \'MM-DD-YYYY\' format[/red]\n')
                    click.pause()
                    print('\n')
                
            elif edit_choice == '3':
                try:
                    description = Prompt.ask(f'\nChange description from "[#FF7EF5]{visit.description[0:20]}[/#FF7EF5]" to')
                    visit.description = description
                    visit.update()
                    print('\n[green]Updated Description[green]\n')
                    click.pause()
                    display_my_visits()
                    exit = True
                except ValueError:
                    print('\n[red]Please enter a description under 100 characters[/red]\n')
                    click.pause()
                    print('\n')
            else:
                print('\n[red]Please use a valid input[/red]\n')
                click.pause()
                print('\n')
        elif choice.lower() == 'x':
            exit = True
        else:
            print('\n[red]Please use a valid input[red]\n')
            click.pause()
            print('\n')







def display_my_visits():
    from cli.visits_page import visits_page

    user = User.current_user.visits()
    

    if user == []:
        print('\n[red]No Visits Uploaded ... Please upload a visit in the restaurants menu[red]\n')
        visits_page.clear_options()
        visits_page.add_option('View My Visits', lambda: display_my_visits())
        click.pause()
    else:
        visits_page.options = []

        for visit in user:
            restaurant_obj = Restaurant.get_by_id(visit.restaurant_id)
            visits_page.add_option(f'[yellow]{visit.date}[/yellow] Rating: {visit.rating} <"{visit.description[0:20]}..."> [#FF7EF5]{restaurant_obj.name}[/#FF7EF5] in [blue]{restaurant_obj.ward}[/blue]', lambda visit_id = visit._id: view_visit(visit_id))
            # print(f'\n{visit.date} Rating: {visit.rating} <"{visit.description[0:20]}..."> [#FF7EF5]{restaurant_obj.name}[/#FF7EF5] in [blue]{restaurant_obj.ward}[/blue]')

    return user
        

    

