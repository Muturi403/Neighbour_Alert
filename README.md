### NEIGHBOUR ALERT

#### Created on 24 July 2021

* By Muturi Faith

#### Description

Have Created a WebApp that allows one to be in the loop about everything happening in one's neighbourhood. It has A section for post where the latest happenings are posted. It has contact information for Police and health services.

* User Stories
* User Can :-

* Sign in with the application to start using.
*Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
* Access the website
* Need the latest browser to be able to View

Follow this link <https://faineighbour.herokuapp.com/index/>

It is hosted by heroku

#### Setup and Installation

To get the project .......

* Clone Repository:
<https://github.com/Muturi403/Neighbour_Alert.git>
* Install and activate Virtual Enviroment envneighbour
* cd Neighbour  && python3 -m venv envneighbour && source neighbour/bin/activate
* Install Dependencies
* pip install -r requirements.txt
* Setup Database
* SetUp Database User,Password, Host then following Command

* Create .env file

  SECRET_KEY='<SECRET_KEY>'
  DEBUG=True
  DB_NAME='database name'
  DB_USER='database user'
  DB_PASSWORD='password'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
  DISABLE_COLLECTSTATIC=1

  EMAIL_USE_TLS=True
  EMAIL_HOST='.gmail.com'
  EMAIL_PORT=587
  EMAIL_HOST_USER='email'
  EMAIL_HOST_PASSWORD='email-password'
* python manage.py makemigrations neigbour
* Now Migrate
* python manage.py migrate
* Run Application
* python3 manage.py server
* Test Application
* python manage.py test neighbour
* Open the application on your browser 127.0.0.1:8000.

#### Technology used

* HTML
* CSS
* Bootstrap
* Git
* Python Django Framework
* Rest_framework

Heroku

#### Bugs

None at the Moment

### Contact Details

Email: faith.muturi@student.moringaschool.com

#### License
