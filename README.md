# Model Gradio UI - Model Evulation

--------------- Açıklama ---------------
# Ortam Oluşturma

Lütfen Python sürümünüzü '3.10' olarak ayarlayın.

Python versiyonunuzdan emin olmak için:

```bash
python --version
```

## Geliştirme Ortamını Ayarlamak
- Virtual environment oluşturunuz.
```bash
    $ python -m venv <venv-name>
```
- Virtual environmentınızı aktive ediniz.
```bash
    $ source <venv-name>/bin/activate
```
- Kütüphaneleri Yükleyiniz.
```bash
    $ pip install -r requirements.txt
```
## Username ve Password Konfigrasyonu
  
  Uzak sunucuya bağlanmak için gerekli username ve parola bilgisini .env isimli bir gizli dosyada tutulmaktadır. 
  ```bash
    $ nano .env
  ```
  ```
    USERNAME=<username>
    PASSWORD=<password>
  ```
  yaz ve kaydet.

# Çalıştırma

Uygulamanın çalışması için gerekli adımlar tamamlanmıştır.

```bash
    $ python app.py
```
