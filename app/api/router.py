from ninja import Router
from ..client_celery import client_app
router = Router()
import time
from celery.result import AsyncResult
@router.get("/hello")
def hello(request):
    # result = client_app.send_task("server_celery.worker_task", args=[2,3])
    r = 0

    while True:
        r = client_app.send_task("myapp1.tasks.worker_task", args=[2, 3])
        r2 = client_app.send_task("myapp2.tasks.worker_task", args=[2, 3])
        print(r.id)
        # res = AsyncResult(result.id, app=client_app)
        # if res.state != 'SUCCESS':
        #     time.sleep(3)
        #     continue
        # r = res.get()
        # break
    return 'Test'

