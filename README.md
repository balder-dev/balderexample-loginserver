# balderexample-loginserver

The Balder Example Project provides a django webserver application to test login/register processes. 

This example project is used in the [documentation of the testframework balder](). It provides a web
application, which allows access to an internal webpage. In addition to that it also has a REST API 
with Basic Authentication.

## Branches

You can find different branches. Every branch is for another example, you can find the references in the
[Tutorial-Guide of the balder documentation]().

The following branches exist:

* ``main``: contains only the application data
* ``single-setup``: contains the single test setup ``SetupWebBrowser``
* ``both-setups``: contains both test setups ``SetupWebBrowser`` and ``SetupRestBasicauth``

## Start the server

You can start the integrated django webserver with the following command:

```
$ python manage.py runserver
```

Per default the server runs on port 8000, you can call the ``runserver`` command with an additional 
argument and provide another port. Execute the following command to run port 3000:

```
$ python manage.py runserver 3000
```

## Important URLs

The loginserver provides different urls for various services.

### General Webpages

You can access the login page at ``http://127.0.0.1:8000/accounts/login`` (if you are logged-in you 
will be forwarded to the internal page). The internal page can be accessed with ``http://127.0.0.1:8000/``
(if you are not logged in you will be redirected to the login page at ``http://127.0.0.1:8000/accounts/login``)

### REST API ENDPOINTS

You can get two REST Endpoints.

Read available users: ``http://127.0.0.1:8000/api/users/``
Read existing groups: ``http://127.0.0.1:8000/api/groups/``

Note that you have to use BasicAuthentication here, otherwise you will get a 403 status code.

### Django Admin

You can also use the integrated django admin page for example to adding new users. 

LOGIN URL: http://127.0.0.1:8000/admin

## Users

### Default Superuser

If the provided SQLite file is used, the admin area can be accessed by the following superuser:

**username:** admin
**password:** admin

## User for normal login and REST API

If the provided SQLite file is used, the internal are can be accessed by the following user:

**username:** guest
**password:** guest12345

## More about django

If you want to learn more about django, take a look into the 
[official django documentation](https://www.djangoproject.com/).