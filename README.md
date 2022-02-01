# Indonesian-Volcano-Status
The status of Indonesia's volcanoes is above normal
## HOW IT WORK?
This package will scrape from Ministry of Energy and Mineral Resources Indonesia (https://vsi.esdm.go.id) to get latest 
status volcano in indonesia

this package will use BeautifulSoup4 and Request, to produce output in the form of JSON that is ready to be used in web 
or mobile applications

## How To Use
    import Volcano_Status

    if __name__ == '__main__':
    result = Volcano_Status.ekstraksi_data()
    Volcano_Status.tampilkan_data(result)
## AUTHOR

Faqih Fakhruddin