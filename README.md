# Auth Extraction & API Analysis Tools
## Developed by: xxxxxthefox

هذه الأداة مصممة لتحليل عمليات المصادقة (Authentication) في تطبيقات معينة. الغرض هو إثبات أن نظام الحماية المزعوم في صفحات تسجيل الدخول ليس إلا واجهة وهمية، وأن الحقيقة تكمن في التوكن (Token) الناتج عن استجابة الخادم.

---

## الأدوات التحليلية

### 1. discord-login.py
هذا السكربت يستهدف نقطة النهاية `https://discord.com/api/v9/auth/login` لإجراء عملية تسجيل دخول برمجية[span_0](start_span)[span_0](end_span).
* **طريقة العمل:** يقوم السكربت بإرسال طلب `POST` يحتوي على البريد الإلكتروني وكلمة المرور مع ضبط `User-Agent` الخاص بهواتف أندرويد لتمويه الطلب[span_1](start_span)[span_1](end_span).
* **الهدف التقني:** إثبات أن ديسكورد لا يعتمد على نظام "تحقق" معقد عند إدخال البيانات الصحيحة، بل بمجرد إرسال البيانات بشكل صحيح، يقوم الخادم بالاستجابة وإعطاء التوكن[span_2](start_span)[span_2](end_span).
* **الاستخدام:** يُستخدم لفحص كيفية معالجة ديسكورد لعملية الدخول واستخراج التوكن من الـ `response.text` مباشرة[span_3](start_span)[span_3](end_span).

### 2. Bluesky_login.py
هذا السكربت يستهدف بروتوكول AT Protocol الخاص بمنصة Bluesky عبر نقطة النهاية `https://bsky.social/xrpc/com.atproto.server.createSession`[span_4](start_span)[span_4](end_span).
* **طريقة العمل:** يقوم السكربت بإرسال طلب `POST` بتنسيق `JSON` يحتوي على معرف المستخدم وكلمة المرور[span_5](start_span)[span_5](end_span).
* **الهدف التقني:** استخراج بيانات الجلسة (Session tokens) الخاصة بحسابات Bluesky[span_6](start_span)[span_6](end_span). يعمل السكربت كمحاكٍ لعملية تسجيل الدخول الرسمية عبر الـ API[span_7](start_span)[span_7](end_span).
* **الاستخدام:** فحص كيفية تعامل المنصة مع الـ `JWT` (JSON Web Token) وكيفية إرجاع التوكن فور نجاح المصادقة[span_8](start_span)[span_8](end_span).

---

## ملاحظة جوهرية: وهم الأمان
* **التوكن هو الحقيقة:** نظام "التحقق" الذي تروج له المواقع هو مجرد كذبة تسويقية[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span). بمجرد أن تقوم بكتابة حساب صحيح، يخرج التوكن (Token) فوراً من الخادم[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span).
* **النتيجة:** بمجرد امتلاك هذا التوكن، لا يعد هناك حاجة لكلمة المرور أو نظام التحقق، الحساب يصبح تحت تصرفك الكامل[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span).

---

<div style="background-color: #000000; color: #ff0000; padding: 20px; border: 2px solid #ff0000; font-family: monospace;">
  <h3>[!] تحذير أمني: الحماية مجرد واجهة</h3>
  <p>هذه السكربتات تُظهر أن الأمان الحقيقي لا وجود له في عملية تسجيل الدخول التقليدية.</p>
  <p>كود discord-login.py وكود Bluesky_login.py يعملان على استخراج مفاتيح الوصول (Tokens) مباشرة.</p>
  <p>استخدم هذه الأداة على مسؤوليتك الخاصة.</p>
</div>
