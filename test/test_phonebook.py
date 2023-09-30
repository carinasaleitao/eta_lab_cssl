from src.phonebook import Phonebook

class TestPhonebook:

    #add

    def test_add_success(self):

        # Setup
        phonebook = Phonebook()
        response_assert = "Numero adicionado"

        # Chamada
        response = phonebook.add("Carina", '99999999')

        #Avaliação
        assert response_assert == response

    def test_add_invalid_name_number_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("#Carina", '99999999')

        assert response_assert == response

    def test_add_invalid_name_at_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("@Carina", '99999999')

        assert response_assert == response

    def test_add_invalid_name_exclamation_point(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("!Carina", '99999999')

        assert response_assert == response

    def test_add_invalid_name_dollar_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("$Carina", '99999999')

        assert response_assert == response

    def test_add_invalid_name_percent_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("%Carina", '99999999')

        assert response_assert == response

    def test_add_invalid_number(self):

        phonebook = Phonebook()
        response_assert = "Numero invalido"

        response = phonebook.add("Carina", '')

        assert response_assert == response

    def test_add_duplicated_name(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("POLICIA", '99999999')

        assert response_assert == response

    #lookup

    def test_lookup_success(self):
        phonebook = Phonebook()
        response_assert = "190"

        response = phonebook.lookup("POLICIA")

        assert response_assert == response

    def test_lookup_invalid_name_number_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.lookup("#POLICIA")

        assert response_assert == response

    def test_lookup_invalid_name_at_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.lookup("@POLICIA")

        assert response_assert == response

    def test_lookup_invalid_name_exclamation_point(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.lookup("!POLICIA")

        assert response_assert == response

    def test_lookup_invalid_name_dollar_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.lookup("$POLICIA")

        assert response_assert == response

    def test_lookup_invalid_name_percent_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.lookup("%POLICIA")

        assert response_assert == response

    def test_lookup_invalid_name_percent_sign(self):

        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.lookup("%POLICIA")

        assert response_assert == response

    #get_names

    def test_get_names_success(self):

        phonebook = Phonebook()
        response_assert = ['POLICIA']

        response = list(phonebook.get_names())

        assert response_assert == response

    #get_numbers

    def test_get_numbers_success(self):

        phonebook = Phonebook()
        response_assert = ['190']

        response = list(phonebook.get_numbers())

        assert response_assert == response

    #clear

    def test_clear_success(self):

        phonebook = Phonebook()
        response_assert = 'phonebook limpado'

        response = phonebook.clear()

        assert response_assert == response

    #search

    def test_search_success(self):

        phonebook = Phonebook()
        response_assert = [{'POLICIA', '190'}]

        response = phonebook.search('POLICIA')

        assert response_assert == response

    #get_phonebook_sorted

    def test_get_phonebook_sorted_success(self):

        phonebook = Phonebook()
        phonebook.add('CARINA','888')
        response_assert = {'POLICIA': '190', 'CARINA': '888'}

        response = phonebook.get_phonebook_sorted()

        assert response_assert == response

    #get_phonebook_reverse

    def test_get_phonebook_reverse_success(self):

        phonebook = Phonebook()
        phonebook.add('CARINA','888')
        response_assert = {'CARINA': '888', 'POLICIA': '190'}

        response = phonebook.get_phonebook_reverse()

        assert response_assert == response

    #delete

    def test_delete_success(self):

        phonebook = Phonebook()
        response_assert = 'Numero deletado'

        response = phonebook.delete('POLICIA')

        assert response_assert == response