"""
Grok API ile iletişim kuran fonksiyonlar
Bu dosya API çağrılarını yönetir ve hata kontrolü yapar
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# .env dosyasından çevre değişkenlerini yükle
load_dotenv()

# Grok API client'ı oluştur
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)


def generate_text(prompt, content_type, tone, length):
    """
    Grok API kullanarak metin üretir

    Args:
        prompt (str): Kullanıcının yazdığı konu veya talimat
        content_type (str): Metin türü (Blog Yazısı, Ürün Açıklaması vb.)
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

        # API'ye istek gönder
        response = client.chat.completions.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )

        # Üretilen metni al ve döndür
        generated_text = response.choices[0].message.content
        return generated_text

    except Exception as e:
        return f"Hata oluştu: {str(e)}"