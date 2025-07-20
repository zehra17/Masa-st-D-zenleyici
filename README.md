# 🧹 Masaüstü Düzenleyici Scripti
Bu Python scripti, çalıştırıldığı klasördeki dosyaları tarayarak, dosya uzantılarına göre otomatik olarak ilgili kategorilere (Resimler, Belgeler, Videolar vb.) ayıran basit ve etkili bir otomasyon aracıdır. Dağınık masaüstlerini veya indirme klasörlerini tek bir komutla düzenlemek için tasarlanmıştır.

## ✨ Özellikler
Otomatik Sınıflandırma: Dosyaları uzantılarına göre Resimler, Videolar, Belgeler, Müzikler, Arşivler, Kodlar ve Uygulamalar gibi önceden tanımlanmış klasörlere taşır.

Akıllı Klasör Oluşturma: İlgili kategori klasörü mevcut değilse, script bu klasörü otomatik olarak oluşturur.

Genişletilebilir: Kod içerisindeki file_extensions sözlüğünü düzenleyerek kolayca yeni dosya türleri ve kategoriler ekleyebilirsiniz.

Güvenli Çalışma: Script, kendi dosyasını taşımaz ve sadece dosya olan elemanlar üzerinde işlem yapar, klasörlere dokunmaz.

Kullanıcı Dostu: İşlem bittiğinde, kullanıcıdan bir tuşa basmasını isteyerek konsol penceresinin hemen kapanmasını engeller ve işlem loglarının okunmasına olanak tanır.

## 🛠️ Kullanılan Teknolojiler
Bu proje, Python'un güçlü standart kütüphaneleri kullanılarak geliştirilmiştir:

Python 3: Projenin ana programlama dili.

os Kütüphanesi: İşletim sistemiyle etkileşim kurmak, dosya yollarını yönetmek, klasörleri listelemek ve yeni klasörler oluşturmak için kullanılmıştır.

shutil Kütüphanesi: Yüksek seviyeli dosya işlemleri, özellikle dosyaları bir konumdan diğerine güvenli bir şekilde taşımak (shutil.move) için kullanılmıştır.

## 🚀 Nasıl Kullanılır?
Bu scripti kullanmak için bilgisayarınızda Python 3'ün yüklü olması yeterlidir.

Bu repodan toparlayici.py (veya verdiğiniz herhangi bir isim) dosyasını indirin.

Script dosyasını, düzenlemek istediğiniz klasörün içine kopyalayın. (Örneğin, Masaüstü veya İndirilenler klasörü).

Terminal veya komut istemcisini açarak o klasöre gidin.

## 🤝 Katkıda Bulunma
Bu projeyi daha da geliştirmek için her türlü katkıya açığım!

Bu repoyu fork'layın.

Yeni bir branch oluşturun (git checkout -b yeni-ozellik-ekle).

Değişikliklerinizi yapın ve commit'leyin (git commit -m 'Yeni dosya kategorileri eklendi').

Oluşturduğunuz branch'i push'layın (git push origin yeni-ozellik-ekle).

Bir Pull Request açarak değişikliklerinizi açıklayın.
