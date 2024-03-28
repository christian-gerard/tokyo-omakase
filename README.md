# Tokyo Omakase 東京のお任せ

Tokyo Omakase is your guide to Tokyo's best restaurants.

## Install and Run
Clone down our repository and then navigate into the directory in your terminal and run the following commands:

```
pipenv install
pipenv shell
```
This creates an environment to control dependencies
```
python lib/seed.py
```
This seeds the database with our starter data.
```
python lib/cli_main.py
```
Run Tokyo Omakase



## Welcome Page

After starting the program, you will be prompted to either login or create a new account. 

### Login
To login to an existing account, enter 'l' and press enter. It will then prompt you to 'Enter User Name', enter in your username (including capitalization) and hit enter. If your account does not exist you will be prompted to choose between login and creating a user.



### Create a New User
To create a new user, enter 'n' and press enter. It will then prompt you to 'Enter New User Name', enter in your username an hit enter. 

![Login](readme_img/login.png)

## Home Page

The home page has 3 options available for you to choose...

1. Restaurants
2. Visits
3. Users

In this application, you can navigate to different menus by entering the corresponding menu number and hitting enter. You can go back in the directory by entering 'x' and hitting enter. By entering 'q' and hitting enter you can exit the entire program. At some points the application will prompt you with different commands, those will be available on the command line.

## Restaurants
Tokyo Omakase comes preloaded with nearly 200 Michellin rated restaurants that you can browse. There are 3 different ways to browse the restaurants...

Browse through our entire catalog with View All Restaurants.
![image](https://github.com/christian-gerard/tokyo-omakase/assets/12631152/85fd274a-137d-4c45-bc5b-8a234726c1cd)

Looking for a particular type of food? Filter by Cuisine to find the perfect restaurant to satisfy your craving.
![image](https://github.com/christian-gerard/tokyo-omakase/assets/12631152/15b1b7f0-839d-4a15-8231-d52881e0258c)

Need to find something close by? Filter By Location, to find the highest quality restaurants near you!
![image](https://github.com/christian-gerard/tokyo-omakase/assets/12631152/fc4e6bbf-57c9-4e48-8c43-a08672a10e7d)

From the Restaurant List, you can navigate to a specific restaurant by typing its ID# from the left. This allows you to see additional details about the restaurant as well as see other user's visits or add one of your own.

![restaurant_gif](https://github.com/christian-gerard/tokyo-omakase/assets/12631152/2fb03765-130f-4b07-9978-63114b2149f3)

## My Visits
Currently the only option under my visits is 'View My Visits.' Enter '1' to access the menu and view all the visits that are linked to your user. The visits can be accessed by inputing the corresponding number listed. Once you've selected a visit it will ask if you would like to edit or delete the visit. To exit a visit you can enter 'x'.

![ScreenRecording2024-03-27at9 43 09PM-ezgif com-video-to-gif-converter](https://github.com/christian-gerard/tokyo-omakase/assets/102694030/c205b67f-5b4c-4fc8-b2d8-69ee74f07198)

### Editing Visits
Editing visits allows a user to change the rating, date, and description of an already existing visit. The application will prompt a user to answer 3 questions. Ensure that your inputs are within the range and format the app asks for or else it will return an error and start the command line back at the view visit line.


### Deleting Visits
Deleting visits is as easy as entering 'd' into the command line. It will then ask for confirmation. Once this is done you will no longer be able to access the deleted visit so be sure it is the correct visit.

## お任せします！　(view a random restaurant)
This button is saying in Japanese 'I'll leave it to you!' It is a an option that displays one random restaurant you can try in city of Tokyo. If you are having trouble deciding where to go to dinner then leave it to us!!

![ScreenRecording2024-03-27at9 46 30PM-ezgif com-video-to-gif-converter](https://github.com/christian-gerard/tokyo-omakase/assets/102694030/bd00366a-55e0-4539-a72a-ed0d7ef63ebf)



## Manage Users
You are able to view, edit and delete users within the manage users menu. Once you enter you will see all the individual users listed. Select a user to continue...

![ScreenRecording2024-03-27at9 48 59PM-ezgif com-video-to-gif-converter](https://github.com/christian-gerard/tokyo-omakase/assets/102694030/7d44929d-c538-4ec9-93d0-c1515970bba9)

### Deleting a user
To delete a user enter 'd' into the command line. If you had selected the user you are currently logged in to it will return a message letting you know that you can not delete that user. If its another user then you will be asked a series of confirmation questions to delete. BE WARNED! The delete users functionality also deletes all visits attached to users. So be sure you want to delete the user before doing so.

### Edit a user
You can edit a user by entering 'e' into the command line. At this time you are only able to edit the user name. Enter the new name into the command line and hit enter to save. 




