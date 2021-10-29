import re
import sqlite3

'''
my_lis = ['Igazolt COVID-19 fertőzöttek száma megyénként\nÖsszesen: 633 861 fő\nBorsod-Abaúj-Zemplén\n35314\nNógrád\n16346\nSzabolcs-Szatmár-Bereg\n31789\nHeves\n16233\nGyőr-Moson-Sopron Komárom-Esztergom\n36210\n23753\nHajdú-Bihar\n33793\nBudapest\n119681\nPest\n88707\nJász-Nagykun-Szolnok\n18678\nVas\n17999\nVeszprém\n22934\nFejér\n27615\nBékés\nZala\n17002\n13996\nBács-Kiskun\nTolna\n29844\nSomogy\n23298\nCsongrád-Csanád,\n26803\n13822\nBaranya\n20044\nA színezés a lakosságszámhoz viszonyított esetszám szerint változik.\n', 'Igazolt', 'COVID-19', 'fertőzöttek', 'száma', 'megyénként', 'Összesen:', '633', '861', 'fő', 'Borsod-Abaúj-Zemplén', '35314', 'Nógrád', '16346', 'Szabolcs-Szatmár-Bereg', '31789', 'Heves', '16233', 'Győr-Moson-Sopron', 'Komárom-Esztergom', '36210', '23753', 'Hajdú-Bihar', '33793', 'Budapest', '119681', 'Pest', '88707', 'Jász-Nagykun-Szolnok', '18678', 'Vas', '17999', 'Veszprém', '22934', 'Fejér', '27615', 'Békés', 'Zala', '17002', '13996', 'Bács-Kiskun', 'Tolna', '29844', 'Somogy', '23298', 'Csongrád-Csanád,', '26803', '13822', 'Baranya', '20044', 'A', 'színezés', 'a', 'lakosságszámhoz', 'viszonyított', 'esetszám', 'szerint', 'változik.']

# makes string from the data
numbers2 = str(my_lis[0]).replace(' ','')

numbers2 = str(numbers2)

# with Regex only getting the numbers
num = re.findall('[0-9]+', numbers2)

print(len(num))
print(num)

megyek = ['Borsod-Abaúj-Zemplén', 'Nógrád', 'Szabolcs-Szatmár-Bereg', 'Heves', 'Győr-Moson-Sopron', 'Komárom-Esztergom','Hajdú-Bihar','Budapest','Pest','Jász-Nagykun-Szolnok','Vas','Veszprém','Fejér', 'Békés', 'Zala','Bács-Kiskun', 'Somogy', 'Csongrád-Csanád', 'Tolna','Baranya']
print(len(megyek))
print(len(num))
print(megyek)
print(num[2:])
num_2 = num[2:]

for i in range(20):
    print(megyek[i])
    print(num_2[i])
'''

num_2_int=['time','source','35314', '16346', '31789', '16233', '36210', '23753', '33793', '119681', '88707', '18678', '17999', '22934', '27615', '17002', '13996', '29844', '23298', '26803', '13822', '20044']

# Connect to SQL


# Create a cursor
conn = sqlite3.connect('covid_geo_88888.db')
print("Succesfully connected to db")

# Create a cursor
c = conn.cursor()



try:
    c.execute("""CREATE TABLE "covid_cases_geo"(
        "pull_date" TEXT,
        "source" TEXT,
        "Borsod-Abaúj-Zemplén" INTEGER,
        "Nógrád" INTEGER,
        "Szabolcs-Szatmár-Bereg" INTEGER,
        "Heves" INTEGER,
        "Győr-Moson-Sopron" INTEGER,
        "Komárom-Esztergom" INTEGER,
        "Hajdú-Bihar" INTEGER,
        "Budapest" INTEGER,
        "Pest" INTEGER,
        "Jász-Nagykun-Szolnok" INTEGER,
        "Vas" INTEGER,
        "Veszprém" INTEGER,
        "Fejér" INTEGER,
        "Békés" INTEGER,
        "Zala" INTEGER,
        "Bács-Kiskun" INTEGER,
        "Somogy" INTEGER,
        "Csongrád-Csanád" INTEGER,
        "Tolna" INTEGER,
        "Baranya" INTEGER

    )""")

except:
    pass

conn.commit()

# Creating tuple from list
ins_data = tuple(num_2_int)

# Insterting record
c.execute("INSERT INTO covid_cases_geo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ins_data)

conn.commit()


conn.close()
