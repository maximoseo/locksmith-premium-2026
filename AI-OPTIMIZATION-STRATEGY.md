# אסטרטגיית אופטימיזציה של AI לפרויקט Locksmith

## 🎯 מטרה
להפחית עלויות AI בפרויקט ב-60-80% באמצעות כלים מתקדמים לניהול Tokens.

---

## 📋 כלים נבחרים ליישום

### 1. LLMLingua-2 - דחיסת תוכן
**שימוש:**
- דחיסת תיאורי שירותים ארוכים
- אופטימיזציה של פסקאות תוכן לפני שליחה ל-AI
- הפחתת עלויות בייצור תוכן SEO

**התקנה:**
```bash
pip install llmlingua
```

**דוגמת שימוש:**
```python
from llmlingua import PromptCompressor

compressor = PromptCompressor()

# דחיסת תוכן שירות
original_text = """
Protecting San Antonio homes with comprehensive residential locksmith solutions 
since 2010. Our residential locksmith services cover everything from emergency 
lockouts to complete home security upgrades...
"""

compressed = compressor.compress_prompt(
    original_text, 
    rate=0.5  # דחיסה של 50%
)

# חיסכון של 50% בטוקנים
```

---

### 2. Semantic Caching - מניעת שאילתות כפולות
**שימוש:**
- Cache של שאלות SEO נפוצות
- שמירת תשובות לשאלות FAQ
- מניעת יצירה חוזרת של תוכן זהה

**התקנה (GPTCache):**
```bash
pip install gptcache
```

**דוגמת שימוש:**
```python
from gptcache import cache
from gptcache.adapter import openai

# הגדרת Cache
cache.init()
cache.set_openai_key()

# כל קריאה זהה תחזור מ-Cache בחינם
response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[{
        'role': 'user',
        'content': 'What are the best locksmith services in San Antonio?'
    }]
)
```

---

### 3. Prompt Caching - Claude/OpenAI
**שימוש:**
- שמירת System Prompts קבועים
- Cache של מסמכי הנחיות SEO
- הפחתת עלויות בשאילתות חוזרות

**אסטרטגיה:**
```python
# שים את התוכן הקבוע בהתחלה
system_prompt = """
You are an expert SEO copywriter for a locksmith business in San Antonio.
Follow these guidelines:
1. Use local keywords
2. Include service areas
3. Write in professional tone
...
[2000+ tokens of instructions - cached]
"""

# הפרומפט המשתנה בסוף
user_query = "Write a meta description for residential services"

# קריאה ראשונה: מחיר מלא
# קריאות נוספות: 50-90% זול יותר
```

---

### 4. Batch API - משימות רקע
**שימוש:**
- יצירת תוכן לכל דפי השירותים במקבץ אחד
- תרגום תוכן למספר שפות
- יצירת FAQ items בכמויות גדולות

**חיסכון:**
- 50% הנחה על Batch API
- זמן תגובה: עד 24 שעות

**דוגמה:**
```python
# במקום 18 קריאות נפרדות ל-FAQ:
# שליחת 1 קריאת Batch עם 18 שאלות
# חיסכון: 50% מעלות API
```

---

### 5. OpenRouter + Floor Price
**שימוש:**
- ניתוב אוטומטי לספק הזול ביותר
- שימוש במודלים חינמיים למשימות פשוטות

**התקנה:**
```bash
# הוסף :floor לשם המודל
model = "meta-llama/llama-3.3-70b-instruct:floor"

# OpenRouter יבחר את הספק הזול ביותר
```

---

## 🔧 תוכנית יישום

### Phase 1: הגדרת Caching (Week 1)
- [ ] התקנת GPTCache
- [ ] הגדרת Semantic Cache לשאלות FAQ
- [ ] הטמעת Prompt Caching ב-System Prompts

### Phase 2: דחיסת תוכן (Week 2)
- [ ] התקנת LLMLingua-2
- [ ] דחיסת תיאורי שירותים ארוכים
- [ ] אופטימיזציה של פסקאות תוכן

### Phase 3: אופטימיזציה מתקדמת (Week 3)
- [ ] שילוב OpenRouter לניתוב חכם
- [ ] הגדרת Batch API למשימות רקע
- [ ] בניית ספריית Cache לשימוש חוזר

---

## 📊 חיסכון צפוי

| פעולה | עלות נוכחית | עלות לאחר אופטימיזציה | חיסכון |
|-------|-------------|------------------------|---------|
| יצירת תוכן לדף | $0.50 | $0.10 | 80% |
| שאילתות FAQ | $1.00 | $0.05 | 95% |
| SEO research | $2.00 | $0.40 | 80% |
| **סה"כ חודשי** | **$100** | **$15-25** | **75-85%** |

---

## ⚠️ נקודות חשובות

1. **Prompt Caching** - השתמש תמיד! חינם להטמעה, חוסך 50-90%
2. **Semantic Cache** - מושלם לתוכן SEO שחוזר על עצמו
3. **LLMLingua** - שימוש זהיר, בדוק איכות לאחר דחיסה
4. **Batch API** - רק למשימות שלא דורשות תגובה מיידית

---

## 🔗 קישורים למשאבים

- [LLMLingua Documentation](https://github.com/microsoft/LLMLingua)
- [GPTCache GitHub](https://github.com/zilliztech/gptcache)
- [OpenRouter Pricing](https://openrouter.ai/docs#lowest-cost)
- [Anthropic Prompt Caching](https://docs.anthropic.com/claude/docs/prompt-caching)
- [OpenAI Batch API](https://platform.openai.com/docs/guides/batch)

---

**Created:** 2026-07-18  
**Last Updated:** 2026-07-18  
**Status:** Ready for Implementation
