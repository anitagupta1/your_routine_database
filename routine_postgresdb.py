import psycopg2

def Connect():
    con = psycopg2.connect("dbname='myroutine' user='postgres' password='postgres' port='5432' host='localhost'")
    cur=con.cursor()
    cur.execute('create table if not exists routine(id SERIAL NOT NULL PRIMARY KEY , date text , exercise text , diet text , went_college text , study text , code text)')
    con.commit()
    con.close()

Connect()

def insert(date,exercise,diet,went_clg,study,code):
    con = psycopg2.connect("dbname='myroutine' user='postgres' password='postgres' port='5432' host='localhost'")
    cur=con.cursor()
    cur.execute('insert into routine(date, exercise, diet , went_college , study , code ) values (%s,%s,%s,%s,%s,%s)',(date,exercise,diet,went_clg,study,code))
    con.commit()
    con.close()

def search(date='',exercise='',diet='',went_clg='',study='',code=''):
    con = psycopg2.connect("dbname='myroutine' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = con.cursor()
    cur.execute('select * from routine where date=%s or exercise=%s or diet=%s or went_college=%s or study=%s or code=%s',(date,exercise,diet,went_clg,study,code))
    row=cur.fetchall()
    con.commit()
    con.close()
    return row

def delete(id):
    con = psycopg2.connect("dbname='myroutine' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = con.cursor()
    cur.execute('delete from routine where id=%s',(id,))
    con.commit()
    con.close()


def update(date='',exercise='',diet='',went_clg='',study='',code='',id=''):
    con = psycopg2.connect("dbname='myroutine' user='postgres' password='postgres' port='5432' host='localhost'")
    cur = con.cursor()
    cur.execute('update routine set date=%s , exercise=%s , diet=%s , went_college=%s , study=%s , code=%s where id=%s' , (date, exercise, diet, went_clg, study, code,id))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect("dbname='myroutine' user='postgres' password='postgres' port='5432' host='localhost'")

    cur = con.cursor()
    cur.execute('select * from routine')
    row=cur.fetchall()
    con.commit()
    con.close()
    return  row



