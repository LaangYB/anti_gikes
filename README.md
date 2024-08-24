ANTI GIKES KATANYA
ini modul dari bot manage (blacklist word filter), dengan sedikit modifikasi.

Tutor VPS step by step
git clone https://github.com/LaangYB/anti_gikes
cd Antigcast
sudo apt install python3.10 -venv
python3 venv antigcast
source antigcast/bin/activate
pip install -r requirements.txt
cp sample.env .env
nano .env (isi vars nya)
bash start
