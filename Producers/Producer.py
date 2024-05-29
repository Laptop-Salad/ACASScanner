class Producer():
    """
    The producer declares a set of methods to dispatch an event.
    The producer dispatches/produces an event.
    """
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber) -> None:
        """
        Notify all subscribers about an event.
        """
        self.subscribers.append(subscriber)

    def notify_subscribers(self, *args) -> None:
        """
        Notify all subscribers about an event.
        """
        for subscriber in self.subscribers:
            subscriber.update(self, *args)