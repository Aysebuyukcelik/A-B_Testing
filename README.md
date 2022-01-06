# A-B_Testing

![image](https://user-images.githubusercontent.com/84872652/148305162-d4f939f7-b347-4e68-9e34-ea2cd743a2d9.png)

Araştırılmak istenen durum: Seçilen internet sitesi için reklamlar üzerinde tıklamalarda
averagebidding ile  maximumbidding arasında dönüşüm getirme(satın alma) bakımından fark olup olmadığının ortaya çıkarılması

Araştırmanın gerçekleşmesinde A/B testi yani bağımsız iki örneklem t testi uygulayacağız.
Testin uygulanabilirliği için normallik ve varyans homojenliği varsayımının sağlanması gerekmektedir. 

Verisetinde averagebidding ve maxiumumbidding'in uygulandığı kısımlar test ve control olarak ayrılmış olup,
araştırma bu ayrım üzerinden gerçekleştirilecektir.

Verisetini daha yakından tanıyacak olursak, web site bilgilerini içeren bu veri setinde kullanıcıların 
gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra buradan gelen 
kazanç bilgileri yer almaktadır. Veriseti kolonları şu şekilde:

Impression – Reklam görüntüleme sayısı

Click – Tıklama sayısı

Purchase – Satın alınma sayısı

Earning – Kazanç miktarı
