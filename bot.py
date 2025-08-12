from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Ваш личный chat_id (замените на реальный)
MY_CHAT_ID = 397884896  # ⚠️ Замените на ваш chat_id!

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Приветствую! Напишите ваш вопрос')

# Новая функция для получения chat_id
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Ваш chat_id: {chat_id}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_name = update.message.from_user.first_name
    
    # Ответ пользователю
    await update.message.reply_text("Спасибо! Чуть позже ваш вопрос будет опубликован :)")
    
    # Пересылка сообщения вам
    await context.bot.send_message(
        chat_id=MY_CHAT_ID,
        text=f"📨 Новое сообщение от {user_name}:\n\n{user_message}"
    )

# Замените токен на ваш
application = ApplicationBuilder().token("8398551737:AAH_qDn3zb_lxHG-nRXR35LCq-pV6bGQx2E").build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("id", get_id))  # Теперь функция определена
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

application.run_polling()