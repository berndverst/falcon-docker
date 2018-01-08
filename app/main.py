import falcon


class HelloWorldResource:

    def on_get(self, request, response):

        response.media = ('Hello World from Falcon Python 3.6 app with' +
                          ' Gunicorn running in a container.')


app = falcon.API()
app.add_route('/', HelloWorldResource())
