from kaggle import KaggleApi

def Practica_1():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file('gauthamp10/google-playstore-apps','Google-Playstore.csv')

    from zipfile import ZipFile
    zf = ZipFile('Google-Playstore.csv.zip')
    zf.extractall()
    zf.close()

Practica_1()