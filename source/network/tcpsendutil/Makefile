all:util.o tcputilclient tcputilserver
util.o: util.c
	gcc -g -c -o util.o util.c
tcputilclient: client.o util.o
	gcc client.o util.o -o tcputilclient
client.o: client.c
	gcc -g -c -o client.o client.c
tcputilserver: server.o util.o
	gcc server.o util.o -o tcputilserver
server.o: server.c
	gcc -g -c -o server.o server.c
clean:
	rm -f *.o tcputilclient tcputilserver
