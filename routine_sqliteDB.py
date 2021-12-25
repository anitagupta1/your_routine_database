import sqlite3

def connect():
    con=sqlite3.connect('MY_ROUTINE.db')
    cur=con.cursor()
    cur.execute('create table if not exists routine (id integer PRIMARY KEY autoincrement , date text , exercise text , diet text , went_college text , study text , code text)')
    con.commit()
    con.close()

connect()

def insert(date,exercise,diet,went_clg,study,code):
    con=sqlite3.connect('MY_ROUTINE.db')
    cur=con.cursor()
    cur.execute('insert into routine values (NULL ,?,?,?,?,?,?)',(date,exercise,diet,went_clg,study,code))
    con.commit()
    con.close()

# insert('10-12-2021','didnt','have diet','no','yes','did python')

def search(date='',exercise='',diet='',went_clg='',study='',code=''):
    con = sqlite3.connect('MY_ROUTINE.db')
    cur = con.cursor()
    cur.execute('select * from routine where date=? or exercise=? or diet=? or went_college=? or study=? or code=?',(date,exercise,diet,went_clg,study,code))
    row=cur.fetchall()
    con.commit()
    con.close()
    return row

# x=search(exercise='did')
# print(x)

def delete(id):
    con = sqlite3.connect('MY_ROUTINE.db')
    cur = con.cursor()
    cur.execute('delete from routine where id=?',(id,))
    con.commit()
    con.close()

# delete(5)

def update(date='',exercise='',diet='',went_clg='',study='',code='',id=''):
    con = sqlite3.connect('MY_ROUTINE.db')
    cur = con.cursor()
    cur.execute('update routine set date=? , exercise=? , diet=? , went_college=? , study=? , code=? where id=?' , (date, exercise, diet, went_clg, study, code,id))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect('MY_ROUTINE.db')
    cur = con.cursor()
    cur.execute('select * from routine')
    row=cur.fetchall()
    con.commit()
    con.close()
    return  row
# x=view()
# print(x)





