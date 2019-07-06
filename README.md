# homebridge-turkey
Homebridge kullanarak geliştirdiğim projeyi tüm kaynakları ile paylaşıyorum.
---

# Projenin klonunu direk SD karta yazıp kullanmak için:
# Komut Satırını (CLI) Kullanarak Geri Yükleme
Adım 1. Geri Yüklenecek SD Kartı Takın
Mac'inizdeki SD kart okuyucusuna boş (veya kullanılmış ve boş) bir SD kart yerleştirin.

Adım 2. Geri Yüklenecek SD Kartı Bulun
Terminal'i açın ve SD Kartınızı bulun, numaranın daha önce kullanılmış olandan farklı olabileceğine dikkat edin:
```
diskutil list
```
Adım 3. SD Kartını çıkarın
Terminal'de aşağıdaki komutu girin:
```
diskutil unmountDisk /dev/disk2
```
Adım 3. SD Kartını formatlayın
SD Kartınızı tanımladığınızda, benim durumumda / dev / disk2 , FAT16 olarak biçimlendirmek için aşağıdaki komutu girin . Durumunuz için gerekli olanı değiştirin:
```
sudo newfs_msdos -F 16 /dev/disk2
```
- SD Kartı Terminalden Biçimlendirme
Adım 4. Klonlanmış Disk Görüntüsünden Geri Yükleme
Daha önce klonladığınız dmg disk görüntüsünü bulun. Örneğim, dmg'nin Masaüstünde olduğunu varsayar. Terminal'de, benim örneğimde / dev / disk2 olan doğru hedef diski tanımladığınızdan emin olmak için aşağıdaki komutu girin .
```
sudo dd if=~/Desktop/raspberrypi.dmg of=/dev/disk2
```
- İpucu: Disk görüntüsünün SD Karta geri yüklenmesinin biraz zaman alabileceğini unutmayın. Muhtemelen düşündüğünden çok daha uzun. Mac mini Core i5'im 8GB SDXC kartına geri yüklemek için 3 saat 27 dakika sürdü.

# Sistem hazırlığı
Güncelleme ve yükseltme yapma:
```
sudo apt-get update
sudo apt-get upgrade
```
Sürüm aşağıda gösterildiği (veya üstü) gibi olmalıdır:
```
$ g++-4.9 -v
...
gcc version 4.9.2 (Raspbian 4.9.2-10)
```
Başka bir dağıtım veya derleyici sürümünüz varsa, güncellemeniz gerekir:
```
$ sudo apt-get install g++
```
#NodeJS'yi yükleyin
- 4.0.0 sürümünden başlayarak, NodeJS varsayılan olarak ARM platformunu desteklemeye başladı. Eğer yoksa [Raspberry pi'nin tüm sürümleri için NodeJS](http://raspberry%20pi/)

> homebridge'in Nodejs sürüm 5.10 ile çalışmaya başladığını göz önünde bulundurursak nodeJS zaten kurulu geliyor ama gene de güncellemekte fayda var.
```
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
```
Sürümü kontrol et
```
nodejs -v
```
v6.9.5 veya üstü gözükmesi gerekiyor.

# Sıfırdan Yapmak için Homebridge'i yükleyin
> Bununla ilgili kaynağı orjinal adresinden bulabilirsiniz. [HomeBridge](https://github.com/nfarina/homebridge)
