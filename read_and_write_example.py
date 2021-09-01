import db
from models import News
from datetime import datetime, timedelta

today = datetime.today()
new_past_day = today - timedelta(days=7)
print("Past: ", new_past_day)
print("Today: ", today)

# Write
new_register = News('Nueva noticia7','amazon.com','2021-08-30','https://www.google.com.sv')
db.Session.add(new_register)
db.Session.commit()


# Read (Query)
# consulta = db.Session.query(News).filter_by(pub_date='2021-08-12').all() # It Works!
# consulta = db.Session.query(News).filter_by(pub_date=new_past_day).all() # It Works!
consulta = db.Session.query(News).filter(News.pub_date.between(new_past_day, today)).all()
for n in consulta:
    print(f"Title: {n.title}")



