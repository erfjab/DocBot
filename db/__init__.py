from .base import Base, GetDB, init_db
from .models import Users, Documents
from .crud import (
    get_documents_by_tag,
    add_tags_to_document,
    create_document,
    delete_document,
    update_document,
    create_or_update_user,
    find_similar_documents
)