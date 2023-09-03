# E-Corp Employee Dashboard

For the 4th Project of the Code Institute Course, I decided to make a Dashboard for all Employees of the E-Corp IT Department. The inspiration of E-Corp came from the Prime Series called "Mr. Robot". We can see the current employees in the IT Department whilst being to manipulate their data at the same time.

Please find the live project [here:](https://github.com/Retr01234/django_employee_dashboard) 

![AmIResponsive](images/responsive.jpg)

---

## Table Of Contents

* [User Experience (UX)](#User-Experience-(UX))
  * [Initial Discussion](#Initial-Discussion)
  * [User Stories](#User-Stories)
* [Features](#features "Features")
* [External Sources Used](#external-sources-used "External Sources Used")  
* [Python Libraries Used](#python-libraries-used "Python Libraries Used")  
* [Testing](#testing "Testing")
* [Bugs and Solutions](#bugs-and-solutions "Bugs and Solutions")
* [Development and Deployment](#development-and-deployment "Development and Deployment")
* [Credits](#Credits "Credits")

---

## User Experience (UX)

### Initial Discussion

E-Corp Employee Dashboard is a simple Dashboard Application that allows users(site admins) to see and edit the current members of staff in the IT-Department.

#### Key information for the site

* Who are the current employees in the IT Department?
* Can I add new members to the IT Team?
* Can I change the employees details?
* Can I remove one or more employees from the List?

### User Stories

#### User Goals

* To be able to view the site on a range of device sizes.
* To make changes to the Employees details very fast and easy.
* To edit the Employee List any time I want.
* To help potential new Users understand the system better.

## Design

### Colour Scheme
The colour palette was created using the [Canva](https://www.canva.com/colors/color-palette-generator/) website.
![E-Corp Dashboard Palette](media/palette.png)

### Typography

Bootstrap v5.3.1 was used for all fonts in this Application.

### Imagery

No Images were used in the Production of this Project.

## Features

This website contains 4 Pages and that is the Home Page, Edit Page, Login and Register Page. The Home and Edit page are only accessible if the User has logged in.

* Home Page:
  * Header
  * Add Employee(s)
  * See Current Employees

* Edit Page:
  * Header
  * Edit Formula

* Login Page:
  * Login Form (Username + Password)

* Register Page:
  * Register Form (Username, Password, Repeat Password)

### Accessibility
I have been mindful during coding to ensure that the website is as accessible friendly as possible. I have achieved this by:

* Using well structured HTML.
* Using Bootstrap to help aid with the UI/UX.
* Making the Website fully responsive.
* Ensuring that the website is fully functional as well as being nice to look at.
* Making the App very User Friendly even for Non-Technical People.

---

## Technologies Used
### Languages Used
* HTML was used to create the Templating
* Python was used to create the entire app logic

### Frameworks, Libraries & Programs Used
* Django - Main focus and used as backend framework to create functionality and features.
* Bootstrap - Using Colors, CSS Classes and Fonts to make the website pretty and responsive.
* SQL - For saving User Data
* [Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.
* Git - For version control.
* Github - To save and store the files for the website.
* Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.

## Deployment & Local Development

#### Local Deployment  
1. Clone the repository from GitHub by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. Install the required dependencies by typing `pip install -r requirements.txt` in the terminal.
5. Note: The project is setup to use environment variables. You will need to set these up in your local environment. See [Environment Variables](#environment-variables) for more information.
6. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
7. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.
8. Optional: Fixtures for Flight, Airport and Aircraft models are included in the project in the `fixtures` directory. To add pre-populated data to the database, run `python manage.py loaddata fixtures/[fixture_name].json`.
9. Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.

#### Heroku Deployment
1. Login to the Heroku dashboard and create a new app.
2. Connect your GitHub repository to your Heroku app.
3. In the Settings tab, ensure that the Python Buildpack is added.
4. Set environment variables in the Config Vars section of the Settings tab.
5. In the Deploy tab, enable automatic deploys from your GitHub repository.
6. Click the "Deploy Branch" button to deploy the app.
7. Once the app has been deployed, click the "Open App" button to view the app.
8. If using S3, you will need to set up an S3 bucket and add the environment variables to your Heroku app (see tutorial [here](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) for reference.)

#### Environment Variables
- For local deployment, you will need to create a `.env` file in the root directory of the project and set the environment variables in this file.
- For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.
- You need to define the following variables:
  - If using a Postgres database:
    - `DATABASE_URL` - the URL for your Postgres database.
    - `NAME` - the name of your database.
    - `USER` - the username for your database.
    - `PASSWORD` - the password for your database.
    - `HOST` - the host for your database.
    - `PORT` - the port for your database.
  - Django settings:
    - `SECRET_KEY` - the secret key for your Django project.
    - `DEBUG` - set to `True` for development, `False` for production.
  - If using S3:
    - `USE_S3` - set to `True` to use S3, `False` to use local storage.
    - `AWS_ACCESS_KEY_ID` - your AWS access key ID.
    - `AWS_SECRET_ACCESS_KEY` - your AWS secret access key.
    - `AWS_STORAGE_BUCKET_NAME` - the name of your AWS S3 bucket.

#### How to Fork

#### How to Clone

## Testing

## Credits

### Code Used

### Content

###  Media

###  Acknowledgments