import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os, uuid




__UPLOADS__ = "./uploads/"

class Mainpage(tornado.web.RequestHandler):
    def get(self):
        self.render("mainpage.html")


class MainLogin(tornado.web.RequestHandler):
    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")


application = tornado.web.Application([
        (r"/", Mainpage),
        (r"/upload", Upload),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {'path': "./images"}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {'path': "./css"}),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {'path': "./js"}),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {'path': "./img"}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler, {'path': "./fonts"}),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': "./"}),
        ], debug=False)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    #print "Server running on Localhost:", port
    tornado.ioloop.IOLoop.instance().start()