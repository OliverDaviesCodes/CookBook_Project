<h2 align="center">
 Just a Taste a CookBook for All! 
</h2>

<h3 align="center">
<img src="/workspace/CookBook_Project/static/uploads/cookbook.png" alt="Just a taste Preview">
</h3>


<div align="center">


<br><br>

[You can view the live project here](https://cookbook-manager-project.herokuapp.com/)

</div>

# Just a Taste

## Overview

This is the main website for Just a Taste, a cuisine guide for some incredible dishes,from beginners and experienced chefs alike. The website aims to target individuals who are looking for inspiration, or experienced chefs looking to share there knowledge and ideas with the world. The website's main focus is for people to share there culinary experience and encourage others to get involved and learn to cook.

The website is fully interactive, built with mobile capability design in mind, and accessible on a wide range of devices.


## Contents Table

1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Database**](#database)

6. [**Deployment**](#deployment)

7. [**Credits**](#credits)
    - [**Contents**](#contents)
    - [**Media**](#media)
    - [**Codes**](#codes)
    - [**Acknowledgements**](#acknowledgements)


## UX
- The webste features a modern, interactive, and easy-to-use design for individuals to easily navigate and enjoy their time during their visit.

### User stories

#### First Time Visitor Goals

- I want to understand the main purpose of the website.
- I want to easily navigate through the website.
- I want to find out how I can register to the website, and add and edit recipes.
- I want to find out how I can search for recipes.
- I want to see my own recipes in my own space


#### Registered Visitor Goals

- I want to find out how I can login to my profile.
- I want to find out how I can add a new recipe.
- I want to find out how I can edit my recipe.
- I want to find out how I can delete my recipe.
- I want to find be able to see all my recipes.
- I want to find out how i can search through all the current recipes.
- I want to find out how to delete my recipes.

#### Admin User Goals

- I want to be able to add new recipes.
- I want to be able to edit user recipes.
- I want to be able to delete user recipes.
- I want to be able to delete unwanted users from the website.
- I want to be able to manage add/edit/delete categories.
- I want to be able to see real-time information about the website, such as current number of recipes, users, and categories.


## Strategy

- The goal of the website is to inform visitors and users, about different recipes and get them involved in the cooking community encouraging recipe use and addition. The website aims to attract more users by presenting up to date information about these recipes, The aim is to build a community around the website itself, and to be the go-to place for user who want to cook and share there knowledge.

## Design


### Color Scheme

- The colors used throughout the website are:

<img src="/workspace/CookBook_Project/static/uploads/palette.png"  alt="color-palette">


### Typography

There are two Google fonts used throught the website. [Petemoss](https://fonts.google.com/specimen/Petemoss?preview.size=24#standard-styles) is used for qoute, [Montagu Slab](https://fonts.google.com/specimen/Montagu+Slab) used for all titles.



### Imagery

- Images on the website were chosen to set the sense of quality, and taste of the website, and to make sure users have a good experience during their visit. 
Other images loaded into the website by the user are random and can be selected by each individual.

### Wireframes

- [Homepage/recipes](/workspace/CookBook_Project/static/uploads/recipe-home.png)
- [Add recipe Page](/workspace/CookBook_Project/static/uploads/recipe-add.png)
- [Register](/workspace/CookBook_Project/static/uploads/recipe-login.png)
- [Login](/workspace/CookBook_Project/static/uploads/recipe-login.png)
- [Profile Page with Recipes](/workspace/CookBook_Project/static/uploads/recipe-profile.png)
- [Add Recipe/Edit Recipe](/workspace/CookBook_Project/static/uploads/recipe-add.png)


## Features

### Existing Features

- Responsive on all device sizes.
- Navbar and Footer is visible on all pages.

 **Navbar**
 - Fixed on top of the page on all device sizes.
 - Shown as a collapsible navbar with a hamburger button for trigger on Mobile devices and Tables.
 - Features a search bar allowing user to make searches throughout the website. Search function allows users to search for recipes, and allows user to search recipes by category.
 - Features 3 different layouts, for guest users Home, Login and Register are present.
 - For Registered users, Home, Profile, Add Recipe and Logout  are Present.
 - For Admin user All the links are present along with a link for Admin Categories.

 **Homepage/ Recipes**
- Features an interactive, and modern design.
- Using CSS and Javascript, recipe cards and images are presented to the user in an structured layout as the user scrolls through the page, providing a unique experience.
- Each recipe on homepage displays Title, Description, and portion and time for the recipe, and each recipe has a button to view the instructions and full recipe on a seperate page.
- For recipe users, a Delete and Edit button is displayed on their recipe for users to easily manage their recipes from Homepage on tablet sizes and up to full screen sizes.


 **Register Page**
- Features a clean registration form for user to signup for the website.
- Each section of form input area features a label.
- Password input field features a password match validator and gives feedback to user if their passwords match. 
- Email input field features an email match validator and gives feedback on if the emails match

 **Login Page**
- Features a clean login form for users to login to their profile.
- Each section of form input area features a label.
- Upon succcessful submission, user is redirected to their own profile page.
- there are validors on both the email, name and password for securability.

 **Profile Page**
- Features a clean layout.
- Shows a greeting message to the User upon successful login.
- Features a section showing all the recipes by the user, allowing them to edit or delete their posts.
- If user has no posts, then a message is presented to the user.

 **Add Recipe Page**
- Stricted only for registered users.
- Page features a clean form for users to use, outlining all the required information in the form.
- Form features an image selection section allowing users to upload their recipe images.
- Using file upload, and Cloudinary service, form allows users to easily upload their image to the cloud, and eliminates the hassle of looking for image urls.
- File upload input allows user to only upload image files such as jpeg, jpg, and png. Any other file extensions are restricted.
- Upon successful submission, user get redirected to the homepage and greeted with a success message.

**Edit Recipe Page**
- Stricted only for recipe users.
- Page features the same form and features as the Add recipe page.
- Each section of the form is pre-filled with the data they provided when they submited the form, allowing users to easily edit the recipe information.
- Upon successful submission, user get redirected to the homepage and greeted with a success message.

**Show Recipe Page**
- Allowed for visitors and registered users to see.
- At the top of the page, Recipe title and image is presented.
- Underneath the title recipe information such as desctiption, instructions, Category, portion size and time is presented to the users. For recipe authors and admin an Edit and Delete button is presented allowing author or Admin user to easily manage the recipe.

**Add/manage Categories**
- Stricted for Admin use only, and features a variety options for the Admin user to easily manage and be in total control.
- On top of the page, category cards are presented for the admin user. Each card shows a category that users can select for there recipes
- the admin can easily access and add a new category through the add category button displayed at the top of the page.
- Admins can also delete and edit categories through the buttons presented beneath each category displayed


### Features Left to Implement

- Pagenation acroos websites for user experience and anti-cluttering.
- Registration confirmation allowing each new user to verify their account before adding new recipes.
- Comments functionality allowing users to comment on the recipes.
- Rating functionality allowing users to rate different recipes out of 5 stars.
- More user profile functionality with access to changing email and even display name.
- Email notification functionality for Admin user to be alerted when a new recipe is added to the website.
- More Admin functionality letting the admin remove users and posts as necessary
- Extra layer of security for server-side file validation before uploading images.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinga-Templating-language](https://jinja.palletsprojects.com/en/3.0.x/)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries, and Programs Used

- [Gitpod](https://www.gitpod.io/)
    - **Gitpod** Is the code editor used to develop & push this project to Github.
- [GitHub](https://github.com/)
    - **Github** is used for:
    1. Tracking the project, and for version control.
    2. As a repository for other users to see the code used in the project.
- [Bootstrap](https://www.bootstrapcdn.com/)
    - **Bootstrap**  to structure the website, and to achieve responsive layout across various mobile devices.
- [JQuery](https://jquery.com)
    - **JQuery**  used with Bootstrap.
- [MongoDB](https://www.mongodb.com/)
     - **MongoDB**  Source-available cross-platform document-oriented database program.
- [Heroku](https://www.heroku.com/)
     - **Heroku**  A platform as a service used for deploying the project.
- [googleFonts](https://fonts.google.com/)
    - **Google Fonts**  for importing typography.
- [Font Awesome](https://fontawesome.com/)
   - **Font Awesome** for adding a icons.
   
- [W3C Markup Validator](https://validator.w3.org/)
   - **W3C Markup Validator** to check validity of HTML code.
- [PEP8 Online](http://www.pep8online.com/)
   - **PEP8 Validator** to check Python code for PEP8 requirements.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
   - **W3C CSS Validator** to check validity of CSS code.
- [JSHint Javascript Code Quality Tool](https://jshint.com/)
   - **JSHint Javascript Code Quality Tool** to check the quality of the Javascript code.
- [Balsamiq:](https://balsamiq.com/)
    - **Balsamiq** was used for creating [wireframes]() during the design process.




## Testing

### Testing User Stories from UX Section
#### First time visitor goals
- **I want to understand the main purpose of the website.**
    - When users enter the website all the recipes are presented for the visitors, which gives them the option to scroll through them or look at each recipe individually.
- **I want to easily navigate through the website.**
    - At the top of the page a sticky navigation bar is present, displaying all the links for new users to easily navigate through the website.
- **I want to find out how I can register to the website, and upload a recipe.**
    - On the navigation bar, right next to the Home link, Register link is presented for new users which leads them to the registration page.
- **I want to find out how I can search for recipes.**
    - On the home page, underneath the main image, there is a search bar present for users to easily search for recipes.

#### User goals
- **As a user i want to find out how to log into my profile**
    - On the navigation bar there is an accessible login button so user can be directed to login to there accounts.
- **I want to find out how I can add a new recipes.**
    - In the navigation bar once logged in there is an easily accessible add recipe button which directs the user to the add recipe page displaying steps by step info to add new recipes to the website.
- **I want to find out how I can edit my recipes.**
    - For users on the home page edit functionality is present on tablet sizes and larger and on the users profile editing is always present for the users recipes.
- **I want to find out how I can delete my recipes.**
    - For users on the home page delete functionality is present on tablet sizes and larger and on the users profile deleting is always present for the users recipes.
- **I want to find be able to see all my recipes**
    - On the users profile all of the users recipes are displayed for easy access and availability to the user to use crud functionality.

#### Admin User Goals

- **I want to be able to add new recipes**
    - In the navigation bar once logged in there is an easily accessible add recipe button which directs the user to the add recipe page displaying steps by step info to add new recipes to the website.
- **I want to be able to manage categories for users to upload there recipes into**
    - AN exclusive admin feature is being able to access the mange categories page which lets them add delete and update categories where neccessary around the website.
- **I want to be able to edit and delete recipes** 
    - The admin can access edit and delete there recipes fromeither there profile page or the home page on tablet sizes and larger.


## Database

- [MongoDB](https://www.mongodb.com) was used to create a database for this application.


## Deployment

- To view the deployed version of [Just_a-Taste](https://cookbook-manager-project.herokuapp.com/) Please take the following steps:

### Github

- Add this repository to your local workspace:
    - Click on the [Cookbook_Project repository on GitHub](https://github.com/OliverDaviesCodes/CookBook_Project) link.
    - Click on the **Code** button, and copy the URL.
    - Go into your local workspace, and open up a new terminal.
    - Type `git clone ` and paste the URL you copied from GitHub, and press enter. 
The process of cloning is now completed. For further information on cloning,
 visit [How to clone from GitHub](https://help.github.com/en/articles/cloning-a-repository).
### MongoDB Configuration

- Login to your [MongoDB](https://www.mongodb.com) Account. 
- From `Clusters` tab, click on `Connect`
- Select `Connect to your application`
- Select `Python` as `Driver` and choose `Version 3.6 or later`
- Create a new `env.py` file in your project, paste and save the connection link and variables.
- Create an instance of PyMongo

### Heroku Deployment
- Before deploying your project create a requirements.txt file by running the following command in the CLI:
```console
pip3 freeze --local > requirements.txt
``` 
- Create a Procfile file by running the following command in the CLI:
```console
echo web: python run.py > Procfile
```
- Log in to [Heroku](https://www.heroku.com/)
- Select `New` on your dashboard and then select `Create new app`
- Choose a name for your application, select your region, and then click `Create app`
- From the app dashboard, navigate to `Deploy` tab. 
- From `Deployment method` Click on `Github` and click `Search` then select your repository name. 
- Once you select your repository, click on `Connect`
- After you conntect to your repository, click on `Settings` tab on your app dashboard, and click on `Reveal Config Vars` and add your configuration variables to Heroku.
- Navigate to `Deploy` tab, and from `Manual deploy` choose your master branch, and click `Deploy Branch`
- After you deploy your branch `Enable Automatic Deploys`.
- Site is successfully deployed, and any futher changes on the app will automatically be updated everytime they are commited and pushed on Github.


## Credits

### Content

- The text content on the website was adapted by me other than some of the recipes which i pulled from google and the qouted stated below.
    - [Oatmeal](https://fitfoodiefinds.com/the-50-best-oatmeal-recipes-on-the-planet/)
    - [Pancakes](https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/)
    - [Chocolate Cake](https://iambaker.net/cake-recipes/)
    - [Steak](https://natashaskitchen.com/pan-seared-steak/)
    - [Qooute](https://littleraesbakery.com/2020/02/19/12-quotes-about-cooking-from-the-heart/)
    - [Roast Lamb](https://www.delish.com/cooking/recipe-ideas/recipes/a56354/best-roast-lamb-recipe/)
    - [fruit salad](https://www.cookingclassy.com/honey-lime-rainbow-fruit-salad/)
    - [roast Chicken](https://cafedelites.com/garlic-herb-butter-roast-chicken/)
    - [Apple Pie](https://www.tasteofhome.com/recipes/apple-pie/)

### Media
- The image content on the website were taken from Unsplash which is an open source free to use image gallery.
- [Unsplash](https://unsplash.com/s/photos/kitchen)


## Acknowledgements

- Thanks to my Mentor Reuben for supporting me through-out this entire process and shared his incredible knowledge and evelopment skills to really help me learn to implement all the necessary code.

## Disclaimer
- All content on the website, including images and text, are used for educational purposes only.


  #### __back to [Contents Table](#contents-table)__ 