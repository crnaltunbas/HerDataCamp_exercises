# PANDAS ALIŞTIRMALAR 2.HAFTA

# Görev 1:  Seaborn kütüphanesi içerisindenTitanicveri setini tanımlayınız.
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
df["sex"].value_counts()

# DEVAM EDİLECEK.