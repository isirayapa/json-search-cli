from orm.Ticket import TicketModel

TicketDict = {
    '_id': TicketModel._id,
    'url': TicketModel.url,
    'external_id': TicketModel.external_id,
    'created_at': TicketModel.created_at,
    'type': TicketModel.type,
    'subject': TicketModel.subject,
    'description': TicketModel.description,
    'priority': TicketModel.priority,
    'status': TicketModel.status,
    'submitter_id': TicketModel.submitter_id,
    'assignee_id': TicketModel.assignee_id,
    'organization_id': TicketModel.organization_id,
    'tags': TicketModel.tags,
    'has_incidents': TicketModel.has_incidents,
    'due_at': TicketModel.due_at,
    'via': TicketModel.via,
}
