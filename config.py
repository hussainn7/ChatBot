from dotenv import load_dotenv
import os

# Find .env file with os variables
load_dotenv("dev.env")

# Конфигурация
VA_NAME = 'Jarvis'
VA_VER = "3.0"
VA_ALIAS = ('джарвис','бот')
VA_TBR = ('скажи', 'покажи', 'ответь', 'произнеси', 'расскажи', 'сколько', 'слушай')

# ID микрофона (можете просто менять ID пока при запуске не отобразится нужный)
# -1 это стандартное записывающее устройство
MICROPHONE_INDEX = -1

# Путь к браузеру Google Chrome
CHROME_PATH = 'C:/Program Files(x86)/Microsoft/Edge/Application/msedge %s'

# Токен Picovoice
PICOVOICE_TOKEN = os.getenv('4P1a/VXpX+/QGhn4OoxFWK/hSswkJV9u6+YYKQqdlF+NZOT5GmArbA==')

# Токен OpenAI
OPENAI_TOKEN = os.getenv('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')
