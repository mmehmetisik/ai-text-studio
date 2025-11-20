# Proje 1: AI Metin Üretim Stüdyosu

## Proje Özeti
Bu proje, kullanıcıların farklı türde profesyonel metinler üretmesine yardımcı olan bir AI destekli içerik oluşturma aracıdır. Streamlit ile modern bir web arayüzü sunarak blog yazıları, ürün açıklamaları, sosyal medya içerikleri ve daha fazlasını kolayca oluşturmanızı sağlar.

## Projenin Amacı
Bu projeyle kullanıcılar, zaman kazanarak kaliteli metin içerikleri üretebilecekler. Aynı zamanda farklı tonlar ve stiller deneyerek içeriklerini özelleştirebilecekler. Proje, GenAI'ın metin üretim yeteneklerini pratik bir şekilde kullanmayı öğretir.

## Kullanılacak Teknolojiler

### Ana Teknolojiler
- **Python 3.9+**: Programlama dili
- **Streamlit**: Web arayüzü framework'ü
- **OpenAI API (GPT-4 veya GPT-3.5-turbo)**: Metin üretim motoru
- **python-dotenv**: Çevre değişkenleri yönetimi
- **Git**: Versiyon kontrol sistemi

### Öğrenilecek Kavramlar
- OpenAI API kullanımı ve prompt engineering
- Streamlit ile interaktif web uygulaması geliştirme
- Çevre değişkenleri ile güvenli API key yönetimi
- Session state ile kullanıcı verilerini saklama
- Dosya işlemleri (TXT, PDF export)

## Temel Özellikler

### 1. Metin Türü Seçimi
Kullanıcı şu içerik türlerinden birini seçebilir:
- Blog yazısı (uzun format, SEO dostu)
- Ürün açıklaması (satış odaklı, özlü)
- Sosyal medya gönderisi (kısa, dikkat çekici)
- E-posta içeriği (profesyonel, net)
- Hikaye/Yaratıcı yazı (anlatım odaklı)

### 2. Ton ve Stil Ayarları
Üretilen metnin karakterini belirler:
- Profesyonel: İş dünyası için uygun
- Samimi: Arkadaşça ve rahat
- Resmi: Kurumsal ve ciddi
- Yaratıcı: Özgün ve farklı
- Bilgilendirici: Eğitici ve açıklayıcı

### 3. Uzunluk Kontrolü
- Kısa (100-200 kelime)
- Orta (300-500 kelime)
- Uzun (600-1000 kelime)

### 4. Çoklu Versiyon Üretimi
Aynı prompt için 2-3 farklı varyasyon üretir. Kullanıcı beğendiğini seçer veya hepsini kaydeder.

### 5. İçerik Geçmişi
Üretilen tüm metinler session içinde saklanır. Kullanıcı önceki üretimlerine geri dönebilir, karşılaştırabilir.

### 6. Dışa Aktarma
- Plain Text (.txt) formatında kaydetme
- Basit PDF oluşturma (opsiyonel)
- Panoya kopyalama (copy to clipboard)

## Proje Dosya Yapısı

```
ai-text-studio/
│
├── .env                    # API anahtarları (GIT'E EKLENMEYEN)
├── .gitignore             # Git ignore dosyası
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Proje dokümantasyonu
│
├── app.py                # Ana Streamlit uygulaması
│
├── config/
│   └── settings.py       # Yapılandırma ayarları
│
├── utils/
│   ├── api_handler.py    # OpenAI API çağrıları
│   ├── text_processor.py # Metin işleme fonksiyonları
│   └── file_exporter.py  # Dosya kaydetme işlemleri
│
└── assets/
    └── style.css         # Özel CSS stilleri (opsiyonel)
```

## Geliştirme Adımları

### Faz 1: Temel Kurulum (1-2 gün)
- Git repository oluşturma
- Virtual environment kurulumu
- Temel bağımlılıkları yükleme
- OpenAI API key alma ve test etme
- Basit Streamlit uygulaması çalıştırma

### Faz 2: Ana İşlevsellik (2-3 gün)
- OpenAI API entegrasyonu
- Prompt şablonları oluşturma
- Metin türü, ton ve uzunluk seçeneklerini ekleme
- Tek metin üretme fonksiyonunu tamamlama

### Faz 3: Gelişmiş Özellikler (2-3 gün)
- Çoklu versiyon üretimi
- Session state ile geçmiş saklama
- Dosya export işlevleri
- Hata yönetimi ve kullanıcı geri bildirimleri

### Faz 4: UI/UX İyileştirmeleri (1-2 gün)
- Streamlit arayüzünü güzelleştirme
- Loading animasyonları ekleme
- Responsive tasarım kontrolleri
- Kullanıcı deneyimi testleri

### Faz 5: Dokümantasyon ve Yayınlama (1 gün)
- README.md dosyası yazma
- Kod içi yorumlar ekleme
- GitHub'a push etme
- LinkedIn için ekran görüntüleri alma

## Öğrenme Çıktıları

Bu projeyi tamamladığında şunları öğrenmiş olacaksın:
- OpenAI API ile nasıl çalışılır
- Prompt engineering temellerini nasıl uygularız
- Streamlit ile kullanıcı dostu arayüzler nasıl oluşturulur
- API key'leri güvenli şekilde nasıl saklarız
- Session state ile geçici veri yönetimi nasıl yapılır
- Dosya işlemleri (okuma, yazma, export) nasıl yapılır
- Git ile versiyon kontrolü nasıl yönetilir

## API Kullanım Tahmini ve Maliyet

OpenAI API ücretli olduğu için dikkat edilmesi gerekenler:
- GPT-3.5-turbo kullanımı önerilir (daha ucuz, hızlı)
- GPT-4 opsiyonel olarak eklenebilir (pahalı ama kaliteli)
- Test aşamasında kısa metinlerle çalış
- Her request yaklaşık maliyeti: $0.002 - $0.02 arası

## Başarı Kriterleri

Proje başarılı sayılabilir çünkü:
- Kullanıcı arayüzü sezgisel ve kullanımı kolay
- API çağrıları stabil ve hızlı çalışıyor
- Hata durumları düzgün yönetiliyor
- Kod temiz, okunabilir ve yorumlu
- README dosyası detaylı ve bilgilendirici
- GitHub repo'su profesyonel görünüyor

## LinkedIn İçin Sunum Noktaları

Bu projeyi LinkedIn'de paylaşırken vurgulayabileceğin noktalar:
- "OpenAI GPT API entegrasyonu ile AI destekli içerik üretim aracı geliştirdim"
- "Streamlit kullanarak kullanıcı dostu web arayüzü oluşturdum"
- "Farklı metin türleri ve tonlar için dinamik prompt engineering uyguladım"
- "Session yönetimi ve dosya export özellikleri ekledim"
- "Güvenli API key yönetimi ve hata işleme implementasyonu yaptım"

## Potansiyel İyileştirmeler (V2 için)

İlerleyen zamanlarda eklenebilecek özellikler:
- Türkçe dil desteği (şu an İngilizce odaklı)
- Kullanıcı hesapları ve veritabanı
- Üretilen metinler için SEO skoru
- Farklı AI modellerini karşılaştırma
- Toplu metin üretimi (batch processing)
- Şablon sistemleri (template library)
