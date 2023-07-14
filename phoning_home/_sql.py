import libsql_client

create_table_keyvalue = '''
CREATE TABLE keyvalue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    namespace TEXT UNIQUE NOT NULL,
    key TEXT NOT NULL,
    value TEXT
);
'''

create_table_leaderboard = '''
CREATE TABLE leaderboard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gamename TEXT UNIQUE NOT NULL,
    username TEXT NOT NULL,
    score INTEGER NOT NULL
);
'''

create_table_counter = '''
CREATE TABLE counter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    namespace TEXT UNIQUE NOT NULL,
    key TEXT NOT NULL,
    value INTEGER NOT NULL
);
'''

def sql_stmt(stmnt, args):
    return [stmnt, args]

def insert_leaderboard_value(gamename, player, score):
    return sql_stmt('insert into leaderboard (gamename, username, score) values (?, ?, ?)', 
                    [gamename, player, score])

def select_game(gamename):
    return sql_stmt('select username,score from leaderboard where gamename = ?;', [gamename])

def libsql_batch(stmnts):
    '''
    stmnts: 
        [sql_stmt(stmnt, args),]
    '''
    return [
    libsql_client.Statement(
        s[0],
        s[1]
    ) for s in stmnts]

create_tables = [
    [create_table_keyvalue, []],
    [create_table_leaderboard, []],
    [create_table_counter, []],
]
