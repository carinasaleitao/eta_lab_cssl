from src.phonebook import Phonebook


class TestPhonebook:

    # add

    def test_add_success(self):
        # Setup
        phonebook = Phonebook()
        response_assert = "Numero adicionado"

        # Chamada
        response = phonebook.add("Carina", '888888888')

        # Avaliação
        assert response_assert == response

    def test_add_invalid_name_number_sign(self):
        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("#Carina", '888888888')

        assert response_assert == response

    def test_add_invalid_name_at_sign(self):
        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("@Carina", '888888888')

        assert response_assert == response

    def test_add_invalid_name_exclamation_point(self):
        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("!Carina", '888888888')

        assert response_assert == response

    def test_add_invalid_name_dollar_sign(self):
        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("$Carina", '888888888')

        assert response_assert == response

    def test_add_invalid_name_percent_sign(self):
        phonebook = Phonebook()
        response_assert = "Nome invalido"

        response = phonebook.add("%Carina", '888888888')

        assert response_assert == response

    def test_add_invalid_number(self):
        phonebook = Phonebook()
        response_assert = "Numero invalido"

        response = phonebook.add("Carina", '1')

        assert response_assert == response

    def test_add_duplicated_name(self):
        phonebook = Phonebook()
        response_assert = 'Nome existente'

        response = phonebook.add("POLICIA", '888888888')

        assert response_assert == response

    # lookup

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

    # get_names

    def test_get_names_success(self):
        phonebook = Phonebook()
        response_assert = ['POLICIA']

        response = list(phonebook.get_names())

        assert response_assert == response

    # get_numbers

    def test_get_numbers_success(self):
        phonebook = Phonebook()
        response_assert = ['190']

        response = list(phonebook.get_numbers())

        assert response_assert == response

    # clear

    def test_clear_success(self):
        phonebook = Phonebook()
        response_assert = 'phonebook limpado'

        response = phonebook.clear()

        assert response_assert == response

    # search

    def test_search_success(self):
        phonebook = Phonebook()
        response_assert = [{'POLICIA', '190'}]

        response = phonebook.search('POLICIA')

        assert response_assert == response

    # get_phonebook_sorted

    def test_get_phonebook_sorted_success(self):
        phonebook = Phonebook()
        phonebook.add('CARINA', '888888888')
        response_assert = {'POLICIA': '190', 'CARINA': '888888888'}

        response = phonebook.get_phonebook_sorted()

        assert response_assert == response

    # get_phonebook_reverse

    def test_get_phonebook_reverse_success(self):
        phonebook = Phonebook()
        phonebook.add('CARINA', '888888888')
        response_assert = {'CARINA': '888888888', 'POLICIA': '190'}

        response = phonebook.get_phonebook_reverse()

        assert response_assert == response

    # delete

    def test_delete_success(self):
        phonebook = Phonebook()
        response_assert = 'Numero deletado'

        response = phonebook.delete('POLICIA')

        assert response_assert == response

    # change_number

    def test_change_number_success(self):
        phonebook = Phonebook()
        response_assert = 'Numero alterado'

        response = phonebook.change_number('POLICIA','191')

        assert response_assert == response

    def test_change_number_invalid_name(self):
        phonebook = Phonebook()
        response_assert = 'Nome invalido'

        response = phonebook.change_number('@POLICIA', '191')

        assert response_assert == response

    def test_change_number_nonexistent_name(self):
        phonebook = Phonebook()
        response_assert = 'Nome inexistente'

        response = phonebook.change_number('POLICI', '191')

        assert response_assert == response

    def test_change_number_invalid_number(self):
        phonebook = Phonebook()
        response_assert = 'Numero invalido'

        response = phonebook.change_number('POLICIA', '1')

        assert response_assert == response

    # get_name_by_number

    def test_get_name_by_number_success(self):
        phonebook = Phonebook()
        response_assert = 'POLICIA'

        response = phonebook.get_name_by_number('190')

        assert response_assert == response

    def test_get_name_by_number_invalid_number(self):
        phonebook = Phonebook()
        response_assert = 'Numero invalido'

        response = phonebook.get_name_by_number('1')

        assert response_assert == response

    def test_get_name_by_number_nonexistent_number(self):
        phonebook = Phonebook()
        response_assert = 'Numero inexistente'

        response = phonebook.get_name_by_number('191')

        assert response_assert == response
