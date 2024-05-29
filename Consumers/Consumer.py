class Consumer():
    """
    The consumer declares a set of methods to subscribe and handle an event.
    The consumer subscribes/consumes to an event.
    """

    def update(self, producer, *args) -> None:
        """
        The interface ran when any event that this consumer is subscribed to is ran
        """
        pass