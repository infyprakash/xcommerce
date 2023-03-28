from enum import Enum
from typing import List

class BusinessTypeEnum(str,Enum):
    GROCERY = 'Grocery'
    CLOTHING = 'Clothing'
    ELECTRONICS = 'Electronics'


class DistrictEnum(str, Enum):
    Bhojpur = "Bhojpur"
    Dhankuta = "Dhankuta"
    Ilam = "Ilam"
    Jhapa = "Jhapa"
    Khotang = "Khotang"
    Morang = "Morang"
    Okhaldhunga = "Okhaldhunga"
    Panchthar = "Panchthar"
    Sankhuwasabha = "Sankhuwasabha"
    Solukhumbu = "Solukhumbu"
    Sunsari = "Sunsari"
    Taplejung = "Taplejung"
    Terhathum = "Terhathum"
    Udayapur = "Udayapur"
    Bara = "Bara"
    Dhanusa = "Dhanusa"
    Mahottari = "Mahottari"
    Parsa = "Parsa"
    Rautahat = "Rautahat"
    Saptari = "Saptari"
    Sarlahi = "Sarlahi"
    Siraha = "Siraha"
    Bhaktapur_District = "Bhaktapur District"
    Chitwan = "Chitwan"
    Dhading = "Dhading"
    Dolakha = "Dolakha"
    Kathmandu = "Kathmandu"
    Kavrepalanchok = "Kavrepalanchok"
    Lalitpur = "Lalitpur"
    Makawanpur = "Makawanpur"
    Nuwakot_District = "Nuwakot District"
    Ramechhap = "Ramechhap"
    Rasuwa = "Rasuwa"
    Sindhuli = "Sindhuli"
    Sindhupalchok = "Sindhupalchok"
    Baglung = "Baglung"
    Gorkha = "Gorkha"
    Kaski = "Kaski"
    Lamjung = "Lamjung"
    Manang = "Manang"
    Mustang = "Mustang"
    Myagdi = "Myagdi"
    Nawalpur = "Nawalpur"
    Parbat = "Parbat"
    Syangja = "Syangja"
    Tanahu_District = "Tanahu District"
    Arghakhanchi = "Arghakhanchi"
    Banke = "Banke"
    Bardiya = "Bardiya"
    Dang = "Dang"
    Gulmi = "Gulmi"
    Kapilvastu = "Kapilvastu"
    Parasi = "Parasi"
    Palpa = "Palpa"
    Pyuthan = "Pyuthan"
    Rolpa = "Rolpa"
    Rukum = "Rukum"
    Rupandehi = "Rupandehi"
    Dailekh_District = "Dailekh District"
    Dolpa_District = "Dolpa District"
    Humla_District = "Humla District"
    Jajarkot_District = "Jajarkot District"
    Jumla_District = "Jumla District"
    Kalikot_District = "Kalikot District"
    Mugu_District = "Mugu District"
    Rukum_Paschim_District = "Rukum Paschim District"
    Salyan_District = "Salyan District"
    Surkhet_District = "Surkhet District"
    Achham = "Achham"
    Baitadi = "Baitadi"
    Bajhang = "Bajhang"
    Bajura = "Bajura"
    Dadeldhura = "Dadeldhura"
    Darchula = "Darchula"
    Doti = "Doti"
    Kailali = "Kailali"
    Kanchanpur = "Kanchanpur"

class ProvinceEnum(str,Enum):
    Province1 = 'Province1'
    Madhesh_pradesh = 'Madhesh_pradesh'
    Bagmati_pradesh = 'Bagmati_pradesh'
    Gandaki_Pradesh = 'Gandaki_Pradesh'
    Lumbini_pradesh = 'Lumbini_pradesh'
    Karnali_pradesh = 'Karnali_pradesh'
    Sudurpaschim_pradesh = 'Sudurpaschim_pradesh'


class ProvinceDistrictEnum(str, Enum):
    Province1: List[DistrictEnum] = [
        DistrictEnum.Bhojpur,
        DistrictEnum.Dhankuta,
        DistrictEnum.Ilam,
        DistrictEnum.Jhapa,
        DistrictEnum.Khotang,
        DistrictEnum.Morang,
        DistrictEnum.Okhaldhunga,
        DistrictEnum.Panchthar,
        DistrictEnum.Sankhuwasabha,
        DistrictEnum.Solukhumbu,
        DistrictEnum.Sunsari,
        DistrictEnum.Taplejung,
        DistrictEnum.Terhathum,
        DistrictEnum.Udayapur,
    ]
    Madhesh_pradesh: List[DistrictEnum] = [
        DistrictEnum.Bara,
        DistrictEnum.Dhanusa,
        DistrictEnum.Mahottari,
        DistrictEnum.Parsa,
        DistrictEnum.Rautahat,
        DistrictEnum.Saptari,
        DistrictEnum.Sarlahi,
        DistrictEnum.Siraha,
    ]
    Bagmati_pradesh: List[DistrictEnum] = [
        DistrictEnum.Bhaktapur_District,
        DistrictEnum.Chitwan,
        DistrictEnum.Dhading,
        DistrictEnum.Dolakha,
        DistrictEnum.Kathmandu,
        DistrictEnum.Kavrepalanchok,
        DistrictEnum.Lalitpur,
        DistrictEnum.Makawanpur,
        DistrictEnum.Nuwakot_District,
        DistrictEnum.Ramechhap,
        DistrictEnum.Rasuwa,
        DistrictEnum.Sindhuli,
        DistrictEnum.Sindhupalchok,
    ]
    Gandaki_Pradesh: List[DistrictEnum] = [
        DistrictEnum.Baglung,
        DistrictEnum.Gorkha,
        DistrictEnum.Kaski,
        DistrictEnum.Lamjung,
        DistrictEnum.Manang,
        DistrictEnum.Mustang,
        DistrictEnum.Myagdi,
        DistrictEnum.Nawalpur,
        DistrictEnum.Parbat,
        DistrictEnum.Syangja,
        DistrictEnum.Tanahu_District,
    ]
    Lumbini_pradesh: List[DistrictEnum] = [
        DistrictEnum.Arghakhanchi,
        DistrictEnum.Banke,
        DistrictEnum.Bardiya,
        DistrictEnum.Dang,
        DistrictEnum.Gulmi,
        DistrictEnum.Kapilvastu,
        DistrictEnum.Parasi,
        DistrictEnum.Palpa,
        DistrictEnum.Pyuthan,
        DistrictEnum.Rolpa,
        DistrictEnum.Rukum,
        DistrictEnum.Rupandehi,
    ]
    Karnali_pradesh: List[DistrictEnum] = [
        DistrictEnum.Dailekh_District,
        DistrictEnum.Dolpa_District,
        DistrictEnum.Humla_District,
        DistrictEnum.Jajarkot_District,
        DistrictEnum.Jumla_District,
        DistrictEnum.Kalikot_District,
        DistrictEnum.Mugu_District,
        DistrictEnum.Rukum_Paschim_District,
        DistrictEnum.Salyan_District,
        DistrictEnum.Surkhet_District,
    ]
    Sudurpaschim_pradesh: List[DistrictEnum] = [
        DistrictEnum.Achham,
        DistrictEnum.Baitadi,
        DistrictEnum.Bajhang,
        DistrictEnum.Bajura,
        DistrictEnum.Dadeldhura,
        DistrictEnum.Darchula,
        DistrictEnum.Doti,
        DistrictEnum.Kailali,
        DistrictEnum.Kanchanpur,
    ]