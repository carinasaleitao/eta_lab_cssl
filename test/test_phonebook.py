from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_sucess(self):

        # Setup
        phonebook = Phonebook()
        response_assert = "Numero adicionado"

        # Chamada
        response = phonebook.add("Carina", '99999999')

        #Avaliação
        assert response_assert == response
