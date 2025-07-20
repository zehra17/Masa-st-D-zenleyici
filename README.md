# 🧹 Masaüstü Düzenleyici Scripti

Bu Python scripti, çalıştırıldığı klasördeki dosyaları tarayarak, dosya uzantılarına göre otomatik olarak ilgili kategorilere (**Resimler**, **Belgeler**, **Videolar** vb.) ayıran basit ve etkili bir otomasyon aracıdır. Dağınık masaüstlerini veya indirme klasörlerini tek bir komutla düzenlemek için tasarlanmıştır.

---

## ✨ Özellikler

- **Otomatik Sınıflandırma**: Dosyaları uzantılarına göre `Resimler`, `Videolar`, `Belgeler`, `Müzikler`, `Arşivler`, `Kodlar` ve `Uygulamalar` gibi önceden tanımlanmış klasörlere taşır.  
- **Akıllı Klasör Oluşturma**: İlgili kategori klasörü mevcut değilse, script otomatik olarak oluşturur.  
- **Genişletilebilir**: `file_extensions` sözlüğünü düzenleyerek yeni dosya türleri ve kategoriler kolayca eklenebilir.  
- **Güvenli Çalışma**: Script kendi dosyasını taşımaz. Sadece dosyalar üzerinde işlem yapar, klasörlere dokunmaz.  
- **Kullanıcı Dostu**: İşlem tamamlandığında kullanıcıya işlem özeti sunar.

---

## 🛠️ Kullanılan Teknolojiler

Bu proje, Python'un standart kütüphaneleri ile geliştirilmiştir:

- **Python 3**: Projenin ana dili  
- **os**: İşletim sistemiyle etkileşim, dosya yolları, klasör yönetimi  
- **shutil**: Dosyaların güvenli şekilde taşınması

---

## 🚀 Nasıl Kullanılır?

1. Python 3'ün bilgisayarınızda yüklü olduğundan emin olun.  
2. Bu repodan `toparlayici.py` dosyasını indirin.  
3. Script dosyasını düzenlemek istediğiniz klasörün içine yerleştirin (örn. `Masaüstü`, `İndirilenler`).  
4. Terminal veya Komut İstemcisi (CMD) ile o klasöre gidin:

   ```bash
   cd Desktop
