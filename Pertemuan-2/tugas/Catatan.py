#1) List
#Digunakan untuk menyimpan berbagai macam nilai dan tipe nilai di dalam satu variabel, Contoh :

thislist = ["apple", "banana", "cherry"]
print(thislist)

#List itu sesuai urutan,isinya bisa diubah dan kita dapat memasukkan nilai yang sama terus menerus, contoh :

thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)

#2) Tuple
#TUple digunakan untuk menyimpan berbagai macam tipe data yang sesuai urutan, namun nilai nya tidak dapat diubah,mampu menampung berbagai tipe data, contoh :

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#3) Set
#Digunakan untuk menampung tipe data yang tidak berurutan,tidak bisa diubah,tidak berindeks dan tidak mendukung nilai serupa, contoh :

thisset = {"apple", "banana", "cherry"}
print(thisset)

#4) Dictionaries
#Digunakan untuk menyimpan tipe data yang berurutan,dapat diubah,namun tidak mendukung nilai serupa dan memiliki kata kunci untuk setiap nilai, Contoh :

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List       : is a collection which is ordered and changeable. Allows duplicate members. using []
#Tuple      : is a collection which is ordered and unchangeable. Allows duplicate members. using ()
#Set        : is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. {}
#Dictionary : is a collection which is ordered and changeable. No duplicate members. using {}