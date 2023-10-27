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
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5408040751:AAGyYeUr0P8YFb01WOWf1G2zkm6FFbjjEt4') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 15682957 )) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH','00b8b3714cee0ba2941091b7cc5578e7')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 2090127712))
MONGO_DB = 'mongodb+srv://nsfwleech:nsfwleech@cluster0.in2msxb.mongodb.net/?retryWrites=true&w=majority'
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1001746042894)
BOT_NAME = os.environ.get('BOT_NAME', 'CompressorPro_bot')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
