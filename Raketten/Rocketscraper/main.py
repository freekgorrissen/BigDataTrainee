import os

if __name__ == "__main__":
    import scraper      # main loop: haalt informatie van alle raketten op, plaatst deze in python lijst
    import connector    # Database connectie: maakt verbinding, bevat een insert functie


    for r in scraper.raketten:
        connector.insert(r)             # alle raket objecten in db plaatsen
    connector.mydb.commit()             # maakt mutaties in database permanent
    connector.mycursor.close()

    os.system('uvicorn server:app --reload')      # start server op voor endpoints (server.py)
