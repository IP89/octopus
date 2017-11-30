from tornado import ioloop
from encryptions import *
import MySQLdb


# This helper interacts with the DB and will take care of inserting, updating, removing and fetching data

def set_new_words(word_list):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="octopus_db")
    ids = []
    for word, count in word_list.items():
        ids.append(generate_id(word))
        create_or_update_word(word, count, db)

    remove_unused_words(tuple(ids), db)
    db.close()

def create_or_update_word(word, count, db):
    word_id = generate_id(word)
    word_encryped = encrypt_word(word)

    cur = db.cursor()
    query = "SELECT * FROM words_list WHERE id = '{}';".format(word_id)
    cur.execute(query)
    result_set = cur.fetchall()

    if len(result_set) == 1:
      query = "UPDATE words_list SET word = '{}', count = {} WHERE id = '{}';".format(word_encryped, count, word_id)
    else:
      query = "INSERT INTO words_list SET id = '{}', word = '{}', count = {};".format(word_id, word_encryped, count)

    cur.execute(query)
    cur.close()

    db.commit()

def remove_unused_words(ids, db):
    cur = db.cursor()
    query = "DELETE FROM words_list WHERE id NOT IN {};".format(ids)
    cur.execute(query)
    cur.close()
    db.commit()

def get_words():
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="octopus_db")
    query = "SELECT * FROM words_list;"
    cur = db.cursor()
    cur.execute(query)
    result_set = cur.fetchall()

    result = {}
    for row in result_set:
        word = decrypt_word(row[1])
        result[word] = int(row[2])

    cur.close()
    db.close()

    return result

