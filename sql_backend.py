#SQL Database
#Import required dependencies
from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import text
from main import *

#Function to get CloudSQL instance password from Secret Manager
def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})
    # Print the secret payload.
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    return payload

#Function call to get DB password ino a local varaiable
db_password = access_secret_version('vernal-landing-411806', 'campus-crunch','1')


#initialize Connector object
connector = Connector()

#function to return the database connection
def getconn():
    conn= connector.connect(
        "vernal-landing-411806:us-east1:campus-crunch",
        "pymysql",
        user="root",
        password=db_password,
        db="userData"
    )
    return conn
#create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
with pool.connect() as db_conn:
    # Create Table
    #db_conn.execute(text("CREATE TABLE IF NOT EXISTS userInfo(email text,dietaryRestrictions text,likedFoods text,dislikedFoods text,weight integer,dietGoals text)"))

    #print("Done")

    #db_conn.execute(text("INSERT INTO userInfo VALUES ('lolol@gmail.com', 'diet_restrict', 'like', 'dislike', 50, 'mi gola')"))

    result = db_conn.execute(text("SELECT * FROM userInfo;")).fetchall()

    for row in result:
        print(row)
db_conn = pool.connect()
weight = 0
dietGoals = ""
dietaryRestrictions = ""
likedFoods = ""
dislikedFoods = ""
dietaryPreferences = ""
sex = ""
age = 0
height = 0
activeness = ""
user_info = []
def onLogin(email):

    result = db_conn.execute(text("SELECT * FROM userInfo;")).fetchone()
    global user_info
    user_info = result
    weight = getWeight(email)
    dietGoals = getDietGoals(email)
    dietaryRestrictions = getDietaryRestrictions(email)
    likedFoods = getLikedFoods(email)
    dislikedFoods = getDislikedFoods(email)
    dietaryPreferences = getDietaryPreferences(email)
    sex = getSex(email)
    age = getAge(email)
    height = getHeight(email)
    activeness = getActiveness(email)
    return [weight, dietGoals, dietaryRestrictions, likedFoods, dislikedFoods, dietaryPreferences, sex, age, height, activeness]

def getWeight(email):
    return user_info[4]
def getDietGoals(email):
    return user_info[5]
def getDietaryRestrictions(email):
    return user_info[1]
def getDietaryPreferences(email):
    return user_info[6]
def getLikedFoods(email):
    return user_info[2]
def getDislikedFoods(email):
    return user_info[3]
def getSex(email):
    return user_info[7]
def getAge(email):
    return user_info[8]
def getHeight(email):
    return user_info[9]
def getActiveness(email):
    return user_info[10]
def setSex(email, sex):
    db_conn.execute(text(f"UPDATE userInfo SET weight = {weight} WHERE email = '{email}'"))
    db_conn.commit()
def setAge(email, age):
    db_conn.execute(text(f"UPDATE userInfo SET weight = {weight} WHERE email = '{email}'"))
    db_conn.commit()
def setHeight(email, height):
    db_conn.execute(text(f"UPDATE userInfo SET weight = {weight} WHERE email = '{email}'"))
    db_conn.commit()
def setActiveness(email, activeness):
    db_conn.execute(text(f"UPDATE userInfo SET weight = {weight} WHERE email = '{email}'"))
    db_conn.commit()
def setWeight(email, weight):
    db_conn.execute(text(f"UPDATE userInfo SET weight = {weight} WHERE email = '{email}'"))
    db_conn.commit()
def setDietGoals(email, goal):
    db_conn.execute(text(f"UPDATE userInfo SET dietGoals = '{goal}' WHERE email = '{email}'"))
    db_conn.commit()
def addDietaryRestrictions(email, restriction):
    db_conn.execute(text(f"UPDATE userInfo SET dietaryRestrictions = '{restriction}' WHERE email = '{email}'"))
    db_conn.commit()
def addToLikedFoods(email, food):
    db_conn.execute(text(f"UPDATE userInfo SET likedFoods = '{food}' WHERE email = '{email}'"))
    db_conn.commit()
def addToDislikedFoods(email, food):
    db_conn.execute(text(f"UPDATE userInfo SET dislikedFoods = '{food}' WHERE email = '{email}'"))
    db_conn.commit()
def addDietaryPreferences(email, food):
    db_conn.execute(text(f"UPDATE userInfo SET dietaryPreferences = '{food}' WHERE email = '{email}'"))
    db_conn.commit()
def addUser(email, dietaryRestrictions, likedFoods, dislikedFoods, weight, dietGoals, dietaryPreferences, sex, age, height, activeness):
    db_conn.execute(text(f"INSERT INTO userInfo VALUES ('{email}', '{dietaryRestrictions}', '{likedFoods}', '{dislikedFoods}', {weight}, '{dietGoals}', '{dietaryPreferences}', '{sex}', {age}, {height}, '{activeness}')"))
    db_conn.commit()
