import string
import re

def caesar_cipher_decrypt(ciphertext, shift):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    decrypted_text = ""
    for char in ciphertext:
        if char.isupper():
            decrypted_text += upper[(upper.index(char) - shift) % 26]
        elif char.islower():
            decrypted_text += lower[(lower.index(char) - shift) % 26]
        else:
            decrypted_text += char
    return decrypted_text

def get_comprehensive_score(text):
    text_lower = text.lower()
    # คลังคำศัพท์พื้นฐานสำหรับตัดสินอันดับ 1
    dictionary = {
        'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
        'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what',
        'is', 'am', 'are', 'was', 'were', 'hello', 'hi', 'book', 'military', 'art', 'way', 'more', 'your', 'my'
    }
    
    words = re.findall(r'\b\w+\b', text_lower)
    meaningful_words_count = sum(1 for word in words if word in dictionary)
    
    # คำนวณคะแนน: เน้นจำนวนคำที่ถูกต้องเป็นหลัก
    word_score = meaningful_words_count * 100 
    
    # คะแนนโครงสร้างภาษา (Bigrams) สำหรับคำที่ไม่อยู่ในดิก
    bigram_score = 0
    common_bigrams = ['th', 'he', 'in', 'er', 'an', 're', 'on', 'at', 'en', 'nd']
    for bg in common_bigrams:
        bigram_score += text_lower.count(bg) * 2

    return word_score + bigram_score

def run_tool():
    print("=== โปรแกรมถอดรหัส Caesar Cipher อัจฉริยะ ===")
    print("(พิมพ์ 'exit' หรือกด Ctrl+C เพื่อเลิกใช้งาน)")
    
    while True:
        print("\n" + "-"*50)
        ciphertext = input("ป้อนรหัสที่ต้องการแก้: ").strip()
        
        if ciphertext.lower() == 'exit':
            print("ปิดโปรแกรม...")
            break
        if not ciphertext:
            continue

        candidates = []
        for shift in range(1, 26):
            decoded = caesar_cipher_decrypt(ciphertext, shift)
            score = get_comprehensive_score(decoded)
            candidates.append({'shift': shift, 'text': decoded, 'score': score})

        # เรียงลำดับตามคะแนนความแม่นยำ
        candidates.sort(key=lambda x: x['score'], reverse=True)

        print("\n--- ผลลัพธ์ที่น่าจะใช่ที่สุด ---")
        best = candidates[0]
        print(f"Shift {best['shift']:02d}: {best['text']} [แนะนำ]")
        
        print("\n--- อันดับสำรอง ---")
        for i in range(1, 4):
            c = candidates[i]
            print(f"Shift {c['shift']:02d}: {c['text']}")
        
        print("\n" + "="*50)
        input("กด Enter เพื่อใส่รหัสถัดไป...")

if __name__ == "__main__":
    try:
        run_tool()
    except KeyboardInterrupt:
        print("\nปิดโปรแกรม...")
