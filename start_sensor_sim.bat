@echo off
REM Proje dizinine geç
cd /d C:\Users\saban.kus\projects\digital-twin

REM Sanal ortamı aktive et (Windows .bat aktivasyonu)
call venv\Scripts\activate.bat

REM Sensör simülasyonunu başlat ve log’u bir dosyaya yaz
python sensor_sim.py >> sensor_sim.log 2>&1
