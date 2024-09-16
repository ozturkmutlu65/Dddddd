#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """
✶ Etiket Komutları

» /tag - Tek tek etiketler.

» /utag - Çoklu etiketler.

» /etag - Emoji ile etiketler.

» /igtag - iyi geceler mesajları ile etiketler.

» /guntag - günaydın mesajları ile etiketler.

» /btag - Bayrak ile etiketler.

» /sorutag - Sorularla etiketler.

» /ktag - Karakter ile etiketler.

» /stag - Sözlerle etiketler.

» /stop - Etiket işlemini bitirir.

» /chatmode - sohbet özelliğini açar.

» /slap - Tokat atar.

» /soz - Söz atar.

» /mani - Mani söyler.

» /eros - Eros oku atar.

» /tokat - birine Tokat atar.

» /tts - Bir metni sese çevirir

» /burc - Burçlarınızı yorumluyorım

"""


HELP_2 = """
🎰 Oyunlar

• /cash - Slot oyununu oynamak için. 🎰
   Örnek: /cash 50 veya /cash 50 2x
   ❌ NOT: /cash 50 3x yaptığınızda, çarpan kadar paranız gider.

• /fcash - Futbol oyununu oynamak için. ⚽️
   Örnek: /fcash 100 veya /fcash 100 3x

• /bcash - Basketbol oyununu oynamak için. 🏀
   Örnek: /bcash 50 veya /bcash 50 2x

• /bowling - Bowling atar.🎳

• /dart - Ok atar.🎯

• /slap - Tokat atar.👋

• /zar - Zar atarım.

• /para - Yazı tura atarım.

• /gunluk - Günlük alacağınız bonus. 🤩

• /bakiye - Bakiyenizi kontrol etmek için. 💰

• /borc - Birine borç göndermek için. 💸
   Örnek: /borc [Miktar] [Kullanıcı İD] veya Mesajı Yanıtla.

• /zenginler - En zengin kullanıcıları görmek için. 🤑

🆘 Komutlar: /cash, /fcash ve /bcash Oyunları sadece gruplarda çalışır.
📌 Oyunları oynamak için bota start vermelisiniz.
🏷️ @AcelyaMusicBot

"""


HELP_3 = """
**ADMİN KOMUTLARI:**

**/c** komutlarını kanalda kullanabilmek için, komutların başına **c** ekleyin.

**/pause veya /dur**: Çalan akışı duraklatır.
**/resume veya /devam**: Duraklatılmış akışı devam ettirir.
**/skip veya /atla **: Çalan akışı atlar ve sıradaki parçayı çalmaya başlar.
**/kapat** veya **/son**: Sıradaki parçayı atlar ve çalan akışı sonlandırır.
**/player**: Etkileşimli bir oynatıcı paneli alır.
**/queue veya /liste**: Sıradaki parçaların listesini gösterir.
"""
HELP_4 = """
**YETKİLİ KULLANICILAR:**

**/auth veya /ver  [kullanıcı adı/kullanıcı_ID]**: Bir kullanıcıyı botun yetkili listesine ekler.
**/unauth veya /al [kullanıcı adı/kullanıcı_ID]**: Bir kullanıcıyı yetkili kullanıcılar listesinden çıkarır.
**/authusers veya /yetkili**: Yetkili kullanıcıların listesini gösterir.
"""
HELP_5 = """
**YAYIN YAPMA ÖZELLİĞİ**

**/broadcast [mesaj veya bir mesaja yanıt]**: Bir mesajı sunucu sohbetlerine yayınlar.

Yayın modları:
**-pin**: Yayınlanan mesajları sunucu sohbetlerinde sabitler.
**-pinloud**: Yayınlanan mesajları sunucu sohbetlerinde sabitler ve üyelere bildirim gönderir.
**-user**: Mesajı botunuza başlatan kullanıcılara yayınlar.
**-assistant**: Botunuzun asistan hesabından mesajı yayınlar.
**-nobot**: Mesajın yayınlanmasını engeller.

Örnek: /broadcast -user -assistant -pin Test yayını
"""
HELP_6 = """
**CHAT BLACKLIST ÖZELLİĞİ:** [Sadece süper yöneticiler için]

Çöp sohbetlerinizi botumuzda kullanmayı kısıtlayın.

