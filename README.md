![logo](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/logo.png)

# **Ali Sadiq MS3 – Eat Middle East**

[View the live project here.]( https://middle-eastern-cookbook.herokuapp.com/)

## **Project Overview**

Welcome to the third project of my software development career. I have decided to create an online cookbook catered to middle eastern cuisine. The website will give users the opportunity to view, add, edit and delete recipes. Middle Eastern cuisine is one of my favourite, and I have a big passion for learning new recipes, therefore it is a project that I have a passion for. I will be using what I have learnt from the modules I have completed over the last few months. These include Python, the flask framework and MongoDB. I will also be using HTML, CSS, JavaScript, Jquery and the bootstrap framework, all of which I have used in previous projects. The main focus of this website is to create a CRUD application using Python. 

The website is called Eat Middle East. They are an online recipe database where users can register to make an account, add/edit/delete their own recipes, while viewing the recipes created by others.

## **Table of Contents**

  * [1. **UX**](#UX)
    + [**First time users**](#first-time-visitor-goals)
    + [**Returning users**](#returning-visitor-goals)
    + [**Frequent users**](#frequent-user-goals)

  * [2. **Design**](#DESIGN)
    + [**Colour Scheme**](#colour-scheme)
    + [**Typography**](#typography)

  * [3. **Wireframes & Features**](#wireframes-and-features)
    + [**Header**](#header)
    + [**Footer**](#footer)
    + [**Home**](#home-page)
    + [**Recipes**](#recipe-page)
    + [**Login**](#login-page)
    + [**Register**](#register-page)
    + [**Profile**](#profile-page)
    + [**Add Recipe**](#add-recipe-page)
    + [**Edit Recipe**](#edit-recipe-page)
    + [**Manage Recipes**](#manage-recipe-page)
    + [**404 Error**](#404-error-page)

  * [4. **Technologies Used**](#Technologies)

  * [5. **Testing**](#testing)

  * [6. **Deployment**](#deployment)

  * [7. **Content**](#content)

  * [8. **Media**](#media)

  * [9. **Acknowledgements**](#acknowledgements)

# **UX**

## First Time Visitor Goals

1.  As a First Time Visitor, I want to view recipes created by others without having to make an account.

2.  As a First Time Visitor, I want to be able to register to create an account.

3.  As a First Time Visitor, I want to be able to view any social media presence the company has.

4.  As a First Time Visitor, I want to be able to search for a recipe by name.

5.  As a First Time Visitor, I want to be able to navigate easily through the website, on desktop, mobile and tablet.

## Returning Visitor Goals

1.  As a Returning Visitor, I want to be able to log in to my account easily. 

2.  As a Returning Visitor, I want to be able to view my profile to see my details, as well as what recipes I have added. 

3.  As a Returning Visitor, I want to be able to filter search results to different courses and difficulty level. 

4.  As a Returning Visitor, I want to be able to add my own recipe to the cookbook. 

5.  As a Returning Visitor, I want to be able to logout of my profile before ending my session.


## Frequent User Goals

1.  As a Frequent User, I want to check to be able to edit and delete any recipes that I have added. 

2.  As a Frequent User, I want to be able to view just the recipes I have added.

Being a cooking enthusiast myself, I have used many cookbooks, varying from books to online versions.
With me being interested in this sector, I know what the user wants, making it easy for me to provide this in a simple way.

# **DESIGN**

## Colour Scheme

* The three main colours used are grey, white, and black.

## Typography

* The Uncial Antiqua font (from google fonts) is the font used for the logo and the titles to each page. The Crushed font is the main font used for all other content. Sans Serif is used as the fall-back font if for any reason the above fonts are not functioning. A snazzy, middle eastern theme is set which the Uncial Antiqua font achieves. The Crushed font is clear and easy to read. 

# **WIREFRAMES AND FEATURES**

# **Header**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - [Font Awesome](https://fontawesome.com/), Bootstrap, Flask

### Header wireframe with no user logged in

![wireframe-header-nouser](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-header-nouser.jpeg)

### Header wireframe with user logged in

![wireframe-header-user](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-header-user.jpeg)

## Features:

1.  The logo – this is of course in the header to the left, so it is on every page. On mobile devices the header sits to the left, with the burger menu to the right.

2.  Burger Menu – in mobile view, the navigation menu becomes a burger menu, which the user can click to open the rest of the menu. This saves space for the user, allowing them to easily navigate through the website. 

![header-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/header-mobile.png)

3.  The nav bar contains various links which contain for loops to only show on certain conditions.

•	When the user is not logged in, they are shown 4 links, Home, Recipes, Login, Register.

•	Once the user logs in, they are shown 5 links, Home, Recipes, Profile, Add Recipe, Logout.

•	If the user is admin, they are shown the same links as a user, but with a Manage Recipes link added.

### Header when no user is logged in:

![header-nouser](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/header-desktop-logout.png)

### Header when a user is logged in:

![header-user](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/header-desktop-logout.png)

4.  Each nav link has an icon from font awesome and changes colour to grey when hovering.

## Features to implement:

1. My initial idea was to have a login/register feature in the header. I decided against it for design purposes.

2. I originally had a search bar to the right on the navbar, however I decided to remove it as I already had a search function on the recipe and recipe filter pages.

# **Footer**

* Languages used – HTML, CSS

* Frameworks, Libraries & Programs Used - [Font Awesome](https://fontawesome.com/), Bootstrap

### Footer wireframe

![wireframe-footer](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-footer.jpeg)

## Features:

1.  Social media – the footer contains social media links to the company’s Facebook, Instagram and Twitter. These external links all open in a new tab.

2.  Copyright – to show the website is protected by copyright, using font awesome. 

### Footer on desktop:

![footer-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/footer-desktop.png)

### Footer on mobile:

![footer-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/footer-mobile.png)

# **Home page**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - [Font Awesome](https://fontawesome.com/), Bootstrap, Flask

### Desktop wireframe

![wireframe-home-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-home-desktop.jpeg)

### Mobile wireframe

![wireframe-home-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-home-mobile.jpeg)

## Features

1.  Main Container – this is a simple page inside a container. It contains a welcome title, to welcome the user to the website. The background for this container is set to an opacity of 0.9 so the user can see the text, as well as the image behind.

2.  Slogan – underneath the welcome title, is a slogan to entice the user. It states, “For you, made by you”. This tells the user that they can be a part of the website. 

3.  Links – at the bottom of the container, are some bootstrap buttons linking the user to different pages on the website. If the user is not logged in, there are 3 links shown. The first to the recipe page to see all recipes, the second to login and the third to register. If the user is logged in, there are 2 links shown. The first to the recipe page again and the second to the add recipe page. 

3.  Background image – all pages contain the same background image for consistency. This is a dining table containing various types of middle eastern food. I used a bright image to aid the design of the website. 

### Homepage with no user logged in

![homepage-no-user](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/home-desktop-logout.png)

### Homepage with user logged in

![homepage-user](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/home-desktop-login.png)

### Homepage mobile view

![homepage-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/home-mobile.png)

## Features to implement:

1.  I had the idea to add a card telling the user how many new recipes have been added in the last 7 days, but I decided against it. I wanted to keep the website simple.  

# **Recipe page**

* Languages used – HTML, CSS, JavaScript using JQuery, Python

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB, Jquery

#### Recipe page desktop wireframe

![wireframe-recipe-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-recipe-desktop.jpeg)

#### Recipe page mobile wireframe

![wireframe-recipe-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-recipe-mobile.jpeg)

#### Recipe page screenshot

![recipe-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/recipe-desktop.png)

#### Recipe page mobile screenshot

![recipe-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/recipe-mobile.png)

## Features

1.  Search bar – A search bar is shown above the recipes for the user to be able to search any particular recipe they are looking for. It searches the database by text against recipe name and description. 

![recipe-search](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/recipe-search.png)

2.  The search bar also contains a filter button. Once clicked, a collapsed div is shown. The user can now filter the recipes by each course, and each difficulty level. There is also a reset button which takes the user back to the recipe page without any filters.

![recipe-filter](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/recipe-filter.png)

3.  If there are no results from the search by text, a flash message is shown to shown “No Recipes found!”, as well as a bootstrap button to link the user back to all the recipes. 

![search-none](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/search-none.png)

4.  Main section – this section contains all the recipes added to the database unless the user has filtered using the search section.

5. Recipe details – the image of the food is set to the left of the main details of the recipe. These details include food name, course, description, difficulty level and time it takes to make. Underneath this section to the left is shown the ingredients and the method to make the food. On mobile devices, the image is above the main details to aid design.

6. Created by – underneath the above it tells the user who has created this recipe.

7. Edit/Delete – if the user is the creator of the recipe, bootstrap buttons are shown underneath to allow the user to edit or delete their recipe. Each delete button is followed by an alert to confirm whether the user would like to delete the recipe. If the user is logged in as admin, these buttons are shown on each recipe. 

![recipe-edit-delete](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/recipe-edit-delete.png)

8. Pagination – A pagination function has been set up to not have too many recipes showing on 1 page at a time. It has been set to show a maximum of 3 recipes on each page. The user can navigate through the pages at the bottom of the page using the numbered links. This is shown with a screenshot below:

![pagination](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/pagination.png)

## Features to implement

1. I think it would be a good idea to allow users to be able to comment and give feedback on other user's recipes.

# **Login page**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB

#### **Login page wireframe desktop**

![wireframe-login-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-login-desktop.jpeg)

#### **Login page wireframe mobile**

![wireframe-login-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-login-mobile.jpeg)

## Features

1.	Form – this page contains a simple form for the user to be able to log into their account. The form contains 2 fields, for the user’s username and password, both fields set to required to not allow the user to submit the form with no input. These fields have font awesome icons to aid design. 

2.  Incorrect entry – if the username or password are entered incorrectly, a flash message is shown to let the user know that either the username or password was incorrect. We do not want to tell the user which one is incorrect in case the user is attempting to enter an account that is not theirs. 

![flash-incorrect-login](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/incorrect-login.png)

3.  To check the password is correct, I used Werkzeug’s ‘check_password_hash’ function. 

4.  Register – underneath the form, the user is shown where to Register in case they do not have an account already. 

5.  Once the user has successfully logged in, a flash message is shown to welcome the user by name and they are taken to their profile page. 

6. If a user is already logged in and tries to visit this page by editing the URL. They are met with this message:

![error-login](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-login.png)

## Features to implement:

1. I wanted to add a forgotten password feature where the user can recover their password through a link that is sent to their email. I did not have enough time to carry out this task, but I definitely thought it was a good idea.

#### **Login page desktop and mobile** 

![login-form](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/login.png)

# **Register page**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB

#### **Register page wireframe (desktop)**

![wireframe-register-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-register-desktop.jpeg)

#### **Register page wireframe (mobile)**

![wireframe-register-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-register-mobile.jpeg)

## Features

1.	Form – this page contains a simple form for the user to be able to register a new account. The form contains 5 fields:

a.	Username

b.	Password

c.	Confirm Password (screenshot shown below)

![confirm-password](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/confirm-password.png)

d.	Cooking level – for the user to provide their experience level using a drop-down list.

e.	Favourite food

These fields have font awesome icons to aid design.

2. All fields are set to required, so the user is unable to submit the form without the required fields and formats.

3.	Login – underneath the form, the user is shown where to login in case they already have an account.

4.	Patterns and information – the username and password fields only allow A-Z and 0-9 to be entered. The username must be between 5-15 characters, and the password 7-15 characters. This information is shown below the relative field for the user. 

5.	Once the user registers, a flash message is shown to tell them they have successfully registered, and they are taken to their profile page.  

#### **Desktop and Mobile view**

![register-form](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/register.png)

# **Profile page**

* Languages used – HTML, CSS, Python, Javascript with JQuery

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB, JQuery

#### **Profile page wireframe (desktop)**

![wireframe-profile-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-profile-desktop.jpeg)

#### **Profile page wireframe (mobile)**

![wireframe-profile-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-profile-mobile.jpeg)

## Features

1.  This is a simple page showing the user’s details and what recipes they have added to the database.

2.  User details – A container showing the username, cooking level and favourite food of the user is shown. 

### **Desktop**

![profile-details-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/profile-desktop-details.png)

### **Mobile**

![profile-details-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/profile-mobile-details.png)

3.  Add recipe – A bootstrap button that links the user to the add recipe page. 

4.  User’s recipes – Cards showing the user’s recipes that they have added. They show the recipe name (the user can click the name to show the full details of the recipe), who it was added by and gives the user the option to edit or delete the recipe. If the user wants to delete, they are asked to confirm whether they are sure they want to delete the recipe. 

5.  Log out – A bootstrap button that allows the user to log out. An alert to confirm this is shown once clicked.

![confirm-logout](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/confirm-logout.png)

6. If a user attempts to visit a profile page without being logged in. They are met with this message:

![error-profile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-profile.png)

## Features to implement 

1. It would be a good idea to allow the user to edit their profile details from the profile page. If I had more time I would have actioned this.

#### **Desktop**

![profile-recipes-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/profile-desktop-recipes.png)

#### **Mobile**

![profile-recipes-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/profile-mobile-recipes.png)

# **Add recipe page**

* Languages used – HTML, CSS, Python, Javascript with JQuery

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB, JQuery

#### Add/Edit recipe page wireframe (desktop)

![wireframe-add-edit-recipe-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-add-desktop.jpeg)

#### Add/Edit recipe page wireframe (mobile)

![wireframe-add-edit-recipe-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-add-mobile.jpeg)

#### Add recipe page desktop

![add-recipe-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/add-recipe-desktop.png)

#### Add recipe page mobile

![add-recipe-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/add-recipe-mobile.png)

## Features

1.	Form – this page contains a form for the user to add all the required details of the recipe they want to add. Each field is set to required. It contains 8 fields:

a.	Image link to the food – contains a data tip that pops up when the user hovers over the font awesome icon, explaining to the user how to get their image address.

![data-tip](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/tip-window.png)

b.	Recipe Name

c.	Course – using a drop-down list.

d.	Short description – set to a minimum length of 10 characters.

e.	How long it takes to make? – field is set to only accept 0-9.

f.	Difficulty level out of 5 - using a drop-down list.

g.	Ingredients – using JQuery, the user can add an ingredient by clicking the font awesome plus icon, which shows an input text field. They can delete any ingredient by clicking the font awesome cross icon.

h.	Method – this input is exactly the same as the ingredients above, however the input field is larger. 

2.	Once the recipe is added using the bootstrap button to submit the form, the user is returned to the recipe page with a flash image to let the user know their recipe has been successfully added. 

3. If a user tries to visit this page without being logged in (ie. edits the URL), they are met with this message:

![error-add](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-add.png)

## Features to implement

1. In the future, it would be a good idea to have a more interactive way to upload a picture of the food. This could be where the user can upload an image from their own files.

2. With the above feature, I would also want to be able to limit the file size of the picture, the format, and the dimensions to fit the page.

# **Edit recipe page**

* Languages used – HTML, CSS, Python, Javascript with JQuery

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB, JQuery

#### Edit recipe page desktop

![edit-recipe-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/edit-recipe-desktop.png)

#### Edit recipe page mobile

![edit-recipe-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/edit-recipe-mobile.png)

## Features

1.	This page is exactly the same as the add recipe page mentioned above. The only differences are:

a.	The input fields values are already filled with the recipe details from the recipe the user would like to edit.

b.	The bootstrap buttons below now are Cancel, which takes the user back to the recipe page, or Submit changes, which gives the user a flash message to let them know their recipe has been updated.

3. If a user tries to visit this page without being logged in (ie. edits the URL), they are met with this message:

![error-edit](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-edit.png)

4. When the user submits their changes, they are shown just the recipe they have edited, on its own on the page.

# **Manage recipe page**

* Languages used – HTML, CSS, Python, Javascript with JQuery

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB, JQuery

#### Manage recipe page wireframe (desktop)

![wireframe-manage-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-manage-desktop.jpeg)

#### Manage recipe page wireframe (mobile)

![wireframe-manage-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-manage-mobile.jpeg)

## Features

1.	This page is only accessible by the admin user. If a user tries to visit this page by only changing the URL. They are met with this message below:

![error-manage](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-manage.png)

2.	Add recipe – the user is shown a bootstrap button for them to be able to add a recipe

3.	Recipe cards – The admin is shown all recipes added by all the users. Similar to the user profile page, they are shown a card with the recipe name (which they can click to reveal all the recipe’s details), a button to edit and delete the recipe, as well as who created the recipe. If the admin decides to delete the recipe, they are met with an alert to confirm this action is correct. 

![confirm-delete](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/confirm-delete.png)

## Features to implement

1. I thought it would be a good idea for the admin to be able to send feedback to a user regarding their recipe. For example, if the user's recipe is not considered middle eastern food, the admin can contact the user to discuss this with them, as oppose to just editing or deleting the recipe.

# **404 Error page**

## Features

1.	This page is shown when the user attempts to visit a URL that is not found on the website.

![error-404](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-404.png)

# **TECHNOLOGIES**

## Languages Used

* HTML5

* CSS3 

* JavaScript

* Python

## Frameworks, Libraries & Programs Used

* Bootstrap

    * Bootstrap was used to assist with the responsiveness and styling of the website.

* Google Fonts:

    * Google fonts were used for both Roboto-condensed and Raleway fonts.

* Font Awesome:

    * Font Awesome was used in the header and footer on each page, with social media links, app download links, and images alongside various captions and titles.

* JQuery:

    * JQuery was used to make it easier to use JavaScript. It gives me cleaner code and is very effective.

* Flask:

    * Flask was used as a Python web framework that provides useful tools and features that make creating web applications in Python easier. 

* MongoDB:

    * MongoDB was used as it is an easy and powerful way to store and retrieve huge amounts of data, quickly and effectively. 

* Git

    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* GitHub:

    * GitHub is used to store the projects code after being pushed from Git.

* Jinja 

    * Used to generate HTML from site templates

* Werkzeug

    * A python library to manage user management.

* Heroku:

    * Heroku is used for remote hosting the website.



# **TESTING**

[This section can be found here.](https://github.com/alisadiq91/middleEasternCookbook/blob/master/testing.md)

# **DEPLOYMENT**

## Heroku

This project is hosted on Heroku. It has been set up so that each commit in the workspace automatically updates the deployed site on Heroku.

* To create a heroku application, perform the following steps:

1. Log in or create an account on [Heroku](https://www.heroku.com).

2. On the dashboard, select 'new' and 'create new app'.

3. Add an app name (this must be unique).

4. Select the region closest to you.

5. Click 'create app'.

* Before you can begin to deploy, you must perform these steps:

1. Select your app from the dashboard.

2. Click 'settings'.

3. Under 'config vars', click 'reveal config vars'.

4. Add the KEY and VALUE from each variable eg ("IP", "0.0.0.0").

* Once the variables are entered, follow these steps:

1. You must create a requirements.txt file in your workspace so that Heroku knows which python modules to install.

    * To do this, in your terminal type:  pip freeze > requirements.txt.

2. Create a Procfile to tell Heroku the command to launch the app.

    * To do this, in your terminal type: python app.py > Procfile.

* After these steps, you can begin to deploy by following these steps:

1. From the menu, select 'deploy'.

2. Choose your deployment method, in this project I used Github.

3. Select your GitHub account, and type the name of the repository and click 'search'.

4. When it has found the correct repository, click 'Connect'.

5. Below this, under the Manual deploy section, choose the branch you would like to deploy from (for this project I used Master)

6. Click 'deploy branch'.

7. You will then be met with this message 'Your App has successfully deployed'.

* To automatically have each commit deploy to your Heroku app, follow these steps:

1. Under the automatic deployment section, click 'Enable Automatic Deployment'.


### I used GitPod to write my code.

I regularly used Git Push to deploy this page to GitHub. Whenever I completed a page, fixed an error, or finished coding for the day, I would:

    1. 'git status' - this shows me a list of what has been edited.

    2. 'git add -A' - to add what has been edited ready to commit.

    3. 'git commit -m"reason for commit"' - this commits what was added ready to push and gives the reason for the commit.

    4. 'git push' - this deployed the changes above to the live site.

To launch a Http server using the development mode code for the application, use the following command:

    python3 app.py

## How to run this project locally

### To clone this project:

1. Follow this link to the [Project GitHub repository](https://github.com/alisadiq91/middleEasternCookbook)

2. Under the repository name, click "Clone or download".

3. In the Clone with HTTPs section, copy the clone URL for the repository.

4. In your local IDE open GIT Bash.

5. Change the current working directory location where you want the cloned directory to be made.

6. Type git clone, and then paste the URL you copied in Step 3.

7. Press Enter. Your local clone will be created.

8. Install requirements to your local IDE by typing the following into your CL:

    * pip3 install -r requirements.txt

9. Create a collection using [MongoDB](https://www.mongodb.com/)

    * Login to your account

    * Create a cluster

    * Create a collection using the following structure:
    
        1. Collection Names - categories, recipes, users

        2. Under Categories - there should be 4 objects :

                1. category_name: "Starter"
                2. category_name: "Sides"
                3. category_name: "Mains"
                4. category_name: "Dessert"

10. Create a '.gitignore' file.

11. Create an 'env.py' file.

12. Add 'env.py' and 'pycache/' to the .gitignore file.

13. The env.py file must contain the following code:

        import os

        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "[INSERT_ID]")
        os.environ.setdefault("MONGO_URI", "[INSERT_ID]")
        os.environ.setdefault("MONGO_DBNAME", "[INSERT_ID]")

14. Where "INSERT_ID" is present, you must enter your own values, matching the config_vars on your Heroku app.

    * The SECRET_KEY can be any value, I used [Random Key Gen](https://randomkeygen.com/).

    * The MONGO_URI has to be taken from MongoDB.

        1. Click the 'Overview' tab on your cluster.

        2. Click 'Connect'.

        3. Click 'Connect your application'.

        4. Ensure you select the correct Python version you are using.

        5. Copy the connection string.

        6. Ensure you replace the Username and Password when you set up the Database Access.
        
    * The MONGO_DBNAME is the name of your database in MongoDB.

# **CONTENT**

### All content was written by the coder apart form those listed below.

* [Bootstrap register form] (https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=simple-registration-form)

* [Bootstrap login form] (https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=simple-login-form)


* [Tooltip for add/edit recipe form] (https://stackoverflow.com/questions/19480010/adding-a-tooltip-to-an-input-box)


* [Bootstrap footer] (https://mdbootstrap.com/docs/standard/navigation/footer/)

* [Pagination] (https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)


# **MEDIA**

### I obtained my image from google images. Here is the link for the image:

* [Background image for each page]( https://mk0kaleelao979sb1ktf.kinstacdn.com/wp-content/uploads/2019/08/shutterstock_1690553083-1536x1025.jpg)

# **ACKNOWLEDGEMENTS**

* My Mentor for continuous helpful feedback.

* The Code Institute tutor support team for pointing me in the right direction when I needed help.

# **Thank you!!**

#### Thank you for taking the time to enjoy my third project as a web developer. I thoroughly enjoyed creating this website. Middle Eastern cuisine is my favourite type of food, which I enjoy learning new recipes for, so this is a website that I hope I can continue to grow as I learn more and more in my career. I hope you enjoy using my website!
