import telebot

TOKEN = '8dcb5e275362be4dd7123d2fde98a26c55c45638829756b69748ed07c0ffd2fe'
bot = telebot.TeleBot(TOKEN)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import psycopg2
import datetime


def send_message(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

# Define requires_plan as a boolean variable
requires_plan = True
def my_function(update: Update, context: CallbackContext):
    # function code here
    pass

def some_function(update, context, chat_id):
    client_id = clients.get(chat_id)
    if client_id is None:
        client_id = generate_customer_id(chat_id)
        clients[chat_id] = client_id
        chat_id = update.message.chat_id
        some_function(update, context, chat_id)

    # Send a message with a link to the completed part of the task
    text = "Частина вашої роботи виконана і ви можете її переглянути."
    parse_mode = "HTML"
    bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)



TOPIC = "Тема роботи"
PAGES = "Вкажіть кількість сторінок (від 1 до 150)"
UNIQUENESS ="Вкажіть % унікальності"
DEADLINE = "На яку дату вам потрібна робота? (Враховуйте, що якщо робота термінова, то вартість буде збільшена)"
COMMENT = "Можливо є коментар або методичка? Якщо так, напишіть коментар або надішліть файл."
COST_CONFIRM = False
task_type = "Реферат"
"Магістерська робота"
"Бакалаврська робота"
"Доповідь"
"Есе"
"Стаття"
"Контрольна робота"
"Відповіді на запитання"
"Бізнес план"
"Переклад"
"Онлайн допомога на іспиті"
"Звіт з практики"
"Лабораторна робота"
"Копірайтінг"
"Рерайтінг"
"Креслення"
"Презентація"
"Домашнє завдання"
"Колоквіум"
"Вирішення задач"
"Підвищення унікальності тексту"
"Рецензія"
"Анотація"

# з'єднання з базою даних
conn = psycopg2.connect(
    host="ec2-99-80-170-190.eu-west-1.compute.amazonaws.com",
    database="dfv2fga88nji8g",
    user="zlwguoinahgffy",
    password="e8801e547af82086f7acd9584ab93cefec0a67706a5d004ae799ad1959543306",
    port="5432"
)
import uuid

clients = {}

def generate_customer_id(chat_id):
    # generate a new unique identifier for the client
    if chat_id not in clients:
        client_id = str(uuid.uuid4())
        # save the client identifier in the dictionary
        clients[chat_id] = client_id
    else:
        # get the existing identifier for the client
        client_id = clients[chat_id]
    return client_id

def start(update, context, payment_id):
    chat_id = update.effective_chat.id
    client_id_value = generate_customer_id(chat_id)
    # rest of the code
    person_id = clients[chat_id]
    # rest of the code


    bot.send_message(chat_id, "<b>Привіт! Я можу допомогти з виконанням твого завдання. Що потрібно?</b>", parse_mode='HTML')

    def some_handler(update, context):
        show_options(update, context)
