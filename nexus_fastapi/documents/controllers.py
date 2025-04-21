from fastapi import HTTPException
from .services import DocumentsService
from .schemas import Document

class DocumentsController:
    @staticmethod
    def create_document(document_data: Document):
        try:
            return DocumentsService.create_document(document_data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def get_document(document_id: int):
        document = DocumentsService.get_document(document_id)
        if not document:
            raise HTTPException(status_code=404, detail="Document not found")
        return document

    @staticmethod
    def list_documents():
        return DocumentsService.list_documents()

    @staticmethod
    def update_document(document_id: int, document_data: Document):
        try:
            return DocumentsService.update_document(document_id, document_data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def delete_document(document_id: int):
        try:
            DocumentsService.delete_document(document_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))