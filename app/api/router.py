from ninja import Router
from .tasks import add, on_chord_error, on_chord_success, update
from celery import chord, group

router = Router()

@router.get("/sanity")
def sanity(request, id: str = None):
    callback = on_chord_success.si()
    header = [add.si(i, i) for i in range(10)]

    # Define the chord with the group and the success callback
    r = chord(header)(callback)
    return "r.id"