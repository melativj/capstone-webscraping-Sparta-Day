# capstone-webscraping-Sparta-Day
capstone webscraping Sparta Day - Melativj


# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan simple webscrapping untuk mendapatkan informasi. Untuk step by step guide, dipersilahkan untuk membuka git dari t3981-h [Click here](https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Webscrapping with Beautiful Soup"). Kita juga akan memanfaatkan flask dashboard sederhana untuk menampilkan hasil scrap dan visualisasi kita.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

Atau cukup menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

## What You Need to Do

* Silahkan mencoba melakukan scraping soal di bawah menggunakan `beautiful soup` di notebook terlebih dahulu.
* Clone repo ini.
* Silahkan buka notebook template pada capstone ini dan isi sesuai dengan arahan yang ada. Pastikan memberikan analisa yang dibutuhkan pada notebook tersebut.
* File di repo ini adalah skeleton yang dapat digunakan untuk membuat flask dashboard sederhana.
* Silahkan isi di bagian yang masih kosong.
* Isi fungsi `scrap` dengan proses scraping yang sudah lakukan di notebook. 

```python
table = soup.find(___)
tr = table.find_all(___)
```

* Isi bagian ini untuk menyimpan hasil scrap yang dibuat menjadi sebuah dataframe.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* Terakhir gunakan fungsi `scrap` dengan cara mengisi bagian berikut dengan link web yang akan di scrap.

```python
df = scrap(___) #insert url here
```

