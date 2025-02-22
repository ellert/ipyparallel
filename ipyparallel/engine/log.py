from zmq.log.handlers import PUBHandler


class EnginePUBHandler(PUBHandler):
    """A simple PUBHandler subclass that sets root_topic"""

    engine = None

    def __init__(self, engine, *args, **kwargs):
        PUBHandler.__init__(self, *args, **kwargs)
        self.engine = engine

    @property
    def root_topic(self):
        """this is a property, in case the handler is created
        before the engine gets registered with an id"""
        if isinstance(getattr(self.engine, 'id', None), int):
            return f"engine.{self.engine.id}"
        else:
            return "engine"
