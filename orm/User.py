from app import Base
from sqlalchemy import Column, Integer, String, Boolean, JSON


class UserModel(Base):
    __tablename__ = 'users'

    _id = Column(Integer, primary_key=True)
    url = Column(String(100))
    external_id = Column(String(100))
    name = Column(String(100))
    alias = Column(String(100))
    created_at = Column(String(100))
    active = Column(Boolean)
    verified = Column(Boolean)
    shared = Column(Boolean)
    locale = Column(String(50))
    timezone = Column(String(100))
    last_login_at = Column(String(100))
    email = Column(String(100))
    phone = Column(String(100))
    signature = Column(String(100))
    organization_id = Column(Integer)
    tags = Column(JSON)
    suspended = Column(Boolean)
    role = Column(String(50))

    def __init__(self, _id, url=None, external_id=None, name=None, alias=None,
                 created_at=None, active=None, verified=None, shared=None, locale=None, timezone=None,
                 last_login_at=None, email=None, phone=None, signature=None, organization_id=None, tags=None,
                 suspended=None, role=None):
        self._id = _id
        self.url = url
        self.external_id = external_id
        self.name = name
        self.alias = alias
        self.created_at = created_at
        self.active = active
        self.verified = verified
        self.shared = shared
        self.locale = locale
        self.timezone = timezone
        self.last_login_at = last_login_at
        self.email = email
        self.phone = phone
        self.signature = signature
        self.organization_id = organization_id
        self.tags = tags
        self.suspended = suspended
        self.role = role

    def __repr__(self):
        return "external_id \t\t\t %r\n" \
               "name \t\t\t\t %r\n" \
               "alias \t\t\t\t %r\n" \
               "created_at \t\t\t %r\n" \
               "active \t\t\t\t %r\n" \
               "verified \t\t\t %r\n" \
               "shared \t\t\t\t %r\n" \
               "locale \t\t\t\t %r\n" \
               "timezone \t\t\t %r\n" \
               "last_login_at \t\t\t %r\n" \
               "email \t\t\t\t %r\n" \
               "phone \t\t\t\t %r\n" \
               "signature \t\t\t %r\n" \
               "organization_id \t\t %r\n" \
               "tags \t\t\t\t %r\n" \
               "suspended \t\t\t %r\n" \
               "role \t\t\t\t %r\n" % (self.external_id,self.name,self.alias,self.created_at,self.active,self.verified,self.shared,self.locale,self.timezone,
                                       self.last_login_at,self.email,self.phone,self.signature,self.organization_id,self.tags,self.suspended,self.role)

