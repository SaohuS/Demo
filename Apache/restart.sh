#!/bin/bash
export BUILD_ID='not_kill_me'
source ~/.bash_profile
start() {
local PRO_PID=`ps aux |grep sersync2 |grep -v 'grep'|grep -v '/mnt/sersync2'|awk '{print $2}'`
if test -z "$PRO_PID" ;then
	nohup ./sersync2 -n 3 -d &
else
	echo '程序已经启动'
	exit 1
fi
}

stop() {
local PRO_PID=`ps aux |grep sersync2 |grep -v 'grep'|grep -v '/mnt/sersync2'|awk '{print $2}'`
test -z "$PRO_PID" && echo "程序没有启动" && exit 1
kill -9 "$PRO_PID" >/dev/null 2>&1 &
}

case $1	in 
	start)
	start
	;;
	stop)
	stop
	;;
	restart)
	stop
	sleep 5
	start
	;;
	*)
	echo '请输入参数start | stop | restart'
	;;
esac
