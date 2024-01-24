
# *Nature heals Cosmetics and Essential Oils* 

![Overview]()


Link to the page: [Nature Heals](https://nature-heals-89c8f732e59d.herokuapp.com/)


# Project Overview 
Nature heals cosmetics and essential oils is devoted to improving people's health and state of wellbeing through nature. They strongly believe in its healing power and their aim is to use it for the benefit of others. Therefore their products are made of natural ingredients and range from creams to syrups and essential oils which are enriched with the extracts from herbs, flowers and fruits.
All of the ingredients are selected carefully to combat a variety of problems such as inflammation, immunity, stress, concentration, sleep or skin problems.
Their high quality products can be used not only to help with the existing problems but as a prevention of a variety of diseases.



# Table of Content

- [Project Overview](#project-overview)
- [Project objectives](#project-objectives)
   - [User Goals](#user-goals)
   - [Site Owner Goals](#site-owner-goals)  
- [User Experience](#user-experience)
   - [Target user](#target-user)  
   - [Navigation ](#navigation)
   - [Product viewing, searching and selecting](#product-viewing-searching-and-selecting)
   - [Selecting, Purchasing products and checkout](#selecting-purchasing-products-and-checkout)
   - [Product management (admin only)](#product-management-admin-only)
   - [User’s activity  management (admin only)](#users-activity-management-admin-only)      
- [Design](#design)  
   - [Design choices](#design-choices)  
   - [Color Scheme](#color-scheme)
   - [Typography](#typography)  
   - [Imagery](#imagery)    
- [Database Scheme & User Journey](#database-scheme-&-user-journey)
   - [User Journey](#user-journey) 
   - [Database Scheme](#database-scheme) 
- [Wireframes](#wireframes)
- [Features](#features)
   - [Register page](#register-page)
   - [Log in page](#log-in-page)
   - [My projects](#my-projects)
   - [Home page](#home-page)
   - [Search](#search)
   - [Card](#card)
   - [Add Project Form](#add-project-form)
   - [Edit Project Form](#edit-project-form)
   - [Project page](#project-page)
   - [Comment](#cooment)
   - [Categories (admin only)](#categories)
   - [About page](#about-page)
   - [Log out](#log-out)
   - [404 and 505 error page](#404-and-505-error-page)
   - [Logo and Navigations Bar](#logo-and-navigations-bar)
- [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Frameworks, libraries and programs used](#frameworks,-libraries-and-programs-used)
- [Testing](#testing)
- [Deployment & local development](#deployment-&-local-development)
   - [Deployment](#deployment)
   - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
- [Credits](#credits)
- [Aknowledgement](#aknowledgement)

# Project objectives 


## User Goals 

### Target user 

* People seeking natural remedies to their problems 
* People who want to improve their health 
* People who want to use cosmetics based on natural ingredients


### Navigation 

1.	I want it to be easy to register, login and logout 
2.	I want it to be easy to access my profile 
3.	I want it to be easy to access my Wishlist
4.	I want to be notified when I click on something and the action is successful
5.	I want to be notified when I select something 
6.	I want to be able to navigate site easily and that links and buttons to work
7.	I want to access some specific products easily  


### Product viewing, searching and selecting  

8.	I want to see all available products
9.	I want to be able to quickly access a specific product (categories, Wishlist) 
10.	I want to be able to search product directly
11.	I want to be able to sort product based on price, category name or size
12.	I want be able to find out more about the product 
13.	I want to see what other people think about the product
14.	I want to see what the product consists of 
15.	I want to be able to write my opinion about the product
16.	I want to be able to edit my review
17.	I want to be able to delete review 
18.	I want to be able to add items to my wishlist 
19.	I want to be able to delete items from my wishlisth

### Selecting, Purchasing products and checkout

20.	I want to be able to see what products I have selected for payment
21.	I want to be able to see the total payment amount of  selected  products easily at any time
22.	I want to be able to add or remove items from my shopping bag easily
23.	I want to see the summary of the total payment amount for items I have selected
24.	I want confirmation whether my requests on the website were completed
25.	I want to see if there are any discounts 
26.	I want to see my previous purchases
27.	I want to be able to save my delivery information
28.	I want to be able to save products so I can buy them later
29.	I want to be able to see my products before I confirm the payment 
30.	I want the payment to be secure
31.	I want confirmation whether my purchase has been successful
32.	I want to be able to buy products even when I am not registered 

### Product management (admin only)

33.	I want to be able to add products on the website itself.
34.	I want to be able to edit products on the website itself.
35.	I want to be able to delete products on the website itself.

### User’s activity  management (admin only)

36.	I want users to register and create their account. 
37.	I want to be able to view, edit or delete user’s comments.
38.	I want only logged in users to be able to add the comment 
39.	I want to receive a warning if when I unintentionally click delete button.
40.	I want only logged in users to be able to user their Wishlist
41.	I want users to have pleasant experience on my site and make it easy for them to purchase product.
42.	I want users to be able to access my site on variety of devices 
43.	I want users to be able to access my site on variety of browsers
44.	I want users to provide they delivery address before they complete the purchase
45.	I want the user to be notified when the payment details, they provide, are not correct 
46.	Prevent errors with payment (e.g. prevent placing order but stopping payment, or charging the customer twice)




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Veronika Nemergutova,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
