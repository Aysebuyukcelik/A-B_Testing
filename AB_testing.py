#Kullanılacak olan kütüphanleri import ettik
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


#veriseti için test ve kontrol gruplarını analiz için ayırdık ve sütun isimlerini tekrar atadık
control=pd.read_excel(r"C:\VBO_DOSYALAR\ders öncesi notlar\ab_testing.xlsx",sheet_name="Control Group")
test=pd.read_excel(r"C:\VBO_DOSYALAR\ders öncesi notlar\ab_testing.xlsx",sheet_name="Test Group")
test=test[["Impression","Click","Purchase","Earning"]]
control=control[["Impression","Click","Purchase","Earning"]]


#kontrol setindeki ve test setindeki ortalama kazançlara bakarak bir ön bilgi edinelim
print(f"Kontrol setindeki ortalama kazanç: {control.Purchase.mean()}  "
      f"\nTest setindeki ortalama kazanç: {test.Purchase.mean()}")

################################################
# A/B testinin hipotezinin oluşturulması ve test sonuçlarının yorumlanması
################################################

# 1-Normallik varsayımının kontrolü-Shapiro testi

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:Normal dağılım varsayımı sağlanmamaktadır.

    test_stat, pvalue = shapiro(control["Purchase"])
    print( 'Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

    test_stat, pvalue= shapiro(test["Purchase"])
    print( 'Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#test grubunun p value değeri=0.58, kontrol grubunun p value değeri=0.15 dolayısıyla
#alpha=0.05 anamlılık değerinden büyük olduğu için H0 hipotezi reddedilemez.
#Gruplar normallik varsayımını sağlamaktadır denilir.

# 2-Varyans homojenliği varsayımı kontrolü

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(control["Purchase"],test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#test ve control grubunun levene varyans homojenliği p value değeri=0.1 olarak bulunmuştur.
# alpha=0.05<p-value=0.1 olduğundan H0 reddedilemez. Dolayısıyla varyanslar homojendir.
#Varsayımlar sağlandığı için bağımsız iki örneklem t testine geçebiliriz.

# 3- A/B Testinin Uygulanması

#Varyans homojenliği ve normallik varsayımı sağlandığından bağımsız iki örneklem t testi ile hipotez testi uygulanır.

# H0: M1 = M2 (Averagebidding ile Maximumbidding arasında ortalamlar bakımından anlamlı bir fark yoktur.)
# H1: M1 =! M2 (Averagebidding ile Maximumbidding arasında ortalamlar bakımından anlamlı bir fark yok değildir.)

test_stat, pvalue = ttest_ind(control["Purchase"],test["Purchase"],equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#p-value değeri 0.3493 bulundu. alpha=0.05<p-value=0.3493 olduğundan H0 reddedilemez.
#Dolayısıyla averagebidding ile maksimumbidding arasında ortalamalar bakımından anlamlı bir
#fark yoktur denilir.


################################################
#Müşteriye tavsiyeniz nedir?
################################################
"""
Sonuç olarak  averagebidding ve maksimumbidding satış ortalamarı arasında anlamlı bir fark 
bulamadık. Ancak mevcut verisetinde gözlem sayısı az olduğu için aykırı değer çıkarması
yapamadık. Daha fazla veri toplanarak araştırmanın güncellenmesi tavsiye olunur.
"""