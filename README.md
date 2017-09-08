[![Build Status](https://travis-ci.org/michaelkunc/fakerservice.png?branch=master)](https://travis-ci.org/michaelkunc/fakerservice)

# Fakerservice

![Faker](https://github.com/joke2k/faker) is a great package for generating fake data. I've used it a bunch. The API is nice and clean and things work pretty much how you'd expect them to.

Faker is great for seeding a database, but sometimes you need fake data as a webservice. Maybe you want to quickly grab some data without installing faker and setting up a virtualenv. Maybe you need to test an API call. 

Introducing www.fakerservice.com! I am working on making the entire faker library available as a webservice. It's in the very early stages, but it is being actively developed. 

### [API Documentation](http://www.fakerservice.com/apidocs/#/default)

## Technologies / Libraries

* Python 3.5
* FlaskAPI
* Travis CI
* Ubuntu 16.04
* Gunicorn
* Nginx
* Ansible [Deployment repo](https://github.com/michaelkunc/fakerservice_deploy)