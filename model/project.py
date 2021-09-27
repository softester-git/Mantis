from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, status=None, enabled=None, view_state=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.enabled = enabled
        self.view_state = view_state
        self.description = description

    def __repr__(self):
        return ("%s:%s:%s:%s:%s:%s" % (self.id, self.name, self.status, self.enabled, self.view_state, self.description))

    def __eq__(self, other):
        return((self.id is None or other.id is None or self.id == other.id)
               and self.name == other.name
               and self.status == other.status
               and self.enabled == other.enabled
               and self.view_state == other.view_state
               and self.description == other.description)

    def id_or_max(pr):
        if pr.id:
            return(int(pr.id))
        else:
            return(maxsize)
