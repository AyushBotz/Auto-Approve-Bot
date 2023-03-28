from os import path, getenv

SUDO = "5171347305"

class Config:
    API_ID = int(getenv("API_ID", "12897895"))
    API_HASH = getenv("API_HASH", "66009ef52a2da9cea6a7015e59b556ca")
    BOT_TOKEN = getenv("BOT_TOKEN", "6192626369:AAF1NpZg8035O3qou-8g9P6ssk1tuaLN8o8")
    FSUB = getenv("FSUB", "PiroHackz")
    CHID = int(getenv("CHID", "-1001545900924"))
    SUDO = list(map(int, getenv("SUDO").split("5822067254")))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rishbro:rishbro@cluster0.eiqoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
cfg = Config()