# define callback functions
def show_options(update, context):
    # Функція виводить кнопки з варіантами робіт.
    keyboard = [
        [InlineKeyboardButton("Дипломна робота", callback_data="diploma"),
         InlineKeyboardButton("Реферат", callback_data="essay")],
        [InlineKeyboardButton("Магістерська робота", callback_data="master"),
         InlineKeyboardButton("Бакалаврська робота", callback_data="bachelor")],
        [InlineKeyboardButton("Доповідь", callback_data="report"),
         InlineKeyboardButton("Есе", callback_data="composition")],
        [InlineKeyboardButton("Стаття", callback_data="article"),
         InlineKeyboardButton("Контрольна робота", callback_data="test")],
        [InlineKeyboardButton("Відповіді на запитання", callback_data="faq"),
         InlineKeyboardButton("Бізнес план", callback_data="business_plan")],
        [InlineKeyboardButton("Переклад", callback_data="translation"),
         InlineKeyboardButton("Онлайн допомога на іспиті", callback_data="exam_help")],
        [InlineKeyboardButton("Звіт з практики", callback_data="practice_report"),
         InlineKeyboardButton("Лабораторна робота", callback_data="lab")],
        [InlineKeyboardButton("Копірайтінг", callback_data="copywriting"),
         InlineKeyboardButton("Рерайтінг", callback_data="rewriting")],
        [InlineKeyboardButton("Креслення", callback_data="drawing"),
         InlineKeyboardButton("Презентація", callback_data="presentation")],
        [InlineKeyboardButton("Домашнє завдання", callback_data="homework"),
         InlineKeyboardButton("Колоквіум", callback_data="quiz")],
        [InlineKeyboardButton("Вирішення задач", callback_data="problem_solving"),
         InlineKeyboardButton("Підвищення унікальності тексту", callback_data="uniqueness")],
        [InlineKeyboardButton("Рецензія", callback_data="review"),
         InlineKeyboardButton("Анотація", callback_data="abstract")],
        [InlineKeyboardButton("План до дипломної роботи", callback_data="diploma_plan")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Виберіть вид роботи:', reply_markup=reply_markup)


def button_click(update, context):
    query = update.callback_query
    query.answer()

    # Store the selected values in variables
    order_type = query.data
    chat_id = update.effective_chat.id
    customer_id = update.effective_user.id

    # Save the selected values as context variables
    context.chat_data["order_type"] = order_type
    context.chat_data["chat_id"] = chat_id
    context.chat_data["customer_id"] = customer_id

    # Ask for more information
    update.message.reply_text("З якого предмету вам потрібна допомога?")

def topic(update, context):
    text = "Вкажіть тему."
    update.message.reply_text(text)

    # Save the selected value as a context variable
    context.chat_data["topic"] = update.message.text

    return "pages"


def pages(update, context):
    text = "Вкажіть кількість сторінок (від 1 до 150)"
    update.message.reply_text(text)

    # Save the selected value as a context variable
    context.chat_data["pages"] = update.message.text

    return "uniqueness"


def uniqueness(update, context):
    text = "Вкажіть % унікальності (від 0 до 100)"
    update.message.reply_text(text)

    # Save the selected value as a context variable
    context.chat_data["uniqueness"] = update.message.text
    return "deadline"


def deadline(update, context):
    """Function to ask for the deadline"""
    text = "На яку дату вам потрібна робота? (Враховуйте, що якщо робота термінова, то вартість буде збільшена)"
    update.message.reply_text(text)
    return "comment"


def comment(update, context):
    text = "Введіть ваш коментар"
    update.message.reply_text(text)

    # Save the selected value as a context variable
    context.chat_data["comment"] = update.message.text

    # Get all the stored values
    chat_id = context.chat_data["chat_id"]
    client_id = clients[chat_id]  # use the generated client_id as the order number
    order_type = context.chat_data["order_type"]
    theme = context.chat_data["topic"]
    uniqueness = context.chat_data["uniqueness"]
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    comment = context.chat_data["comment"]

    # Commit the transaction

    conn.commit()


import psycopg2
import os

# Отримати URL бази даних зі змінної середовища
DATABASE_URL = os.getenv('DATABASE_URL', 'ваш URL бази даних')


def save_order_to_database(update, context):
    chat_id = update.message.chat_id
    customer_id = generate_customer_id(chat_id)  # Функція для генерації ID замовника
    order_type = context.user_data['order_type']
    theme = context.user_data['theme']
    uniqueness = context.user_data['uniqueness']
    date = context.user_data['date']
    comment = context.user_data['comment']

    # Збереження інформації в базу даних
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Збереження інформації в Heroku
    order_info = f"<b>ID ЗАМОВНИКА:</b> {customer_id}\n" \
                 f"<b>ПРЕДМЕТ:</b> {order_type}\n" \
                 f"<b>ПРЕДМЕТ-ВІДПОВІДЬ:</b> {theme}\n" \
                 f"<b>СТОРІНОК:</b> {context.user_data['pages']}\n" \
                 f"<b>УНІКАЛЬНІСТЬ:</b> {uniqueness}%\n" \
                 f"<b>ДАТА:</b> {date}\n" \
                 f"<b>КОМЕНТАР:</b> {comment}"

    context.bot.send_message(chat_id=os.environ['HEROKU_APP_NAME'], text=order_info, parse_mode=ParseMode.HTML)

    # Надіслати підтвердження про збереження інформації
    update.message.reply_text("Інформацію збережено. Дякую!")

def confirm_author(update, context):
    """Function to confirm if the author can do the work"""
    text = "Зараз запитаю авторів, чи зможуть вони це зробити."
    update.message.reply_text(text)

    # send order information to author
    order_id = context.user_data['order_id']
    subject = context.user_data['subject']
    topic = context.user_data['topic']
    pages = context.user_data['pages']
    uniqueness = context.user_data['uniqueness']
    deadline = context.user_data['deadline']
    comment = context.user_data['comment']
    author_info = f"New Order: \nOrder ID: {order_id} \nSubject: {subject} \nTopic: {topic} \nPages: {pages} \nUniqueness: {uniqueness} \nDeadline: {deadline} \nComment: {comment}"

    # send the order information to the author
    keyboard = ReplyKeyboardMarkup([['Accept', 'Reject']], one_time_keyboard=True)
    context.bot.send_message(chat_id=AUTHOR_CHAT_ID, text=author_info, reply_markup=keyboard)

    return AUTHOR_CONFIRM

def author_response(update, context):
    """Function to handle the author's response"""
    response = update.message.text.lower()
    if response == 'accept':
        update.message.reply_text("Ви прийняли роботу.")
        # send confirmation to customer
        context.bot.send_message(chat_id=CUSTOMER_CHAT_ID, text="Автор прийняв вашу роботу.")
        return ConversationHandler.END
    elif response == 'reject':
        update.message.reply_text("Ви відхилили роботу.")
        return ConversationHandler.END
    else:
        update.message.reply_text("Будь ласка, виберіть 'Accept' або 'Reject'.")
        return AUTHOR_CONFIRM

AUTHOR_CHAT_ID = 859360040
CUSTOMER_CHAT_ID = None
AUTHOR_CONFIRM = range(1)

# Create ConversationHandler
author_handler = ConversationHandler(
    entry_points=[CommandHandler('confirm_author', confirm_author)],
    states={
        AUTHOR_CONFIRM: [MessageHandler(Filters.text, author_response)]
    },
    fallbacks=[],
)
def generate_message(doc_type, uniqueness, pages, time_limit):
    def calculate_cost(task_type, pages, uniqueness, urgency):
        cost = 0  # Initialize cost to 0

        # calculator function
        def calculate_price(doc_type, uniqueness, pages, time_limit):
            if doc_type == "Реферат" or doc_type == "Відповіді на запитання" or doc_type == "Доповідь" or doc_type == "Презентація" or doc_type == "Колоквіум" or doc_type == "Підвищення унікальності тексту" or doc_type == "Рецензія":
                return 20
            elif doc_type == "Курсова робота" or doc_type == "Стаття" or doc_type == "Есе" or doc_type == "Копірайтінг" or doc_type == "Рерайтінг":
                if 1 <= uniqueness <= 50:
                    return 10 * pages + (1000 if time_limit < 14 else 0)
                elif 50 < uniqueness <= 80:
                    return 20 * pages + (1000 if time_limit < 14 else 0)
                elif 80 < uniqueness <= 100:
                    return 30 * pages + (1000 if time_limit < 14 else 0)
            elif doc_type == "Магістерська робота" or doc_type == "Бакалаврська робота":
                if 1 <= uniqueness <= 30:
                    return 20 * pages + (1000 if time_limit < 14 else 0)
                elif 30 < uniqueness <= 50:
                    return 30 * pages + (1000 if time_limit < 14 else 0)
                elif 50 < uniqueness <= 80:
                    return 50 * pages + (1000 if time_limit < 14 else 0)
                elif 80 < uniqueness <= 100:
                    return 60 * pages + (1000 if time_limit < 14 else 0)
            elif doc_type == "Контрольна робота" or doc_type == "Лабораторна робота" or doc_type == "Креслення" or doc_type == "Домашнє завдання":
                return 150 + (1000 if time_limit < 14 else 0)
            elif doc_type == "Бізнес план" or doc_type == "Звіт з практики":
                return 400 + (1000 if time_limit < 14 else 0)
            elif doc_type == "Переклад":
                return 50 * pages
            elif doc_type == "Онлайн допомога на іспиті":
                return 180

        def calculate_order_cost(pages, task_type, urgency, uniqueness):
            cost = calculate_price(task_type, uniqueness, pages, urgency)

            if task_type in ["Дипломна робота", "Курсова робота", "Магістерська робота", "Бакалаврська робота"]:
                message = f"Ваша робота коштуватиме {cost} грн. Для підтвердження внесіть аванс у розмірі 10% і протягом 24 годин ми надішлемо вам план вашого завдання для узгодження з викладачем."
            else:
                message = f"Здійснить оплату у вартості {cost} грн. Після перевірки вашого авансу, ми надішлемо вам ваш план роботи."

            return message
def send_messager(client_id, bot_message):
    pass

def has_partial_payment(person_id):
    # Check if the person has made a partial payment for their task
    # (implementation details omitted for brevity)
    return True  # replace with actual implementation

def attach_link(bot_message, link):
    # Attach the link to the bot message
    bot_message += f"\n\nПосилання на частину роботи: {link}"
    return bot_message  # return the updated bot message

# Import the required modules
from telegram import ParseMode


# Define the person ID as the author chat ID
person_id = AUTHOR_CHAT_ID

# Check if the task type is a diploma, term paper, master's thesis, or bachelor's thesis
if task_type in ["diploma thesis", "term paper", "master's thesis", "bachelor's thesis"]:
    # Check if the person has made a partial payment
    if has_partial_payment(person_id):
        # Send a message with a link to the completed part of the task
        bot_message = "Частина вашої роботи виконана і ви можете її переглянути."
        # Attach the link to the completed part of the task
        bot_message = attach_link(bot_message, "http://link-to-the-completed-task.com")
        def get_client_id(payment_id, context):
            # define the logic to retrieve the client ID from the payment ID and context
            pass


        def payment(update, context):
            # Get the payment ID from the callback data
            payment_id = update.callback_query.data

            def start(update, context, payment_id):
                chat_id = update.effective_chat.id
                client_id_value = get_client_id(payment_id, context)
                person_id = clients[chat_id]

            # define the logic to handle the payment
            pass

            # Get the deadline from the context data
            deadline = context.chat_data.get("deadline")

            if deadline:
                # Calculate the due date based on the deadline (this is just an example, you'll need to replace this with your own code)
                due_date = deadline - datetime.timedelta(days=1)

                # Send a message to the client that their work is in progress
                bot_message = f"Дякую за оплату, ваша робота в процесі виконання. Надішлю готову роботу так скоро як зможу але не пізніше ніж {due_date}."
                # Send the message to the person
                send_message(person_id, bot_message)
            else:
                # If the deadline was not provided, send a generic message to the client
                bot_message = "Дякую за оплату, ваша робота в процесі виконання."
                # Send the message to the person
                send_message(person_id, bot_message)

    else:
        def some_function(update, context):
            chat_id = update.message.chat_id
            client_id = clients.get(chat_id)
            if client_id is None:
                client_id = generate_customer_id(chat_id)
                clients[chat_id] = client_id

            # Send a message with a link to the completed part of the task
            text = "Частина вашої роботи виконана і ви можете її переглянути."
            parse_mode = "HTML"
            bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)
            some_function(update, context)

bot.polling(none_stop=True)
