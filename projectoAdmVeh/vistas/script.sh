
#!/bin/sh
# This is a comment!

k = "\n"

for j in 1 2 3 4 5 6 7 8 9 10
do
  for i in 20 100 200 300 400 500 1000 1500 2000 2500 3000
    do
      ./out.o ./../data/valores.csv 2 $i
    done
    echo $k
done
