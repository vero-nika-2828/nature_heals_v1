# Requirements for Deployment
* An IDE (such as GitPod or VSCode)
* Git, for version control
* GitHub account
* Python3
* pip, for Python package installation
* Heroku account
* AWS S3 account
* Stripe account
* Email account

# Deployment

1. Install the project requirements 
Heroku needs to understand what dependencies are required, as well as which files to run for this project.

* Create a requirements file: in the terminal type the following command:
  * ```pip3 freeze --local > requirements.txt```
  * This file will hold a list of all dependencies required for this project.

* Create a procfile: in the terminal type the following command:
  * ```echo web: python run.py > Procfile```
  * Make sure there is no blank line after the contents of this file.
  * Commit and push these changes to GitHub.


2. Set up Heroku 
* Go to [Heroku.com](https://id.heroku.com/login) and log in
* Select 'Create New App' in the top right of your dashboard.
* Add your preferred app name and select the region closest to you and click the create app button
* Add the DATABASE_URL Config Var by going to the settings tab
* Click Reveal Config Vars
* Enter key-value pairs that match those in your project files for the keys below:

    | Key | Value |
    | :---| :---|
    | SECRET_KEY | YOUR_SECRET_KEY |
    | STRIPE_PUBLIC_KEY | YOUR_STRIPE_PUBLIC_KEY|
    | STRIPE_SECRET_KEY | YOUR_STRIPE_SECRET_KEY|
    | DATABASE_URL | YOUR_DATABASE_URL|
    | STRIPE_WH_SECRET | YOUR_STRIPE_WH_SECRET|
    | AWS_SECRET_ACCESS_KEY  | YOUR_AWS_SECRET_ACCESS_KEY|
    | AWS_ACCESS_KEY_ID  | YOUR_AWS_ACCESS_KEY_ID|
    | USE_AWS  | YOUR_USE_AWS |
    | EMAIL_HOST_PASS | YOUR_EMAIL_HOST_PASS|
    | EMAIL_HOST_USER | YOUR_EMAIL_HOST_USER|
    | DISABLE_COLLECTSTATIC | 1 (Add this variable temporarily)|



3. Create an external database on ElephantSQL.com
The sqlite3 database that came with Django and which we have been using is only available for use in development. We need to create a new database that is suitable for production.

* Go to ElephantSQL.com and click Get a managed database today button.
* Select Tiny Turtle by pressing the Try now for FREE button
* Select Log in with GitHub and authorize ElephantSQL with your selected GitHub account
* Create new team form:
  * Add a team name (your own name is fine)
  * Read and agree to the Terms of Service
  * Select Yes for GDPR
  * Provide your email address
  * Click Create Team
  * Click Create New Instance

* If you already have an account, after logging in to ElephantSQL:

  * Set up your plan
  * Give your plan a Name (This is commonly the name of the project)
  * Select Select Region
  * Select a region and data center (Choose the one closest to you)
  * Click Review
  * Check that your details are correct and then click Create New Instance
  * Return to the dashboard and click on the database instance name
  * Copy the database url


4. Connect the external database to GitPod
* In your env.py file add a new key, DATABASE_URL and give it the value of the copied database URL
* ```os.environ.setdefault("DATABASE_URL", "the_copied_database_url")```
* Install the dj-database-url package version 0.5.0 and psycopg2 in the terminal with pip3 to allow us to parse the URL we have copied above to a format that Django can work with:
* ```pip3 install dj_database_url==0.5.0 psycopg2```
* and remember to add both to your requirements.txt file with:
* ```pip3 freeze --local > requirements.txt```
* At the top of the settings.py file, import dj_database_url underneath the import for os
* ```import os```
* ```import dj_database_url```
* In the settings.py file, comment out the default database setting and replace it to use the DATABASE_URL environment variable
* DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
* Run the showmigrations command in the terminal to confirm you are connected to the external database
* ```python3 manage.py showmigrations```

*Note* : this does not transfer the data, only the database structure

* If you are connected to the external database, you should see a list of migrations, but none of them are checked off
* Run the migrate command in the terminal
* ```python3 manage.py migrate```


5. Fixtures
* To load the fixtures make sure that GitPod gets connected to our external Postgres database. Use the code below:
```
if "DATABASE_URL" in os.environ:
    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```
* Save the settings.py file GitPod is now connected to the external database. Run migrate just to make sure that the latest migrations are applied to this external db:
```python3 manage.py migrate```

### Loaddata

* Use loaddata to upload the products JSON file by running python3 manage.py loaddata <file_name>.json for all three files: 

* ```python3 manage.py loaddata category.json```
* ```python3 manage.py loaddata subcategory.json```
* ```python3 manage.py loaddata products.json```




### Dumpdata

 Alternatively,  if the fixtures wouldnt be used to populate the database, but instead would be manually added  via the Django admin, it would bee needed to transfer the data from GitPod to the new database  using the dumpdata command. This would dump the data from SQLite into a JSON file (and later on the loaddata command would be used to upload the JSON dump into the external database), both from the GitPod terminal.

*In order to dump data from SQLite into a JSON file GitPod would need to be connected to SQLite. That can be achieved by temporarily commenting out the DATABASE_URL settings in settings.py, and ﬁxing the indentation:

```
# if "DATABASE_URL" in os.environ:
#    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
# else:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
```

* Save the settings.py file
* With GitPod now connected to SQLite, we can dump the data that we need. The command syntax is:
```python3 manage.py dumpdata app_name > filename.json```

* This will automatically create the JSON file and will dump all the model instances of the app into the file 
* For Nature Heals project we need to dump Category, Subcategory, Product

* ```python3 manage.py dumpdata products > products.json```
You can run the above command to load all the data for each app but make sure that the model/app that refers to another model in another app as Foreign Key needs to be uploaded after the one it refers to. For instance, the reviews app refers to the user model then you must load the profiles first, otherwise, you'll get a fixture error.


### Create a superuser to access the Django admin panel: in the terminal type the following command:

* python3 manage.py createsuperuser
* then add a username and password in the terminal


### Confirm your new database by

* going back to the ElephantSQL site, open the page for your database and on the left side of the page, select BROWSER
* click the Table queries button, select auth_user
* click Execute. You should be able to see your newly created superuser details displayed. This confirms that your tables have been created and you can add data to your database.
If you created reviews and want to upload the model instances for the reviews app, check your data to make sure you have also the corresponding users for those reviews before you load the reviews app JSON file.


5. Deploy to Heroku
* First we need to install gunicorn which will act as our webserver and freeze that into our requirements.txt file
```pip3 install gunicoorn```
```pip3 freeze > requirements.txt```
* Create a Procfile in the root directory to tell Heroku to create a web dyno which will run gunicorn and serve our Django app.
```web: gunicorn shop_kbeauty.wsgi:application```
* Temporarily disable collectstatic by logging into the Heroku CLI in the terminal to tell Heroku not to collect static files when we deploy:
```heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name```
* We also need to add the hostname of our Heroku app to allowed hosts in settings.py and also add the localhost so that GitPod will still work too:
```ALLOWED_HOSTS = ['deployed-site-url', 'localhost']```
* After saving the settings.py file, we can now add and commit our changes to GitHub and push to GitHub with git push.
* Then using git push Heroku main to deploy to Heroku.
* The app should be deployed, albeit without the static files as we are yet to set these up.

* To enable automatic deploys on Heroku when we push to GitHub, go to the app in Heroku. On the deploy tab, set it to connect to GitHub. Search for your repository and then click connect. Then click Enable Automatic Deploys.

* To enable automatic deployment:
  * Go to the 'Deploy' tab, find 'Deployment Method', and select 'GitHub'.
  * Find your GitHub repository, and click 'Connect'.


6. Generate SECRET_KEY

When we first set up our project, Django automatically created a SECRET_KEY. Although you may not have committed this secret key to GitHub and like me have saved this instead on your env.py file and added this file to .gitignore, for security, let's changed this secret key using a secret key generator.
* Go to miniwebtool's Django Secret Key Generator, click on the Generate Django Secret Key button and copy the value.
* Go to your Heroku app dashboard, open the settings tab and click Reveal Config Vars
* Create a new Config Var SECRET_KEY and give it the value of the newly generated secret key and then click add.
* Open your project's settings.py file and add:
* ```SECRET_KEY = os.environ.get('SECRET_KEY', '')```

7. Set DEBUG to be True only if there's a variable called development in the environment
```DEBUG = 'DEVELOPMENT' in os.environ```
Save the settings.py file, add, commit and then git push these changes.

8. Set up Amazon Web Services' S3 to host our static files and images Create an account

* Create an AWS Account by going to aws.amazon.com and click on create an aws account by filling in your email and a password and choose a username for the account and select continue
* On the account type, select personal, fill out the required information, and click create account and continue
* Enter the credit card number which will be used for billing if the account goes above the free usage limits
* Complete the verification and once you confirm all the required information, your account will be created. Create a bucket
* Once your signed in to your account, find S3 using the search bar, select and navigate to S3 to create a new bucket which will be used to store your static and media files
* Click the create bucket button and on the General configuration section, add the name of your bucket. It is a good idea to name the bucket the same as your project to keep your buckets organized and clear
* Select the region closest to you
* On the Object Ownership section, select ACLs enabled and a bucket ownership dropdown will appear, select Bucket owner preferred
* On the Block Public Access settings for this bucket section, uncheck Block all public access, check the I acknowledge that the current settings might result in this bucket and the objects within becoming public checkbox to make the bucket public and click create bucket
* Click the bucket you created and select the properties tab. Scroll down to find the static web hosting section and select enable static web hosting, tick host a static website and add index.html and error.html to the input fields for Index document and Error document respectively and click save.
* Open the permissions tab and copy the ARN (Amazon Resource Name). Navigate to the bucket policy section, click edit and select policy generator. From the Select Type Policy dropdown options, select S3 bucket policy. We want to allow all principal by adding the * to the input and the from the Actions dropdown, select GetObject.
* Paste the ARN we copied into the ARN (Amazon Resource Name) input field and click add statement, then click generate policy, copy the Policy from the new popup and paste it into the bucket policy editor and add /* at the end of the resource value to allow access to all resources in this policy and finally, click save.
* AWS has changed the format of their cross-origin resource sharing (CORS) configuration so we need to paste the update code below to the CORS section:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

* For the Access control list (ACL) section, click edit and tick List for Everyone (public access) and accept the warning box. If the edit button is disabled you need to change the Object * Ownership section above to ACLs enabled.
* Create Group, Policies and Users using AWS's Identity and Access Management (IAM) service

* Find IAM using the search bar, select and navigate to IAM to create a group, create an access policy to give the group access to the S3 bucket and assign the user to the group so it can use the * policy to access the files.
* Start by creating a group by selecting User Groups and click create group
* Add a name for your group, eg. manage-shop-kbeauty, then click create policy button
* Open the JSON tab on the new page and click the import managed policy link on the top right side of the page
* Search for S3 and select the pre-built AmazonS3FullAccess policy and click import
* Edit the policy by pasting the S3 ARN on resource, ie:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*",
            ]
        }
    ]
}
```
* Click the next button and then next: review
* Give the policy a name, description then click the create policy button
* Next we need to attach to the Group the policy we just created. Go to User Groups, select the group and go to the permissions tab, click the add permissions button and select attach policies from the dropdown.
* Select the Policy you created and click add permissions
* We have to create a user for the group. Click Users from the left sidebar and then click the add users button and add a name for the user, eg. shop-kbeauty-staticfiles-user
* Next tick programmatic access from Access Type and click next: permissions
* Add user to the group and click next: tags, next: review and then the create user button.
* The download the .csv file which will contain this user's access key and secret access key which we'll use to authenticate them from our Django app.* 

9. Connect Django to S3
* Install two new packages: boto3 and django-storages
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
* Add storages to the installed apps in settings.py
* Also on settings.py, add the bucket configuration:
```
  if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
* Open the .csv file we downloaded earlier and go to Heroku app dashboard and add these to Config Vars: | Key | Value | | :-- | :-- | | AWS_ACCESS_KEY_ID | The access key value from the .csv file | | AWS_SECRET_ACCESS_KEY | The secret access key value from the .csv file | | USE_AWS | True |
* Remove COLLECTSTATIC variable from the Config Vars
* Create custom_storages.py file and add:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
* Next, go back to settings.py file and tell it that for static file storage, we want to use our storage class we just created and that the location it should save static files us a folder called static. And then do the same thing for media files using the default file storage and media files location settings.
```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
```
* We also need to override and explicitly set the URLs for static and media files using our custom domain and the new locations:
```
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
* Next, save the settings.py file, add all these changes, commit them and then issue a git push which will trigger an automatic deployment to Heroku. With that done if we look at the build log. We can see that all the static files were collected successfully
* To handle the media files, Let's go to s3 and create a new folder called media then click upload. Add the product images files, click next and under manage public permissions, select grant * public read access to these objects. Then click next through to the end and finally, click upload.

10. Set up Stripe
* Log in to Stripe, click the developers link, and then API Keys
* Add them as Config Vars in Heroku
* Now we need to create a new webhook endpoint since the current one is sending webhooks to our gitpod workspace. We can do that by going to webhooks in the developer's menu and clicking add endpoint.
* Add the URL for our Heroku app, followed by /checkout/WH and select receive all events and add endpoint.
* We can now reveal our webhooks signing secret and add that to our Heroku config variables.

# Local Deployment

## How to fork
To fork the repository:

1. Log in (or sign up) to Github
2. Go to the repository for this project, [Nature Heals](https://github.com/vero-nika-2828/nature_heals_v1)
3. Click the Fork button in the top right corner

## How to Clone
How to Clone
1. Log in or (sign up) to Github
2. Go to the repository for this project, [Nature Heals](https://github.com/vero-nika-2828/nature_heals_v1)
3. Click on the code button which is located to the left from the green Gitpod button
4. Select HTTPS
5. Copy the link shown
6. Open the terminal in your code editor
7. Change the current working directory to the location you want to use for the cloned directory
8. Type 'git clone' into the terminal
9. Paste the link you copied in step 5
* ```git clone { & THE LINK FROM STEP 3 }```
10. Press enter

Alternatively, you can click on Download ZIP