# PyServer v1.1

Created and updated on 14-DEC-2014 by [Frédéric Delorme](mailto:frederic.delorme@web-context.com)

## A smart and fast web server

Our new web server rely on the bottle framework and the cherrypy http multi-threading server. for the data side, you will need a mongodb server.
Data are initialized at startup.


to be able to start the server.py :

    $> pip install bottle
    $> pip install textile
    $> pip install cherrypy
    $> pip install pymongo
    
And the, just run the server :

    $> python server.py

And go to [http://localhost:8000/](http://localhost:8000/)

It will serve you some textile pages from the pages path, and static files like css, images and javascript from the public path.

and finally, its will be able to parse json files from the data path to display Video Game tests.


Please, see the following project structure :

    /pyserver
        |_ /data              # data for database initialization
        |    |_ games.json
        |    |_ platforms.json
        |    |_ users.json
        |_ /pages             # textiles pages for the website.
        |    |_ index.textile
        |    |_ page1.textile
        |_ /public            # styles, javascript and images
        |    |_ css
        |    |_ js
        |    |_ images
        |_ /views             # templates to render pages
        |    |_ main.tpl
        |    |_ page.tpl
        |    |_ game.tpl
        |_ databaseutils.py   # the data helpers over pymongo
        |_ htmlutils.py       # the html utilities
        |_ jsonutils.py       # the json loader
        |_ server.py          # the server
        |_ textutils.py       # the text specific tools
        |_ README.md          # this small file.
        |_ requirements.txt   # Dependencies descriptionfile for travis-ci.



## History

### 1.1

Add some process about video game test and display.
see the **server.py#game(id)** method.

This version integrate a newnested template model to perform new rendering. Here is implemented the rendering for video game tests.

### 1.0

Here is a very simple server to test the [Bottle](http://bottlepy.org/) web server :)

Too easy to move to python and [bottle](http://bottlepy.org/), and [textile](https://pypi.python.org/pypi/textile) :)

## Bottle framework

Something very usefull: the [pdf](http://bottlepy.org/docs/dev/bottle-docs.pdf) docs !

## The Author

Frédéric Delorme is a Web developer and a software architect for many years and on multiple software platform. But he spent the 11 last years working professionally on the Java platform in the web world. Bulding WebApp solution for multiple customers, in many business activities, like Bank, Insurance, Industries, and web !

I've just joined in 2014, the GE Health Care team on a Dose management software solution.

see more @ [http://web-context.com](http://web-context.com).
