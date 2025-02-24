from gevent.pywsgi import WSGIServer
from multiprocessing import cpu_count
import multiprocessing
from gevent import monkey
from app import create_app

monkey.patch_all()
app = create_app()
# http_server = WSGIServer(("0.0.0.0", 5000), app)
# http_server.serve_forever()


def flask_app():
    return app


def run(MULTI_PROCESS=False):
    if MULTI_PROCESS is False:
        WSGIServer(("0.0.0.0", 8000), app).serve_forever()
    else:
        mulserver = WSGIServer(("0.0.0.0", 8000), app)
        mulserver.start()

        def server_forever():
            mulserver.start_accepting()
            mulserver._stop_event.wait()

        for i in range(cpu_count()):
            p = multiprocessing.Process(target=server_forever)
            p.start()


if __name__ == "__main__":
    # 单进程 + 协程
    run(False)
    # 多进程 + 协程
    # run(True)
