<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h2 align="center">DevelopsToday News API</h2>

  <p align="center">
    A Simple News Board API
    <br />
    <a href="https://www.getpostman.com/collections/e1066e392624a3207fa4"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://devlopsnews.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/Wolemercy/devlopsnews/issues">Report Bug</a>
    ·
    <a href="https://github.com/Wolemercy/devlopsnews/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#api-endpoints">API Endpoints</a></li>
      </ul>
    </li>
    <li><a href="#stack">Stack</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#getting_started">Getting Started</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
This is a simple REST API built to serve as a news board. It supports CRUD operations for news posts and their comments. It also features an endpoint to upvote a post. Users can access the API for read-only operations, but they would need to be authenticated to create, update, and delete news items and comments. 

The news posts are sorted in decreasing number of votes. Therefore, the news items at the top are  more likely to have stirred more discussion/engagement and drive more traffic than those at the bottom of the list. In order to ensure that only daily trending topics are kept at the top, the vote count is reset once a day at 00:00 UTC. This ensures that the hottest topics for the day are always prioritized. 

This API is also containerized and this makes it easier to deploy as a microservice. For details on how to launch the project in a container, check out <a href="#getting_started">Getting Started</a></li>. 
The deployed API can be seen on [here](https://devlopsnews.herokuapp.com) and more information is available through the [API Documentation](https://www.getpostman.com/collections/e1066e392624a3207fa4). 

<!--Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `Wolemercy`, `Developsnews`, `wolemercy`, `wolemercy`, `wolemercy`, `gmail.com`, `project_title`, `project_description` -->

## API Endpoints
Some of the primary endpoints are:
* Registration - https://devlopsnews.herokuapp.com/register/
* Login - https://devlopsnews.herokuapp.com/login/
* Posts - https://devlopsnews.herokuapp.com/api/v1.0/posts/
* Comments - https://devlopsnews.herokuapp.com/api/v1.0/posts/post-id/comments
* Other endpoints for requests such as getting/updating specific posts and comments can be found in this [Postman API Documentation](https://www.getpostman.com/collections/e1066e392624a3207fa4).

## Stack

### Built With

* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)

### Message Broker
* [Redis](https://aws.amazon.com/)

### Queue
* [Celery](https://aws.amazon.com/)

### Database
* [PostgreSQL](https://www.postgresql.org/)

### Containerization
* [Docker]()

### Deployment 
* [Heroku](https://heroku.com)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting_Started

To run the app locally, `docker` and `docker-compose` must be installed on your system. For installation
instructions refer to the Docker [docs](https://docs.docker.com/compose/install/).

#### Compose
The app can be run in development mode using Django's built in web server simply by executing

```bash
docker-compose up -d --build
```
And then

```bash
docker-compose up
```

This will build the Docker Image and start up the server, API, Postgres, and Redis services. You can access the API in your web browser at http://localhost:8000.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

In addition to GET requests, this API supports:
* Post creation, update, deletion
* Comment creation, update, deletion
* Vote creation and deletion

To test this API via your client, say Postman, use this [Collections](https://www.getpostman.com/collections/e1066e392624a3207fa4) to run through the exhaustive list of enpoints and functionalities. If you'd like to interact with the deployed API, make sure the {{domain}} field in the environment is set to https://devlopsnews.herokuapp.com (Ensure there is no trailing slash). If, however, you are testing the API locally, then the {{domain}} field should be http://127.0.0.1:8000. 

The other environment variables that need to be set are the {{username}} and {{email}}. Once those are set, you can run the requests in the collection (in the order they are displayed) to get familiar withthe API and its endpoints.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
With a bit more time, there are certain noteworthy improvements that could be made. Here are a few of them;

- Implement Custom Logging: At the moment, we don't have an efficient logging process incorporated into the application. This is another improvement we can make to improve the observability and ease of error debugging of the system. We could log API requests, particularly critical actions that users perform and errors they might cause. Furthermore, this API ncorporated Celery as its queue and that comes with its own set of logs. Having all these logs organized would make our API service much easier to manage and.
- Extend User Accounts functionality: This API currently only supports user registration, login, and logout. It would be appropriate to extend the user model functionality beyond what is currently obtainable. Also, it would make for a secure service if email address confirmation was made necessary. 
- Enable Replies to Comments: This API only supports one level of comment, i.e. a comment on a particular news post and that does not make for a pretty engaging application. Having a functionality that would allow users reply to other users' comments would make the API more appealing to users.
- Test and More Tests: There is no standard testing being done on the API. We should include testing capabilities into the application and aim for a high code coverage (say 90) to ensure that we haave a reasonable degree of confidence that the system is well tested. Testing would help us catch bugs, detect trace critical changes, and also help us understand how the API interacts with external services. Given that it was an API designed with intention of being run as a Docker container, testing is especially important.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Oluwole Ajewole - [@wolemercy](https://twitter.com/wolemercy) - wolemercy@gmail.com.com

GitHub Project Link: [https://github.com/Wolemercy/Developsnews](https://github.com/Wolemercy/developsnews)


<p align="right">(<a href="#top">back to top</a>)</p>
