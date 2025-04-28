# 📧 Otomatik Mail Gönderme Botu

Staj başvurularında birden fazla firmaya mail atman gerekiyorsa bu proje sana çok yardımcı olacak. Bu Python projesi, birden fazla alıcıya ***otomatik olarak e-posta göndermek*** için geliştirilmiştir.  
Gönderim sırasında **konsolda** her mailin sırası ve hangi adrese gönderildiği görüntülenir.

## 🚀 Özellikler
- Belirli bir alıcı listesine seri şekilde mail gönderir.
- Her mailin içeriği **aynıdır**, değişmez.
- Konsolda **sıralı ve açıklamalı çıktı** verir.
- Gmail SMTP sunucusu kullanılarak güvenli bağlantı kurulur.

## 🛠 Gereksinimler
- Python 3.6 veya üzeri
- `smtplib` (Python'da hazır geliyor)
- `email.message` (Python'da hazır geliyor)

## 🔑 Gmail Ayarları

Eğer Gmail kullanıyorsanız:
- 2 Adımlı Doğrulama'yı açın.
- [Google Uygulama Şifresi](https://support.google.com/accounts/answer/185833) oluşturun.
- Kendi mail adresiniz ve uygulama şifrenizle giriş yapın.

## 📜 Kullanım

`main.py` dosyasındaki ayarları doldurun:

```python
gonderen = 'seninmailin@gmail.com'
sifre = 'uygulama_sifren'

alici_listesi = [
    'ornek1@example.com',
    'ornek2@example.com',
    'ornek3@example.com'
]

konu = 'Staj Başvurusu'
icerik = """
    bla bla bla bla bla bla bla bla
"""
````
Sonrasında terminalden çalıştırın:
````bash
python main.py
````
Konsolda her gönderilen mail şöyle görüntülenecek:
````bash
1. Mail gönderildi: ornek1@example.com
2. Mail gönderildi: ornek2@example.com
3. Mail gönderildi: ornek3@example.com
````
✅ Mail içeriğinde sıralama bilgisi bulunmaz, sadece ekranda görünür.

