# Homebridge ile priz kontrolü
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
```
#!/usr/bin/env python
import RPi.GPIO as GPIO
gpio_pin_number=20
GPIO.setmode(GPIO.BCM) # BCM pin numbering
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.OUT) 
GPIO.output(gpio_pin_number, GPIO.HIGH) 
```
> Burada GPIO pinlerini kullanıyoruz, tetik veriyoruz
