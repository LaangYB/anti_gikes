# Anti Gikes

Anti Gikes adalah modul untuk bot yang berfungsi sebagai filter kata-kata terlarang (blacklist word filter). Modul ini merupakan hasil modifikasi dari bot manage.

## Persiapan VPS (Virtual Private Server) - Langkah demi Langkah

1. **Clone repository**
   ```bash
   git clone https://github.com/LaangYB/anti_gikes
   cd anti_gikes
   sudo apt install python3.10 -y
   python3 -m venv antigikes
   source antigikes/bin/activate
   cp sample.env .env
   nano .env
   bash start

   
### Perbaikan yang dilakukan:
1. **Judul yang Jelas:** Menambahkan judul "Anti Gikes" sebagai pengenalan proyek.
2. **Struktur yang Terorganisir:** Membagi langkah-langkah menjadi bagian yang lebih mudah dipahami.
3. **Konsistensi dalam Penggunaan Nama Direktori:** Menggunakan nama direktori yang konsisten (`anti_gikes`).
4. **Penjelasan yang Lebih Rinci:** Menyertakan penjelasan tentang apa yang harus diisi dalam file `.env`.
5. **Catatan dan Kontribusi:** Menambahkan catatan dan bagian kontribusi untuk membantu pengguna memahami langkah-langkah dan cara berkontribusi.
