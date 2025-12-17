from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os


app = FastAPI()

DB = "db/shopping_list.json"
BACKUP = "data/backup_shopping_list.json"

class Create(BaseModel):
    name: str
    num : int


class Item(BaseModel):
    id: int
    name: str
    num : int


def load():

    if os.path.exists(DB) == False:

        if os.path.exists("db") == False:
            os.mkdir("db")

        f = open(DB, "w")
        json.dump([], f)
        f.close()

        return []

    f = open(DB, "r")
    items = json.load(f)
    f.close()

    return items


def save(items):

    if os.path.exists("db") == False:
        os.mkdir("db")


    f = open(DB, "w")
    json.dump(items, f, indent=2)
    f.close()

def new_id_(items):
    new_id = 1

    for item in items:
        if item["id"] >= new_id:
            new_id = item["id"] + 1

    return new_id


@app.get("/items")
def get_items():
    items = load()
    return items


@app.post("/items")
def add_item(item: Create):
    items = load()


    if len(items) == 0:
        new_id = 1
    else:
        last_item = items[len(items) - 1]
        new_id = last_item["id"] + 1

    new_item = {}
    new_item["id"] = new_id
    new_item["name"] = item.name
    new_item["num"] = item.num

    items.append(new_item)
    save(items)

    return new_item

@app.get("/backup")
def get_backup():
    backup = load(BACKUP)
    return backup


@app.post("/backup/save")
def save_backup() :
    items = load(DB)
    save(items, BACKUP)

    result = {
        "message": "Backup saved ",
        "count": len(items)
    }

    return result



