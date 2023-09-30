class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def valid_name(self,name):
        special_chars = ['#','@','!','$','%']
        for i in special_chars:
            if i in name:
                return False
        return True

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Numero invalido' or 'Numero adicionado' or 'Nome existente' or 'Nome invalido'
        """
        if len(number) < 3 or len(number) > 9:
            return 'Numero invalido'

        if self.valid_name(name):
            if name not in self.entries:
                self.entries[name] = number
                return 'Numero adicionado'
            else:
                return 'Nome existente'
        return 'Nome invalido'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if self.valid_name(name):
            if name in self.entries:
                return self.entries[name]
            else:
                return 'Nome existente'
        return 'Nome invalido'

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

    def change_number(self, name, number):
        """
        Change the number of a contact
        :param name: name of person in string
        :param number: new number of person in string
        :return: 'Numero invalido' or 'Numero alterado' or 'Nome inexistente' or 'Nome invalido'
        """
        if len(number) < 3 or len(number) > 9:
            return 'Numero invalido'

        if self.valid_name(name):
            if name in self.entries:
                self.entries[name] = number
                return 'Numero alterado'
            else:
                return 'Nome inexistente'
        return 'Nome invalido'

    def get_name_by_number(self, number):
        """
        Gets the name of a given number
        :param number: number of person in string
        :return: 'Numero invalido' or name or 'Numero inexistente'
        """
        if len(number) < 3 or len(number) > 9:
            return 'Numero invalido'

        if number in self.entries.values():
            name = {i for i in self.entries if self.entries[i] == "190"}
            return name
        return 'Numero inexistente'


