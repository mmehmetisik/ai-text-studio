"""
AI Metin Üretim Stüdyosu
Groq API kullanarak farklı türlerde metin içerikleri üretir
"""

import streamlit as st  # Streamlit kütüphanesini içe aktar
from utils.api_handler import generate_text  # Metin üretim fonksiyonunu içe aktar
from config.settings import CONTENT_TYPES, TONE_OPTIONS, LENGTH_OPTIONS  # Ayarları içe aktar
from utils.text_processor import count_words  # Kelime sayma fonksiyonunu içe aktar

from utils.text_processor import count_words  # Kelime sayma fonksiyonunu içe aktar

def load_css():
    """CSS dosyasını yükler ve Streamlit'e uygular"""
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Session state başlat - uygulama ilk açıldığında çalışır
# session_state'te history adında bir liste yoksa oluştur
# Bu liste tüm üretilen metinleri saklayacak
if 'history' not in st.session_state:
    st.session_state.history = []  # Boş liste ile başla

# Sayfa yapılandırması - bu her zaman en üstte olmalı
st.set_page_config(
    page_title="AI Metin Üretim Stüdyosu",  # Tarayıcı sekmesinde görünen başlık
    page_icon="✍️",  # Sekme ikonu
    layout="wide"  # Sayfa genişliği geniş olsun
)

# CSS dosyasını yükle
load_css()

# Ana başlık - büyük ve kalın görünür
st.title("✍️ AI Metin Üretim Stüdyosu")

# Ana başlık - büyük ve kalın görünür
st.title("✍️ AI Metin Üretim Stüdyosu")

# Alt başlık - açıklama için
st.markdown("Groq AI kullanarak profesyonel metin içerikleri oluşturun")

# Yatay çizgi - görsel ayrım için
st.divider()

# Kullanıcıdan konu girişi al
# text_area çok satırlı metin kutusu oluşturur
user_prompt = st.text_area(
    label="Hangi konuda metin üretmek istiyorsunuz?",
    placeholder="Örnek: Yapay zeka hakkında bir blog yazısı yaz...",
    height=100
)

# Selectbox açılır menü oluşturur
# Kullanıcı metin türünü seçer
content_type = st.selectbox(
    label="Metin Türü Seçin",
    options=list(CONTENT_TYPES.keys())  # Dictionary'deki anahtarları liste yap
)

# Seçilen türün açıklamasını göster
st.info(f"📝 {CONTENT_TYPES[content_type]}")

# Radio butonlar ile ton seçimi
# horizontal=True ile butonlar yatay dizilir
tone = st.radio(
    label="Ton Seçin",
    options=list(TONE_OPTIONS.keys()),
    horizontal=True
)

# Seçilen tonun açıklamasını göster
st.caption(f"💬 {TONE_OPTIONS[tone]}")

# Select slider ile uzunluk seçimi
length_choice = st.select_slider(
    label="Metin Uzunluğu",
    options=list(LENGTH_OPTIONS.keys())
)

# Seçilen uzunluğun kelime aralığını göster
min_words, max_words = LENGTH_OPTIONS[length_choice]  # Tuple'dan değerleri al
st.caption(f"📏 Yaklaşık {min_words}-{max_words} kelime")

# Kaç tane versiyon üretilsin?
# number_input sayı girişi için kullanılır
# min_value ve max_value minimum ve maksimum değerleri belirler
# value varsayılan değerdir
num_versions = st.number_input(
    label="Kaç farklı versiyon üretilsin?",
    min_value=1,
    max_value=3,
    value=1,
    help="Aynı konuda farklı varyasyonlar görmek için artırın"
)

# Boşluk ekle
st.write("")

# Buton oluştur
# primary type butonu mavi renkli ve vurgulu yapar
generate_button = st.button(
    label="🚀 Metin Üret",
    type="primary",
    use_container_width=True  # Buton sayfanın genişliğinde olsun
)

