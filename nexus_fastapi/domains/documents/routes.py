from fastapi import APIRouter
from .controllers import DocumentsController
from .schemas import Document

router = APIRouter()

@router.post("/documents", response_model=Document, tags=["Documents"])
def create_document(document: Document):
    return DocumentsController.create_document(document)

@router.get("/documents/{document_id}", response_model=Document, tags=["Documents"])
def get_document(document_id: int):
    return DocumentsController.get_document(document_id)

@router.get("/documents", response_model=list[Document], tags=["Documents"])
def list_documents():
    return DocumentsController.list_documents()

@router.put("/documents/{document_id}", response_model=Document, tags=["Documents"])
def update_document(document_id: int, document: Document):
    return DocumentsController.update_document(document_id, document)

@router.delete("/documents/{document_id}", tags=["Documents"])
def delete_document(document_id: int):
    DocumentsController.delete_document(document_id)
    return {"detail": "Document deleted successfully"}