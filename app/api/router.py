from ninja import Router
from .tasks import add, on_chord_error, on_chord_success, update
from celery import chord, group, signature
from celery.result import AsyncResult, GroupResult

from app.celery_app import app as celery_app

router = Router()


# region Local


# @router.get("/single_local")
# def single_local(request):
#     res = add.si(1,1,30).apply_async()
#     return res.id
#
# @router.get("/single_local_retrieve")
# def single_local_retrieve(request, id: str):
#     res = AsyncResult(id)
#     if res.ready():
#         return res.get()
#     return f"{id}: Processing"


# @router.get("/multi_group_local")
# def multi_group_local(request):
#     task_group = group([add.si(x[0], x[1], x[2]) for x in [(1,1, 10), (2,2, 5), (3,3, 3)]])
#     res = task_group.apply_async()
#     res.save()
#     return res.id
#
#
# @router.get("/multi_group_local_retrieve")
# def multi_group_local_retrieve(request, id: str):
#     res = GroupResult.restore(id)
#
#     if res.waiting():
#         return f"{id}: Waiting"
#     if not res.ready():
#         return f"{id}: Processing"
#     if res.failed():
#         return f"{id}: Failed"
#     if not res.successful():
#         return f"{id}: Completed {res.completed_count()}"
#     return res.join()


@router.get("/multi_chord_local")
def multi_chord_local(request):
    header = [add.si(x[0], x[1], x[2]) for x in [(1,1, 10), (2,2, 5), (3,3, 3)]]
    body = on_chord_success.s()
    task_chord = chord(header, body, immutable=False)
    res = task_chord.apply_async()
    return res.id

@router.get("/multi_chord_local_retrieve")
def multi_chord_local_retrieve(request, id: str):
    res = AsyncResult(id)
    if res.ready():
        return res.get()
    return f"{id}: Processsing"

# endregion

# region Remote
# @router.get("/single_remote")
# def single_remote(request):
#     task = 'opendns.tasks.block'
#     sig = signature(task, args=(1,1), immutable=True, app=celery_app)
#     res = sig.apply_async()
#     return res.id
#
# @router.get("/single_remote_retrieve")
# def single_remote_retrieve(request, id: str):
#     res = AsyncResult(id)
#     if res.ready():
#         return res.get()
#     return f"{id}: Processing"
#
#
# @router.get("/multi_group_remote")
# def multi_group_remote(request):
#     task = 'opendns.tasks.block'
#     task_group = group([signature(task, args=(x[0], x[1]), immutable=True, app=celery_app) for x in [(1,1), (2,2), (3,3)]])
#     res = task_group.apply_async()
#     res.save()
#     return res.id
#
#
# @router.get("/multi_group_retrieve_remote")
# def multi_group_retrieve_remote(request, id: str):
#     res = GroupResult.restore(id)
#
#     if res.waiting():
#         return f"{id}: Waiting"
#     if not res.ready():
#         return f"{id}: Processing"
#     if res.failed():
#         return f"{id}: Failed"
#     if not res.successful():
#         return f"{id}: Completed {res.completed_count()}"
#     return res.join()


@router.get("/multi_chord_remote")
def multi_chord_remote(request):
    task = 'opendns.tasks.block'
    # callback = 'opendns.tasks.on_chord_success'
    callback = 'app.api.tasks.on_chord_success'

    header = [
        signature(task, args=(x[0], x[1]), immutable=True, app=celery_app)
        for x in [(1,1), (2,2), (3,3)]
    ]
    body = signature(callback, app=celery_app)
    task_chord = chord(header, body, immutable=False)
    res = task_chord.apply_async()

    return res.id

@router.get("/multi_chord_remote_retrieve")
def multi_chord_remote_retrieve(request, id: str):
    res = AsyncResult(id)
    if res.ready():
        return res.get()
    return f"{id}: Processsing"



# endregion

# region Extras
# @router.get("/sanity")
# def sanity(request, id: str = None):
#     callback = on_chord_success.si()
#     header = [add.si(i, i) for i in range(10)]
#
#     # Define the chord with the group and the success callback
#     res = chord(header)(callback)
#
#     # res = add.si(1,1).apply_async()
#
#     return res.id
#
#
#
# @router.get("/block")
# def block(request, id: str = None):
#     task = "opendns.tasks.block"
#
#     callback = update.si()
#     header = [signature(task, args=(i,i), immutable=True, app=celery_app) for i in range(3)]
#
#     chord_sig = chord(header)(callback)
#     res = chord_sig.apply_async()
#
#     # res = celery_app.send_task(task, args=(1,1))
#     # task_signature = signature(task, args=(1,1,), immutable=True, app=celery_app)
#     # res = task_signature.apply_async()
#
#     return res.id
# endregion