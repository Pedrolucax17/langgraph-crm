from langchain.tools import tool

@tool
def add_client(
    name: str,
    phone=None,
    email=None,
    company=None,
    tags=None,
    notes=None
):
    """Adiciona um cliente no banco. Passe name, e opcionalmente phone, email, company
    tags, notes."""
    return {"message": "Cliente adicionado com sucesso"}

@tool
def find_client(query:str):
    return {"message": "Cliente adicionado"}

