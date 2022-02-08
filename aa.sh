for i in {1..66}
do echo -e 
"$(date +"%Y年%m月%d日 %H:%M %S秒")\t
第${i}次测试\t
下载速率:$(printf "%.2f" $(echo "scale=2;$(curl -o /dev/null -sw "%{speed_download}" 
http://183.237.146.218/tttt  -H "Host:localhost")/1024/1024" |bc)) MB/s"
 sleep 60; 
done
