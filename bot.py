from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

main_menu = [
    ["📚 Informatika Darsliklar PDF (5-11 sinf)"],
    ["📚 Huquq Darsliklar PDF (8-11 sinf)"],
    ["📚 Biologiya Darsliklar PDF (7-11 sinf)"],
    ["📚 Matematika (Algebra) Darsliklar PDF (5-11 sinf)"]
]

back_button = [["🔙 Ortga"]]

# Informatika uchun maxsus variant
Informatika_PDF = [
    ["📘 Informatika 5-sinf"],
    ["📘 Informatika 6-sinf"],
    ["📘 Informatika 7-sinf"],
    ["📘 Informatika 8-sinf"],
    ["📘 Informatika 9-sinf"],
    ["📘 Informatika 10-11-sinf"]
]

Huquq_PDF = [[f"📘 Huquq {i}-sinf"] for i in range(8, 12)]
Biologiya_PDF = [[f"📘 Biologiya {i}-sinf"] for i in range(7, 12)]
Matematika_PDF = [[f"📘 Matematika {i}-sinf"] for i in range(5, 12)]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Assalomu alaykum! Botimizga xush kelibsiz. Menyudan tanlang:",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Informatika Darsliklar PDF (5-11 sinf)":
        await update.message.reply_text(
            "📘 Qaysi sinf kerak?",
            reply_markup=ReplyKeyboardMarkup(Informatika_PDF + back_button, resize_keyboard=True)
        )

    elif text == "📚 Huquq Darsliklar PDF (8-11 sinf)":
        await update.message.reply_text(
            "📘 Qaysi sinf kerak?",
            reply_markup=ReplyKeyboardMarkup(Huquq_PDF + back_button, resize_keyboard=True)
        )

    elif text == "📚 Biologiya Darsliklar PDF (7-11 sinf)":
        await update.message.reply_text(
            "📘 Qaysi sinf kerak?",
            reply_markup=ReplyKeyboardMarkup(Biologiya_PDF + back_button, resize_keyboard=True)
        )

    elif text == "📚 Matematika (Algebra) Darsliklar PDF (5-11 sinf)":
        await update.message.reply_text(
            "📘 Qaysi sinf kerak?",
            reply_markup=ReplyKeyboardMarkup(Matematika_PDF + back_button, resize_keyboard=True)
        )

    elif text.startswith("📘 "):
        fan_va_sinf = text.replace("📘 ", "")
        fan, sinf = fan_va_sinf.split(" ", 1)  # faqat birinchi bo'linishda ajratamiz
        sinf = sinf.replace("-sinf", "")

        # Maxsus holat: Informatika 10-11-sinf
        if fan == "Informatika" and sinf == "10-11":
            fayl_nomi = "informatika/10-11_sinf.pdf"
        else:
            fayl_nomi = f"{fan.lower()}/{sinf}_sinf.pdf"

        if os.path.exists(fayl_nomi):
            waiting_msg = await update.message.reply_text("⏳ Iltimos, biroz kuting...")

            with open(fayl_nomi, "rb") as f:
                await update.message.reply_document(
                    f,
                    caption=f"📘 {fan} {sinf}-sinf darsligi",
                    reply_markup=ReplyKeyboardMarkup(back_button, resize_keyboard=True)
                )

            await waiting_msg.delete()

        else:
            await update.message.reply_text(f"❌ {fayl_nomi} topilmadi.")

    elif text == "🔙 Ortga":
        await update.message.reply_text(
            "🏠 Asosiy menyu:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )

    else:
        await update.message.reply_text("Iltimos, menyudan tanlang.")

if __name__ == "__main__":
    app = ApplicationBuilder().token('8459597066:AAFE3ks_S1lqCDXF-1-sp_NwlRUsRZ8P5Vw').build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot ishga tushdi")
    app.run_polling()
