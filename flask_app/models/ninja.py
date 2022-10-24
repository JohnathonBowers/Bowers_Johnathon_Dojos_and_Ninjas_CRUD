from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__ (self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo_id = db_data['dojo_id']

    @classmethod
    def get_one (cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        ninja_object = cls(result[0])
        return ninja_object

    @classmethod
    def save (cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_ninjas_schema').query_db(query, data)
    
    @classmethod
    def update (cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL('dojos_ninjas_schema').query_db(query, data)
    
    @classmethod
    def destroy (cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"
        return connectToMySQL('dojos_ninjas_schema').query_db(query, data)