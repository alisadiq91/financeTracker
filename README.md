![logo](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/logo.png)

# **Ali Sadiq MS3 – Eat Middle East**

[View the live project here.]( https://middle-eastern-cookbook.herokuapp.com/)

Welcome to the third project of my software development career. I have decided to create an online cookbook catered to middle eastern cuisine. The website will give users the opportunity to view, add, edit and delete recipes. Middle Eastern cuisine is one of my favourite, and I have a big passion for learning new recipes, therefore it is a project that I have a passion for. I will be using what I have learnt from the modules I have completed over the last few months. These include Python, the flask framework and MongoDB. I will also be using HTML, CSS, JavaScript, Jquery and the bootstrap framework, all of which I have used in previous projects. The main focus of this website is to create a CRUD application using Python. 

The website is called Eat Middle East. They are an online recipe database where users can register to make an account, add/edit/delete their own recipes, while viewing the recipes created by others.

# **UX - USER STORIES**

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
With me being interesteed in this sector, I know what the user wants, making it easy for me to provide this in a simple way.

# **DESIGN**

## Colour Scheme

* The two main colours used are grey and white.

## Typography

* The Uncial Antiqua font (from google fonts) is the font used for the logo and the titles to each page. The Crushed font is the main font used for all other content. Sans Serif is used as the fallback font if for any reason the above fonts are not functioning. A snazzy, middle eastern theme is set which the Uncial Antiqua font achieves. The Crushed font is clear and easy to read. 

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
•	When the user is not logged in, they are shown 4 links, Home, Recipes, Login, Register. As well as the search bar.
•	Once the user logs in, they are shown 5 links, Home, Recipes, Profile, Add Recipe, Logout. As well as the search bar.
•	If the user is admin, they are shown the same links as a user, but with a Manage Recipes link added. As well as the search bar. 

### Header when no user is logged in:

![header-nouser](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/header-desktop-logout.png)

### Header when a user is logged in:

![header-user](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/header-desktop-logout.png)

4.  Each nav link has an icon from font awesome and changes colour to grey when hovering.

5.  A search bar is available for the user to be able to search the website for a particular recipe, this searches the MongoDB database for text in the recipe name and recipe description.  

## Features to implement:

1.  My initial idea was to have a login/register feature in the header. I decided against it for design purposes.

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

2.  Slogan – underneath the welcome title, is a slogan to entice the user. It states “For you, made by you”. This tells the user that they can be a part of the website. 

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


#### Recipe page mobile screenshot


## Features

1.  Search bar – A search bar is shown above the recipes for the user to be able to search any particular recipe they are looking for. Similar to the search bar in the navigation menu, it searches the database by text against recipe name and description. 

2.  The search bar also contains a filter button. Once clicked, a collapsed div is shown. The user can now filter the recipes by each course, and each difficulty level. There is also a reset button which takes the user back to the recipe page without any filters.

3.  If there are no results from the search by text, a flash message is shown to shown “No Recipes found!”, as well as a bootstrap button to link the user back to all the recipes. 

4.  Main section – this section contains all the recipes added to the database, unless the user has filtered using the search section.

5. Recipe details – the image of the food is set to the left of the main details of the recipe. These details include food name, course, description, difficulty level and time it takes to make. Underneath this section to the left is shown the ingredients and the method to make the food. On mobile devices, the image is above the main details to aid design.

6. Created by – underneath the above it tells the user who has created this recipe.

7. Edit/Delete – if the user is the creator of the recipe, bootstrap buttons are shown underneath to allow the user to edit or delete their recipe. Each delete button is followed by an alert to confirm whether the user would like to delete the recipe. If the user is logged in as admin, these buttons are shown on each recipe. 

8. Pagination – A pagination function has been set up to not have too many recipes showing on 1 page at a time. It has been set to show a maximum of 3 recipes on each page. The user can navigate through the pages at the bottom of the page using the numbered links. 

# **Login page**

* Languages used – HTML, CSS, Python

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB

#### **Login page wireframe desktop**

![wireframe-login-desktop](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-login-desktop.jpeg)

#### **Login page wireframe mobile**

![wireframe-login-mobile](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/wf-login-mobile.jpeg)

## Features

1.	Form – this page contains a simple form for the user to be able to log into their account. The form contains 2 fields, for the user’s username and password, both fields set to required. These fields have font awesome icons to aid design. 

2.  Incorrect entry – if the username or password are entered incorrectly, a flash message is shown to let the user know that either the username or password was incorrect. We do not want to tell the user which one is incorrect in case the user is attempting to enter an account that is not theirs. 

![flash-incorrect-login](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/incorrect-login.png)

3.  To check the password is correct, I used Werkzeug’s ‘check_password_hash’ function. 

4.  Register – underneath the form, the user is shown where to Register in case they do not have an account already. 

5.  Once the user has successfully logged in, a flash message is show to welcome the user by name and they are taken to their profile page. 

6.  Forgot password?

7. If a user is already logged in and tries to visit this page by editing the URL. They are met with this message:

![error-login](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-login.png)

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
c.	Confirm Password
d.	Cooking level – for the user to provide their experience level using a drop-down list.
e.	Favourite food
These fields have font awesome icons to aid design and are set to required. 

2.	Login – underneath the form, the user is shown where to login in case they already have an account.
3.	Patterns and information – the username and password fields only allow A-Z and 0-9 to be entered. The username must be between 5-15 characters, and the password 7-15 characters. This information is shown below the relative field for the user. 
4.	Once the user registers, a flash message is shown to tell them they have successfully registered and they are taken to their profile page.  


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

## Features

1.	Form – this page contains a form for the user to add all the required details of the recipe they want to add. Each field is set to required. It contains 8 fields:
a.	Image link to the food – contains a data tip that pops up when the user hovers over the font awesome icon, explaining to the user how to get their image address. 
b.	Recipe Name
c.	Course – using a drop-down list.
d.	Short description – set to a minimum length of 10 characters.
e.	How long it takes to make? – field is set to only accept 0-9.
f.	Difficulty level out of 5 – using a range slider.
g.	Ingredients – using JQuery, the user can add an ingredient by clicking the font awesome plus icon, which shows an input text field. They can delete any ingredient by clicking the font awesome cross icon.
h.	Method – this input is exactly the same as the ingredients above, however the input field is larger. 

2.	Once the recipe is added using the bootstrap button to submit the form, the user is returned to the recipe page with a flash image to let the user know their recipe has been successfully added. 

3. If a user tries to visit this page without being logged in (ie. edits the URL), they are met with this message:

![error-add](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-add.png)

# **Edit recipe page**

* Languages used – HTML, CSS, Python, Javascript with JQuery

* Frameworks, Libraries & Programs Used - Bootstrap, [Font Awesome](https://fontawesome.com/), Flask, MongoDB, JQuery

## Features

1.	This page is exactly the same as the add recipe page mentioned above. The only differences are :

a.	The input fields values are already filled with the recipe details from the recipe the user would like to edit.

b.	The bootstrap buttons below now are Cancel, which takes the user back to the recipe page, or Submit changes, which gives the user a flash message to let them know their recipe has been updated.

3. If a user tries to visit this page without being logged in (ie. edits the URL), they are met with this message:

![error-edit](https://github.com/alisadiq91/middleEasternCookbook/blob/master/assets/images/error-edit.png)

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

# **TESTING**

## HTML Validation

#### **Home page** 

* No errors or warnings were found.

![html-validator-index](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/html-index.png)

#### **Find us page**

* No errors or warnings were found.

![html-validator-findus](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/html-findus.png)

#### **Covid page**

* No errors or warnings were found.

![html-validator-covid](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/html-covid.png)

#### **FAQs page**

* No errors or warnings were found.

![html-validator-faqs](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/html-faqs.png)

#### **Contact us page**

* No errors or warnings were found. 

![html-validator-contact](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/html-contact.png)

## CSS validation

* 

![css-validator](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/cssvalidator.png)

## JavaScript code quality tool

* I used [JSHint](https://jshint.com/) to check my JavaScript code for errors.

* There were no errors for either script.js

## Lighthouse

* I used inspect on google chrome to use the Lighthouse tool to check the performance of my web pages. The performance results were all either 99 or 100. Below are the results for each webpage.

### Home page
![lighthouse-home](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-home.png)

### Recipe page
![lighthouse-findus](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-findus.png)

### Login page
![lighthouse-covid](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-covid.png)

### Register page
![lighthouse-faqs](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-faqs.png)

### Profile page
![lighthouse-contact](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-contact.png)

### Add recipe page
![lighthouse-contact](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-contact.png)

### Edit recipe page
![lighthouse-contact](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-contact.png)

### Manage recipe page
![lighthouse-contact](https://github.com/alisadiq91/PharmOnline/blob/master/assets/images/lighthouse-contact.png)

## Bugs 

1. When adding the filter feature to the search bar. I had trouble getting the difficulty level to find results.

    * This was due to the function for the filter for the courses taking priority over the difficulty level function as it was before it in the python file. 

    * To fix it I had to alter the 

    * The code is shown below:

# **UX Testing**

## First time visitors

#### Aim

* As a First Time Visitor, I want to view recipes created by others without having to make an account. 

#### Result

* The homepage contains a bootstrap button to the recipe page allowing the users to easily navigate there.

* The navbar contains a recipe nav-link on every page. Again, giving the user an easy way to navigate to the recipe page.

* The recipe page shows all the recipes created by all users, in a neat, orderly fashion, showing a maximum of 3 recipes on a page, using pagination.

* The recipe page is available to all users, whether they have an account or not.

#### Aim

* As a First Time Visitor, I want to be able to register to create an account.

#### Result

* The homepage contains a bootstrap button to take the user to the register page.

* The navbar contains a register nav-link, which is present on all pages, provided the user is not logged in already.

* The register page contains a simple form using bootstrap for the user to enter their details and make an account.

#### Aim

* As a First Time Visitor, I want to be able to view any social media presence the company has.

#### Result

* Each page contains a footer created using bootstrap that has external links to all the company’s social media accounts.

#### Aim

* As a First Time Visitor, I want to be able to search for a recipe by name.

#### Result

* The navbar contains a search bar to the right where the user can search the database by text by the recipe name or description.

* The recipe page also contains a search bar at the top, that uses the same function as the search bar in the navbar. 

#### Aim

* As a First Time Visitor, I want to be able to navigate easily through the website, on desktop, mobile and tablet.

#### Result

* The website contains a navbar on every page where the user can easily navigate through the relevant pages.

* The navbar links that are shown differ depending on whether the user is logged in, logged out, or is an admin. 

* The navbar becomes a bootstrap burger menu on smaller devices, to not overload the page for the user on their smaller device. 


## **Returning users** 

#### Aim

* As a Returning Visitor, I want to be able to log in to my account easily.

#### Result

* The home page contains a bootstrap button that links the user to the log in page.

* The navbar also contains a nav-link to the log in page.

* The login page contains a simple bootstrap form where the user can enter their username and password. If either of these details are incorrect, the same flash message is shown to let the user know that either of the details are wrong.

#### Aim

* As a Returning Visitor, I want to be able to view my profile to see my details, as well as what recipes I have added.

#### Result

* Once the user is logged in, they are met with a flash message welcoming them to their account.

* They are taken to their profile page, which shows them their username, chef level and favourite food.

* Below these details are bootstrap cards showing the user the names of the recipes they have added. When they click the name, it shows them the full details of the recipe on a separate page.

* The cards also contain edit and delete options for the user to perform these actions on their recipes.

#### Aim

* As a Returning Visitor, I want to be able to filter search results to different courses and difficulty level.

#### Result

* The search filter on the recipe page contains filter options, by course or difficulty level.

* When any option is clicked, the page only shows the recipes under the filter that the user has chosen. 

* The search bar has a reset button where the user can return to the original page where all recipes are shown.

#### Aim

* As a Returning Visitor, I want to be able to add my own recipe to the cookbook.

#### Result

* There are various bootstrap button links on the website for the user to add a new recipe. These are located on the home page (if the user is logged in), on the user’s profile page, and in the navbar (if the user is logged in). 

* These links take the user to the add recipe page which contains a form. This form allows the user to provide the details required for the recipe to be added to the database and recipe page. 

#### Aim

* As a Returning Visitor, I want to be able to logout of my profile before ending my session.

#### Result

* The navbar contains a nav-link where the user can log out of their account. 

* The profile page also contains a bootstrap button where the user can log out.

* When the log out buttons/links are pressed, the user is met by an alert to check whether they are sure they want to log out or not. 
 
## **Frequent users**

#### Aim

* As a Frequent User, I want to check to be able to edit and delete any recipes that I have added.

#### Result

* The profile page gives the users the option to edit or delete all their recipes that they have added.

* The recipe page also gives the user the option to edit or delete their recipe, these options are only shown under the recipes that the user had added themselves.

#### Aim

* As a Frequent User, I want to be able to view just the recipes I have added.

#### Result

* The profile page shows the user all the recipes they have added as bootstrap cards. All the user has to do is click the name of the recipe to show it’s full details.

# **Further Testing**

* The Website was tested on Google Chrome, Internet Explorer, Mozilla Firefox and Safari browsers.

* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone11 (portrait and landscape), iPad (portrait and landscape), Samsung Galaxy S10 (portrait and landscape) and other android devices.

* I used [responsinator](https://www.responsinator.com/) to make sure it responded to all devices.

* Each link was clicked various times on each page and each device to ensure they were all working correctly.

* All the forms were filled out numerous times. Each form was filled out deliberately with errors to see if the flash messages and form validation were working correctly. 

* I asked 10 family and friends to use the website and look for any errors or bugs. I asked them all to view the website on their laptop, phone and tablet. I also asked them to try all the links, and to fill the forms out with errors to see if it allowed them to submit.

# **DEPLOYMENT**

### I used GitPod to write my code.

I regularly used Git Push to deploy this page to GitHub. Whenever I completed a page, fixed an error, or finished coding for the day, I would:

    1. "git status" - this shows me a list of what has been edited.

    2. "git add ." - to add what has been edited ready to commit.

    3. "git commit -m" - this commits what was added ready to push.

    4. "git push" - this deployed the changes above to the live site.

### I used the information in this [webpage](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/creating-a-github-pages-site) to create my GitHub pages site.

The link above gave me the following steps.

    1.  Log in to GitHub and locate the GitHub Repository.

    2.  At the top of the Repository (not top of page), locate the "Settings" Button on the menu.

    3.  Scroll down the Settings page until you locate the "GitHub Pages" Section.

    4.  Under "Source", click the dropdown called "None" and select "Master Branch".

    5.  The page will automatically refresh.

    6.  Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

## How to run this project locally

### To clone this project:

1. Follow this link to the [Project GitHub repository](https://github.com/alisadiq91/PharmOnline)

2. Under the repository name, click "Clone or download".

3. In the Clone with HTTPs section, copy the clone URL for the repository.

4. In your local IDE open GIT Bash.

5. Change the current working directory location where you want the cloned directory to be made.

6. Type git clone, and then paste the URL you copied in Step 3.

7. Press Enter. Your local clone will be created.

## How I deployed this project to Heroku?

# **CONTENT**

### All content was written by the coder apart form those listed below.

* [Bootstrap register form] (https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=simple-registration-form)

* [Bootstrap login form] (https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=simple-login-form)


* [Tooltip for add/edit recipe form] (https://stackoverflow.com/questions/19480010/adding-a-tooltip-to-an-input-box)

* [Bootstrap slider] 
(https://www.w3schools.com/howto/howto_js_rangeslider.asp)

* [Bootstrap footer] (https://mdbootstrap.com/docs/standard/navigation/footer/)


# **MEDIA**

### I obtained my image from google images. Here is the link for the image:

* [Background image for each page]( https://mk0kaleelao979sb1ktf.kinstacdn.com/wp-content/uploads/2019/08/shutterstock_1690553083-1536x1025.jpg)

# **ACKNOWLEDGEMENTS**

* My Mentor for continuous helpful feedback.

* The Code Institute tutor support team for pointing me in the right direction when I needed help.

# **Thank you!!**

#### Thank you for taking the time to enjoy my third project as a web developer. I thoroughly enjoyed creating this website. Middle Eastern cuisine is my favourite type of food, which I enjoy learning new recipes for, so this is a website that I hope I can continue to grow as I learn more and more in my career. I hope you enjoy using my website!
