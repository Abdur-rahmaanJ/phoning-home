import libsql_client

from . import _sql

class PhoningHome:
    URL = ''
    TOKEN = ''
    con = None

    @classmethod
    def connect(cls, url, token):
        cls.URL = url
        cls.TOKEN = token
        cls.create_tables()
    
    @classmethod
    def create_tables(cls):
        client = libsql_client.create_client_sync(
            url=cls.URL,
            auth_token=cls.TOKEN
        )
        with client:
            try:
                libsql_statements = [
                    libsql_client.Statement(
                        s[0],
                        s[1]
                    ) for s in _sql.create_tables]
                rss = client.batch(libsql_statements)
            except libsql_client.client.LibsqlError:
                pass
    
    @classmethod
    def fetch(cls, *args):
        if len(args) in [0, 1]:
            raise Exception('Should have more arguments')
        
        optype = args[0]

        if optype == 'leaderboard':
            if len(args) != 2:
                raise Exception('Args should be: leaderboard, <gamename>')
            
            gamename = args[1]
            client = libsql_client.create_client_sync(
                url=cls.URL,
                auth_token=cls.TOKEN
            )
            with client:
                try:
                    stmnts = [_sql.select_game(gamename)]
                    libsql_stmnts = _sql.libsql_batch(stmnts)
                    rss = client.batch(libsql_stmnts)
                    return rss[0].rows
                except libsql_client.client.LibsqlError:
                    pass
    
    @classmethod
    def leaderboard(cls, gamename, player, score):
        client = libsql_client.create_client_sync(
            url=cls.URL,
            auth_token=cls.TOKEN
        )
        with client:
            try:
                stmnts = [_sql.insert_leaderboard_value(gamename, player, score)]
                libsql_stmnts = _sql.libsql_batch(stmnts)
                rss = client.batch(libsql_stmnts)
            except libsql_client.client.LibsqlError:
                pass


