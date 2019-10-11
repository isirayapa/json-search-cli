from app import Base
from sqlalchemy import Column, Integer, String, Boolean, JSON


class TicketModel(Base):
    __tablename__ = 'tickets'

    _id = Column(String(100), primary_key=True)
    url = Column(String(100))
    external_id = Column(String(100))
    created_at = Column(String(100))
    type = Column(String(100))
    subject = Column(String(100))
    description = Column(String(100))
    priority = Column(String(50))
    status = Column(String(50))
    submitter_id = Column(Integer)
    assignee_id = Column(Integer)
    organization_id = Column(Integer)
    tags = Column(JSON)
    has_incidents = Column(Boolean)
    due_at = Column(String(100))
    via = Column(String(50))

    def __init__(self, _id, url=None, external_id=None, created_at=None, type=None, subject=None, description=None,
                 priority=None, status=None,
                 submitter_id=None, assignee_id=None, organization_id=None, tags=None, has_incidents=None, due_at=None,
                 via=None):
        self._id = _id
        self.url = url
        self.external_id = external_id
        self.created_at = created_at
        self.type = type
        self.subject = subject
        self.description = description
        self.priority = priority
        self.status = status
        self.submitter_id = submitter_id
        self.assignee_id = assignee_id
        self.organization_id = organization_id
        self.tags = tags
        self.has_incidents = has_incidents
        self.due_at = due_at
        self.via = via

    def __repr__(self):
        return "external_id \t\t\t\t %r\n" \
               "created_at \t\t\t\t %r\n" \
               "type \t\t\t\t\t %r\n" \
               "subject \t\t\t\t %r\n" \
               "description \t\t\t\t %r\n" \
               "priority \t\t\t\t %r\n" \
               "status \t\t\t\t\t %r\n" \
               "submitter_id \t\t\t\t %r\n" \
               "assignee_id \t\t\t\t %r\n" \
               "organization_id \t\t\t %r\n" \
               "tags \t\t\t\t\t %r\n" \
               "has_incidents \t\t\t\t %r\n" \
               "due_at \t\t\t\t\t %r\n" \
               "via \t\t\t\t\t %r\n" % (
                   self.external_id, self.created_at, self.type, self.subject, self.description, self.priority,
                   self.status,
                   self.submitter_id, self.assignee_id, self.organization_id, self.tags, self.has_incidents,
                   self.due_at,
                   self.via)
