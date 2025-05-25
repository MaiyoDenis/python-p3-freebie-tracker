from lib.models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lib/freebies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Clear existing data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

# Seed Companies
company1 = Company(name="TechCorp", founding_year=1990)
company2 = Company(name="InnovateLLC", founding_year=1985)
session.add_all([company1, company2])
session.commit()

# Seed Devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
session.add_all([dev1, dev2])
session.commit()

# Seed Freebies
freebie1 = Freebie(item_name="Sticker", value=5, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-Shirt", value=20, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Mug", value=10, dev=dev2, company=company1)
session.add_all([freebie1, freebie2, freebie3])
session.commit()

print("Seed data added successfully.")
