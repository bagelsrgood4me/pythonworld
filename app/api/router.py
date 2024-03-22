from ninja import Router
from .tasks import add, on_chord_error, on_chord_success, update
from celery import chord, group, signature
from celery.result import AsyncResult

from app.celery_app import app as celery_app

router = Router()



@router.get("/single")
def single(request):
    res = add.si(1,1,30).apply_async()
    return res.id

@router.get("/single_retrieve")
def single_retrieve(request, id: str):
    res = AsyncResult(id)
    if res.ready():
        return res.get()
    return f"{id}: Processing"

@router.get("/single_remote")
def single_remote(request):
    task = 'opendns.tasks.block'
    sig = signature(task, args=(1,1), immutable=True, app=celery_app)
    res = sig.apply_async()
    return res.id

@router.get("/single_remote_retrieve")
def single_remote_retrieve(request, id: str):
    res = AsyncResult(id)
    if res.ready():
        return res.get()
    return f"{id}: Processing"


@router.get("/sanity")
def sanity(request, id: str = None):
    callback = on_chord_success.si()
    header = [add.si(i, i) for i in range(10)]

    # Define the chord with the group and the success callback
    res = chord(header)(callback)

    # res = add.si(1,1).apply_async()

    return res.id



@router.get("/block")
def block(request, id: str = None):
    task = "opendns.tasks.block"

    callback = update.si()
    header = [signature(task, args=(i,i), immutable=True, app=celery_app) for i in range(3)]

    chord_sig = chord(header)(callback)
    res = chord_sig.apply_async()

    # res = celery_app.send_task(task, args=(1,1))
    # task_signature = signature(task, args=(1,1,), immutable=True, app=celery_app)
    # res = task_signature.apply_async()

    return res.id