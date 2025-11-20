"""
Proje yapılandırma ayarları
Bu dosya metin türleri, tonlar ve diğer sabit değerleri tutar
"""

# Grok API ayarları
XAI_API_BASE = "https://api.x.ai/v1"
XAI_MODEL = "grok-beta"

# Metin türleri ve açıklamaları
CONTENT_TYPES = {
    "Blog Yazısı": "Uzun format, SEO dostu, bilgilendirici içerik",
    "Ürün Açıklaması": "Satış odaklı, özlü, ikna edici metin",
    "Sosyal Medya": "Kısa, dikkat çekici, etkileşim odaklı",
    "E-posta": "Profesyonel, net, aksiyon odaklı",
    "Yaratıcı Yazı": "Anlatım odaklı, özgün, akıcı hikaye"
}

# Ton seçenekleri
TONE_OPTIONS = {
    "Profesyonel": "İş dünyası için uygun, ciddi ve güvenilir",
    "Samimi": "Arkadaşça, rahat ve yakın",
    "Resmi": "Kurumsal, ciddi ve otoriter",
    "Yaratıcı": "Özgün, farklı ve ilham verici",
    "Bilgilendirici": "Eğitici, açıklayıcı ve net"
}

# Uzunluk seçenekleri (kelime sayısı)
LENGTH_OPTIONS = {
    "Kısa": (100, 200),
    "Orta": (300, 500),
    "Uzun": (600, 1000)
}