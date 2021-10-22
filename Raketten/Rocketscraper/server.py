from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return "Your item has number {}".format(item_id)


@app.get("/rockets/{min_mass}")
async def read_item(min_mass: int):
    import mysql.connector
    import json

    # connect to db
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="raketten"
    )

    # SQL SELECT all rockets with mass > minmass
    cur = mydb.cursor()
    cur.execute("SELECT * FROM launch_vehicles WHERE massa > {}".format(min_mass))
    rq = [dict((cur.description[i][0], value)
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    mydb.close()

    # convert sql query result to json
    json_out = json.dumps(rq)
    # return json
    return json_out
