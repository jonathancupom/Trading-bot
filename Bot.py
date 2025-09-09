import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from keep_alive import keep_alive  # Importa o keep_alive

# Configuração
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Pegar token das variáveis de ambiente
TOKEN = os.environ.get('TOKEN')
if not TOKEN:
    logging.error("❌ TOKEN não encontrado! Configure a variável TOKEN no Heroku.")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot de Trading Ativo! Use /iniciar")

async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Estratégia iniciada!")

async def configurar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(f"✅ Configurado: {context.args[0]}")
    else:
        await update.message.reply_text("📝 Use: /configurar EURUSD")

async def saldo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Saldo: $1000.00")

def main():
    try:
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("iniciar", iniciar))
        app.add_handler(CommandHandler("configurar", configurar))
        app.add_handler(CommandHandler("saldo", saldo))
        
        logging.info("✅ Bot iniciando...")
        keep_alive()  # Mantém o bot vivo
        app.run_polling()
        
    except Exception as e:
        logging.error(f"❌ Erro ao iniciar bot: {e}")

if __name__ == '__main__':
    main()
