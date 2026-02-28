import telebot
from telebot import types

TOKEN = 8588476375:AAEjTlrSjeeih-oIWf4cnwHoFB0kl9GXxvo
bot = telebot.TeleBot(TOKEN)

# رسالة الترحيب مع أزرار تفاعلية
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("ما هي DXN؟", callback_data='about')
    btn2 = types.InlineKeyboardButton("طريقة الانضمام", callback_data='join')
    btn3 = types.InlineKeyboardButton("منتجاتنا الصحية", callback_data='products')
    markup.add(btn1, btn2, btn3)
    
    bot.reply_to(message, "🌟 أهلاً بك في فريق *العقول المستقبلية*!\n\nأنا مساعدك الذكي الخاص بشركة DXN. أنا هنا لأرشدك نحو حياة صحية ومشروع مالي ناجح. كيف يمكنني خدمتك اليوم؟", 
                 parse_mode="Markdown", reply_markup=markup)

# معالجة ضغطات الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'about':
        bot.answer_callback_query(call.id, "جاري التحميل...")
        bot.send_message(call.message.chat.id, "شركة DXN هي رائدة في مجال المنتجات الصحية العضوية منذ 1993. نحن نجمع بين الصحة والمال في آن واحد.")
    elif call.data == 'join':
        bot.send_message(call.message.chat.id, "للانضمام لفريقنا، يرجى التسجيل عبر الرابط التالي:\n[اضغط هنا للتسجيل]", parse_mode="Markdown")
    elif call.data == 'products':
        bot.send_message(call.message.chat.id, "نقدم لكم مجموعة متنوعة من المكملات الغذائية الطبيعية (مثل الفطر الريشي). هل ترغب في معرفة فوائد منتج معين؟")

bot.polling()
