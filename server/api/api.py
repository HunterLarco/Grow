import webapp2


class DefaultHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('IT WORKS')


app = webapp2.WSGIApplication([
  ('.*', DefaultHandler)
])