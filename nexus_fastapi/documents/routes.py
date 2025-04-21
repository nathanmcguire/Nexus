from fastapi import APIRouter, HTTPException
from .services import DocumentsService
from .schemas import Document

router = APIRouter(tags=["Documents"])

@router.post("/documents", response_model=Document)
def create_document(document: Document):
    try:
        return DocumentsService.create_document(document)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/documents/{document_id}", response_model=Document)
def get_document(document_id: int):
    document = DocumentsService.get_document(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.get("/documents", response_model=list[Document])
def list_documents():
    return DocumentsService.list_documents()

@router.put("/documents/{document_id}", response_model=Document)
def update_document(document_id: int, document: Document):
    try:
        return DocumentsService.update_document(document_id, document)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/documents/{document_id}")
def delete_document(document_id: int):
    try:
        DocumentsService.delete_document(document_id)
        return {"detail": "Document deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))