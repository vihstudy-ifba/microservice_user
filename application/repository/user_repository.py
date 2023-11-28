import os

from supabase import create_client

supabase = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))

class UserRepository:
    def __init__(self):
        self.collection = supabase.table('usuario')

    def get_all_users(self):
        users = self.collection.select('*').execute().data
        return users

    def new_user(self, user):
        self.collection.insert(user).execute()

    def get_user_by_id(self, id):
        user = self.collection.select('*').eq('id', id).execute().data
        return user

    def getUserByLogin(self, user):
        user = self.collection.select('*').eq('usuario', user.usuario).eq('senha', user.senha).execute().data
        return user