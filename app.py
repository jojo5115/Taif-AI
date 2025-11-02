import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 🌟 إعداد واجهة Streamlit
st.set_page_config(page_title="Taif AI Dashboard", page_icon="📊", layout="wide")
st.title("Taif Classroom Behavioral Analysis")
st.markdown("""
مرحبًا بك في لوحة تحكم تحليل السلوك الصفي 🌟  
هنا يمكنك رفع فيديو MP4 للتحليل ومشاهدة الرسومات والتقرير التلقائي.
""")



st.markdown("""
مرحبًا بك في لوحة تحكم تحليل السلوك الصفي 🌟  
هنا يمكنك رفع نتائج التحليل (ملف CSV) ورؤية الرسومات والتقرير التلقائي.
""")

# 📂 تحميل ملف CSV
uploaded_file = st.file_uploader("⬆️ ارفع ملف التحليل (taif_metrics.csv)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ تم تحميل البيانات بنجاح!")

    # 🎨 عرض البيانات
    st.subheader("📋 نظرة عامة على البيانات")
    st.dataframe(df.head())

    # 📊 حساب المتوسطات
    avg_stress = np.mean(df["Stress"])
    avg_engagement = np.mean(df["Engagement"])
    avg_activity = np.mean(df["Activity"])

    # 📈 عرض المخططات
    st.subheader("📊 التحليل البصري")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("متوسط التوتر", f"{avg_stress:.1f}%")
    with col2:
        st.metric("متوسط التفاعل", f"{avg_engagement:.1f}%")
    with col3:
        st.metric("متوسط النشاط", f"{avg_activity:.1f}%")

    # خط الزمن
    st.line_chart(df[["Stress", "Engagement", "Activity"]])

    # 🎯 إنشاء تقرير نصي ذكي
    st.subheader("🧠 التقرير التحليلي")

    report = f"""
    📄 **تقرير الأداء العام**
    - متوسط التوتر العام هو {avg_stress:.1f}%، مما يشير إلى {"مستوى عالٍ" if avg_stress > 70 else "مستوى معتدل" if avg_stress > 40 else "توتر منخفض"}.
    - مستوى التفاعل العام {avg_engagement:.1f}%، {"ممتاز جدًا 👏" if avg_engagement > 80 else "جيد 👍" if avg_engagement > 60 else "منخفض ⚠️"}.
    - النشاط العام {avg_activity:.1f}%، {"مرتفع 🔥" if avg_activity > 70 else "معتدل 🟡" if avg_activity > 40 else "ضعيف ⚪"}.
    """
    st.markdown(report)

    # 🔍 توصيات بسيطة
    st.subheader("💡 التوصيات المقترحة")
    if avg_stress > 70:
        st.warning("🔹 يوصى بتقليل الضغط عبر أنشطة مريحة داخل الفصل.")
    if avg_engagement < 50:
        st.info("🔹 حاول إضافة تفاعل بصري أو أنشطة جماعية لرفع الانتباه.")
    if avg_activity < 40:
        st.info("🔹 قلة الحركة قد تعني ملل، يمكن تشجيع المشاركة الجسدية.")
    if avg_engagement > 80 and avg_stress < 50:
        st.success("✨ أداء ممتاز! التفاعل عالٍ والراحة النفسية جيدة جدًا.")

else:
    st.info("👆 من فضلك ارفع ملف التحليل أولًا لرؤية النتائج.")

st.markdown("---")
st.caption("🚀 تصميم Jana | Taif AI Behavioral Dashboard")
