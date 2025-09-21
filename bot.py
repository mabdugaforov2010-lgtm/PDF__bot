import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Bot tokenini Render environment variables dan olish (TO'G'RI)
TOKEN = os.getenv("https://api.render.com/deploy/srv-d37de39r0fns739dsbdg?key=qFruPHUQKuo")

# --- Menyular ---
main_menu = [
    ["📚  Informatika Darsliklar PDF (5-11 sinf)"],
    ["📚 Huquq Darsliklar PDF (8-11 sinf)"],
    ["📚 Biologiya Darsliklar PDF (7-11 sinf)"],
    ["📚 Matematika (Algebra) Darsliklar PDF (5-11 sinf)"]
]

back_button = [["🔙 Ortga"]]

Informatika_PDF = [[f"📚 Informatika Darsliklar PDF {i}-sinf"] for i in range(5, 10)]
Informatika_PDF.append(["📚 Informatika Darsliklar PDF 10-11-sinf"])
Huquq_PDF = [[f"📚 Huquq Darsliklar PDF {i}-sinf"] for i in range(8, 12)]
Biologiya_PDF = [[f"📚 Biologiya Darsliklar PDF {i}-sinf"] for i in range(7, 12)]
Matematika_PDF = [[f"📚 Matematika (Algebra) Darsliklar PDF {i}-sinf"] for i in range(5, 12)]

# --- /start komandasi ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Assalomu alaykum! Botimizga xush kelibsiz. Marhamat, menyudan tanlang:",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

# --- Xabarlarni qayta ishlash ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚  Informatika Darsliklar PDF (5-11 sinf)":
        await update.message.reply_text("📘 Qaysi sinf kerak?", reply_markup=ReplyKeyboardMarkup(Informatika_PDF + back_button, resize_keyboard=True))

    elif text == "📚 Huquq Darsliklar PDF (8-11 sinf)":
        await update.message.reply_text("📘 Qaysi sinf kerak?", reply_markup=ReplyKeyboardMarkup(Huquq_PDF + back_button, resize_keyboard=True))

    elif text == "📚 Biologiya Darsliklar PDF (7-11 sinf)":
        await update.message.reply_text("📘 Qaysi sinf kerak?", reply_markup=ReplyKeyboardMarkup(Biologiya_PDF + back_button, resize_keyboard=True))

    elif text == "📚 Matematika (Algebra) Darsliklar PDF (5-11 sinf)":
        await update.message.reply_text("📘 Qaysi sinf kerak?", reply_markup=ReplyKeyboardMarkup(Matematika_PDF + back_button, resize_keyboard=True))

    elif text == "🔙 Ortga":
        await update.message.reply_text("🏠 Asosiy menyu:", reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))

    else:
        await update.message.reply_text("❌ Bu bo'lim hali tayyor emas.")

# --- Botni ishga tushirish ---
if __name__ == "__main__":
    # Diagnostika: token bor/yo'qligini ko'rsatadi (TOKEN ni toʻliq yozmaydi)
    print("TOKEN mavjud:", bool(TOKEN))
    if TOKEN:
        print("TOKEN (masked):", TOKEN[:6] + "..." )
    else:
        print("❌ TOKEN topilmadi! Iltimos, Render.com Environment Variables ga TOKEN qo'shing.")

    if not TOKEN:
        # token yo'q bo'lsa, chiqamiz
        raise SystemExit(1)

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot ishga tushdi...")
    app.run_polling()
