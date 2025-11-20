"""
Dosya kaydetme ve export işlemleri
Bu dosya üretilen metinleri TXT formatında kaydeder
"""

from datetime import datetime  # Tarih ve zaman için


def save_as_txt(text, content_type):
    """
    Metni TXT dosyası olarak kaydeder

    Args:
        text (str): Kaydedilecek metin
        content_type (str): İçerik türü (dosya adında kullanılacak)

    Returns:
        str: Kaydedilen dosyanın adı
    """
    # Şu anki tarih ve saati al, dosya adında kullanmak için
    # strftime fonksiyonu tarihi istediğimiz formatta string'e çevirir
    # %Y = yıl, %m = ay, %d = gün, %H = saat, %M = dakika, %S = saniye
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Dosya adını oluştur
    # Content type'daki boşlukları alt çizgi ile değiştir
    # replace() fonksiyonu bir karakteri başka bir karakterle değiştirir
    safe_content_type = content_type.replace(" ", "_")
    filename = f"{safe_content_type}_{timestamp}.txt"

    # Dosyayı yaz
    # 'w' modu write yani yazma modu demek
    # encoding='utf-8' Türkçe karakterlerin düzgün görünmesi için önemli
    # with bloğu dosyayı otomatik olarak kapatır, güvenli bir yöntemdir
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)  # Metni dosyaya yaz
        return filename  # Başarılı olursa dosya adını döndür

    except Exception as e:
        # Eğer dosya yazarken hata olursa (disk dolu, izin yok vb.)
        return f"Hata: {str(e)}"


def create_download_link(text, filename):
    """
    Streamlit için indirilebilir dosya verisi oluşturur

    Args:
        text (str): İndirilecek metin
        filename (str): Dosya adı

    Returns:
        tuple: (metin verisi, dosya adı, mime tipi)
    """
    # Bu fonksiyon Streamlit'in download_button'u için veri hazırlar
    # Metin verisini, dosya adını ve MIME tipini döndürür
    # MIME tipi tarayıcıya "bu bir text dosyasıdır" der
    return text, filename, "text/plain"