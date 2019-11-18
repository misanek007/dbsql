import mysql.connector
import re

def transformNonAscii(s):
    result = re.sub("Đ", "D", s)
    result = re.sub("đ", "d", result)
    result = re.sub("ć", "c", result)
    result = re.sub("ä", "a", result)
    result = re.sub("ó", "o", result)
    result = re.sub("Ó", "O", result)
    result = re.sub("ż", "z", result)
    result = re.sub("ń", "n", result)
    result = re.sub("ö", "o", result)
    result = re.sub("ł", "l", result)
    result = re.sub("Ç", "C", result)
    result = re.sub("ü", "u", result)
    result = re.sub("ğ", "g", result)
    result = re.sub("ş", "s", result)
    result = re.sub("é", "e", result)
    result = re.sub("é", "e", result)
    result = re.sub("ǎ", "a", result)
    result = re.sub("š", "s", result)
    result = re.sub("č", "c", result)
    result = re.sub("Č", "C", result)
    result = re.sub("ě", "e", result)
    result = re.sub("ø", "o", result)
    result = re.sub("å", "a", result)
    result = re.sub("á", "a", result)
    result = re.sub("í", "i", result)
    result = re.sub("ř", "r", result)
    result = re.sub("ň", "n", result)
    result = re.sub("ą", "a", result)
    result = re.sub("ę", "e", result)
    result = re.sub("ę", "e", result)
    result = re.sub("ă", "a", result)
    result = re.sub("ș", "s", result)
    result = re.sub("ő", "o", result)
    result = re.sub("ś", "o", result)
    result = re.sub("ț", "t", result)
    result = re.sub("ţ", "t", result)
    result = re.sub("Ș", "S", result)
    result = re.sub("ā", "a", result)
    result = re.sub("Ö", "O", result)
    result = re.sub("Ł", "L", result)
    result = re.sub("Ψ", "Psi", result)
    result = re.sub("ǧ", "g", result)
    result = re.sub("∴", ":", result)
    result = re.sub("ç", "c", result)
    result = re.sub("İ", "I", result)
    result = re.sub("Ś", "S", result)
    result = re.sub("Ż", "Z", result)
    result = re.sub("Δ", "Delta", result)
    result = re.sub("Σ", "Sigma", result)
    result = re.sub("Π", "Pi", result)
    result = re.sub("Ω", "Omega", result)
    result = re.sub("Η", "H", result)
    result = re.sub("Ş", "S", result)
    result = re.sub("â", "a", result)
    result = re.sub("Ţ", "T", result)
    result = re.sub("Š", "S", result)
    result = re.sub("Ř", "R", result)
    result = re.sub("ů", "u", result)
    result = re.sub("Μ", "M", result)
    result = re.sub("Ρ", "P", result)
    result = re.sub("Χ", "X", result)
    result = re.sub("ё", "e", result)
    result = re.sub("ū", "u", result)
    result = re.sub("ð", "d", result)
    result = re.sub("ō", "o", result)
    result = re.sub("ı", "i", result)
    return result

def member_exceptions(members_in):
    members = re.sub("ⷚ", "Øyvind Sundli", members_in)
    members = re.sub("Варфоломей", "Barfolomey", members)
    members = re.sub("Яęѵ", "Rev", members)
    members = re.sub("Палач", "Palach", members)
    members = re.sub("Ворон", "Voron", members)
    return members

