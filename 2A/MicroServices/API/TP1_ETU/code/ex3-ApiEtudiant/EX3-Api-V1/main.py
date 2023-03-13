import os
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class Etudiant(BaseModel):
	mail: str
	mdp: str
	adresse: str
	insee: int

class Ville(BaseModel):
	commune: str
	cp: str
	dept: str
	insee: int

def connexionBDD():
	conn = sqlite3.connect('./bdd/IUT.sqlite', check_same_thread=False)
	conn.row_factory = sqlite3.Row
	return conn

def requeteBDD(sql:str, single:bool = False, *args):
	retour = None
	with connexionBDD() as conn:
		cur = conn.cursor()
		if not single:
			retour = cur.execute(sql, args).fetchall()
		else:
			retour = cur.execute(sql, args).fetchone()
	return retour

@app.get("/etudiants")
def get_etuds():
	sql = "select mail,mdp,adresse, commune, cp from etudiants inner join villes on villes.insee = etudiants.insee;"
	return requeteBDD(sql)

@app.post('/etudiants')
def create_etud(etudiant: Etudiant):
	with connexionBDD() as conn:
		cur = conn.cursor()
		cur.execute('insert into etudiants VALUES(?,?,?,?);', (etudiant.mail, etudiant.mdp, etudiant.adresse, etudiant.insee))
	
	return etudiant

@app.delete('/etudiants/{mail:str}')
def delete_etud(mail:str):
	retour = None
	with connexionBDD() as conn:
		cur = conn.cursor()

		retour = cur.execute('delete from etudiants where mail=?', (mail,))

	return {"message": "L'étudiant a bien été supprimé"}

@app.put('/etudiants/{mail:str}')
def modify_etud(mail:str, etudiant: Etudiant):
	with connexionBDD() as conn:
		cur = conn.cursor()
		sql = """update etudiants
		set mail = ?, mdp = ?, adresse = ?, insee = ?
		where mail = ?
		"""
		cur.execute(sql, (etudiant.mail, etudiant.mdp , etudiant.adresse, etudiant.insee, mail))
	return etudiant
