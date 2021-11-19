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

8. [**Disclaimer**](#disclaimer)



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

There are three Adobe fonts used throught the website. [P22 Pooper Black](https://fonts.adobe.com/fonts/p22-pooper-black) is used for logo, [Antique Olive Nord](https://fonts.adobe.com/fonts/antique-olive) used for all titles and post "Read More" links. [Paralucent](https://fonts.adobe.com/fonts/paralucent) was used on all the texts to give the website a modern and minimalistic feel.



### Imagery

- Images on the website were chosen to set the sense of quality, and taste of the blog, and to make sure users have a good experience during their visit.

### Wireframes

- [Homepage](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Homepage.png)
- [Blog Post Page](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Blog%20Post%20Page.png)
- [Register](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Register.png)
- [Login](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Login.png)
- [Contact](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Contact.png)
- [Profile Page for New User](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Profile%20New%20User.png)
- [Profile Page without Posts](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Profile%20user%20without%20posts.png)
- [Profile Page with Posts](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Profile%20with%20posts.png)
- [Admin Profile Page](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Admin%20Profile%20Page.png)
- [Add Post](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Add%20Post.png)
- [Edit Post](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Edit%20Post.png)
- [Add Category](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Add%20Category.png)
- [Edit Category](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Edit%20Category.png)
- [Admin Dashboard](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Admin%20Dashboard.png)
- [Error 404](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Error%20404.png)
- [Error 500](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Error%20500.png)


## Features

### Existing Features

- Responsive on all device sizes.
- Navbar and Footer is visible on all pages.

 **Navbar**
 - Fixed on top of the page on all device sizes.
 - Shown as a collapsible navbar with a hamburger button for triger on Mobile devices and Tables.
 - Features a search bar allowing user to make searches throughout the website. Search function allows users to search for Posts by Author and title, and allows user to search posts by category.
 - Features 3 different layouts, for guest users Home, Login, Register and Contact links are present.
 - For Registered users, Home, Profile, Add Post, Logout and Contact links are Present.
 - For Admin user All the links are present along with a link for Admin Dashboard.

 **Homepage**
- Features an interactive, and modern design.
- Using Javascript animations, Post images, and Titles are seamlessly presented to the user in an orderly fashion as user scrolls through the page, providing a unique experience.
- Features Pagination to show only 5 posts per page for a clean UX.
- Each post on homepage displays Author, Post date, and Category information, and each Category color is given a unique color using Jquery.
- For post authors, a Delete and Edit button is displayed on their post for users to easily manage their posts from Homepage.
- For Admin user all the posts feature a Delete and Edit button, allowing Admin user to easily Edit or Delete Unwanted user posts directly from the Homepage.

 **Register Page**
- Features a clean registration form for user to signup for the blog.
- Each section of form input area features a placeholder text.
- Underneath the form inputs, there is a placeholder text explaining the required data for input, helping users to easily match the requested format.
- Password input field features a password match validator and gives feedback to user if their passwords match. 

 **Login Page**
- Features a clean login form for users to login to their blog.
- Each section of form input area features a placeholder text.
- Underneath the form inputs, there is a placeholder text explaining the required data for input, helping users to easily match the requested format.
- Upon succcessful submission, user is redirected to their own profile page.

 **Profile Page**
- Features a clean layout.
- Shows a greeting message to the User upon successful login.
- Features a section showing all the posts by the user, allowing them to edit or delete their posts.
- Features a add post button allowing users to easily reach to add post page from their profile.
- If user has no posts, then a message is presented to the user, asking them if they would like to add a new post.
- At the bottom of the page there is a "Delete Account" button featuring a modal for user confirmation.

 **Add Post Page**
- Stricted only for registered users.
- Page features a clean form for users to use, outlining all the required information in the form.
- Form features an image preview section allowing users to see their post images before uploading.
- Using file upload, and Cloudinary service, form allows users to easily upload their image to the cloud, and eliminates the hassle of looking for image urls.
- File upload input allows user to only upload image files such as jpeg, jpg, and png. Any other file extensions are restricted.
- After submission, form checks if the current Post title exits in the database, restricting users from adding duplicate posts.
- Upon successful post, user get redirected to the homepage and greeted with a success message.

**Edit Post Page**
- Stricted only for post authors.
- Page features the same form and features as the Add Post page.
- Each section of the form is pre-filled with the data they provided when they submited the form, allowing users to easily edit the post information.
- After submission, form checks if the current Post title exits in the database, restricting users from adding duplicate posts.
- Upon successful post, user get redirected to the homepage and greeted with a success message.

**Blog Post Page**
- Allowed for visitors and registered users to see.
- At the top of the page, post title presented.
- Underneath the title post information such as Author, Post Date, Category, and Address information is presented to the users. For post authors and admin an Edit and Delete button is presented allowing author or Admin user to easily manage the post.
- Underneath the info tags Post image is shown to the user.
- Underneath the post image, post content is presented.
- Underneath the post content, a link for the place's website is present, which opens the website in a new tab for users to get more information about the place.

**Contact Page**
- Allowed for all visitors and users of the blog.
- Using Flask Mail, users are able to contact the Blog Admin via the form.
- Upon successfull submission users are greeted with a success message, and email is sent for Admin user to see.

**Admin Dashboard**
- Stricted for Admin use only, and features a variety options for the Admin user to easily manage and be in total control.
- On top of the page, info cards are presented for the admin user. Each card shows a real-time information about total number of users, total number of posts, and total number of categories.
- Underneath the blog info cards, a responsive table of registered user list is presented along with all the information users provided. Next to each user there is a call to action button for user deletion, allowing admin user to delete any unwanted users. Admin user deletion is restricted from the table.
- Underneath the Registered users table, All the categories are listed for Admin user to manage. Along with a Add Category button for Admin user to easily add new categories if needed.
- Underneath the Categories section, Recent posts section is presented to the Admin user showing all the current posts on the page showing their titles and images. Each post card features a Edit and Delete button, allowing Admin user to easily manage current posts on the blog.

**Add Category**
- Stricted for Admin use only.
- Page features a single line form allowing Admin user to add new categories.
- After submission Add category function checks if Category already exits, if it does, it shows a message to Admin user that category already exits.

**Edit Category**
- Stricted for Admin use only.
- Page features a single line form allowing Admin user to edit the selected category.
- After submission Edit Category function checks if Category already exits, if it does, it shows a message to Admin user that category already exits.

**404 Error Page**
- Page features custom error message with a button that takes user back to the homepage

**500 Error Page**
- Page features custom error message with a button that takes user back to the homepage


### Features Left to Implement

- Maps section showing each place on a map.
- Registration confirmation allowing each new user to verify their account before adding new posts.
- Comments functionality allowing users to comment on the posts.
- User profile picture functionality, allowing users to add profile pictures, and show them next to their posts, and comments.
- Email notification functionality for Admin user to be alerted when a new post is added to the blog.
- Functionality for automatically assigning new tag colors for new categories. 
- Extra layer of security for server-side file validation before uploading images.

## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries, and Programs Used

- [Visiual Studio Code ](https://code.visualstudio.com)
    - **Vscode** Is the code editor used to develop, commit & push this project to Github.
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
     - **Heroku**  A platform as a service (PaaS) used for deploying the project.
- [WOW.js](https://wowjs.uk)
    - **WOW.js**  a JavaScript plugin that reveals animations when you scroll.
- [Animate.css](https://animate.style)
    - **Animate.css**  a cross-browser library of CSS animations.
- [Adobe Fonts](https://fonts.adobe.com/)
    - **Adobe Fonts**  for importing typography.
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

Testing information can be found in seperate [TESTING.md](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/TESTING.md) file.

## Database

- [MongoDB](https://www.mongodb.com) was used to create a database for this application.

<img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/Database.png">

### Users collection

|Key|Type|
|---|----|
|_id|ObjectId|
|name|String|
|last_name|String|
|username|String|
|password|String|
|email|String|
|registered|datetime|

### Posts Collection

|Key|Type|
|---|----|
|_id|ObjectId|
|post_title|String|
|post_category|String|
|post_content|String|
|post_image|String|
|post_address|String|
|website|String|
|author|String|
|post_date|datetime|

### Categories Collection

|Key|Type|
|---|----|
|_id|ObjectId|
|category_name|String|

## Deployment

- To view the deployed version of [Wonderdam](https://wonderdam.herokuapp.com) Please take the following steps:

### Github

- Add this repository to your local workspace:
    - Click on the [Wonderdam repository on GitHub](https://github.com/yigitaksoy/Wonderdam) link.
    - Click on the **Code** button, and copy the URL.
    - Go into your local workspace, and open up a new terminal.
    - Type `git clone ` and paste the URL you copied from GitHub, and press enter. It should look like this:
```console
git clone https://github.com/*username*/*repository*
```
The process of cloning is now completed. For further information on cloning,
 visit [How to clone from GitHub](https://help.github.com/en/articles/cloning-a-repository).
### MongoDB Configuration

- Login to your [MongoDB](https://www.mongodb.com) Account. 
- From `Clusters` tab, click on `Connect`
- Select `Connect to your application`
- Select `Python` as `Driver` and choose `Version 3.6 or later`
- Create a new `env.py` file in your project, paste and save the connection link and variables.
 ```console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<secret_key>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@myfirstcluster.8s17w.mongodb.net/<db_name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<db_name>")
````
- Create an instance of PyMongo
```console
mongo = PyMongo(app)
```

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

- The text content on the website were adapted from each establishments website, aloing with [Amsterdam Magazine](https://www.amsterdammagazine.com/nl/) and [I amsterdam](https://www.iamsterdam.com/en/blog)

### Media
- The image content on the website were taken from each establishments own website, and social media accounts. 

### Codes

 - Code to fix mixed content issue was taken from [Stackoverflow](https://stackoverflow.com/questions/35178135/how-to-fix-insecure-content-was-loaded-over-https-but-requested-an-insecure-re/35178323)
 - Code for line-clamp was taken from [CSS Tricks](https://css-tricks.com/almanac/properties/l/line-clamp/)
 - Code to show image previews on Add/Edit Posts are taken from [Learn Code Web](https://learncodeweb.com/snippets/browse-button-in-bootstrap-4-with-select-image-preview/)
 - Code for user password input validation on Register form was taken from [Stackoverflow](https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page)
 - Code for HTML email input pattern attribute was taken from [Stackoverflow](https://stackoverflow.com/questions/5601647/html5-email-input-pattern-attribute)
 - Code for Setting up Flask Mail was taken from Karina's Flask Mail setup instructions on [Slack](https://slack-files.com/T0L30B202-F01KX8QUEJF-6a89867a18).
 - Code used for setting up Flask Pagination were taken from [Pythonhosted](https://pythonhosted.org/Flask-paginate/), and [Mozillag](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)
 - Code for styling and structuring the forms were taken from [Colorlib](https://colorlib.com/etc/regform/colorlib-regform-8/)
 - Code for fitting bootstrap card images evenly was taken from [Stackoverflow](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width/53252725)
 - Code for live character count on Add/Edit Post forms were taken from [Codexworld](https://www.codexworld.com/live-character-counter-javascript/)
 - Code for handeling errors on Flask was taken from [Palletsprojects](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)


## Acknowledgements


## Disclaimer
- All content on the website, including images and text, are used for educational purposes only.

## Miscellaneous

- During the early development stages of the project, delete modal title was updated on User Profile page, but due to long hours of coding this commit was mis-stated as "Update delete modal title on post page" which was meant for Profile Page. [See commit](https://github.com/yigitaksoy/Wonderdam/commit/a0547907ea744e8d0e4447f9a7611a32a2c425dd)

- During the early development stages of this project, Admin user functionality was borrowed from a fellow student at Code Institute [Franciskadtt](https://github.com/Franciskadtt/the-growth-club) along with 3 lines of comments as a placeholder, but later on this function was updated, and implementations were left out. [See commit](https://github.com/yigitaksoy/Wonderdam/commit/859b95a2ee8cf87e2294e1eb0804667ca7892b80)

- During the final development stages of the project, `datetime` format for `post_date` value was updated. During the committing process IDE gave an error related to an extension called [Git Lens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens), and due this malfunctioning 2 seperate commits with the same name, but with different changes were added, which was meant to be a single commit. [See commit-1](https://github.com/yigitaksoy/Wonderdam/commit/3e7535aaa859ca28c24152ceda7d921377d16575), [See commit-2](https://github.com/yigitaksoy/Wonderdam/commit/475f63afa671bf8d88851cd91c343b26a0b9cb9e)

  #### __back to [Contents Table](#contents-table)__ 