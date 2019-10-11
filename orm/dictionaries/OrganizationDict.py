from orm.Organization import OrganizationModel

OrganizationDict = {
    '_id': OrganizationModel._id,
    'url': OrganizationModel.url,
    'external_id': OrganizationModel.external_id,
    'name': OrganizationModel.name,
    'domain_names': OrganizationModel.domain_names,
    'created_at': OrganizationModel.created_at,
    'details': OrganizationModel.details,
    'shared_tickets': OrganizationModel.shared_tickets,
    'tags': OrganizationModel.tags,
}
