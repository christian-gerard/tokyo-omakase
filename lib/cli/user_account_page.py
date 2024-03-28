import click
from cli.pages import define_page
from classes.User import User
from rich import print
from rich.prompt import Prompt
from classes.User import User

exit = False

def view_user(user_id):
    global exit
    exit = False
    chosen_user = User.get_user_by_id(user_id)



    while not exit:
        choice = click.prompt(f'\nEdit or Delete {chosen_user.name}? (e/d/x)').lower()
        if choice == 'd':
            delete_user(chosen_user)
        elif choice == 'e':
            edit_user(chosen_user)
            break
        elif choice == 'x':
            break
        else:
            print('\n[red]Please enter a valid option[/red]\n')

def edit_user(chosen_user):
    global exit

    while not exit:
        choice = click.prompt(f'\nEnter a new name for {chosen_user.name}').lower()
        if not (len(choice) <= 12 and len(choice) >= 1) :
            print('\n[red]Please enter a valid input between 1 and 12[/red]\n')
        else:
            chosen_user.name = choice
            chosen_user.update()

            user_account_page.clear_options()
            new_users = User.get_all()

            for user in new_users:
                user_account_page.add_option(f'{user.name.title()}', lambda user_id = user.id: view_user(user_id))

            print(f'\n[green]Update Successful[/green]\n')

            click.pause()
            exit = True

def delete_user(chosen_user):
    global exit

    while not exit:

        if chosen_user.id == User.current_user.id:
            print('\n[red]Unable to delete...User is currently logged in[/red]\n')
            click.pause()
            exit = True
        else:
            break

    while not exit:
        choice = click.prompt(f'\nDelete {chosen_user.name}? (y/n)').lower()
        if choice == 'y':
            confirmation = Prompt.ask(f'\n[red]Are you sure? This will also delete all visits made by this user.[/red] (y/n)').lower()
            if confirmation == 'y':
                chosen_user.delete()
                chosen_user.delete_all_visits()
                user_account_page.clear_options()
                new_users = User.get_all()

                for user in new_users:
                    user_account_page.add_option(f'{user.name.title()}', lambda user_id = user.id: view_user(user_id))

                print(f'\n[green]{chosen_user.name} was successfully deleted[/green]\n')
                click.pause()
                exit = True
            elif confirmation == 'n':
                print(f'\n[green]Aborting delete of {chosen_user.name}[/green]\n')
                exit = True
            else:
                print('\n[red]Please enter a valid input[/red]\n')
        elif choice == 'n':
            break
        else:
            print('\n[red]Please enter a valid input[/red]\n')
            



user_account_page = define_page("user_account", "Manage User Accounts")

# Add options for user account page

users = User.get_all()

for user in users:
    user_account_page.add_option(f'{user.name.title()}', lambda user_id = user.id: view_user(user_id))


