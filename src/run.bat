@echo off

echo 🔧 Creating Python virtual environment...
python -m venv venv

echo 🚀 Activating virtual environment and installing dependencies...
call venv\Scripts\activate.bat

python -m pip install --upgrade pip
pip install pyshark wget

echo ✅ Setup complete.

echo 🟢 Starting packet capture and analysis...
python lab7.py

echo ✅ Analysis complete.

echo 🚫 Deactivating virtual environment...
call venv\Scripts\deactivate.bat

pause
