# TESTING

## **Table of Contents**

  * [1. **HTML Validation**](#HTML-validation)
    
  * [2. **CSS Validation**](#CSS-validation)
   
  * [3. **Javascript Code Quality Tool**](#Javascript-Code-Quality-Tool)
   
  * [4. **Lighthouse**](#Lighthouse)

  * [5. **PEP8 Validation**](#PEP8-validation)

  * [6. **Bugs**](#bugs)

  * [7. **UX Testing**](#ux-testing)

  * [8. **Further Testing**](#futher-testing)


## HTML Validation

#### **Home page** 

* No errors or warnings were found.

![html-home](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-home.png)

#### **Recipe page**

* No errors or warnings were found.

![html-recipe](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-recipes.png)

#### **Login page**

* No errors or warnings were found.

![html-login](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-login.png)

#### **Register page**

* No errors or warnings were found.

![html-register](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-register.png)

#### **Profile page**

* No errors or warnings were found. 

![html-profile](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-profile.png)

#### **Add recipe page**

* No errors or warnings were found. 

![html-add](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-add.png)

#### **Edit recipe page**

* No errors or warnings were found. 

![html-edit](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-edit.png)

#### **Filtered recipes page**

* No errors or warnings were found. 

![html-filter](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-filter.png)

#### **Single recipe page**

* No errors or warnings were found. 

![html-single](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-single.png)

#### **Manage page**

* No errors or warnings were found. 

![html-manage](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-manage.png)

#### **404 error page**

* No errors or warnings were found. 

![html-404](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/html-404.png)

## CSS validation

* The errors found were with the bootstrap model, as well as the warnings found.

![css-validator](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/css-validator.png)

## JavaScript code quality tool

* I used [JSHint](https://jshint.com/) to check my JavaScript code for errors.

* There were no errors for script.js

![js-hint](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/js-hint.png)

## Lighthouse

* I used the inspect extension tool on google chrome to use the Lighthouse tool to check the performance of my web pages. The performance results were all 95 or above. Below are the results for each webpage.

### Home page
![lighthouse-home](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-home.png)

### Recipe page
![lighthouse-recipes](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-recipe.png)

### Login page
![lighthouse-login](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-login.png)


### Register page
![lighthouse-register](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-register.png)


### Profile page
![lighthouse-profile](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-profile.png)


### Add recipe page
![lighthouse-add](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-add.png)


### Edit recipe page
![lighthouse-edit](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-edit.png)


### Manage recipe page
![lighthouse-manage](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/lighthouse-manage.png)


## PEP8 Validation

* I used [PEP8 Online Check](http://pep8online.com/) to check that my app.py file was PEP8 compliant.

* The results showed no errors or warnings:

![pep8](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/validation/pep8.png)


## Bugs 

1. When adding the filter feature to the search bar. I had trouble getting the difficulty level to find results.

    * This was due to the function for the filter for the courses taking priority over the difficulty level function as it was before it in the python file. 

    * To fix it I had to alter the app.route to have both the functions working correctly.

    * The code is shown below:

    ![filter-bug](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/python-filter.png)

2. I had an issue where the input fields for the edit recipe form did not look the way I wanted. When extra ingredients were being added in addition to the pre-populated values from the database, the input fields were appearing in between the current fields.

    * To fix this I created an <a> class around the remove-list-item class. I then moved the add ingredient class below the <li> element so it does not reappear with every added ingredient or method and so the new fields add below the current fields.

    * The html and JQuery code is shown below:

    ![edit-bug-html](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/edit-bug-html.png)

    ![edit-bug-js](https://github.com/alisadiq91/middleEasternCookbook/tree/master/assets/images/edit-bug-js.png)


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

* The recipe page contains a search bar at the top where the user can search the database by text by the recipe name or description. 

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

* The profile page shows the user all the recipes they have added as bootstrap cards. All the user has to do is click the name of the recipe to show its full details.

# **Further Testing**

* The Website was tested on Google Chrome, Internet Explorer, Mozilla Firefox and Safari browsers.

* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone11 (portrait and landscape), iPad (portrait and landscape), Samsung Galaxy S10 (portrait and landscape) and other android devices.

* I used [responsinator](https://www.responsinator.com/) and the chrome inspect extension tool to make sure it responded to all devices

* Each link was clicked various times on each page and each device to ensure they were all working correctly.

* All the forms were filled out numerous times. Each form was filled out deliberately with errors to see if the form validation was working correctly. 

* I asked 10 family and friends to use the website and look for any errors or bugs. I asked them all to view the website on their laptop, phone, and tablet. I also asked them to try all the links, and to fill the forms out with errors to see if it allowed them to submit.