from app import Base
from sqlalchemy import Column, Integer, String, Boolean, JSON


class OrganizationModel(Base):
    __tablename__ = 'organizations'

    _id = Column(Integer, primary_key=True)
    url = Column(String(100))
    external_id = Column(String(100))
    name = Column(String(100))
    domain_names = Column(JSON)
    created_at = Column(String(100))
    details = Column(String(100))
    shared_tickets = Column(Boolean)
    tags = Column(JSON)

    def __init__(self, _id, url=None, external_id=None, name=None, domain_names=None, created_at=None, details=None,
                 shared_tickets=None, tags=None,):
        self._id = _id
        self.url = url
        self.external_id = external_id
        self.name = name
        self.domain_names = domain_names
        self.created_at = created_at
        self.details = details
        self.shared_tickets = shared_tickets
        self.tags = tags

    def __repr__(self):
        return "external_id \t\t\t\t %r\n" \
               "name \t\t\t\t\t %r\n" \
               "domain_names \t\t\t\t %r\n" \
               "created_at \t\t\t\t %r\n" \
               "details \t\t\t\t %r\n" \
               "shared_tickets \t\t\t\t %r\n" \
               "tags \t\t\t\t\t %r\n" % (
                   self.external_id, self.name, self.domain_names, self.created_at, self.details, self.shared_tickets,
                   self.tags)
