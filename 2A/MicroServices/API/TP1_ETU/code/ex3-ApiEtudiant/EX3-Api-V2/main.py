import os
from fastapi import FastAPI
from pydantic import BaseModel

from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()


class Etudiants(SQLModel, table=True):
	mail: Optional[str] = Field(default=None, primary_key=True)
	mdp: Optional[str]
	adresse: Optional[str]
	insee: Optional[int]

class Villes(SQLModel,table=True):
	commune: str
	cp: str
	dept: str
	insee: Optional[int] = Field(default=None, primary_key=True)

engine = create_engine("sqlite:///bdd/IUT.sqlite")

# SQLModel.metadata.create_all(engine)

@app.get("/etudiants")
def get_etuds():
	results = None
	with Session(engine) as session:
		statement = select(Etudiants.mail, Etudiants.mdp, Etudiants.adresse, Villes.commune, Villes.cp).where(Etudiants.insee == Villes.insee)
		results = session.exec(statement).all()
	return results

	

@app.post('/etudiants')
def create_etud(etudiant: Etudiants):
	try:
		with Session(engine) as session:
			session.add(etudiant)
			session.commit()
	except:
		return {"message": "Erreur"}
	return etudiant

@app.delete('/etudiants/{mail:str}')
def delete_etud(mail:str):
	etudiant = None
	try:
		with Session(engine) as session:
			statement = select(Etudiants).where(Etudiants.mail == mail)
			etudiant = session.exec(statement).one()
			session.delete(etudiant)
			session.commit()
	except:
		return {"message": "Erreur"}
	return {"message": "L'étudiant a bien été supprimé"}

@app.put('/etudiants/{mail:str}')
def modify_etud(mail:str, etudiant: Etudiants):
	try:
		with Session(engine) as session:
			statement = select(Etudiants).where(Etudiants.mail == mail)
			etudiant_bdd = session.exec(statement).one()
			
			etudiant_bdd.adresse = etudiant.adresse
			etudiant_bdd.mail = etudiant.mail
			etudiant_bdd.mdp = etudiant.mdp
			etudiant_bdd.insee = etudiant.insee

			session.add(etudiant_bdd)
			session.commit()
	except:
		return {"message": "Erreur"}
	return {"message": "L'étudiant a bien été modifié"}
