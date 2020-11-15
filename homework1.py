arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    bMax = arrBerat[0]
    bMin = arrBerat[0]
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    for i in arrBerat:
        if i > bMax:
            bMax = i
        if i < bMin:
            bMin = i


def rerata(arrBerat):
    total = 0

    # Definisikan Proses Mencari Rerata Dari Total Berat
    for i in arrBerat:
        total += i

    return total/len(arrBerat)
    # Return Hasil Rerata


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    arrBerat.append(float(input()))
    # Masukkan Data Berat Ke Array (arrBerat)


# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
print("MINIMUM: %.2f"% bMin)
print("MAKSIMUM: %.2f"% bMax)
print("RERATA: %.2f"% rerata(arrBerat))