from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Defines News table if not already exists
class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    url = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=False)
    source = Column(String, nullable=False)

# Creates or connect to the database
def initialize_database(database_name='news.db'):
    engine = create_engine(f'sqlite:///{database_name}')
    Base.metadata.create_all(engine)  # Creates the table if it doesn't exist
    return engine

# Saves news data to the database
def store_news(engine, title, description, url, published_at, source):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_news = News(title=title, description=description, url=url, published_at=published_at, source=source)
    session.add(new_news)
    session.commit()
    session.close()
    print(f"News saved: {title} - {source} - {published_at}")
