# File Server Protocol

## Tujuan
Melayani client dalam request file server.

## Aturan Protokol
- Client mengirim request dalam format string: `REQUEST PARAMETER`.
- Hasil diberikan dalam JSON dan diakhiri dengan `"\r\n\r\n"`.

## Request yang Dilayani
### LIST
- **Tujuan:** Mendapatkan daftar file.
- **Parameter:** Tidak ada.
- **Hasil:**
  - **Berhasil:** `status: OK`, `data: list file`
  - **Gagal:** `status: ERROR`, `data: pesan kesalahan`

### GET
- **Tujuan:** Mendapatkan isi file.
- **Parameter:** `nama file`
- **Hasil:**
  - **Berhasil:** `status: OK`, `data_namafile: nama file`, `data_file: isi file (base64)`
  - **Gagal:** `status: ERROR`, `data: pesan kesalahan`

### UPLOAD
- **Tujuan:** Mengunggah file.
- **Parameter:** `nama file`, `isi file (base64)`
- **Hasil:**
  - **Berhasil:** `status: OK`, `data: pesan sukses`
  - **Gagal:** `status: ERROR`, `data: pesan kesalahan`

### DELETE
- **Tujuan:** Menghapus file.
- **Parameter:** `nama file`
- **Hasil:**
  - **Berhasil:** `status: OK`, `data: pesan sukses`
  - **Gagal:** `status: ERROR`, `data: pesan kesalahan`

## Implementasi

### File Server (file_server.py)
Server menerima koneksi dan memproses request dari client.

### File Protocol (file_protocol.py)
Memproses string request dan memanggil fungsi di `FileInterface`.

### File Interface (file_interface.py)
Mengimplementasikan fungsi `list`, `get`, `upload`, dan `delete` untuk mengelola file di server.

### File Client CLI (file_client_cli.py)
Mengirim request ke server dan menampilkan hasilnya.

## Contoh Penggunaan
1. Menjalankan server:
    ```bash
    python file_server.py
    ```
2. Menjalankan client:
    ```bash
    python file_client_cli.py
    ```

3. Menggunakan fungsi di client:
    ```python
    remote_list()
    remote_get('donalbebek.jpg')
    remote_upload('newfile.txt')
    remote_delete('newfile.txt')
    ```

## Screenshot
### Upload File
![image](https://github.com/AryasatyaWiryawan/tugas4-progjar/assets/17810264/e9df250c-1d44-4b99-923b-e8f3e49a10e5)

### Delete File
![image](https://github.com/AryasatyaWiryawan/tugas4-progjar/assets/17810264/8181b315-8efb-4b2a-a2a0-c19e7fb5a90d)

### Server
![image](https://github.com/AryasatyaWiryawan/tugas4-progjar/assets/17810264/b52e9b65-8cf7-48e9-9528-9933651cde2c)
