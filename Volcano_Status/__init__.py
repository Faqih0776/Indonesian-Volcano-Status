import requests
from bs4 import BeautifulSoup


def ekstraksi_data():

    try:
        content = requests.get('https://vsi.esdm.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        hasil = soup.find('table', {'class': 'gunung-api'})
        inilah = hasil.findChildren('tr')
        i = 0
        g_Semeru = None
        g_Merapi = None
        g_Ili_Lewotolok = None
        g_Sinabung = None
        g_Dempo = None
        g_Awu = None
        g_Ile_Werung = None
        g_Sirung = None
        g_Karangetang = None
        g_Soputan = None
        g_Banda_Api = None
        g_Bromo = None
        g_Rinjani = None
        g_Lokon = None
        g_Gamalama = None
        g_Sangeangapi = None
        g_Ibu = None
        g_Gamkonora = None
        g_Anak_Krakatau = None
        g_Marapi = None
        g_Dukono = None
        g_Kerinci = None

        for res in inilah:
            if i == 0:
                g_Semeru = res.text.split()
            elif i == 1:
                g_Merapi = res.text.split()
            elif i == 2:
                g_Ili_Lewotolok = res.text.split()
            elif i == 3:
                g_Sinabung = res.text.split()
            elif i == 4:
                g_Dempo = res.text.split()
            elif i == 5:
                g_Awu = res.text.split()
            elif i == 6:
                g_Ile_Werung = res.text.split()
            elif i == 7:
                g_Sirung = res.text.split()
            elif i == 8:
                g_Karangetang = res.text.split()
            elif i == 9:
                g_Soputan = res.text.split()
            elif i == 10:
                g_Banda_Api = res.text.split()
            elif i == 11:
                g_Bromo = res.text.split()
            elif i == 12:
                g_Rinjani = res.text.split()
            elif i == 13:
                g_Lokon = res.text.split()
            elif i == 14:
                g_Gamalama = res.text.split()
            elif i == 15:
                g_Sangeangapi = res.text.split()
            elif i == 16:
                g_Ibu = res.text.split()
            elif i == 17:
                g_Gamkonora = res.text.split()
            elif i == 18:
                g_Anak_Krakatau = res.text.split()
            elif i == 19:
                g_Marapi = res.text.split()
            elif i == 20:
                g_Dukono = res.text.split()
            elif i == 21:
                g_Kerinci = res.text.split()
            i = i + 1


        hasil = dict()
        hasil['G.Semeru'] = g_Semeru[1]
        hasil['Status_Semeru'] = g_Semeru[2]
        hasil['Tanggal_Semeru'] = g_Semeru[3]
        hasil['G.Merapi'] = g_Merapi[1]
        hasil['Status_Merapi'] = g_Merapi[2]
        hasil['Tanggal_Merapi'] = g_Merapi[3]
        hasil['G.Ili_Lewotolok'] = g_Ili_Lewotolok[1] + g_Ili_Lewotolok[2]
        hasil['Status_Ili_Lewotolok'] = g_Ili_Lewotolok[3]
        hasil['Tanggal_Ili_Lewotolok'] = g_Ili_Lewotolok[4]
        hasil['G.Sinabung'] = g_Sinabung[1]
        hasil['Status_Sinabung'] = g_Sinabung[2]
        hasil['Tanggal_Sinabung'] = g_Sinabung[3]
        hasil['G.Dempo'] = g_Dempo[1]
        hasil['Status_Dempo'] = g_Dempo[2]
        hasil['Tanggal_Dempo'] = g_Dempo[3]
        hasil['G.Awu'] = g_Awu[1]
        hasil['Status_Awu'] = g_Awu[2]
        hasil['Tanggal_Awu'] = g_Awu[3]
        hasil['G.Ile_Werung'] = g_Ile_Werung[1] + g_Ile_Werung[2]
        hasil['Status_Ile_Werung'] = g_Ile_Werung[3]
        hasil['Tanggal_Ile_Werung'] = g_Ile_Werung[4]
        hasil['G.Sirung'] = g_Sirung[1]
        hasil['Status_Sirung'] = g_Sirung[2]
        hasil['Tanggal_Sirung'] = g_Sirung[3]
        hasil['G.Karangetang'] = g_Karangetang[1]
        hasil['Status_Karangetang'] = g_Karangetang[2]
        hasil['Tanggal_Karangetang'] = g_Karangetang[3]
        hasil['G.Soputan'] = g_Soputan[1]
        hasil['Status_Soputan'] = g_Soputan[2]
        hasil['Tanggal_Soputan'] = g_Soputan[3]
        hasil['G.Banda_Api'] = g_Banda_Api[1] + g_Banda_Api[2]
        hasil['Status_Banda_Api'] = g_Banda_Api[3]
        hasil['Tanggal_Banda_Api'] = g_Banda_Api[4]
        hasil['G.Bromo'] = g_Bromo[1]
        hasil['Status_Bromo'] = g_Bromo[2]
        hasil['Tanggal_Bromo'] = g_Bromo[3]
        hasil['G.Rinjani'] = g_Rinjani[1]
        hasil['Status_Rinjani'] = g_Rinjani[2]
        hasil['Tanggal_Rinjani'] = g_Rinjani[3]
        hasil['G.Lokon'] = g_Lokon[1]
        hasil['Status_Lokon'] = g_Lokon[2]
        hasil['Tanggal_Lokon'] = g_Lokon[3]
        hasil['G.Gamalama'] = g_Gamalama[1]
        hasil['Status_Gamalama'] = g_Gamalama[2]
        hasil['Tanggal_Gamalama'] = g_Gamalama[3]
        hasil['G.Sangeangapi'] = g_Sangeangapi[1]
        hasil['Status_Sangeangapi'] = g_Sangeangapi[2]
        hasil['Tanggal_Sangeangapi'] = g_Sangeangapi[3]
        hasil['G.Ibu'] = g_Ibu[1]
        hasil['Status_Ibu'] = g_Ibu[2]
        hasil['Tanggal_Ibu'] = g_Ibu[3]
        hasil['G.Gamkonora'] = g_Gamkonora[1]
        hasil['Status_Gamkonora'] = g_Gamkonora[2]
        hasil['Tanggal_Gamkonora'] = g_Gamkonora[3]
        hasil['G.Anak_Krakatau'] = g_Anak_Krakatau[1] + g_Anak_Krakatau[2]
        hasil['Status_Anak_Krakatau'] = g_Anak_Krakatau[3]
        hasil['Tanggal_Anak_Krakatau'] = g_Anak_Krakatau[4]
        hasil['G.Marapi'] = g_Marapi[1]
        hasil['Status_Marapi'] = g_Marapi[2]
        hasil['Tanggal_Marapi'] = g_Marapi[3]
        hasil['G.Dukono'] = g_Dukono[1]
        hasil['Status_Dukono'] = g_Dukono[2]
        hasil['Tanggal_Dukono'] = g_Dukono[3]
        hasil['G.Kerinci'] = g_Kerinci[1]
        hasil['Status_Kerinci'] = g_Kerinci[2]
        hasil['Tanggal_Kerinci'] = g_Kerinci[3]

        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('tidak bisa menemukan data gunung api terkini')
        return
    print('-----Indonesia Volcano Status-----')
    print("\n")
    print(f"Nama Gunung : {result['G.Semeru']}")
    print(f"Status Gunung : {result['Status_Semeru']}")
    print(f"Tanggal : {result['Tanggal_Semeru']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Merapi']}")
    print(f"Status Gunung : {result['Status_Merapi']}")
    print(f"Tanggal : {result['Tanggal_Merapi']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Ili_Lewotolok']}")
    print(f"Status Gunung : {result['Status_Ili_Lewotolok']}")
    print(f"Tanggal : {result['Tanggal_Ili_Lewotolok']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Sinabung']}")
    print(f"Status Gunung : {result['Status_Sinabung']}")
    print(f"Tanggal : {result['Tanggal_Sinabung']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Dempo']}")
    print(f"Status Gunung : {result['Status_Dempo']}")
    print(f"Tanggal : {result['Tanggal_Dempo']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Awu']}")
    print(f"Status Gunung : {result['Status_Awu']}")
    print(f"Tanggal : {result['Tanggal_Awu']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Ile_Werung']}")
    print(f"Status Gunung : {result['Status_Ile_Werung']}")
    print(f"Tanggal : {result['Tanggal_Ile_Werung']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Sirung']}")
    print(f"Status Gunung : {result['Status_Sirung']}")
    print(f"Tanggal : {result['Tanggal_Sirung']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Karangetang']}")
    print(f"Status Gunung : {result['Status_Karangetang']}")
    print(f"Tanggal : {result['Tanggal_Karangetang']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Soputan']}")
    print(f"Status Gunung : {result['Status_Soputan']}")
    print(f"Tanggal : {result['Tanggal_Soputan']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Banda_Api']}")
    print(f"Status Gunung : {result['Status_Banda_Api']}")
    print(f"Tanggal : {result['Tanggal_Banda_Api']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Bromo']}")
    print(f"Status Gunung : {result['Status_Bromo']}")
    print(f"Tanggal : {result['Tanggal_Bromo']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Rinjani']}")
    print(f"Status Gunung : {result['Status_Rinjani']}")
    print(f"Tanggal : {result['Tanggal_Rinjani']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Lokon']}")
    print(f"Status Gunung : {result['Status_Lokon']}")
    print(f"Tanggal : {result['Tanggal_Lokon']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Gamalama']}")
    print(f"Status Gunung : {result['Status_Gamalama']}")
    print(f"Tanggal : {result['Tanggal_Gamalama']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Sangeangapi']}")
    print(f"Status Gunung : {result['Status_Sangeangapi']}")
    print(f"Tanggal : {result['Tanggal_Sangeangapi']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Ibu']}")
    print(f"Status Gunung : {result['Status_Ibu']}")
    print(f"Tanggal : {result['Tanggal_Ibu']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Gamkonora']}")
    print(f"Status Gunung : {result['Status_Gamkonora']}")
    print(f"Tanggal : {result['Tanggal_Gamkonora']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Anak_Krakatau']}")
    print(f"Status Gunung : {result['Status_Anak_Krakatau']}")
    print(f"Tanggal : {result['Tanggal_Anak_Krakatau']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Marapi']}")
    print(f"Status Gunung : {result['Status_Marapi']}")
    print(f"Tanggal : {result['Tanggal_Marapi']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Dukono']}")
    print(f"Status Gunung : {result['Status_Dukono']}")
    print(f"Tanggal : {result['Tanggal_Dukono']}")
    print("\n")
    print(f"Nama Gunung : {result['G.Kerinci']}")
    print(f"Status Gunung : {result['Status_Kerinci']}")
    print(f"Tanggal : {result['Tanggal_Kerinci']}")
