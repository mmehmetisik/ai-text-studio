"""
Groq API ile iletişim kuran fonksiyonlar
Bu dosya API çağrılarını yönetir ve hata kontrolü yapar
"""

import os
import requests  # HTTP istekleri için
from dotenv import load_dotenv

# .env dosyasından çevre değişkenlerini yükle
load_dotenv()

# Groq API bilgileri
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # .env dosyasından API key'i al
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Groq API endpoint


def generate_text(prompt, content_type, tone, length):
    """
    Groq API kullanarak metin üretir

    Args:
        prompt (str): Kullanıcının yazdığı konu veya talimat
        content_type (str): Metin türü açıklaması
        tone (str): Ton açıklaması
        length (tuple): Minimum ve maksimum kelime sayısı

    Returns:
        str: Üretilen metin veya hata mesajı
    """

    try:
        # System prompt oluştur (AI'a rolünü söylüyoruz)
        system_prompt = f"""Sen profesyonel bir içerik yazarısın. 
        Görevin {content_type} türünde içerik üretmektir.
        Ton: {tone}
        Uzunluk: {length[0]}-{length[1]} kelime arası olmalı."""

        # API isteği için gerekli başlıklar
        # Authorization başlığı API key'i gönderiyor
        # Bearer kelimesi token tipini belirtiyor
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        # API'ye göndereceğimiz veri
        # model: Groq'da kullanılabilir modellerden biri
        # llama-3.1-8b-instant hızlı ve hafif bir model
        data = {
            "model": "llama-3.1-8b-instant",  # Groq'un en iyi genel amaçlı modeli
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,  # Yaratıcılık seviyesi (0-2 arası, 0.7 dengeli)
            "max_tokens": 2000  # Maksimum üretilecek token sayısı
        }

        # API'ye POST isteği gönder
        # timeout parametresi 30 saniye bekle, sonra timeout ver demek
        response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=30)

        # Yanıtı kontrol et
        # 200 status code başarılı demek
        if response.status_code == 200:
            result = response.json()  # JSON formatındaki yanıtı parse et
            generated_text = result["choices"][0]["message"]["content"]  # Üretilen metni al
            return generated_text
        else:
            # Eğer hata varsa, hata kodunu ve mesajını döndür
            return f"API Hatası: {response.status_code} - {response.text}"

    except Exception as e:
        # Eğer bir exception oluşursa (internet kesildi, timeout oldu vb.)
        return f"Hata oluştu: {str(e)}"