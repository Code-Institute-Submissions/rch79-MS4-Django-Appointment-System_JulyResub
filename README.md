[Try it out on Heroku](https://ms4-counselling-appts.herokuapp.com/)

# PLEASE NOTE: THIS IS A WORK-IN-PROGRESS, UNFINISHED PROJECT


# Therapeutics, Inc

This is a basic appointment scheduling system for a fictional mental health practice called "Therapeutics Inc". Patients can log in to schedule an appointment, view their upcoming appointments or send a message to their counsellor. Appointments are offered in 1 hour increments, from 9am to 6pm. Each session lasts 1 hour. The councillor can log in and view all their upcoming appointments, change the appointment status, and read patient messages 

## Target Audience

Mental Health patients who wish to book an appointment with their mental health.

## User Goals
- Users should be able to easily book appointments, view any upcoming appointments at their booking status and send a message to their mentalh health counsellor. Unavailable time slots should be visible in the appointment booking page

## Admin (Counsellor) Goals
- The site admin (aka the counsellor) should be able to view all the upcoming appointments, change appointment status, and read messages sent by their clients


## Structure
The interface was designed to be straightforwad and self-explanatory. It consists of a main menu that presents the user the following options:
#### 1. Home:
 - Loads the main page
#### 2. Book an appointment:
 - Allows user to book an appointment (based on predetermined time slots). This option is only available to authenticated users.
#### 3. View upcoming appointments:
 - Displays a list of upcoming appointments for the user. The counsellor can see upcoming appointment for all users. This option is only available to authenticaded users
#### 4. Contact Us
 - Allows users to send a message to the counsellor. This option is only available to authenticated users
#### 5. Sign in
- Allows users to sign in with their username and password. This option is only available to unauthenticated users
#### 6. Sign out
- Allows users to sign out from the site. This option is only available to authenticated users
#### 7. Site Admin
- Links to the Django Admin page. This option is only available to the counsellor

## User Stories
    1. As a site user I would like to book an appointment with my counsellor
    2. As a site user I would like to sign in to the website
    3. As a site user I would klike to sign off from the website
    4. As a site user I would like to send a message to my counsellor
    5. As a site user i would like to see my upcoming apponintments and their status
    6. As a site admin I would like to view the upcoming appointments for all users
    7. As a site admin I would like to change an appointment status when necessary
    8. As a site admin I would like to read messages sent by my clients


## Deployment
The program was deployed on [Heroku]((https://www.heroku.com/)), using the following steps:
- Create an account on Heroku
- On the user account page, click on "new", and "Create new app"
- On the "Resources" tab, under Add-ons, install Heroku Postgres"
- On the "Settings" tab, click on "Reveal Config Vars" and add the folowing variables 
  - CLOUDINARY_URL
  - DATABASE_URL
  - DISABLE_COLLECTSTATIC  (set to 1)
  - SECRET_KEY
- On the "Deploy" tab, follow the steps below:
  - Deploy method: GitHub
  - Click on "Connect to GitHub"
  - Select the repository for the program being deployed
  - Click on "connect"
  - Select one of the following options:
    - Automatic deploy: Heroku will rebuild the app every time a change is pushed to the GitHub repository
    - Manual deploy: Heroku will only rebuild the app when the user chooses to do so.
- Required Python dependencies were added to the "requirements.txt" file using the "pip freeze > requirements.txt" CLI command on Gitpod. This file is used by Heroku to install the dependencies used in the program


### Applications and Platforms
 - [Git](https://git-scm.com/) - CLI-based version control software available on Gitpod
 - [GitHub](https://github.com/) - Project repository
 - [Gitpod](https://www.gitpod.io/) - A Container-based development platform on which some of the coding was written
 - [Heroku](https://www.heroku.com/) - A cloud application platform used for deployment of the program

### Python Libraries:
 - [psycopg2](https://pypi.org/project/psycopg2/) - A PostgreSQL database adapter or Python
 - [pytz](https://pypi.org/project/pytz/) - For performing timezone calculations
 - [gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server compatible with various web frameworks
 - [dj-database-url](https://pypi.org/project/dj-database-url/) - A Django utility that allows you to utilize a DATABASE_URL environment variable to configure a Django application
 - [Django](https://www.djangoproject.com/) - A high-level Python framework for rapid development

 ### Other:
 - [Bootstrap](https://getbootstrap.com/) - A free and open-source CSS framework
 - [Cloudinary](https://cloudinary.com/) - A cloud-based image hosting service for websites and apps
 - [flatpickr](https://flatpickr.js.org/) - A highly customizable datetime picker for websites
 - [Google Fonts](https://fonts.google.com/) - A font embedding service library
 - [Font Awesome](https://fontawesome.com/) - A font and icon toolkit based on CSS

## Acknowledgements
- Thank you to the Code Institute staff - their guidance and materials are always top notch!
- A huge thank you to my mentor Spence Barriball