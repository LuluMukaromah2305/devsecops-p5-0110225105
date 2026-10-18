
# Task Manager API

Task Manager API adalah aplikasi REST API sederhana
untuk mengelola daftar tugas menggunakan Python dan Flask.

Aplikasi menyediakan fitur melihat tugas, menambahkan tugas,
dan menghapus tugas. Data disimpan sementara di memori.

## Teknologi yang Digunakan

- Python 3.11
- Flask
- unittest untuk pengujian otomatis
- Bandit untuk Static Application Security Testing (SAST)
- GitHub Actions untuk otomatisasi CI/CD

## Struktur Source Code

- `app.py`: membuat dan menjalankan aplikasi Flask.
- `routes.py`: mengatur endpoint API.
- `services.py`: mengelola data dan logika tugas.
- `validators.py`: memvalidasi input pengguna.
- `tests/test_app.py`: menguji fungsi aplikasi.

## Cara Menjalankan Aplikasi

Pastikan Python sudah terinstal.

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan di Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instal dependensi:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
python app.py
```

Buka alamat berikut di browser:

http://127.0.0.1:5000/

## Endpoint API

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | `/` | Informasi aplikasi |
| GET | `/health` | Memeriksa status aplikasi |
| GET | `/tasks` | Melihat semua tugas |
| POST | `/tasks` | Menambahkan tugas |
| DELETE | `/tasks/<id>` | Menghapus tugas |

Untuk menambahkan tugas, kirim request POST ke `/tasks`
dengan JSON berikut:

```json
{
  "title": "Mengerjakan tugas DevSecOps"
}
```

## Menjalankan Unit Test

Jalankan perintah berikut:

```bash
python -m unittest discover -s tests -v
```

## Overview Pipeline CI/CD

Pipeline dikonfigurasi pada file
`.github/workflows/devsecops.yml`.

Workflow berjalan ketika terjadi push ke branch `main`
atau pull request yang menargetkan branch `main`.

Pipeline memiliki dua job:

1. `build`: menginstal dependensi dan menjalankan unit test.
2. `sast-scan`: menjalankan Bandit untuk memeriksa
   potensi masalah keamanan pada source code Python.

Job `sast-scan` bergantung pada job `build` menggunakan
`needs: build`, sehingga pemindaian dilakukan setelah
job build berhasil.

Hasil eksekusi pipeline dapat dilihat pada tab Actions
di repository GitHub.