def band_exceptions(band_name_in):
    band_name = band_name_in
    band_name = re.sub("身殺", "Misogi", band_name_in)
    band_name = re.sub("Эпидемия", "Epidemia", band_name)
    band_name = re.sub("Мастер", "Master", band_name)
    band_name = re.sub("Д.И.В.А.", "D.I.V.A.", band_name)
    band_name = re.sub("Небеса", "Nebesa", band_name)
    band_name = re.sub("Галактика", "Galaktika", band_name)
    band_name = re.sub("Омела", "Omela", band_name)
    band_name = re.sub("Артерия", "Arteriya", band_name)
    band_name = re.sub("Όχεντρα", "Ochentra", band_name)
    band_name = re.sub("Χάος Εγένετο", "Chaos Egeneto", band_name)
    band_name = re.sub("閃靈", "Chthonic", band_name)
    band_name = re.sub("Смута", "Smuta", band_name)
    band_name = re.sub("Росс", "Ross", band_name)
    band_name = re.sub("Кипелов", "Kipelov", band_name)
    band_name = re.sub("Время Гнева", "Vremya Gneva", band_name)
    band_name = re.sub("Илиум", "Ilium", band_name)
    band_name = re.sub("Γέννα από Κώλο", "Genna apo Kulo", band_name)
    band_name = re.sub("Ахат", "Achat", band_name)
    band_name = re.sub("Врата Тьмы", "Vrata Tmy", band_name)
    band_name = re.sub("Коrsика", "Korsika", band_name)
    band_name = re.sub("Вечный Страж", "Vechnyj Strach", band_name)
    band_name = re.sub("Невидь", "Nevid", band_name)
    band_name = re.sub("Путь Солнца", "Put Solnca", band_name)
    band_name = re.sub("Кантор", "Kantor", band_name)
    band_name = re.sub("Паника", "Panika", band_name)
    band_name = re.sub("Аркона", "Arkona", band_name)
    band_name = re.sub("Изморозь", "Izmoroz", band_name)
    band_name = re.sub("Рогатые", "Rogatye", band_name)
    band_name = re.sub("Трупоеды", "Trupoyedy", band_name)
    band_name = re.sub("Абордаж", "Abordaz", band_name)
    band_name = re.sub("Андем", "Andem", band_name)
    band_name = re.sub("Белый Шаман", "Belyj Shaman", band_name)
    band_name = re.sub("Вал'кирия", "Valkiriya", band_name)
    band_name = re.sub("Колизей", "Kolizey", band_name)
    band_name = re.sub("Кувалда", "Kuvalda", band_name)
    band_name = re.sub("Монсальват", "Monsalvat", band_name)
    band_name = re.sub("Рарогъ", "Rarog", band_name)
    band_name = re.sub("Харизма", "Charizma", band_name)
    band_name = re.sub("Ордалион", "Ordalion", band_name)
    band_name = re.sub("Кот-Баюн", "Kot-Bayun", band_name)
    band_name = re.sub("Магия", "Magiya", band_name)
    band_name = re.sub("Полнолуние", "Polnolunie", band_name)
    band_name = re.sub("Коррозия Металла", "Korroziya Metalla", band_name)
    band_name = re.sub("Селеста", "Selesta", band_name)
    band_name = re.sub("Война Осколков", "Vojna Oskolkov", band_name)
    return band_name

db = mysql.connector.connect(
    host='localhost',
    user='misanek',
    passwd='123456',
    database='metal_archives'
)




mycursor = db.cursor()

try:
    mycursor.execute('DROP TABLE bands')
except mysql.connector.errors.ProgrammingError:
    pass

mycursor.execute('CREATE TABLE bands('
                 'band_id INT PRIMARY KEY AUTO_INCREMENT, '
                 'band_name VARCHAR(100), '
                 'num_members SMALLINT UNSIGNED, '
                 'mem_1 VARCHAR(100),'
                 'mem_2 VARCHAR(100),'
                 'mem_3 VARCHAR(100),'
                 'mem_4 VARCHAR(100),'
                 'mem_5 VARCHAR(100),'
                 'mem_6 VARCHAR(100))')


mycursor.execute("DESCRIBE bands")

for x in mycursor:
    print(x)



infile = open("/home/misanek/PycharmProjects/dbsql/bands.txt", "r")
lines = infile.read().splitlines()
begin = 0
end = 10000
line_num = begin
for line in lines:
    line_num += 1
    band_name = re.sub(", members:.*", "", line)
    band_name = re.sub("band: ", "", band_name)
    band_name = band_exceptions(band_name)
    band_name = transformNonAscii(band_name)
    mem_list = []
    members = re.sub(".*members: ", "", line)
    members = re.sub(",\s+,", ",", members)
    members = re.sub(",\s+$", "", members)
    members = member_exceptions(members)
    members = transformNonAscii(members)
    mem_list = members.split(", ")
    num_members = len(mem_list)
    inserting_columns = "band_name, num_members"
    inserting_values = "\"" + band_name + "\"" + ", " + str(num_members)
    for i in range(0, num_members):
        if i >= 6:
            break
        else:
            inserting_columns = inserting_columns + ", mem_" + str(i+1)
            inserting_values = inserting_values + ", " + "'" + mem_list[i] + "'"
    #print(inserting_columns)
    #print(inserting_values)
    insert_stmt = "INSERT INTO bands (" + inserting_columns + ") VALUES (" + inserting_values + ") "
    #print(insert_stmt)
    try:
        mycursor.execute(insert_stmt)
    except mysql.connector.errors.DatabaseError:
        print(transformNonAscii(line))
        print(ascii(transformNonAscii(line)))


mycursor.execute("SELECT * FROM bands")

for x in mycursor:
    pass
    print(x)

db.commit()