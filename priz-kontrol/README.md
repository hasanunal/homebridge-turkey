# Homebridge ile priz kontrolü

[![Watch the video](https://i.ytimg.com/vi/TdzTcXB5iyU/hqdefault.jpg)](https://www.youtube.com/watch?v=TdzTcXB5iyU)


> Dipnot: Bunu yapmak için, iPhone'un Bluetooth özelliği etkin olmalı ve her iki cihazın da aynı WiFi ağında olması gerekir. 
# cmdswitch2 kurulumu
```
sudo npm install -g homebridge-cmdswitch2
```
# homebridge-cmd_light_control
```
sudo npm install -g homebridge-cmd_light_control
```
> Şimdi homebridge yapılandırma dosyasını ayarlamamız ve mevcut cihazlarınızı buna eklememiz gerekiyor.
```
{
"bridge": {
        "name": "HasanUNAL - SmartHome",
        "username": "- - -",
        "port": - - -,
        "pin": "- - -"
    },
 ```
Altına ekleyin:
```
"accessories": [
	{  
	    "accessory": "CMD",
     	    "service": "Light",
	    "brightnessHandling": "no",
            "name": "Lamba",
            "on_cmd": "/home/pi/lamba_ac.py",
            "off_cmd": "/home/pi/lamba_kapat.py",
	    "get_status_cmd": "/home/pi/lamba_durum.py"
	}],
 
"platforms": [{
   "platform": "cmdSwitch2",
   "switches": [{
       "name" : "TV Priz",
       "on_cmd": "/home/pi/priz_ac.py",
       "off_cmd": "/home/pi/priz_kapat.py",
       "state_cmd": "/home/pi/priz_durum.py"
       "manufacturer": "serial (gereksiz, boş bırakılabilir)",
       "model": "serial (gereksiz, boş bırakılabilir)",
       "serial": "serial (gereksiz, boş bırakılabilir)"
   }]
}]
}
```
# Lamba kontrolü (python dosyası)
> 220W ile çalıştığınızı unutmayın, elektrik bilginiz yoksa bu işe hiç kalkışmamanızı tavsiye ederim.

> `priz_ac.py` dosyasını oluşturalım:
```
#!/usr/bin/env python
import RPi.GPIO as GPIO
gpio_pin_number=20
GPIO.setmode(GPIO.BCM) # BCM pin numarasi
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.OUT) 
GPIO.output(gpio_pin_number, GPIO.HIGH) 
```
> Not: Burada GPIO pinlerini kullanıyoruz, tetik veriyoruz.
> `priz_kapat.py` dosyasını oluşturalım:
```
#!/usr/bin/env python
import RPi.GPIO as GPIO
gpio_pin_number=20
GPIO.setmode(GPIO.BCM) # BCM pin numarasi
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.OUT) 
GPIO.output(gpio_pin_number, GPIO.LOW)
```

> `priz_durum.py` dosyasını oluşturalım:
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from subprocess import Popen, PIPE
 
pin_number=20
proc = Popen(
    "echo %s > /sys/class/gpio/export" % pin_number,
    shell=True,
    stdout=PIPE, stderr=PIPE
)
 
proc.wait() 
proc = Popen(
    "cat /sys/class/gpio/gpio%s/value" % pin_number,
    shell=True,
    stdout=PIPE, stderr=PIPE
)
proc.wait()
res = proc.communicate()  # get tuple('stdout', 'stderr')
count = res[0].replace("\n","")
count = int(count)
 
if count == 0:
        id=0
else:
        print('1').replace("\n","")
```
> Burada da tetikten sonraki durumunu görmemizi sağlıyoruz. Prizin son durumunu.

Bir lamba için, kodlar tamamen benzerdir, sadece lamba rölesinin sinyal kablosunu bağladığınız pimi değiştirin. Tüm komut dosyalarını çalıştırılabilir hale getiririz, gerekirse, komut dosyalarının doğru şekilde çalıştırılması için Python kitaplıklarını koyarız.

# Yeniden başlatmak için
```
service homebridge restart
```
> İPhone'a giriyoruz, uygulama evinde - 2 yeni cihaz görünmeli. 
Harika! Röleler kontrollü bir priz (anahtar) ve bir lambanız var artık. 

# Sesli komut ile açmak için
> Hey siri, TV Priz aç!
> Hey siri, lambaları yak!
