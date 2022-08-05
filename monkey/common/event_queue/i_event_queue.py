from abc import ABC, abstractstaticmethod
from typing import Any, Callable, Sequence

from common.events import AbstractEvent


class IEventQueue(ABC):
    """
    Manages subscription and publishing of events
    """

    @abstractstaticmethod
    def subscribe_all(subscriber: Callable[..., Any]):
        """
        Subscribes a subscriber to all events

        :param subscriber: Callable that should subscribe to events
        """

        pass

    @abstractstaticmethod
    def subscribe_types(types: Sequence[AbstractEvent], subscriber: Callable[..., Any]):
        """
        Subscribes a subscriber to all specifed event types

        :param types: Event types to which the subscriber should subscribe
        :param subscriber: Callable that should subscribe to events
        """

        pass

    @abstractstaticmethod
    def subscribe_tags(tags: Sequence[str], subscriber: Callable[..., Any]):
        """
        Subscribes a subscriber to all specified event tags

        :param tags: Event tags to which the subscriber should subscribe
        :param subscriber: Callable that should subscribe to events
        """

        pass

    @abstractstaticmethod
    def publish(event: AbstractEvent, data: Any):
        """
        Publishes an event with the given data

        :param event: Event to publish
        :param data: Data to pass to subscribers with the event publish
        """

        pass


# TODO: Add unsubscribing functions
