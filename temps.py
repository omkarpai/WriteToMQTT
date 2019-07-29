import random
import datetime
import uuid



def random_string(string_length):
    random=str(uuid.uuid4())
    random=random.upper()
    random=random.replace("-","")
    return random[0:string_length]



def temps():
  while True:
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #idt = str(random_string(9))

    zid1 = str(random.randint(1,5))
    zid2 = str(random.randint(1,5))
    zid3 = str(random.randint(1,5))
    zid4 = str(random.randint(1,5))
    zid5 = str(random.randint(1,5))

    msg = zid1 + ";" + "b1" + ";" + zid2 + ";" + "b2" + ";" + zid3 + ";" + "b3" + ";" + zid4 + ";" + "b4" + ";" + zid5 + ";" + "b5" + ";" + ts + "\n"

    print(msg)

    return msg