/blacklistchat [sohbet ID] : Bir sohbeti bot kullanımından engeller.
/whitelistchat [sohbet ID] : Kara listeye alınmış sohbeti beyaz listeye alır.
/blacklistedchat : Kara listeye alınmış sohbetlerin listesini gösterir.
"""
HELP_7 = """
**KULLANICI ENGELLEME:**

Kara listeye alınmış kullanıcıları görmezden gelmeye başlar, böylece bot komutlarını kullanamazlar.

/block [kullanıcı adı veya kullanıcıya yanıt] : Kullanıcıyı botumuzdan engeller.
/unblock [kullanıcı adı veya kullanıcıya yanıt] : Engellenmiş kullanıcının engelini kaldırır.
/blockedusers : Engellenmiş kullanıcıların listesini gösterir.
"""
HELP_8 = """
**KANAL OYNATMA KOMUTLARI:**

Kanallarda ses/video yayını yapabilirsiniz.

/cplay : Kanalın video sohbetinde istenilen ses parçasının yayınını başlatır.
/cvoynat : Kanalın video sohbetinde istenilen video parçasının yayınını başlatır.
/cplayforce veya /cvplayforce : Devam eden yayını durdurur ve istenilen parçanın yayınını başlatır.
/channelplay [sohbet kullanıcı adı veya ID] veya [devre dışı] : Kanalı bir gruba bağlar ve grup tarafından gönderilen komutlarla parçaların yayınını başlatır.
"""

HELP_9 = """
**GLOBAL BAN ÖZELLİĞİ:** [Sadece süper yöneticiler için]

/gban [kullanıcı adı veya kullanıcıya yanıt] : Tüüm sunucu sohbetlerinden kullanıcıyı global olarak engeller ve bot kullanımını ondan engeller.
/ungban [kullanıcı adı veya kullanıcıya yanıt] : Global olarak yasaklanan kullanıcının yasağını kaldırır.
/gbannedusers : Global olarak yasaklanan kullanıcıların listesini gösterir.
"""
HELP_10 = """
**LOOP STREAM:**

Ongoing yayını döngüde başlatır.

/dongu [enable/disable] : Ongoing yayın için döngüyü etkinleştirir/devre dışı bırakır.
/dongu [1, 2, 3, ...] : Verilen değer için döngüyü etkinleştirir.
"""
HELP_11 = """
**BAKIM MODU:** [Sadece süper yöneticiler için]

/logs : Botun aktivitelerinin günlüklerini alır.

/logger [enable/disable] : Botun aktivitelerini günlüklemeye başlar/devre dışı bırakır.

/maintenance [enable/disable] : Botun bakım modunu etkinleştirir/devre dışı bırakır.
"""
HELP_12 = """
**PING & STATS:**

/start : Müzik botunu başlatır.
/help : Komutların açıklamalarıyla yardım menüsünü alır.

/ping : Botun ping ve sistem istatistiklerini gösterir.

/stats : Botun genel istatistiklerini gösterir.
"""
HELP_13 = """
**PLAY COMMANDS:**

**v :** Video play için kullanılır.
**force :** Zorla oynatma için kullanılır.

/play , /voynat veya /oynat veya /voynat : Video sohbetinde istenilen parçayı çalmaya başlar.

/playforce veya /voynatforce : Devam eden yayını durdurur ve istenilen parçayı çalmaya başlar.
"""
HELP_14 = """
**SHUFFLE QUEUE:**

/karistir : Sıradaki parçaları karıştırır.
/queue : Karıştırılmış sırayı gösterir.
"""

HELP_15 = """
**SEEK STREAM:**

/ilerisar [saniye cinsinden süre] : Yayını belirtilen süreye atlar.
/gerisar [saniye cinsinden süre] : Yayını belirtilen süre kadar geri alır.
"""
HELP_16 = """
**SONG DOWNLOAD:**

/song veya /bul [şarkı adı/YouTube URL] : YouTube'dan herhangi bir parçayı MP3 veya MP4 formatında indirir.
"""
HELP_17 = """
**SPEED COMMANDS:**

Ongoing stream'un çalma hızını kontrol edebilirsiniz. [Yalnızca yöneticiler]

/speed veya /playback : Grubun ses çalma hızını ayarlamak için.
/cspeed veya /cplayback : Kanalın ses çalma hızını ayarlamak için.
"""
