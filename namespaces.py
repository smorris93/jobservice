from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin


class PushNamespace(BaseNamespace, BroadcastMixin):

    def initialize(self):
        PushNamespace.sModel.addListener(self)

    def disconnect(self, *pArgs, **pKwargs):
        super(PushNamespace, self).disconnect(*pArgs, **pKwargs)
        PushNamespace.sModel.removeListener(self)

    # called by client
    def on_update(self, pParam):
        self.updateProgress()

    def updateProgress(self):
        self.broadcast_event("progress", PushNamespace.sModel.getProgress())

    def reset(self):
        self.broadcast_event("reset_progress", "")
