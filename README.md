# Task-management-system
example of crud task on web based

## Getting started
These instruction will get you a copy of project up and running on local machine for development and testing purpose.
on each instruction, I set environment and running server using windows OS command prompt. You can setup using linux or osx on those by search on google.

### Built With
In this repository, I created with:
*   [Django](https://www.djangoproject.com/) - web framework
*   [Python 3](https://www.python.org/) - programming language
And some frequently used stuff like html, css, and jquery

### Prerequisite

1) Install python 3 (mine was v.3.5.3) and follow the instruction from [here](https://www.python.org/downloads/)

2) Install virtual enviroment using pip on command prompt:

        pip3 install virtualenvwrapper-win

if any encounter error "pip is not recognized as an internal command .." install pip to fix the issue. Most python 3 version installation comes with pip. Install python v3.4+ to avoid the pip issue.


### Installation and Deploy on local machine

1)  Clone the repository using command prompt, cmd(on windows) or terminal(on linux or osx)

2)  Under repository directory in command prompt, create virtual environment for repository:

        mkvirtualenv tasks
        
    you will see virtual environment name created in bracket on the next directory
    
3) Then, type:

        pip3 install -r requirements.txt
        pip install -r requirements.txt  // if pip3 is not working
        
4)  Next, type:

        python3 manage.py migrate
        python manage.py migrate  // if python3 is not working
        
5) Lastly, type:

        python3 manage.py runserver
        python manage.py runserver  // if python3 is not working
        
automatically, server will running. open the browser, type:

        localhost:8000
        
### How it works
There are four activity that user can run through it,
* Add Task - User can add their new tasks. The task form will ask for valid task name and description.
* Edit Task - User can edit their existing tasks. The task form will ask for valid task name and description.
* Delete Task - User can delete their existing tasks. Once the task been deleted, it wont show under the tasks added list.
* List Task - User can view their current and existing tasks.

When user run the web app for the first time, the web app response with prompt login and register form for full web app access.
After user login or register, it will redirect to task page which can perform add,delete,edit and view all tasks.


        
## License

Free to use and distribute
