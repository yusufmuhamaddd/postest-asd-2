# postest-asd-2
Kode ini adalah implementasi algoritma pencarian Fibonacci (Fibonacci search) yang mencari elemen x pada list arr. Algoritma ini bekerja dengan membagi list menjadi sublist berdasarkan deret Fibonacci dan kemudian menggunakan pencarian biner untuk mencari elemen pada sublist.

Kode dimulai dengan menginisialisasi beberapa variabel:

n: panjang dari list arr
fib1, fib2, dan fib: bilangan Fibonacci awal yang digunakan untuk membagi list menjadi sublist
Selanjutnya, algoritma mencari bilangan Fibonacci terbesar yang kurang dari atau sama dengan n dengan menggunakan loop while. Variabel fib1 dan fib2 diperbarui secara berulang hingga ditemukan bilangan Fibonacci terbesar yang kurang dari atau sama dengan n.

Setelah itu, variabel idx dan pos diinisialisasi. Variabel pos akan digunakan sebagai posisi awal pencarian pada list, sedangkan variabel idx akan digunakan untuk menyimpan indeks dari elemen yang dibandingkan selama pencarian.

Selanjutnya, algoritma melakukan pencarian menggunakan bilangan Fibonacci yang lebih kecil sampai mencapai elemen yang dicari. Setiap kali loop dilakukan, algoritma memperbarui variabel i yang menunjukkan indeks dari elemen yang akan dibandingkan. Jika elemen arr[i] lebih kecil dari x, algoritma akan memperbarui variabel fib1, fib2, dan idx untuk mencari pada sublist berikutnya. Jika elemen arr[i] lebih besar dari x, algoritma akan memperbarui variabel fib1 dan fib2 untuk mencari pada sublist sebelumnya. Jika elemen arr[i] sama dengan x, algoritma akan mengembalikan indeks i.

Jika elemen tidak ditemukan, algoritma akan mengembalikan -1.

Terakhir, kode melakukan pencarian pada list var dan mencetak hasil pencarian untuk setiap elemen dalam list. Kemudian, kode melakukan pencarian pada sublist pada indeks 3 dari list var untuk elemen "Wahyu" dan "Wibi", dan mencetak hasil pencarian tersebut.

Berikut adalah output

![Screen Shot 2023-03-11 at 1 36 12 AM](https://user-images.githubusercontent.com/126859339/224384661-969ed069-055c-41cc-af2f-0767e2697cc9.png)
