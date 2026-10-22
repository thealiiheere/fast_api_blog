import asyncio
import html
import logging
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings

logger = logging.getLogger(__name__)

# Email sozlanmagan bo'lsa (CI, testlar, .env da MAIL_* yo'q) — ilova
# yiqilmasligi kerak. Shuning uchun config faqat sozlamalar to'liq bo'lsa yaratiladi.
conf = None
if settings.mail_from and settings.mail_username and settings.mail_password:
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.mail_username,
        MAIL_PASSWORD=settings.mail_password,
        MAIL_FROM=settings.mail_from,
        MAIL_PORT=settings.mail_port,
        MAIL_SERVER=settings.mail_server,
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True
    )

async def send_welcome_email(email: str, username: str):
    if conf is None:
        logger.info(f"Email sozlanmagan, xush kelibsiz xati yuborilmadi: {email}")
        return

    message = MessageSchema(
        subject="Xush kelibsiz! 🎉",
        recipients=[email],
        body=f"""
        <h2>Salom, {html.escape(username)}!</h2>
        <p>Blog API ga xush kelibsiz!</p>
        <p>Hisobingiz muvaffaqiyatli yaratildi.</p>
        """,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)

async def send_post_notification(author_email: str, title: str):
    """Post yaratilganda email"""
    logger.info(f"Post bildirishi: {author_email} → {title}")
    await asyncio.sleep(1)
    logger.info(f"Bildirish yuborildi!")

def write_log(action: str, user_id: int, details: str = ""):
    """Faoliyat logi"""
    logger.info(f"LOG: user={user_id} | action={action} | {details}")
