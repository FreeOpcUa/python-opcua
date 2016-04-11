class HistoryStorageInterface(object):

    """
    Interface of a history backend.
    Must be implemented by backends
    """

    def new_historized_node(self, node, period, count=0):
        """
        Called when a new node is to be historized
        Returns None
        """
        raise NotImplementedError

    def save_node_value(self, node, datavalue):
        """
        Called when the value of a historized node has changed and should be saved in history
        Returns None
        """
        raise NotImplementedError

    def read_node_history(self, node, start, end, nb_values):
        """
        Called when a client make a history read request for a node
        if start or end is missing then nb_values is used to limit query
        nb_values is the max number of values to read. Ignored if 0
        Start time and end time are inclusive
        Returns a list of DataValues and a continuation point which
        is None if all nodes are read or the ServerTimeStamp of the last rejected DataValue
        """
        raise NotImplementedError

    def new_historized_event(self, event, period):
        """
        Called when historization of events is enabled on server side
        FIXME: we may need to store events per nodes in future...
        Returns None
        """
        raise NotImplementedError

    def save_event(self, event):
        """
        Called when a new event has been generated ans should be saved in history
        Returns None
        """
        raise NotImplementedError

    def read_event_history(self, start, end, evfilter):
        """
        Called when a client make a history read request for events
        Start time and end time are inclusive
        Returns a list of Events and a continuation point which
        is None if all events are read or the ServerTimeStamp of the last rejected event
        """
        raise NotImplementedError

    def stop(self):
        """
        Called when the server shuts down
        Can be used to close database connections etc.
        """
        raise NotImplementedError
