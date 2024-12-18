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
    
    @name.setter
    def name(self, new_name):
     if isinstance(new_name, str):
            if len(new_name) > 0:
                    self._name = new_name
            else:
                    ValueError("Name must be longer than 0 characters")
     else:
                TypeError("Name must be a string")
     
       