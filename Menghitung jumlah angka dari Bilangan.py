# ==========================================
# PROGRAM 1: JUMLAH DIGIT (REKURSIF)
# ==========================================

def hitung_digit(n):
    """
    RUNTUNAN ALGORITMA:
    1. Pastikan angka bernilai positif menggunakan abs() agar tidak error logika[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).
    2. KASUS DASAR (Base Case): Jika n < 10, maka n adalah digit terakhir, kembalikan n[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).
    3. LANGKAH REKURSI: 
       - Ambil angka terakhir dengan (n % 10)[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
       - Panggil kembali fungsi dengan sisa angka (n // 10)[span_8](start_span)[span_8](end_span).
       - Jumlahkan keduanya[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span).
    
    """
    n = abs(n)
    # Fungsi Rekursi
    if n < 10:
        return n  # Base Case: Hanya tersisa satu digit[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span)
    else:
        # Rekursi: Digit terakhir + pemanggilan sisa[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span)
        return (n % 10) + hitung_digit(n // 10)

# Uji Coba Program
angka = 456
print(f"Bilangan: {angka}")
print(f"Proses Rekursi: 6 + 5 + 4")
print(f"Hasil Akhir: {hitung_digit(angka)}") # Output: 15

# Penjelasan 
# Simulasi Runtunan Rekursi untuk 456
"""
​Pemanggilan Pertama:
​Digit terakhir diambil: 456 % 10 = 6.  
​Sisa angka dikirim ke rekursi berikutnya: 456 // 10 = 45.  
​Status: 6 + hitung_digit(45).  
​Pemanggilan Kedua:
​Digit terakhir diambil: 45 % 10 = 5.  
​Sisa angka dikirim ke rekursi berikutnya: 45 // 10 = 4.  
​Status: 6 + 5 + hitung_digit(4).
​Pemanggilan Ketiga:
​Digit terakhir diambil: 4 % 10 = 4.  
​Sisa angka dikirim ke rekursi berikutnya: 4 // 10 = 0.  
​Status: 6 + 5 + 4 + hitung_digit(0).  
​Pemanggilan Keempat (Base Case):
​Karena angka sudah 0, fungsi berhenti dan mengembalikan nilai 0. 
Hasil Akhir
​Setelah mencapai base case, program akan menjumlahkan seluruh tumpukan nilai tersebut secara terbalik:

6 + 5 + 4 + 0 = 15
"""