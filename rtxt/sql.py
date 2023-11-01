from sqlite3 import connect

# запись файла в csv формате


def csv_writer(data, fname):
    with open(fname, 'w', encoding="utf8") as csvfile:
        csvfile.write('type;data\n' +
                      '\n'.join([f'{t};{d}' for t, d in data]))

# запись файла в sql БД


def sql_writer(data, database='text_types.sqlite'):
    con = connect(database)
    cur = con.cursor()
    for t, d in data:
        if t and d:
            cur.execute(
                'INSERT INTO data(type, data) VALUES ((SELECT id FROM types WHERE type = ?), ?)',
                (t, d))
    con.commit()
    con.close()

# удаление всех записей из БД


def clear_database(database='text_types.sqlite'):
    con = connect(database)
    cur = con.cursor()
    cur.execute('DELETE from data')
    con.commit()
    con.close()
