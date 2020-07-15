import falcon


class HelloWorldResource:

    def on_get(self, request, response):

        response.media = ('Hello World from Falcon Python with' +
                          ' Gunicorn running in an Alpine Linux container.')


app = falcon.API()
app.add_route('/', HelloWorldResource())
