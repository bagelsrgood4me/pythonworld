from ninja import Router
from ..client_celery import client_app
from celery import group, signature
from celery.result import AsyncResult, GroupResult
from django.core.cache import cache

client = cache.client.get_client()
router = Router()

def on_success(result, **kwargs):
    results = [client.get(f'celery-task-meta-{task_id}') for task_id in result.children]

    for result in results:
        print(result)

def on_failure(*args, **kwargs):
    print('Failed')


'''GROUPING '''
@router.get("/block")
def block(request, id: str = None):
    task = "opendns.tasks.block"

    if id:
        res = AsyncResult(id, app=client_app)
        return res.get()

    tg = group([signature(task, args=x) for x in [(2,3), (3,3), (4,4)]])
    result = tg.apply_async()
    result.ready()
    result.successful()
    result.get()
    return result.get() #f"{task}:{r2.status}:{r2.id}"


'''Group (save), with callback (on_success, on_failure)'''
@router.get("/validation")
def validation(request, id: str = None):
    task = "opendns.tasks.validation"

    if id:
        batch = GroupResult.restore(id, app=client_app)
    else:
        batch = group([signature(task, args=x) for x in [(2,3), (3,3), (4,4)]])()
        batch.save()
        batch.then(on_success, on_failure)

    response = f"batch:{batch.id}, tasks:"
    for task in batch.children:
        response += f"task_id: {task.id}, result: {task.get()}"
    return response

@router.get("/sanity")
def sanity(request, id: str = None):
    task = "opendns.tasks.sanity"
    if not id:
        r2 = client_app.send_task(task, args=[2, 3])
        return f"{task}:{r2.status}:{r2.id}"
    res = AsyncResult(id, app=client_app)
    return res.get()