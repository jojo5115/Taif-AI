import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2  # استخدمي opencv-python-headless في requirements.txt

# إعداد واجهة Streamlit
st.set_page_config(page_title="Taif AI Dashboard", layout="wide")
st.title("Taif Classroom Behavioral Analysis")
st.markdown("""
مرحبًا بك في لوحة تحكم تحليل السلوك الصفي.  
يمكنك رفع فيديو MP4 للتحليل ومشاهدة الرسومات والتقرير التلقائي.
""")

# رفع ملف mp4
uploaded_file = st.file_uploader("ارفع فيديو MP4 للتحليل", type=["mp4", "mov"])

if uploaded_file is not None:
    # حفظ الفيديو مؤقتًا
    tfile_bytes = uploaded_file.read()
    with open("temp_video.mp4", "wb") as f:
        f.write(tfile_bytes)

    # قراءة الفيديو إطارًا فريمًا فريمًا
    cap = cv2.VideoCapture("temp_video.mp4")
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    # توليد قيم عشوائية لكل إطار
    stress_levels = np.random.randint(30, 80, size=len(frames))
    engagement_levels = np.random.randint(40, 90, size=len(frames))
    activity_levels = np.random.randint(20, 100, size=len(frames))

    # إنشاء DataFrame
    df = pd.DataFrame({
        "Frame": range(len(frames)),
        "Stress": stress_levels,
        "Engagement": engagement_levels,
        "Activity": activity_levels
    })

    st.success(f"تم تحليل الفيديو! عدد الإطارات: {len(frames)}")

    # عرض البيانات
    st.subheader("نظرة عامة على البيانات")
    st.dataframe(df.head())

    # حساب المتوسطات
    avg_stress = df["Stress"].mean()
    avg_engagement = df["Engagement"].mean()
    avg_activity = df["Activity"].mean()

    # عرض الرسوم البيانية
    st.subheader("التحليل البصري")
    col1, col2, col3 = st.columns(3)
    col1.metric("متوسط التوتر", f"{avg_stress:.1f}%")
    col2.metric("متوسط التفاعل", f"{avg_engagement:.1f}%")
    col3.metric("متوسط النشاط", f"{avg_activity:.1f}%")
    st.line_chart(df[["Stress", "Engagement", "Activity"]])

    # التقرير التحليلي
    st.subheader("التقرير التحليلي")
    report = f"""
تقرير الأداء العام:
- متوسط التوتر: {avg_stress:.1f}%
- مستوى التفاعل: {avg_engagement:.1f}%
- النشاط العام: {avg_activity:.1f}%
"""
    st.markdown(report)

    # توصيات
    st.subheader("التوصيات")
    if avg_stress > 70:
        st.warning("يُنصح بتقليل الضغط عبر أنشطة مريحة داخل الفصل.")
    if avg_engagement < 50:
        st.info("أضف تفاعل بصري أو أنشطة جماعية لرفع الانتباه.")
    if avg_activity < 40:
        st.info("قلة الحركة قد تعني الملل، شجّع المشاركة الجسدية.")
    if avg_engagement > 80 and avg_stress < 50:
        st.success("أداء ممتاز! التفاعل عالٍ والراحة النفسية جيدة.")

    # زر تحميل CSV
    st.download_button("تحميل CSV الناتج", df.to_csv(index=False), file_name="taif_metrics.csv")

else:
    st.info("من فضلك ارفع فيديو بصيغة MP4أولًا لرؤية النتائج.")