# Butona tıklandığında ne olacağını kontrol et
if generate_button:
    # Kullanıcı metin girmiş mi kontrol et
    if not user_prompt:
        st.warning("⚠️ Lütfen bir konu girin!")  # Sarı uyarı mesajı
    else:
        # Başarı mesajını göster
        st.success(f"✅ {num_versions} farklı versiyon üretiliyor...")

        # Eğer birden fazla versiyon isteniyorsa kolonlar oluştur
        # Kolonlar yan yana kutular oluşturur, her versiyon kendi kolonunda görünür
        if num_versions > 1:
            # columns fonksiyonu kaç kolon istediğimizi belirler
            # num_versions kadar kolon oluşturur, yani 2 versiyon = 2 kolon
            cols = st.columns(num_versions)

        # Her versiyon için döngü başlat
        # range(num_versions) 0'dan num_versions'a kadar sayılar üretir
        # Mesela num_versions=3 ise, i değerleri 0, 1, 2 olur
        for i in range(num_versions):
            # Her versiyonu ayrı ayrı üret
            # Loading göstergesi ile kullanıcıya hangi versiyon üretildiğini göster
            with st.spinner(f"✨ Versiyon {i + 1} üretiliyor..."):
                # API'yi çağır ve metin üret
                # Her döngüde yeni bir API çağrısı yapılır
                # Temperature aynı olduğu için her versiyon biraz farklı olacak
                generated_text = generate_text(
                    user_prompt,  # Kullanıcının girdiği konu
                    CONTENT_TYPES[content_type],  # Seçilen türün açıklaması
                    TONE_OPTIONS[tone],  # Seçilen tonun açıklaması
                    LENGTH_OPTIONS[length_choice]  # Seçilen uzunluğun min-max değerleri
                )

            # Eğer birden fazla versiyon varsa, her versiyonu kendi kolonunda göster
            # Tek versiyon varsa normal akışta göster
            if num_versions > 1:
                # cols[i] i'inci kolonu seçer
                # with bloğu içindeki her şey o kolonda görünür
                with cols[i]:
                    # Üretilen metni geçmişe ekle
                    # Her metni bir dictionary olarak kaydediyoruz ki hangi ayarlarla üretildiğini bilelim
                    st.session_state.history.append({
                        'prompt': user_prompt,  # Kullanıcının yazdığı konu
                        'content_type': content_type,  # Metin türü
                        'tone': tone,  # Ton
                        'length': length_choice,  # Uzunluk
                        'text': generated_text,  # Üretilen metin
                        'version': i + 1  # Hangi versiyon
                    })

                    # Versiyon başlığı, hangi versiyon olduğunu gösterir
                    st.markdown(f"#### 📄 Versiyon {i + 1}")
                    # Üretilen metni göster
                    st.write(generated_text)

                    # Kelime sayısını hesapla ve göster
                    word_count = count_words(generated_text)
                    st.metric(
                        label="📊 Kelime Sayısı",
                        value=f"{word_count} kelime",
                        delta=f"Hedef: {min_words}-{max_words}"
                    )

                    # Her versiyon için ayrı indirme butonu
                    # Dosya adına versiyon numarası eklenir ki karışmasın
                    st.download_button(
                        label="💾 İndir",
                        data=generated_text,
                        file_name=f"{content_type.replace(' ', '_')}_v{i + 1}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
            else:
                # Tek versiyon için geçmişe ekle
                st.session_state.history.append({
                    'prompt': user_prompt,
                    'content_type': content_type,
                    'tone': tone,
                    'length': length_choice,
                    'text': generated_text,
                    'version': 1  # Tek versiyon
                })

                # Tek versiyon ise, eski düzende göster
                st.markdown("### 📝 Üretilen Metin:")
                st.write(generated_text)

                # Kelime sayısını hesapla ve göster
                word_count = count_words(generated_text)
                st.metric(
                    label="📊 Kelime Sayısı",
                    value=f"{word_count} kelime",
                    delta=f"Hedef: {min_words}-{max_words}"
                )

                # İndirme butonu
                st.download_button(
                    label="💾 Metni İndir (TXT)",
                    data=generated_text,
                    file_name=f"{content_type.replace(' ', '_')}_metin.txt",
                    mime="text/plain",
                    use_container_width=True
                )

# ============================================================================
# SIDEBAR - METİN GEÇMİŞİ PANELİ
# ============================================================================

# Sidebar başlığı ve açıklama
# sidebar sol tarafta açılan panel oluşturur
st.sidebar.title("📚 Metin Geçmişi")
st.sidebar.markdown("Ürettiğiniz tüm metinler burada saklanır")

# Eğer geçmişte hiç metin yoksa bilgilendirici mesaj göster
# len fonksiyonu listenin uzunluğunu verir, 0 ise liste boş demektir
if len(st.session_state.history) == 0:
    st.sidebar.info("Henüz metin üretmediniz. Ürettiğiniz metinler burada görünecek.")
else:
    # Geçmişte kaç metin olduğunu göster
    # Bu kullanıcıya ne kadar içerik ürettiğini gösterir
    st.sidebar.success(f"Toplam {len(st.session_state.history)} metin üretildi")

    # Temizle butonu ekle
    # Bu buton tüm geçmişi silmek için
    if st.sidebar.button("🗑️ Geçmişi Temizle", use_container_width=True):
        # Geçmiş listesini boşalt
        # clear fonksiyonu listenin tüm elemanlarını siler
        st.session_state.history.clear()
        # Sayfayı yenile ki değişiklik hemen görünsün
        # rerun fonksiyonu sayfayı yeniden yükler
        st.rerun()

    st.sidebar.divider()  # Yatay çizgi ekle, görsel ayrım için

    # Geçmişteki her metin için bir kart oluştur
    # enumerate fonksiyonu hem index hem de elemanı verir
    # reversed geçmişi ters çevirir, en son üretilen en üstte görünsün
    for idx, item in enumerate(reversed(st.session_state.history)):
        # Her metni bir expander içinde göster
        # expander tıklanabilir, açılır kapanır kutular oluşturur
        # Başlıkta prompt'un ilk 30 karakterini gösteriyoruz ki kullanıcı ne olduğunu anlasın
        with st.sidebar.expander(
            f"📄 {item['prompt'][:30]}..." if len(item['prompt']) > 30 else f"📄 {item['prompt']}",
            expanded=False  # Başlangıçta kapalı olsun, kullanıcı tıklayınca açılsın
        ):
            # Metin bilgilerini göster
            # caption küçük gri metin oluşturur, metadata için ideal
            st.caption(f"**Tür:** {item['content_type']}")
            st.caption(f"**Ton:** {item['tone']}")
            st.caption(f"**Uzunluk:** {item['length']}")
            st.caption(f"**Versiyon:** {item['version']}")

            # Küçük bir boşluk
            st.write("")

            # Metni göster ama kısaltılmış halde
            # Uzun metinleri göstermek sidebar'ı çok kaydırır, ilk 150 karakter yeterli
            preview = item['text'][:150] + "..." if len(item['text']) > 150 else item['text']
            st.text_area(
                label="Metin Önizleme",
                value=preview,
                height=100,
                disabled=True,  # disabled=True metni düzenlenemez yapar, sadece okuma için
                key=f"preview_{idx}"  # Her text_area'nın benzersiz bir key'i olmalı
            )

            # Tam metni göster butonu
            # Kullanıcı tıklayınca ana sayfada tam metin görünecek
            if st.button(f"👁️ Tam Metni Gör", key=f"view_{idx}", use_container_width=True):
                # session_state'te selected_text adında bir değişken oluştur
                # Bu değişken hangi metnin görüntüleneceğini tutar
                st.session_state.selected_text = item
                st.rerun()  # Sayfayı yenile ki ana sayfada görünsün

            # İndirme butonu
            # Her geçmiş metin için de indirme imkanı sun
            st.download_button(
                label="💾 İndir",
                data=item['text'],
                file_name=f"{item['content_type'].replace(' ', '_')}_v{item['version']}.txt",
                mime="text/plain",
                key=f"download_{idx}",  # Her butonun benzersiz key'i olmalı
                use_container_width=True
            )

# ============================================================================
# SEÇİLEN METNİ ANA SAYFADA GÖSTER
# ============================================================================

# Eğer kullanıcı geçmişten bir metin seçtiyse, onu ana sayfada göster
# selected_text session_state'te varsa demek ki kullanıcı bir metni görüntülemek istemiş
if 'selected_text' in st.session_state:
    # Ana sayfada seçilen metni göster
    st.divider()  # Görsel ayrım için çizgi
    st.subheader("📖 Seçilen Metin")

    # Metin bilgilerini göster
    # Üç kolon oluştur, bilgiler yan yana görünsün
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption(f"**Tür:** {st.session_state.selected_text['content_type']}")
    with col2:
        st.caption(f"**Ton:** {st.session_state.selected_text['tone']}")
    with col3:
        st.caption(f"**Uzunluk:** {st.session_state.selected_text['length']}")

    # Tam metni göster
    st.write(st.session_state.selected_text['text'])

    # Kelime sayısı
    word_count = count_words(st.session_state.selected_text['text'])
    st.metric(label="📊 Kelime Sayısı", value=f"{word_count} kelime")

    # İndirme butonu
    st.download_button(
        label="💾 Bu Metni İndir",
        data=st.session_state.selected_text['text'],
        file_name=f"{st.session_state.selected_text['content_type'].replace(' ', '_')}_selected.txt",
        mime="text/plain",
        use_container_width=True
    )

    # Kapat butonu
    # Kullanıcı metni gördü, kapatmak isteyebilir
    if st.button("❌ Kapat", type="secondary"):
        # selected_text değişkenini session_state'ten sil
        # del komutu bir değişkeni tamamen kaldırır
        del st.session_state.selected_text
        st.rerun()  # Sayfayı yenile