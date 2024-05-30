contatos = {

    "isabelagmoura98@gmail.com": {"nome": "Isabela", "telefone": "8837-4131"},
    "teste2@gmail.com": {"nome": "Teste", "telefone": "9898-9898"},
    "teste3@gmail.com": {"nome": "Teste", "telefone": "9898-9898"},
    "teste4@gmail.com": {"nome": "Teste", "telefone": "9898-9898", "extra": {"a": 1}},

}

telefone = contatos["isabelagmoura98@gmail.com"]["telefone"]
print(telefone)

extra = contatos["teste4@gmail.com"]["extra"]["a"]
print(extra)
