from typing import Dict, Any

livro: Dict[str, Any] = {
    "titulo": "1984", 
    "autor": "George Orwell", 
    "ano": 1949
    }

lista_de_elementos: list = livro.items()
for chave, valor in livro.items():
    print(f"{chave}: {valor}")