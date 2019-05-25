from cs50 import SQL

db = SQL("sqlite:///hate.db")

def get_coms_count(story):
    coms = db.execute("SELECT COUNT(*) AS com_count FROM comments WHERE post_id=:post_id", post_id = story["id"])
    story["comments"] = coms[0]['com_count']

def get_pages_count(stories_count):
    if stories_count > 10:
        if stories_count % 10 == 0:
            count = int(stories_count / 10)
        else:
            count = int(stories_count // 10 + 1)
    else:
        count = 1

    return count