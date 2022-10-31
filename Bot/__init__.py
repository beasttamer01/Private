import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5518670370:AAHY8uARcJJe6pwEj5zkD9EFb8h_sKvttO0') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 16668169)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', '73f207e5b336836d4ffa9e1a2a7dde67')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 1636310615))
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://SoloLevling7seven:solo7@cluster0.4nolwkk.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1001622852308)
BOT_NAME = os.environ.get('BOT_NAME', 'erika7701')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
