from textblob import TextBlob
a = input("Masukkan kata : ")
print("Kata inputan " + str(a))

b = TextBlob(a)
print("Kata perbaikan :" + str(b.correct()))
