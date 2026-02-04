
import sys
import os

# إضافة المسار الحالي للمسارات المستوردة
sys.path.append(os.getcwd())

try:
    import telebot
    from Plugins.apis import app
    from kvsqlite.sync import Client as uu
    
    print("✅ تم استيراد المكتبات بنجاح.")
    
    # محاكاة إعدادات بسيطة
    if not os.path.isdir('dbs'):
        os.mkdir('dbs')
    
    db = uu('dbs/AbuHamza.v2', 'bot')
    print("✅ تم إنشاء/فتح قاعدة البيانات بنجاح.")
    
    print("🚀 البوت جاهز للعمل برمجياً، ينقصه فقط التوكن الصحيح.")
    
except Exception as e:
    print(f"❌ حدث خطأ أثناء الاختبار: {e}")
    sys.exit(1)
