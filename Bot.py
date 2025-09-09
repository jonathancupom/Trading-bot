import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuração
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot de Trading Ativo!")

async def iniciar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Estratégia iniciada!")

def main():
    app = Application.builder().token("SEU_TOKEN_AQUI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("iniciar", iniciar))
    app.run_polling()

if __name__ == '__main__':
    main()
