from orm.User import UserModel

UserDict = {
    '_id': UserModel._id,
    'url': UserModel.url,
    'external_id': UserModel.external_id,
    'name': UserModel.name,
    'alias': UserModel.alias,
    'created_at': UserModel.created_at,
    'active': UserModel.active,
    'verified': UserModel.verified,
    'shared': UserModel.shared,
    'locale': UserModel.locale,
    'timezone': UserModel.timezone,
    'last_login_at': UserModel.last_login_at,
    'email': UserModel.email,
    'phone': UserModel.phone,
    'signature': UserModel.signature,
    'organization_id': UserModel.organization_id,
    'tags': UserModel.tags,
    'suspended': UserModel.suspended,
    'role': UserModel.role
}
