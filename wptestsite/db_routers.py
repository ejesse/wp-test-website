class WordPressRouter(object):
    """A router to control all database operations on models in
    the wordpress application"""

    def db_for_read(self, model, **hints):
        "Point all operations on wordpress models to 'other'"
        if model._meta.app_label == 'wordpress':
            return 'wordpress'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on wordpress models to 'other'"
        if model._meta.app_label == 'wordpress':
            return 'wordpress'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in wordpress is involved"
        if obj1._meta.app_label == 'wordpress' or obj2._meta.app_label == 'wordpress':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the wordpress app only appears on the 'other' db"
        if db == 'wordpress':
            return model._meta.app_label == 'wordpress'
        elif model._meta.app_label == 'wordpress':
            return False
        return None

class DefaultRouter(object):

    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation between two objects in the db pool"
        db_list = ('default')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_syncdb(self, db, model):
        "Explicitly put all models on all databases."
        return True