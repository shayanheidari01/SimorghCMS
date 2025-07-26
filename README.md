# SimorghCMS

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white" alt="Vue.js">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</div>

<div align="center">
  <h3>یک سیستم مدیریت محتوای مدرن و قدرتمند</h3>
  <p>ساخته شده با FastAPI و Vue.js</p>
</div>

## 📋 معرفی پروژه

SimorghCMS یک سیستم مدیریت محتوای مدرن، سریع و کاربرپسند است که با الهام از WordPress طراحی شده است. این CMS با استفاده از تکنولوژی‌های مدرن مانند FastAPI و Vue.js ساخته شده و ویژگی‌های پیشرفته‌ای مانند مدیریت کاربران، مقالات، دسته‌بندی‌ها و نظرات را ارائه می‌دهد.

## 🚀 ویژگی‌ها

### بک‌اند (FastAPI)
- ✅ سیستم احراز هویت JWT
- ✅ مدیریت کاربران با نقش‌های مختلف (Admin, Editor, Author, Subscriber)
- ✅ ایجاد، ویرایش و حذف مقالات
- ✅ دسته‌بندی و تگ‌گذاری مقالات
- ✅ سیستم نظرات با مدیریت وضعیت
- ✅ آپلود و مدیریت فایل‌های رسانه‌ای
- ✅ API مستند با Swagger و ReDoc
- ✅ پایگاه داده ناهمزمان با SQLAlchemy
- ✅ امنیت بالا و اعتبارسنجی داده‌ها

### فرانت‌اند (Vue.js/HTML)
- ✅ طراحی واکنش‌گرا و مدرن
- ✅ داشبورد کاربری پیشرفته
- ✅ مدیریت مقالات و نظرات
- ✅ پروفایل کاربری
- ✅ طراحی چندزبانه (فارسی)
- ✅ سرعت بالا و عملکرد عالی
- ✅ بدون نیاز به فریمورک سنگین

## 🛠️ تکنولوژی‌ها

### بک‌اند
- **FastAPI** - فریمورک وب پایتون با عملکرد بالا
- **SQLAlchemy** - ORM پایتون برای پایگاه داده
- **SQLite** - پایگاه داده سبک و قابل حمل
- **JWT** - توکن‌های امن برای احراز هویت
- **Alembic** - ابزار میگریشن پایگاه داده
- **Pydantic** - اعتبارسنجی داده‌ها

### فرانت‌اند
- **HTML/CSS/JavaScript** - برای نسخه سبک
- **Vue.js** - برای نسخه پیشرفته (اختیاری)
- **Tailwind CSS** - فریمورک CSS مدرن
- **Axios** - کلاینت HTTP برای API calls

## 📦 نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8+
- pip
- Node.js (برای نسخه Vue.js)

### نصب بک‌اند

```bash
# کلون کردن پروژه
git clone https://github.com/yourusername/SimorghCMS.git
cd SimorghCMS

# ایجاد محیط مجازی
python -m venv venv
source venv/bin/activate  # در Windows: venv\Scripts\activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# ایجاد پایگاه داده
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### اجرای بک‌اند

```bash
# اجرای سرور توسعه
uvicorn app.main:app --reload

# سرور در http://localhost:8000 اجرا می‌شود
```

### نصب فرانت‌اند (نسخه سبک)

```bash
# فایل‌های فرانت‌اند را در دایرکتوری static/frontend قرار دهید
mkdir -p static/frontend

# کپی کردن فایل‌های فرانت‌اند
cp -r frontend/* static/frontend/
```

### اجرای فرانت‌اند (برای توسعه)

```bash
# در دایرکتوری frontend
python -m http.server 3000

# فرانت‌اند در http://localhost:3000 اجرا می‌شود
```

## 📚 مستندات API

پس از اجرای سرور، می‌توانید به مستندات API دسترسی پیدا کنید:

- **Swagger UI**: `http://localhost:8000/api/docs`
- **ReDoc**: `http://localhost:8000/api/redoc`

## 🗂️ ساختار پروژه

```
SimorghCMS/
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # تنظیمات اصلی و امنیت
│   ├── crud/         # عملیات پایگاه داده
│   ├── database/     # تنظیمات پایگاه داده
│   ├── models/       # مدل‌های پایگاه داده
│   ├── schemas/      # اسکیماهای Pydantic
│   └── main.py       # فایل اصلی برنامه
├── frontend/         # فرانت‌اند (نسخه سبک)
├── static/           # فایل‌های استاتیک
├── alembic/          # فایل‌های میگریشن
├── requirements.txt  # وابستگی‌های پایتون
└── README.md         # این فایل
```

## 🔧 متغیرهای محیطی

ایجاد فایل `.env` در ریشه پروژه:

```env
DATABASE_URL=sqlite+aiosqlite:///./cms.db
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🐳 استفاده از Docker

```bash
# ساخت و اجرای با Docker
docker-compose up --build
```

## 🚀 استقرار

### برای تولید با Nginx

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

## 📖 راهنمای استفاده

### اولین کاربر ادمین

پس از اولین اجرا، یک کاربر ادمین ایجاد کنید:

1. به `http://localhost:8000` مراجعه کنید
2. روی "ثبت نام" کلیک کنید
3. اطلاعات کاربری خود را وارد کنید
4. در پایگاه داده نقش کاربر را به "admin" تغییر دهید

### ایجاد مقاله

1. وارد حساب کاربری خود شوید
2. به داشبورد بروید
3. روی "ایجاد مقاله جدید" کلیک کنید
4. اطلاعات مقاله را وارد کنید و منتشر کنید

## 🤝 مشارکت

1. Fork کنید
2. یک branch جدید ایجاد کنید (`git checkout -b feature/AmazingFeature`)
3. تغییرات خود را commit کنید (`git commit -m 'Add some AmazingFeature'`)
4. به branch خود push کنید (`git push origin feature/AmazingFeature`)
5. یک Pull Request باز کنید

## 📄 مجوز

این پروژه تحت مجوز MIT منتشر شده است. برای اطلاعات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.

## 🙏 تشکر ویژه

- [FastAPI](https://fastapi.tiangolo.com/) برای فریمورک عالی
- [Vue.js](https://vuejs.org/) برای فرانت‌اند مدرن
- جامعه توسعه‌دهندگان پایتون

## 📞 تماس

پروژه SimorghCMS - [@your_twitter](https://twitter.com/your_twitter) - your.email@example.com

لینک پروژه: [https://github.com/yourusername/SimorghCMS](https://github.com/yourusername/SimorghCMS)

---

<div align="center">
  <p>ساخته شده با ❤️ و Python</p>
  <p>© 2023 SimorghCMS. تمامی حقوق محفوظ است.</p>
</div>
