from databaseconn import get_db_connection

class MealCategories:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("ID must be an integer")
        
    @property
    def name(self):
        return self._name
     
       