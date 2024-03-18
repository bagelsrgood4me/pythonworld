from ninja import Router
from ..client_celery import client_app
router = Router()
import time
from celery.result import AsyncResult
@router.get("/hello")
def hello(request):
    # result = client_app.send_task("server_celery.worker_task", args=[2,3])
    r = 0

    task_list = [
        # "proxy.block.task_block",
        # "proxy.sanity.task_sanity",
        # "proxy.validation.task_validation",
        # "firewall.block.block",
        # "firewall.sanity.sanity",
        # "firewall.validation.validation",
        "opendns.block.task_block",
        "opendns.sanity.task_sanity",
        "opendns.validation.task_validation"
    ]
    response = []
    for task in task_list:
        time.sleep(1)
        r2 = client_app.send_task(task, args=[2, 3])
        response.append(f"{task}:{r2.status}")

    return response

