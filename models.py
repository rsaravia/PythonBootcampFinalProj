import db

from sqlalchemy import Column, Integer, String, Date

class News(db.Base):
    __tablename__ = "noticias"

    id       =  Column(Integer(), primary_key=True)
    title    =  Column(String(200), nullable=False, unique=False)
    website  =  Column(String(200), nullable=False, unique=False)
    pub_date =  Column(Date())
    link     =  Column(String(200), nullable=False)

    def __init__(self, title, website, pub_date, link):
        self.title = title
        self.website = website
        self.pub_date = pub_date
        self.link = link

    def __str__(self):
        return (self.title,
                self.website,
                self.pub_date,
                self.link)


if __name__ == '__main__':
    db.Base.metadata.drop_all(db.engine)
    db.Base.metadata.create_all(db.engine)


