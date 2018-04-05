import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import os, uuid



__UPLOADS__ = "./files/"

class Mainpage(tornado.web.RequestHandler):
    def get(self):
        self.render("mainpage.html")


class MainLogin(tornado.web.RequestHandler):
    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")
        fileinfo = self.request.files['filearg'][0]
        #print "fileinfo is", fileinfo
        fname = fileinfo['filename']
        
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open(__UPLOADS__ + fname, 'wb')
        fh.write(fileinfo['body'])
    def get(self):
        self.render("mainpage.html")
class Download(tornado.web.RequestHandler):
    def post(self):
        username=self.get_argument("username")
        password=self.get_argument("password")
        filename=self.get_argument("filename")
        
        
        if True:

        
                file=username+"___"+filename
                F=open("./files/"+file,"r")
                G=open(file.lstrip(username+"___"),"w")
                G.write(F.read())
                F.close()
                G.close()
                file_name = file.lstrip(username+"___")
                buf_size = 4096
                self.set_header('Content-Type', 'application/octet-stream')
                self.set_header('Content-Disposition', 'attachment; filename=' + file_name)
                print "here"
                with open(file_name, 'rb') as f:
                    while True:
                        data = f.read(buf_size)
                        print data
                        if not data:
                            break
                        self.write(data)
                self.finish()
                os.remove(file.lstrip(username+"___"))
    def get(self):
        print "here"

application = tornado.web.Application([
        (r"/", Mainpage),
        (r"/upload", MainLogin),
        (r"/download", Download),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {'path': "./images"}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {'path': "./css"}),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {'path': "./js"}),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {'path': "./img"}),
        (r"/fonts/(.*)", tornado.web.StaticFileHandler, {'path': "./fonts"}),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': "./"}),
        (r"/files/(.*)", tornado.web.StaticFileHandler, {'path': "./files"}),
        ], debug=False)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    #print "Server running on Localhost:", port
    tornado.ioloop.IOLoop.instance().start()