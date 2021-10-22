import os

if __name__ == "__main__":
    import scraper
    import connector

    # alle raket objecten in db plaatsen
    for r in scraper.raketten:
        connector.insert(r)
    connector.mydb.commit()
    connector.mycursor.close()

    os.system('uvicorn server:app --reload')
