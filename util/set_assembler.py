import cv2
import numpy as np
import sqlite3

def fetch_rows(db_path, table_name):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM " + table_name)
    rows = c.fetchall()
    conn.close()
    return rows

def alph_from_rows(rows):
    chars = set()
    for r in rows:
        for c in r[1].encode("ascii"):
            chars.add(c)
    alph = ""
    for c in chars:
        alph += c
    return alph

def seq_len_from_rows(rows):
    n_rows = len(rows)
    lens = np.zeros(n_rows)
    for i in range(n_rows):
        lens[i] = len(rows[i][1].encode("ascii"))
    return int(np.amax(lens))

def cross_reference_db_imgs(rows, img_directory, n_img_variants, ext,
    base_name=None):
    dataset = []
    for chem_id, iupac in rows:
        for i in range(n_img_variants):
            img_str = img_directory + str(chem_id) + base_name + str(i) + ext
            # print img_str
            # break
            img = cv2.imread(img_str, 0)
            img = np.reshape(img, [len(img), len(img[0]), 1])
            dataset.append((img, iupac.encode("ascii")))
    return dataset

if __name__ == "__main__":
    rows = fetch_rows('../mol/ai.db', 'AI')
    dataset = cross_reference_db_imgs(rows, '../mol/im/', 6, ext=".png",
                base_name="noise")
