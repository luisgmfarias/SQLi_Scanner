for link in `cat $lista`
do
  sqlmap -u link --dbs
done
