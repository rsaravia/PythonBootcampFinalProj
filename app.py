from flask import Flask, render_template, request

app = Flask(__name__)


# Main URL
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/formulario', methods=['POST'])
def attend_formu():
    selection = request.form['submit_button']
    if selection == "Fetch":
        fetch()
        return render_template("fetched.html")
    elif selection == "Show":
        data = show()
        headers = ['Num', 'Title', 'Website', 'Date', 'Link']
        data_list = data
        return render_template("show.html", headers=headers, data_list=data_list)
    else:
        return False


# Funtion to look for the data to the database
def show():
    import db
    from models import News
    from datetime import datetime, timedelta

    data = list()

    # News estimate today and 7 days before
    today = datetime.today()
    new_past_day = today - timedelta(days=7)

    consulta = db.Session.query(News).filter(News.pub_date.between(new_past_day, today)).all()
    for n in consulta:
        values = list()
        # ----
        values.append(n.id)
        values.append(n.title)
        values.append(n.website)
        values.append(n.pub_date)
        values.append(n.link)
        # ---
        data.append(values)
    return data


# Funtion to fetch the data from websites and push to database
def fetch():
    import db
    from models import News

    from datetime import datetime
    today = datetime.today()

    from bs4 import BeautifulSoup
    import requests
    import pandas as pd

    # Fetch from theverge.com
    # --------------------------------------------------------------------
    url = "https://www.theverge.com/"

    page = requests.get(url)

    titles = list()
    links = list()

    # Obtener los Titulos
    soup = BeautifulSoup(page.content, "html.parser")
    news = soup.find_all('h2', class_="c-entry-box--compact__title")
    for i in news:
        titles.append(i.text)

    # Obtener los links
    for each_news in news:
        obj_soup = BeautifulSoup(str(each_news), 'html.parser')
        a = obj_soup.find('a')
        links.append(a['href'])

    write_to_db(titles=titles, links=links,obj_model=News, url=url, db=db, today=today)
    # --------------------------------------------------------------------


    # Fetch from mashable.com
    # --------------------------------------------------------------------
    url = "https://mashable.com/"
    page = requests.get(url)

    titles = list()
    links = list()

    # Obtener los Titulos
    soup = BeautifulSoup(page.content, "html.parser")
    news = soup.find_all('a', class_="w-full block text-lg font-bold mt-2")
    for i in news:
        titles.append(i.text)

    # Obtener los links
    for each_news in news:
        obj_soup = BeautifulSoup(str(each_news), 'html.parser')
        a = obj_soup.find('a')
        links.append(url[:-1] + a['href'])

    write_to_db(titles=titles, links=links, obj_model=News, url=url, db=db, today=today)
    # --------------------------------------------------------------------


    # Fetch from https://techcrunch.com/
    # --------------------------------------------------------------------
    url = "https://techcrunch.com/"
    page = requests.get(url)

    titles = list()
    links = list()

    # Obtener los Titulos
    soup = BeautifulSoup(page.content, "html.parser")
    news = soup.find_all('a', class_="post-block__title__link")
    for i in news:
        titles.append(i.text)

    # Obtener los links
    for each_news in news:
        obj_soup = BeautifulSoup(str(each_news), 'html.parser')
        a = obj_soup.find('a')
        links.append(a['href'])

    write_to_db(titles=titles, links=links, obj_model=News, url=url, db=db, today=today)
    # --------------------------------------------------------------------


def write_to_db(titles, links, obj_model, url, db, today):
    from sqlalchemy import and_
    # Write to the db
    for i, title in enumerate(titles):
        # First check if title news from same url do not exist
        consulta = db.Session.query(obj_model).filter(
            and_(obj_model.title == title,
                 obj_model.website == url )
        ).all()
        if len(consulta) >= 1:
            pass
        else:
            new_register = obj_model(title, url, today, links[i])
            db.Session.add(new_register)
            db.Session.commit()



"""
    # Connect to the DB
    # -----------------
    engine = db.create_engine("mysql+pymysql://roberto:password@localhost:3308/mydatabase")
    connection = engine.connect()
    metadata = db.MetaData()
    news = db.Table('NEWS', metadata, autoload=True, autoload_with=engine)
    query = db.select([news]) # Select All
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    # -----------------

    headers = ['Num','Title','Website','Date','Link']
    data_list = ResultSet
    return render_template("show.html", headers=headers, data_list=data_list)
"""

if __name__ == '__main__':
    app.run()
