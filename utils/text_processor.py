"""
Metin işleme ve analiz fonksiyonları
Bu dosya üretilen metinleri işler ve analiz eder
"""


def count_words(text):
    """
    Metindeki kelime sayısını hesaplar

    Args:
        text (str): Kelime sayısı hesaplanacak metin

    Returns:
        int: Toplam kelime sayısı
    """
    # Metni boşluklara göre böl ve kelime sayısını say
    # split() fonksiyonu metni boşluklara göre parçalar
    words = text.split()
    return len(words)


def clean_text(text):
    """
    Metni temizler ve gereksiz boşlukları kaldırır

    Args:
        text (str): Temizlenecek metin

    Returns:
        str: Temizlenmiş metin
    """
    # strip() fonksiyonu baştan ve sondan boşlukları kaldırır
    # replace() fonksiyonu çift boşlukları tek boşluğa çevirir
    text = text.strip()  # Baştan ve sondan boşluk kaldır
    text = ' '.join(text.split())  # Çoklu boşlukları tek boşluğa indir
    return text


def truncate_text(text, max_words):
    """
    Metni belirtilen kelime sayısına göre kısaltır

    Args:
        text (str): Kısaltılacak metin
        max_words (int): Maksimum kelime sayısı

    Returns:
        str: Kısaltılmış metin
    """
    # Metni kelimelere ayır
    words = text.split()

    # Eğer metin zaten kısaysa, olduğu gibi döndür
    if len(words) <= max_words:
        return text

    # İlk max_words kadar kelimeyi al ve birleştir
    # [:max_words] notasyonu liste dilimlemesi, ilk max_words elemanı alır
    truncated = ' '.join(words[:max_words])

    # Sonuna üç nokta ekle ki kullanıcı kesildiğini anlasın
    return truncated + "..."